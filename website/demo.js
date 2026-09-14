(() => {
  const host = document.querySelector('.hero-demo');
  if (!host) return;

  const locale = document.documentElement.lang === 'zh-CN' ? 'zh-CN' : document.documentElement.lang;
  if (locale !== 'en' && locale !== 'zh-CN') return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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
      const lanes = localized && localized.lanes;
      if (!localized || !lanes || !Array.isArray(lanes.without) || !Array.isArray(lanes.with) || !Number.isFinite(trace.duration_ms)) return;

      host.classList.add('agnir-demo-player');
      host.innerHTML = `
        <div class="demo-compare" role="region" aria-label="${localized.labels.demo}">
          <div class="demo-grid">
            ${renderLaneShell('without', localized)}
            ${renderLaneShell('with', localized)}
          </div>
          <div class="demo-shared-caption">
            <span class="demo-same-prompt">${localized.labels.samePrompt}</span>
            <strong data-demo-verdict>${localized.labels.verdict}</strong>
          </div>
          <div class="demo-progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-demo-progress-wrap>
            <div class="demo-progress-fill" data-demo-progress></div>
          </div>
          <div class="demo-controls">
            <div class="demo-control-buttons">
              <button type="button" class="demo-control" data-demo-toggle></button>
              <button type="button" class="demo-control" data-demo-replay>${localized.labels.replay}</button>
            </div>
            <span class="demo-time" data-demo-time></span>
            <a class="demo-source" href="https://github.com/iorLab/agnir/tree/main/adoption/demos/fresh-session">${localized.labels.source}</a>
          </div>
        </div>`;

      function renderLaneShell(kind, copy) {
        const label = kind === 'without' ? copy.labels.without : copy.labels.with;
        return `
          <section class="demo-lane is-${kind}" data-demo-lane="${kind}" aria-label="${label}">
            <div class="demo-lane-heading">
              <span class="demo-lane-badge">${label}</span>
            </div>
            <div class="demo-chat">
              <div class="demo-chrome">
                <span class="demo-window-dots" aria-hidden="true"><i></i><i></i><i></i></span>
                <span class="demo-workspace">${copy.labels.workspace}</span>
              </div>
              <div class="demo-sessionbar">
                <div>
                  <span class="demo-session-title" data-demo-session-title></span>
                  <span class="demo-session-subtitle" data-demo-session-subtitle></span>
                </div>
              </div>
              <div class="demo-transcript-wrap">
                <div class="demo-transcript" data-demo-transcript></div>
              </div>
              <div class="demo-composer" aria-hidden="true">
                <span>${copy.labels.composer}</span>
                <b>↵</b>
              </div>
            </div>
          </section>`;
      }

      const laneStates = {};
      ['without', 'with'].forEach((kind) => {
        const lane = host.querySelector(`[data-demo-lane="${kind}"]`);
        laneStates[kind] = {
          kind,
          lane,
          events: lanes[kind],
          transcript: lane.querySelector('[data-demo-transcript]'),
          sessionTitle: lane.querySelector('[data-demo-session-title]'),
          sessionSubtitle: lane.querySelector('[data-demo-session-subtitle]'),
          nextEventIndex: 0,
          activeMessages: [],
          activeTools: []
        };
      });

      const timeElement = host.querySelector('[data-demo-time]');
      const progressWrap = host.querySelector('[data-demo-progress-wrap]');
      const progressElement = host.querySelector('[data-demo-progress]');
      const toggleButton = host.querySelector('[data-demo-toggle]');
      const replayButton = host.querySelector('[data-demo-replay]');
      const verdictElement = host.querySelector('[data-demo-verdict]');

      let elapsed = 0;
      let playing = !reduceMotion;
      let previousTimestamp = null;
      let animationFrame = null;

      const setSession = (state, event, clear = false) => {
        if (clear) state.transcript.replaceChildren();
        state.sessionTitle.textContent = event.title || '';
        state.sessionSubtitle.textContent = event.subtitle || '';
      };

      const appendBoundary = (state, event) => {
        const row = document.createElement('div');
        row.className = 'demo-session-boundary';

        const line = document.createElement('span');
        line.className = 'demo-session-boundary-line';

        const content = document.createElement('div');
        const kicker = document.createElement('strong');
        kicker.textContent = localized.labels.boundary;
        const title = document.createElement('span');
        title.textContent = event.title || '';
        const subtitle = document.createElement('small');
        subtitle.textContent = event.subtitle || '';

        content.append(kicker, title, subtitle);
        row.append(line, content);
        state.transcript.appendChild(row);
      };

      const appendMessage = (state, event) => {
        const row = document.createElement('div');
        row.className = `demo-message-row ${event.role === 'you' ? 'is-user' : 'is-agent'}`;

        const avatar = document.createElement('span');
        if (event.role === 'agent') {
          avatar.className = 'demo-avatar agent-spark-icon';
          avatar.setAttribute('aria-hidden', 'true');
        } else {
          avatar.className = 'demo-avatar';
          avatar.textContent = locale === 'zh-CN' ? '你' : 'Y';
        }

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
        state.transcript.appendChild(row);

        state.activeMessages.push({ event, row, text, cursor });
      };

      const appendTool = (state, event) => {
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
        state.transcript.appendChild(row);

        if (Number.isFinite(event.duration_ms) && event.duration_ms > 0) {
          state.activeTools.push({ event, row, icon });
        }
      };

      const appendResult = (state, event) => {
        const row = document.createElement('div');
        row.className = `demo-result is-${event.tone === 'success' ? 'success' : 'blocked'}`;

        const icon = document.createElement('span');
        icon.className = 'demo-result-icon';
        icon.textContent = event.tone === 'success' ? '✓' : '!';

        const content = document.createElement('div');
        const title = document.createElement('strong');
        title.textContent = event.title || '';
        const text = document.createElement('span');
        text.textContent = event.text || '';

        content.append(title, text);
        row.append(icon, content);
        state.transcript.appendChild(row);
      };

      const processEvent = (state, event) => {
        switch (event.type) {
          case 'session':
            setSession(state, event, true);
            break;
          case 'reset':
            setSession(state, event, true);
            break;
          case 'boundary':
            appendBoundary(state, event);
            break;
          case 'message':
            appendMessage(state, event);
            break;
          case 'tool':
            appendTool(state, event);
            break;
          case 'result':
            appendResult(state, event);
            break;
          default:
            break;
        }
      };

      const updateTyping = (state) => {
        state.activeMessages = state.activeMessages.filter((item) => {
          const duration = reduceMotion ? 1 : Math.max(1, item.event.duration_ms || 1);
          const ratio = Math.max(0, Math.min(1, (elapsed - item.event.at_ms) / duration));
          const count = Math.ceil(item.event.text.length * ratio);
          item.text.textContent = item.event.text.slice(0, count);
          const done = ratio >= 1;
          item.cursor.hidden = done;
          if (done) item.row.classList.add('is-complete');
          return !done;
        });

        state.activeTools = state.activeTools.filter((item) => {
          const done = elapsed >= item.event.at_ms + item.event.duration_ms;
          if (done) {
            item.row.classList.remove('is-working');
            item.row.classList.add('is-done');
            item.icon.textContent = '✓';
          }
          return !done;
        });
      };

      const processLane = (state) => {
        while (state.nextEventIndex < state.events.length && state.events[state.nextEventIndex].at_ms <= elapsed) {
          processEvent(state, state.events[state.nextEventIndex]);
          state.nextEventIndex += 1;
        }
        updateTyping(state);
        state.transcript.scrollTop = state.transcript.scrollHeight;
      };

      const updateChrome = () => {
        const bounded = Math.max(0, Math.min(trace.duration_ms, elapsed));
        const percent = (bounded / trace.duration_ms) * 100;
        progressElement.style.width = `${percent}%`;
        progressWrap.setAttribute('aria-valuenow', String(Math.round(percent)));
        progressWrap.setAttribute('aria-label', localized.labels.progress);
        timeElement.textContent = `${formatTime(bounded, trace.duration_ms)} / ${formatTime(trace.duration_ms, trace.duration_ms)}`;
        toggleButton.textContent = playing ? localized.labels.pause : localized.labels.play;
        toggleButton.setAttribute('aria-label', playing ? localized.labels.pause : localized.labels.play);
        verdictElement.classList.toggle('is-visible', bounded >= 23500);
      };

      const resetPlayback = () => {
        elapsed = 0;
        previousTimestamp = null;
        Object.values(laneStates).forEach((state) => {
          state.nextEventIndex = 0;
          state.activeMessages = [];
          state.activeTools = [];
          state.transcript.replaceChildren();
          state.sessionTitle.textContent = '';
          state.sessionSubtitle.textContent = '';
          processLane(state);
        });
        verdictElement.classList.remove('is-visible');
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
          Object.values(laneStates).forEach(processLane);
          playing = false;
          updateChrome();
          animationFrame = null;
          previousTimestamp = null;
          return;
        }

        Object.values(laneStates).forEach(processLane);
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
