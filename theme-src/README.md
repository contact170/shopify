# Page « À propos » — Daewoo Security

Fichiers de thème pour `/pages/a-propos`.

| Fichier | Rôle |
| --- | --- |
| `sections/page-a-propos-daewoo.liquid` | Les 13 sections, CSS scopé sous `.dwsa`, JSON-LD à 7 nodes, réglages personnalisateur |
| `templates/page.a-propos.json` | Ne contient que cette section, avec images et produits réels par défaut |

## État

En ligne depuis le 17/08/2026 : thème `201592996180`.

Passe SEO / GEO / Schema publiée le 18/08/2026 (thème `201660629332`).

**Correctif du lien comparateur** déposé sur `A propos v5 - lien comparateur (Claude)` —
`gid://shopify/OnlineStoreTheme/201663971668`, dupliqué du thème publié. En attente de
publication.

- Aperçu : `https://daewoo-security.fr/pages/a-propos?preview_theme_id=201663971668`
- Personnalisateur : `https://admin.shopify.com/store/daewoo-security/themes/201663971668/editor`

Les 3 liens « comparateur » pointent désormais vers `/pages/comparateur-am301-sa501-pa501z`,
la page liée par le menu principal, sur décision du client. `/pages/comparateur-vigilia-touch-elite`
(créée le 08/08, contenu dans le corps de la fiche, jamais modifiée depuis) n'est plus liée
depuis la page À propos.

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

1. Vérifier **quel thème porte le rôle MAIN à cet instant** — il change souvent sur cette
   boutique, et ce n'est pas forcément celui de la veille ;
2. le dupliquer ;
3. **attendre `processing: false`** avant d'écrire : tant que la duplication tourne, elle
   écrase les fichiers déposés ;
4. y réappliquer les fichiers de ce dossier ;
5. vérifier les checksums ;
6. publier.

Les checksums de référence (`md5sum` des fichiers de ce dossier) :

| Fichier | Taille | md5 |
| --- | --- | --- |
| `sections/page-a-propos-daewoo.liquid` | 51 649 | `4776416c86a4c6857a0f24f67f24daa7` |
| `snippets/social-meta-tags.liquid` | 2 655 | `17806c7e0ff99f7291da1373733f0382` |
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

- **Ne pas remettre de retour à la ligne dans un `srcset`** (voir « Corrections notables »).
- **Title et meta description** sont appliqués depuis le 17/08 sur les métachamps de la page
  (`global.title_tag`, `global.description_tag`). Ces champs sont partagés entre tous les thèmes :
  les modifier agit immédiatement sur la page en ligne, quel que soit le thème utilisé.
- **Photos Mérignac** : les trois images par défaut sont celles déjà utilisées par l'ancienne page.
  Leurs attributs ALT annoncent locaux / équipe / préparation des commandes — à vérifier et à
  remplacer dans le personnalisateur si le contenu des photos ne correspond pas.
- **Bloc distributeurs** (section 11) : masqué tant que le réglage `resellers_text` est vide.
- **Identifiants légaux dans le JSON-LD** : le node Liz Invest porte `vatID` FR45791022692 et
  les `identifier` RCS Bordeaux / SIREN 791022692. Ces valeurs correspondent aux mentions
  légales du site. La clé de contrôle 45 du numéro de TVA confirme arithmétiquement le SIREN
  791022692 : `(12 + 3 × (791022692 mod 97)) mod 97 = 45`. Un SIREN 792022692 donnerait FR29.
