/** @type {import('tailwindcss').Config} */
export default {
  // The compiled CSS ships as a single theme asset, so every place utility
  // classes actually appear must be scanned — the TS/JS source, the Liquid
  // section markup itself, and the local preview harness.
  content: ['./src/**/*.{ts,html}', '../sections/spatial-hero.liquid', './preview/*.html'],
  // Scope every utility to the section root so the compiled CSS never leaks
  // into the rest of the Shopify theme's global styles.
  important: '#spatial-hero',
  theme: {
    extend: {
      colors: {
        ink: '#04060d',
        navy: '#0c1e4a',
        blue: {
          DEFAULT: '#3d78ef',
          soft: '#6f9bff'
        },
        paper: '#f2f3ff',
        signal: '#ff7a45'
      },
      fontFamily: {
        display: ['"Poppins"', 'sans-serif'],
        body: ['"Poppins"', 'sans-serif']
      },
      transitionTimingFunction: {
        daewoo: 'cubic-bezier(.16,1,.3,1)'
      },
      backdropBlur: {
        card: '20px'
      }
    }
  },
  corePlugins: {
    preflight: false
  },
  plugins: []
};
