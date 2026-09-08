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

  applyTheme(readThemePreference() || (systemTheme.matches ? 'light' : 'dark'));

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
      button.addEventListener('click', () => {
        applyTheme(root.dataset.theme === 'light' ? 'dark' : 'light', true);
      });
    });

    createLanguagePicker();
    applyTheme(root.dataset.theme || 'dark');
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
