import { defineConfig } from 'vite';

// Bundles the Spatial Hero experience straight into the theme's assets/
// folder, matching how every other script/stylesheet in this theme is
// served (asset_url + <script>/<link> tags in the section, no server-side
// bundling on Shopify's end).
export default defineConfig({
  build: {
    outDir: '../assets',
    emptyOutDir: false,
    cssCodeSplit: false,
    lib: {
      entry: 'src/main.ts',
      name: 'DaewooSpatialHero',
      formats: ['iife'],
      fileName: () => 'spatial-hero.js'
    },
    rollupOptions: {
      output: {
        // cssCodeSplit is off, so there is exactly one CSS asset — name it
        // to match what the Liquid section actually requests.
        assetFileNames: (asset) => (asset.name?.endsWith('.css') ? 'spatial-hero.css' : 'spatial-hero-[name][extname]')
      }
    },
    minify: 'esbuild',
    sourcemap: false
  }
});
