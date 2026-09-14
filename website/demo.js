(() => {
  const host = document.querySelector('.hero-demo');
  if (!host) return;

  const locale = document.documentElement.lang === 'zh-CN' ? 'zh-CN' : document.documentElement.lang;
  if (locale !== 'en' && locale !== 'zh-CN') return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const formatTime = (milliseconds) => {
    const seconds = Math.max(0, Math.min(30, Math.floor(milliseconds / 1000)));
    return `00:${String(seconds).padStart(2, '0')}`;
  };

  const roleLabel = (role) => {
    if (role === 'agent') return 'Agent';
    return locale === 'zh-CN' ? '你' : 'you';
  };

  fetch('fresh-session-demo.json', { cache: 'no-cache' })
    .then((response) => {
      if (!response.ok) throw new Error(`demo trace HTTP ${response.status}`);
      return response.json();
    })
    .then((trace) => {
      const copy = trace.copy && trace.copy[locale];
      const timeline = Array.isArray(trace.timeline) ? trace.timeline : [];
      if (!copy || timeline.length === 0 || !Number.isFinite(trace.duration_ms)) return;

      host.classList.add('agnir-demo-player');
      host.innerHTML = `
        <div class="demo-frame" aria-live="polite">
          <div class="demo-topbar">
            <span class="demo-mode" data-demo-mode></span>
            <span class="demo-time" data-demo-time></span>
          </div>
          <div class="demo-scene" data-demo-scene>
            <div class="demo-scene-head">
              <span class="demo-session" data-demo-session></span>
              <h3 data-demo-title></h3>
            </div>
            <div class="demo-messages" data-demo-messages></div>
            <p class="demo-note" data-demo-note></p>
          </div>
          <div class="demo-progress" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-demo-progress-wrap>
            <div class="demo-progress-fill" data-demo-progress></div>
          </div>
          <div class="demo-controls">
            <div class="demo-control-buttons">
              <button type="button" class="demo-control" data-demo-toggle></button>
              <button type="button" class="demo-control" data-demo-replay>${copy.controls.replay}</button>
            </div>
            <a class="demo-source" href="https://github.com/iorLab/agnir/tree/main/adoption/demos/fresh-session">${locale === 'zh-CN' ? '查看可复现场景 ↗' : 'View reproducible scenario ↗'}</a>
          </div>
        </div>`;

      const modeElement = host.querySelector('[data-demo-mode]');
      const timeElement = host.querySelector('[data-demo-time]');
      const sceneElement = host.querySelector('[data-demo-scene]');
      const sessionElement = host.querySelector('[data-demo-session]');
      const titleElement = host.querySelector('[data-demo-title]');
      const messagesElement = host.querySelector('[data-demo-messages]');
      const noteElement = host.querySelector('[data-demo-note]');
      const progressWrap = host.querySelector('[data-demo-progress-wrap]');
      const progressElement = host.querySelector('[data-demo-progress]');
      const toggleButton = host.querySelector('[data-demo-toggle]');
      const replayButton = host.querySelector('[data-demo-replay]');

      let elapsed = 0;
      let playing = !reduceMotion;
      let previousTimestamp = null;
      let animationFrame = null;
      let renderedSceneId = null;

      const sceneForTime = (milliseconds) => timeline.find((scene) => milliseconds >= scene.start_ms && milliseconds < scene.end_ms) || timeline[timeline.length - 1];

      const renderScene = (timelineScene) => {
        if (!timelineScene || renderedSceneId === timelineScene.id) return;
        renderedSceneId = timelineScene.id;

        const sceneCopy = copy.scenes[timelineScene.id];
        if (!sceneCopy) return;

        const isClose = timelineScene.mode === 'close';
        sceneElement.classList.toggle('is-close', isClose);
        host.dataset.demoMode = timelineScene.mode;

        modeElement.textContent = isClose ? 'Agnir' : copy.modes[timelineScene.mode];
        sessionElement.textContent = sceneCopy.session || '';
        titleElement.textContent = sceneCopy.title || '';
        noteElement.textContent = sceneCopy.note || '';
        messagesElement.replaceChildren();

        (sceneCopy.messages || []).forEach((message) => {
          const row = document.createElement('p');
          row.className = `demo-message ${message.role === 'agent' ? 'agent-message' : 'user-message'}`;

          const label = document.createElement('span');
          label.className = `demo-role ${message.role === 'agent' ? 'agent' : 'prompt'}`;
          label.textContent = `${roleLabel(message.role)} ›`;

          const text = document.createElement('span');
          text.className = 'demo-message-text';
          text.textContent = message.text;

          row.append(label, text);
          messagesElement.appendChild(row);
        });
      };

      const renderProgress = () => {
        const bounded = Math.max(0, Math.min(trace.duration_ms, elapsed));
        const percent = (bounded / trace.duration_ms) * 100;
        progressElement.style.width = `${percent}%`;
        progressWrap.setAttribute('aria-valuenow', String(Math.round(percent)));
        progressWrap.setAttribute('aria-label', copy.controls.progress);
        timeElement.textContent = `${formatTime(bounded)} / ${formatTime(trace.duration_ms)}`;
        renderScene(sceneForTime(bounded === trace.duration_ms ? bounded - 1 : bounded));
        toggleButton.textContent = playing ? copy.controls.pause : copy.controls.play;
        toggleButton.setAttribute('aria-label', playing ? copy.controls.pause : copy.controls.play);
      };

      const tick = (timestamp) => {
        if (!playing) {
          previousTimestamp = null;
          animationFrame = null;
          return;
        }

        if (previousTimestamp === null) previousTimestamp = timestamp;
        const delta = Math.min(250, timestamp - previousTimestamp);
        previousTimestamp = timestamp;
        elapsed += delta;

        if (elapsed >= trace.duration_ms) {
          elapsed = trace.duration_ms;
          playing = false;
          renderProgress();
          previousTimestamp = null;
          animationFrame = null;
          return;
        }

        renderProgress();
        animationFrame = requestAnimationFrame(tick);
      };

      const start = () => {
        if (playing && animationFrame !== null) return;
        if (elapsed >= trace.duration_ms) elapsed = 0;
        playing = true;
        previousTimestamp = null;
        renderProgress();
        animationFrame = requestAnimationFrame(tick);
      };

      const pause = () => {
        playing = false;
        previousTimestamp = null;
        if (animationFrame !== null) cancelAnimationFrame(animationFrame);
        animationFrame = null;
        renderProgress();
      };

      toggleButton.addEventListener('click', () => {
        if (playing) pause();
        else start();
      });

      replayButton.addEventListener('click', () => {
        elapsed = 0;
        renderedSceneId = null;
        start();
      });

      document.addEventListener('visibilitychange', () => {
        if (document.hidden && playing) pause();
      });

      renderProgress();
      if (playing) animationFrame = requestAnimationFrame(tick);
    })
    .catch(() => {
      // Keep the server-rendered static comparison as the safe fallback.
    });
})();
