(() => {
  const storageKey = 'agnir-theme';
  const root = document.documentElement;
  const systemTheme = window.matchMedia('(prefers-color-scheme: light)');

  const readPreference = () => {
    try {
      const value = window.localStorage.getItem(storageKey);
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
        window.localStorage.setItem(storageKey, theme);
      } catch {}
    }
  };

  applyTheme(readPreference() || (systemTheme.matches ? 'light' : 'dark'));

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
      button.addEventListener('click', () => {
        applyTheme(root.dataset.theme === 'light' ? 'dark' : 'light', true);
      });
    });

    applyTheme(root.dataset.theme || 'dark');
  });

  const syncSystemTheme = (event) => {
    if (!readPreference()) {
      applyTheme(event.matches ? 'light' : 'dark');
    }
  };

  if (typeof systemTheme.addEventListener === 'function') {
    systemTheme.addEventListener('change', syncSystemTheme);
  } else if (typeof systemTheme.addListener === 'function') {
    systemTheme.addListener(syncSystemTheme);
  }
})();
