(() => {
  const themeStorageKey = 'agnir-theme';
  const languageStorageKey = 'agnir-language';
  const root = document.documentElement;
  const systemTheme = window.matchMedia('(prefers-color-scheme: light)');
  const languages = {
    en: { href: 'index.html', label: 'English', badge: 'EN' },
    'zh-CN': { href: 'zh-CN.html', label: '简体中文', badge: '中' },
    ja: { href: 'ja.html', label: '日本語', badge: '日' },
    ko: { href: 'ko.html', label: '한국어', badge: '한' },
  };

  const installPreviewCopy = {
    en: {
      aria: 'Install conversation example',
      install: 'Install and initialize Agnir for this Project.',
      installed: 'Installed. In a fresh session, just say “continue.”',
      continue: 'Continue.',
      resumed: 'Loaded Project state. Continuing with the next step.',
      composer: 'Message the Agent…',
    },
    'zh-CN': {
      aria: 'Agnir 安装对话示意',
      install: '为这个项目安装并初始化 Agnir',
      installed: '已安装。新会话时，只需说一句“继续”。',
      continue: '继续',
      resumed: '已读取项目状态，继续处理下一步。',
      composer: '输入消息，与 Agent 对话…',
    },
    ja: {
      aria: 'Agnir インストール会話の例',
      install: 'このプロジェクトに Agnir をインストールして初期化して',
      installed: 'インストール完了。新しいセッションでは「続けて」と言うだけです。',
      continue: '続けて',
      resumed: 'プロジェクト状態を読み込みました。次の作業を続けます。',
      composer: 'Agent にメッセージ…',
    },
    ko: {
      aria: 'Agnir 설치 대화 예시',
      install: '이 프로젝트에 Agnir를 설치하고 초기화해 줘',
      installed: '설치 완료. 새 세션에서는 “계속”이라고 말하면 됩니다.',
      continue: '계속',
      resumed: '프로젝트 상태를 불러왔습니다. 다음 작업을 이어갑니다.',
      composer: 'Agent에게 메시지…',
    },
  };

  const normalizeLanguage = (value) => {
    const language = String(value || '').toLowerCase();
    if (language.startsWith('zh')) return 'zh-CN';
    if (language.startsWith('ja')) return 'ja';
    if (language.startsWith('ko')) return 'ko';
    if (language.startsWith('en')) return 'en';
    return null;
  };

  const readLanguagePreference = () => {
    try {
      const value = window.localStorage.getItem(languageStorageKey);
      return languages[value] ? value : null;
    } catch {
      return null;
    }
  };

  const isRootLanguageEntry = () => {
    const path = window.location.pathname;
    return path.endsWith('/') || path.endsWith('/index.html');
  };

  if (isRootLanguageEntry()) {
    const savedLanguage = readLanguagePreference();
    const detectedLanguage = (navigator.languages || [navigator.language || ''])
      .map(normalizeLanguage)
      .find(Boolean);
    const preferredLanguage = savedLanguage || detectedLanguage || 'en';
    if (preferredLanguage !== 'en') {
      window.location.replace(languages[preferredLanguage].href);
      return;
    }
  }

  const readThemePreference = () => {
    try {
      const value = window.localStorage.getItem(themeStorageKey);
      return value === 'light' || value === 'dark' ? value : null;
    } catch {
      return null;
    }
  };

  const applyTheme = (theme, persist = false) => {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;

    const themeColor = document.querySelector('meta[name="theme-color"]');
    if (themeColor) {
      themeColor.setAttribute('content', theme === 'light' ? '#f6efe7' : '#15110d');
    }

    document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
      const label = theme === 'light' ? button.dataset.darkLabel : button.dataset.lightLabel;
      if (label) {
        button.setAttribute('aria-label', label);
        button.title = label;
      }
    });

    if (persist) {
      try {
        window.localStorage.setItem(themeStorageKey, theme);
      } catch {}
    }
  };

  const languageAriaLabel = (locale) => ({
    en: 'Choose language',
    'zh-CN': '选择语言',
    ja: '言語を選択',
    ko: '언어 선택',
  })[locale] || 'Choose language';

  const createLanguagePicker = () => {
    const currentLanguage = normalizeLanguage(root.lang) || 'en';
    document.querySelectorAll('.site-header nav .lang').forEach((fallbackLink) => {
      const picker = document.createElement('details');
      picker.className = 'language-picker';

      const trigger = document.createElement('summary');
      trigger.className = 'language-trigger';
      const triggerLabel = languageAriaLabel(currentLanguage);
      trigger.setAttribute('aria-label', triggerLabel);
      trigger.title = triggerLabel;

      const badge = document.createElement('span');
      badge.className = 'language-badge';
      badge.dataset.locale = currentLanguage;
      badge.textContent = languages[currentLanguage].badge;
      trigger.appendChild(badge);

      const menu = document.createElement('div');
      menu.className = 'language-menu';
      menu.setAttribute('aria-label', triggerLabel);

      Object.entries(languages).forEach(([locale, language]) => {
        const option = document.createElement('a');
        option.className = 'language-option';
        option.href = language.href;
        option.lang = locale;
        option.dataset.languageChoice = locale;
        if (locale === currentLanguage) option.setAttribute('aria-current', 'page');

        const label = document.createElement('span');
        label.textContent = language.label;
        option.appendChild(label);

        const check = document.createElement('span');
        check.className = 'language-check';
        check.setAttribute('aria-hidden', 'true');
        check.textContent = '✓';
        option.appendChild(check);

        option.addEventListener('click', () => {
          try {
            window.localStorage.setItem(languageStorageKey, locale);
          } catch {}
        });
        menu.appendChild(option);
      });

      picker.append(trigger, menu);
      fallbackLink.replaceWith(picker);
    });

    document.addEventListener('click', (event) => {
      document.querySelectorAll('.language-picker[open]').forEach((picker) => {
        if (!picker.contains(event.target)) picker.removeAttribute('open');
      });
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        document.querySelectorAll('.language-picker[open]').forEach((picker) => picker.removeAttribute('open'));
      }
    });
  };

  const ensureStylesheet = (href, dataAttribute) => {
    if (document.querySelector(`link[${dataAttribute}]`)) return;
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = href;
    stylesheet.setAttribute(dataAttribute, 'true');
    document.head.appendChild(stylesheet);
  };

  const enhanceInstallSection = () => {
    const install = document.querySelector('.install');
    if (!install || install.querySelector('.install-chat-preview')) return;

    ensureStylesheet('install-chat.css', 'data-install-chat-preview');

    const locale = normalizeLanguage(root.lang) || 'en';
    const copy = installPreviewCopy[locale] || installPreviewCopy.en;
    const originalChildren = Array.from(install.children);

    const layout = document.createElement('div');
    layout.className = 'install-layout';

    const content = document.createElement('div');
    content.className = 'install-content';
    originalChildren.forEach((child) => content.appendChild(child));

    const preview = document.createElement('aside');
    preview.className = 'install-chat-preview';
    preview.setAttribute('aria-label', copy.aria);
    preview.innerHTML = `
      <div class="install-chat-chrome">
        <div class="install-chat-agent-title">
          <span class="agent-spark-icon" aria-hidden="true"></span>
          <strong>Agent</strong>
        </div>
        <span class="install-chat-window-dots" aria-hidden="true"><i></i><i></i><i></i></span>
      </div>
      <div class="install-chat-thread">
        <div class="install-chat-message is-user">
          <span class="install-user-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="7.5" r="3.2"></circle><path d="M5.5 20c.8-4.1 3-6.2 6.5-6.2s5.7 2.1 6.5 6.2"></path></svg>
          </span>
          <div class="install-chat-message-body">
            <div class="install-chat-bubble">${copy.install}</div>
            <span class="install-chat-time">10:24</span>
          </div>
        </div>
        <div class="install-chat-message is-agent">
          <span class="agent-spark-icon" aria-hidden="true"></span>
          <div class="install-chat-message-body">
            <div class="install-chat-bubble">${copy.installed}</div>
            <span class="install-chat-time">10:24</span>
          </div>
        </div>
        <div class="install-chat-message is-user">
          <span class="install-user-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="7.5" r="3.2"></circle><path d="M5.5 20c.8-4.1 3-6.2 6.5-6.2s5.7 2.1 6.5 6.2"></path></svg>
          </span>
          <div class="install-chat-message-body">
            <div class="install-chat-bubble">${copy.continue}</div>
            <span class="install-chat-time">10:25</span>
          </div>
        </div>
        <div class="install-chat-message is-agent">
          <span class="agent-spark-icon" aria-hidden="true"></span>
          <div class="install-chat-message-body">
            <div class="install-chat-bubble">${copy.resumed}</div>
            <span class="install-chat-time">10:25</span>
          </div>
        </div>
      </div>
      <div class="install-chat-composer" aria-hidden="true">
        <div class="install-chat-input">${copy.composer}</div>
        <span class="install-chat-send">
          <svg viewBox="0 0 24 24"><path d="M21 3 10.5 13.5"></path><path d="m21 3-6.8 18-3.7-7.5L3 9.8 21 3Z"></path></svg>
        </span>
      </div>`;

    layout.append(content, preview);
    install.replaceChildren(layout);
    install.classList.add('has-chat-preview');
  };

  const loadFreshSessionDemo = () => {
    if (!document.querySelector('.hero-demo')) return;

    if (!document.querySelector('link[data-fresh-session-demo]')) {
      const stylesheet = document.createElement('link');
      stylesheet.rel = 'stylesheet';
      stylesheet.href = 'demo.css';
      stylesheet.dataset.freshSessionDemo = 'true';
      document.head.appendChild(stylesheet);
    }

    if (!document.querySelector('script[data-fresh-session-demo]')) {
      const script = document.createElement('script');
      script.src = 'demo.js';
      script.dataset.freshSessionDemo = 'true';
      document.head.appendChild(script);
    }
  };

  applyTheme(readThemePreference() || (systemTheme.matches ? 'light' : 'dark'));

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
      button.addEventListener('click', () => {
        applyTheme(root.dataset.theme === 'light' ? 'dark' : 'light', true);
      });
    });

    createLanguagePicker();
    enhanceInstallSection();
    applyTheme(root.dataset.theme || 'dark');
    loadFreshSessionDemo();
  });

  const syncSystemTheme = (event) => {
    if (!readThemePreference()) {
      applyTheme(event.matches ? 'light' : 'dark');
    }
  };

  if (typeof systemTheme.addEventListener === 'function') {
    systemTheme.addEventListener('change', syncSystemTheme);
  } else if (typeof systemTheme.addListener === 'function') {
    systemTheme.addListener(syncSystemTheme);
  }
})();
