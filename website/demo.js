(() => {
  const host = document.querySelector('.hero-demo');
  if (!host) return;

  const locale = document.documentElement.lang === 'zh-CN' ? 'zh-CN' : document.documentElement.lang;
  if (locale !== 'en' && locale !== 'zh-CN') return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sourceLabel = locale === 'zh-CN' ? '查看可复现场景 ↗' : 'View reproducible scenario ↗';
  const workspaceLabel = locale === 'zh-CN' ? 'Agent 工作区' : 'Agent workspace';

  const formatTime = (milliseconds, duration) => {
    const seconds = Math.max(0, Math.min(Math.ceil(duration / 1000), Math.floor(milliseconds / 1000)));
    return `00:${String(seconds).padStart(2, '0')}`;
  };

  const roleLabel = (role) => {
    if (role === 'agent') return 'Agent';
    return locale === 'zh-CN' ? '你' : 'You';
  };

  fetch('fresh-session-demo.json', { cache: 'no-cache' })
    .then((response) => {
      if (!response.ok) throw new Error(`demo trace HTTP ${response.status}`);
      return response.json();
    })
    .then((trace) => {
      const localized = trace.copy && trace.copy[locale];
      const events = localized && Array.isArray(localized.events) ? localized.events : [];
      if (!localized || events.length === 0 || !Number.isFinite(trace.duration_ms)) return;

      host.classList.add('agnir-demo-player');
      host.innerHTML = `
        <div class="demo-chat" role="region" aria-label="${localized.labels.demo}">
          <div class="demo-chrome">
            <span class="demo-window-dots" aria-hidden="true"><i></i><i></i><i></i></span>
            <span class="demo-workspace">${workspaceLabel}</span>
            <span class="demo-time" data-demo-time></span>
          </div>
          <div class="demo-sessionbar">
            <div>
              <span class="demo-session-title" data-demo-session-title></span>
              <span class="demo-session-subtitle" data-demo-session-subtitle></span>
            </div>
            <span class="demo-mode" data-demo-mode></span>
          </div>
          <div class="demo-transcript-wrap">
            <div class="demo-transcript" data-demo-transcript></div>
            <div class="demo-overlay" data-demo-overlay hidden>
              <span class="demo-overlay-kicker" data-demo-overlay-kicker></span>
              <strong data-demo-overlay-title></strong>
              <span data-demo-overlay-subtitle></span>
            </div>
          </div>
          <div class="demo-composer" aria-hidden="true">
            <span>${locale === 'zh-CN' ? '给 Agent 发消息…' : 'Message the Agent…'}</span>
            <b>↵</b>
          </div>
          <div class="demo-progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-demo-progress-wrap>
            <div class="demo-progress-fill" data-demo-progress></div>
          </div>
          <div class="demo-controls">
            <div class="demo-control-buttons">
              <button type="button" class="demo-control" data-demo-toggle></button>
              <button type="button" class="demo-control" data-demo-replay>${localized.controls.replay}</button>
            </div>
            <a class="demo-source" href="https://github.com/iorLab/agnir/tree/main/adoption/demos/fresh-session">${sourceLabel}</a>
          </div>
        </div>`;

      const transcript = host.querySelector('[data-demo-transcript]');
      const sessionTitle = host.querySelector('[data-demo-session-title]');
      const sessionSubtitle = host.querySelector('[data-demo-session-subtitle]');
      const modeElement = host.querySelector('[data-demo-mode]');
      const timeElement = host.querySelector('[data-demo-time]');
      const progressWrap = host.querySelector('[data-demo-progress-wrap]');
      const progressElement = host.querySelector('[data-demo-progress]');
      const toggleButton = host.querySelector('[data-demo-toggle]');
      const replayButton = host.querySelector('[data-demo-replay]');
      const overlay = host.querySelector('[data-demo-overlay]');
      const overlayKicker = host.querySelector('[data-demo-overlay-kicker]');
      const overlayTitle = host.querySelector('[data-demo-overlay-title]');
      const overlaySubtitle = host.querySelector('[data-demo-overlay-subtitle]');

      let elapsed = 0;
      let playing = !reduceMotion;
      let previousTimestamp = null;
      let animationFrame = null;
      let nextEventIndex = 0;
      let activeMessages = [];
      let activeTools = [];
      let overlayUntil = 0;

      const setMode = (mode) => {
        host.dataset.demoMode = mode || 'with';
        if (mode === 'without') {
          modeElement.textContent = localized.labels.without;
        } else {
          modeElement.textContent = localized.labels.with;
        }
      };

      const setSession = (event, clear = false) => {
        if (clear) transcript.replaceChildren();
        sessionTitle.textContent = event.title || '';
        sessionSubtitle.textContent = event.subtitle || '';
        setMode(event.mode);
      };

      const showOverlay = (event, finale = false) => {
        overlay.hidden = false;
        overlay.classList.toggle('is-finale', finale);
        overlayKicker.textContent = finale ? 'Agnir' : (locale === 'zh-CN' ? '切换会话' : 'Session boundary');
        overlayTitle.textContent = event.title || '';
        overlaySubtitle.textContent = event.subtitle || '';
        overlayUntil = event.at_ms + (event.duration_ms || 800);
      };

      const hideOverlay = () => {
        overlay.hidden = true;
        overlay.classList.remove('is-finale');
        overlayUntil = 0;
      };

      const appendMessage = (event) => {
        const row = document.createElement('div');
        row.className = `demo-message-row ${event.role === 'you' ? 'is-user' : 'is-agent'}`;

        const avatar = document.createElement('span');
        avatar.className = 'demo-avatar';
        avatar.textContent = event.role === 'you' ? (locale === 'zh-CN' ? '你' : 'Y') : 'A';

        const bubble = document.createElement('div');
        bubble.className = 'demo-bubble';

        const label = document.createElement('span');
        label.className = 'demo-message-role';
        label.textContent = roleLabel(event.role);

        const text = document.createElement('span');
        text.className = 'demo-message-text';
        text.textContent = '';

        const cursor = document.createElement('span');
        cursor.className = 'demo-typing-cursor';
        cursor.setAttribute('aria-hidden', 'true');

        bubble.append(label, text, cursor);
        row.append(avatar, bubble);
        transcript.appendChild(row);

        activeMessages.push({ event, row, text, cursor });
      };

      const appendTool = (event) => {
        const row = document.createElement('div');
        row.className = `demo-tool ${event.status === 'working' ? 'is-working' : 'is-done'}`;

        const icon = document.createElement('span');
        icon.className = 'demo-tool-icon';
        icon.textContent = event.status === 'working' ? '●' : '✓';

        const label = document.createElement('strong');
        label.textContent = event.label || '';

        const text = document.createElement('span');
        text.textContent = event.text || '';

        row.append(icon, label, text);
        transcript.appendChild(row);

        if (Number.isFinite(event.duration_ms) && event.duration_ms > 0) {
          activeTools.push({ event, row, icon });
        }
      };

      const processEvent = (event) => {
        switch (event.type) {
          case 'session':
            hideOverlay();
            setSession(event, true);
            break;
          case 'reset':
            hideOverlay();
            setSession(event, true);
            break;
          case 'message':
            appendMessage(event);
            break;
          case 'tool':
            appendTool(event);
            break;
          case 'transition':
            showOverlay(event, false);
            break;
          case 'finale':
            showOverlay(event, true);
            break;
          default:
            break;
        }
      };

      const updateTyping = () => {
        activeMessages = activeMessages.filter((item) => {
          const duration = reduceMotion ? 1 : Math.max(1, item.event.duration_ms || 1);
          const ratio = Math.max(0, Math.min(1, (elapsed - item.event.at_ms) / duration));
          const count = Math.ceil(item.event.text.length * ratio);
          item.text.textContent = item.event.text.slice(0, count);
          const done = ratio >= 1;
          item.cursor.hidden = done;
          if (done) item.row.classList.add('is-complete');
          return !done;
        });

        activeTools = activeTools.filter((item) => {
          const done = elapsed >= item.event.at_ms + item.event.duration_ms;
          if (done) {
            item.row.classList.remove('is-working');
            item.row.classList.add('is-done');
            item.icon.textContent = '✓';
          }
          return !done;
        });
      };

      const processDueEvents = () => {
        while (nextEventIndex < events.length && events[nextEventIndex].at_ms <= elapsed) {
          processEvent(events[nextEventIndex]);
          nextEventIndex += 1;
        }

        if (overlayUntil && elapsed >= overlayUntil) hideOverlay();
        updateTyping();
        transcript.scrollTop = transcript.scrollHeight;
      };

      const updateChrome = () => {
        const bounded = Math.max(0, Math.min(trace.duration_ms, elapsed));
        const percent = (bounded / trace.duration_ms) * 100;
        progressElement.style.width = `${percent}%`;
        progressWrap.setAttribute('aria-valuenow', String(Math.round(percent)));
        progressWrap.setAttribute('aria-label', localized.controls.progress);
        timeElement.textContent = `${formatTime(bounded, trace.duration_ms)} / ${formatTime(trace.duration_ms, trace.duration_ms)}`;
        toggleButton.textContent = playing ? localized.controls.pause : localized.controls.play;
        toggleButton.setAttribute('aria-label', playing ? localized.controls.pause : localized.controls.play);
      };

      const resetPlayback = () => {
        elapsed = 0;
        previousTimestamp = null;
        nextEventIndex = 0;
        activeMessages = [];
        activeTools = [];
        overlayUntil = 0;
        transcript.replaceChildren();
        hideOverlay();
        sessionTitle.textContent = '';
        sessionSubtitle.textContent = '';
        setMode('without');
        processDueEvents();
        updateChrome();
      };

      const tick = (timestamp) => {
        if (!playing) {
          animationFrame = null;
          previousTimestamp = null;
          return;
        }

        if (previousTimestamp === null) previousTimestamp = timestamp;
        const delta = Math.min(120, timestamp - previousTimestamp);
        previousTimestamp = timestamp;
        elapsed += delta;

        if (elapsed >= trace.duration_ms) {
          elapsed = trace.duration_ms;
          processDueEvents();
          playing = false;
          updateChrome();
          animationFrame = null;
          previousTimestamp = null;
          return;
        }

        processDueEvents();
        updateChrome();
        animationFrame = requestAnimationFrame(tick);
      };

      const start = () => {
        if (animationFrame !== null) return;
        if (elapsed >= trace.duration_ms) resetPlayback();
        playing = true;
        previousTimestamp = null;
        updateChrome();
        animationFrame = requestAnimationFrame(tick);
      };

      const pause = () => {
        playing = false;
        previousTimestamp = null;
        if (animationFrame !== null) cancelAnimationFrame(animationFrame);
        animationFrame = null;
        updateChrome();
      };

      toggleButton.addEventListener('click', () => {
        if (playing) pause();
        else start();
      });

      replayButton.addEventListener('click', () => {
        if (animationFrame !== null) cancelAnimationFrame(animationFrame);
        animationFrame = null;
        resetPlayback();
        start();
      });

      document.addEventListener('visibilitychange', () => {
        if (document.hidden && playing) pause();
      });

      resetPlayback();
      if (playing) animationFrame = requestAnimationFrame(tick);
    })
    .catch(() => {
      // Keep the server-rendered static comparison if the trace cannot load.
    });
})();
