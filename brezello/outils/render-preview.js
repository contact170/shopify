// Rend le modèle product.brezello.json avec liquidjs et des données produit fictives,
// puis assemble une page d'aperçu autonome (CSS, JS et polices intégrés).
const fs = require('fs');
const path = require('path');
const { Liquid } = require('liquidjs');

const THEME = process.argv[2];
const OUT = process.argv[3];

const engine = new Liquid({ root: [path.join(THEME, 'snippets')], extname: '.liquid', strictFilters: true });

// Filtres Shopify simulés
engine.registerFilter('money', (v) => (v == null ? '' : '[Prix] €'));
engine.registerFilter('asset_url', (name) => '__ASSET__/' + name);
engine.registerFilter('stylesheet_tag', (url) => '<link rel="stylesheet" href="' + url + '">');
engine.registerFilter('image_url', (img) => String(img || ''));
engine.registerFilter('image_tag', (url) => '<img src="' + url + '" alt="">');
engine.registerFilter('payment_button', () => '');

// Balise {% form %} simulée
engine.registerTag('form', {
  parse(tagToken, remainTokens) {
    this.args = tagToken.args;
    this.tpls = [];
    let closed = false;
    while (remainTokens.length) {
      const token = remainTokens.shift();
      if (token.name === 'endform') { closed = true; break; }
      this.tpls.push(this.liquid.parser.parseToken(token, remainTokens));
    }
    if (!closed) throw new Error('form non fermé');
  },
  * render(ctx, emitter) {
    const idExpr = (/id:\s*([\w.]+)/.exec(this.args) || [])[1];
    const id = idExpr ? ctx.getSync(idExpr.split('.')) : '';
    const cls = (/class:\s*'([^']*)'/.exec(this.args) || [])[1] || '';
    emitter.write('<form method="post" action="/cart/add" id="' + id + '" accept-charset="UTF-8" class="' + cls + '" enctype="multipart/form-data" novalidate="novalidate"><input type="hidden" name="form_type" value="product"><input type="hidden" name="utf8" value="✓">');
    yield this.liquid.renderer.renderTemplates(this.tpls, ctx, emitter);
    emitter.write('</form>');
  }
});

// Produit fictif : 4 parfums x 3 formats, une offre d'abonnement
const parfums = ['Glaciale', 'Agrumi', 'Dolce', 'Calma'];
const formats = ['Solo', 'Duo', 'Pack de 4'];
let vid = 4400000000;
const variants = [];
for (const p of parfums) for (const f of formats) {
  vid += 1;
  variants.push({ id: vid, title: p + ' / ' + f, options: [p, f], option1: p, option2: f, available: true, price: 1490, compare_at_price: null, featured_media: null });
}
const product = {
  id: 9000000001,
  title: 'Inhaler nasal Brezello',
  handle: 'inhaler-nasal-brezello',
  url: '/products/inhaler-nasal-brezello',
  description: '<p>Un boîtier de poche à deux embouts, un pour chaque narine. Sa mèche imprégnée de menthol et d\'huiles essentielles libère ses arômes dès que vous retirez les capuchons.</p><p>Sans nicotine, sans batterie, sans vapeur.</p>',
  media: [],
  featured_media: null,
  has_only_default_variant: false,
  options_with_values: [
    { name: 'Parfum', position: 1, values: parfums, selected_value: 'Glaciale' },
    { name: 'Format', position: 2, values: formats, selected_value: 'Solo' }
  ],
  variants,
  selected_or_first_available_variant: variants[0],
  requires_selling_plan: false,
  selling_plan_groups: [
    { name: 'Livraison régulière', selling_plans: [{ id: 6900001, name: 'Livraison tous les 30 jours · −[X] %', description: 'Sans engagement, modifiable ou annulable à tout moment' }] }
  ],
  price: 1490
};

const template = JSON.parse(fs.readFileSync(path.join(THEME, 'templates/product.brezello.json'), 'utf8'));
const schemas = {};

async function renderSection(key) {
  const conf = template.sections[key];
  const file = path.join(THEME, 'sections', conf.type + '.liquid');
  let src = fs.readFileSync(file, 'utf8');
  const m = /\{%-?\s*schema\s*-?%\}([\s\S]*?)\{%-?\s*endschema\s*-?%\}/.exec(src);
  if (!m) throw new Error('schéma manquant : ' + conf.type);
  const schema = JSON.parse(m[1]); // valide le JSON du schéma
  schemas[conf.type] = schema;
  src = src.replace(m[0], '');
  // Paramètres de section : valeurs du modèle, sinon valeurs par défaut du schéma
  const settings = {};
  for (const s of schema.settings || []) if (s.id) settings[s.id] = s.default;
  Object.assign(settings, conf.settings || {});
  const blocks = (conf.block_order || []).map((id) => {
    const b = conf.blocks[id];
    const def = (schema.blocks || []).find((x) => x.type === b.type);
    if (!def) throw new Error('type de bloc inconnu ' + b.type + ' dans ' + conf.type);
    const bs = {};
    for (const s of def.settings || []) if (s.id) bs[s.id] = s.default;
    for (const k of Object.keys(b.settings || {})) {
      if (!def.settings.find((s) => s.id === k)) throw new Error('réglage inconnu ' + k + ' dans le bloc ' + b.type);
    }
    Object.assign(bs, b.settings || {});
    return { id, type: b.type, settings: bs, shopify_attributes: '' };
  });
  for (const k of Object.keys(conf.settings || {})) {
    if (!(schema.settings || []).find((s) => s.id === k)) throw new Error('réglage inconnu ' + k + ' dans ' + conf.type);
  }
  const section = { id: 'template--brezello__' + key, settings, blocks };
  const html = await engine.parseAndRender(src, { product, section, routes: { all_products_collection_url: '/collections/all' } });
  return '<div id="shopify-section-' + section.id + '" class="shopify-section">' + html + '</div>';
}

(async () => {
  const parts = [];
  for (const key of template.order) parts.push(await renderSection(key));
  let body = parts.join('\n');
  // Les feuilles et scripts du thème sont intégrés une seule fois dans l'aperçu
  body = body.replace(/<link rel="stylesheet" href="__ASSET__\/[^"]+">/g, '').replace(/<script src="__ASSET__\/[^"]+" defer="defer"><\/script>/g, '');
  const leftover = body.match(/\{\{|\{%|__ASSET__/g);
  if (leftover) throw new Error('Liquid non rendu dans la sortie : ' + leftover.length);

  let css = fs.readFileSync(path.join(THEME, 'assets/brezello.css'), 'utf8');
  for (const f of ['bz-bricolage.woff2', 'bz-dmmono-400.woff2', 'bz-dmmono-500.woff2']) {
    const b64 = fs.readFileSync(path.join(THEME, 'assets', f)).toString('base64');
    css = css.replace('url("' + f + '")', 'url("data:font/woff2;base64,' + b64 + '")');
  }
  const js = fs.readFileSync(path.join(THEME, 'assets/brezello.js'), 'utf8');
  const shell = fs.readFileSync(path.join(__dirname, 'preview-shell.html'), 'utf8');
  const page = shell.replace('/*BZ_CSS*/', () => css).replace('<!--BZ_BODY-->', () => body).replace('/*BZ_JS*/', () => js);
  fs.writeFileSync(OUT, page);
  console.log('OK', OUT, Math.round(page.length / 1024) + ' Ko', 'sections:', Object.keys(schemas).join(', '));
})().catch((e) => { console.error('ERREUR', e.message); process.exit(1); });
