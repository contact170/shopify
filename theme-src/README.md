# Page « À propos » — Daewoo Security

Fichiers de thème pour `/pages/a-propos`.

| Fichier | Rôle |
| --- | --- |
| `sections/page-a-propos-daewoo.liquid` | Les 13 sections, CSS scopé sous `.dwsa`, JSON-LD à 5 nœuds, réglages personnalisateur |
| `templates/page.a-propos.json` | Ne contient que cette section, avec images et produits réels par défaut |

## État

En ligne depuis le 17/08/2026 : thème `201592996180`.

**Passe SEO / GEO / Schema du 18/08/2026** déposée sur le thème de prévisualisation
`A propos v3 - SEO + Schema (Claude)` — `gid://shopify/OnlineStoreTheme/201639133524`,
dupliqué du thème publié. En attente de publication.

- Aperçu : `https://daewoo-security.fr/pages/a-propos?preview_theme_id=201639133524`
- Personnalisateur : `https://admin.shopify.com/store/daewoo-security/themes/201639133524/editor`

Fichiers modifiés dans cette passe :

| Fichier | Portée | Objet |
| --- | --- | --- |
| `sections/page-a-propos-daewoo.liquid` | page À propos | srcset, lazy-loading, contenus, JSON-LD à 7 nodes |
| `snippets/social-meta-tags.liquid` | **tout le site** | `og:image` en https, `twitter:site` vide supprimé, `twitter:image` ajouté |

### Corrections notables

- **`srcset` sur une seule ligne.** Les `srcset` multi-lignes étaient réécrits et cassés
  (`600w,,,,`). Le coupable probable est `snippets/vital.liquid`, un snippet injecté par une app
  d'optimisation qui charge `lazysizes.min.js` depuis un CDN tiers. Ne pas réintroduire de
  retour à la ligne à l'intérieur d'un attribut `srcset`.
- **`loading="lazy"` explicite** sur les 6 images sous la ligne de flottaison. L'ancienne version
  s'appuyait sur une injection `replace: "<img", "<img loading='lazy' "` présente dans
  `layout/theme.liquid` **de l'export du 18 mai** ; cette injection n'existe plus dans le layout
  en ligne. La balise hero est donc repassée en `<img>` minuscule (le contournement `<IMG>` n'a
  plus lieu d'être).
- **FAQ : source unique.** Les 8 questions/réponses sont déclarées une seule fois dans
  `assign faq_questions` / `assign faq_answers`, puis rendues à la fois en HTML et en JSON-LD.
  Le schéma ne peut donc plus diverger du visible. Ne pas éditer l'un sans l'autre : éditer les
  deux `assign`.

### Recommandation non appliquée

`snippets/header-logo.liquid` porte un `itemscope itemtype="http://schema.org/Organization"`
sans `name`, sur toutes les pages. C'est une entité Organization incomplète, mais le JSON-LD
complet la supplante. Retirer les attributs `itemscope`, `itemtype`, `itemprop="url"` et
`itemprop: 'logo'` de ce snippet reste souhaitable — non fait ici : le rapport bénéfice/risque
d'une réécriture d'un snippet présent sur tout le site ne le justifiait pas.

### Pour une prochaine mise en ligne

Ne jamais publier un thème de prévisualisation ancien : c'est un instantané, et le publier
écraserait tout ce qui a été fait sur le thème en ligne depuis sa création. Procédure :

1. Dupliquer le thème **publié à cet instant** ;
2. y réappliquer les deux fichiers de ce dossier ;
3. vérifier les checksums ;
4. publier.

Les checksums de référence (`md5sum` des fichiers de ce dossier) :

| Fichier | Taille | md5 |
| --- | --- | --- |
| `sections/page-a-propos-daewoo.liquid` | 51 709 | `50c06beb0547691398f721b67fec8568` |
| `templates/page.a-propos.json` | 922 | `c16b8cb4900adb720cc09ad03b3e6ccc` |

### Envoyer une mise à jour d'un fichier volumineux

`themeFilesUpsert` accepte `body: { type: URL }`, mais **uniquement** une URL hébergée par
Shopify : une URL externe (y compris `raw.githubusercontent.com`) est refusée silencieusement —
`upsertedThemeFiles: []` et `userErrors: []`, sans rien écrire. Le passage par un upload staged
donne un transfert exact :

1. `stagedUploadsCreate` avec `resource: FILE`, `mimeType: text/plain`, `httpMethod: PUT`
2. `curl -X PUT --data-binary @<fichier>` vers l'`url` signée renvoyée
3. `themeFilesUpsert` avec `body: { type: URL, value: <resourceUrl> }`
4. Vérifier avec `theme { files(filenames: [...]) { nodes { size checksumMd5 } } }` et comparer
   au `md5sum` local

Les petits fichiers passent très bien en `body: { type: TEXT }`.

## Points d'attention

- **`layout/theme.liquid` ligne 70** injecte `loading='lazy'` dans tout `<img` du contenu de page.
  Un attribut HTML dupliqué gardant sa première valeur, un `loading="eager"` y serait annulé.
  Le visuel hero utilise donc une balise `<IMG>` en majuscules : le filtre `replace` de Liquid est
  sensible à la casse, ce qui préserve la priorité de chargement de l'image LCP. Ne pas
  « corriger » cette casse sans retirer l'injection du layout.
- **Title et meta description** ne sont pas modifiés : ces champs sont des métachamps de la page
  (`global.title_tag`, `global.description_tag`), partagés entre tous les thèmes. Les changer
  affecterait immédiatement la page en ligne. À faire au moment de la publication :
  - Title : `Daewoo Security | Alarmes connectées sans abonnement`
  - Meta : `Découvrez Daewoo Security, spécialiste des alarmes, caméras et systèmes de sécurité connectée sans abonnement. Équipe et siège basés à Mérignac.`
- **Photos Mérignac** : les trois images par défaut sont celles déjà utilisées par l'ancienne page.
  Leurs attributs ALT annoncent locaux / équipe / préparation des commandes — à vérifier et à
  remplacer dans le personnalisateur si le contenu des photos ne correspond pas.
- **Bloc distributeurs** (section 11) : masqué tant que le réglage `resellers_text` est vide.
