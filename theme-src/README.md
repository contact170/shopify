# Page « À propos » — Daewoo Security

Fichiers de thème pour `/pages/a-propos`.

| Fichier | Rôle |
| --- | --- |
| `sections/page-a-propos-daewoo.liquid` | Les 13 sections, CSS scopé sous `.dwsa`, JSON-LD à 7 nodes, réglages personnalisateur |
| `templates/page.a-propos.json` | Ne contient que cette section, avec images et produits réels par défaut |

## État

En ligne depuis le 17/08/2026 : thème `201592996180`.

Passe SEO / GEO / Schema publiée le 18/08/2026 (thème `201660629332`).

**Passe GEO/AEO du 20/08/2026** déposée sur `A propos v6 - GEO/AEO (Claude)` —
`gid://shopify/OnlineStoreTheme/201821356372`, dupliqué du thème publié
`201716007252`. En attente de publication.

- Aperçu : `https://daewoo-security.fr/pages/a-propos?preview_theme_id=201821356372`
- Personnalisateur : `https://admin.shopify.com/store/daewoo-security/themes/201821356372/editor`

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
| `sections/page-a-propos-daewoo.liquid` | 54 504 | `7a29b91cd24eae5988e456401ef6b4d8` |
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

### ⚠️ La page a été supprimée et recréée le 20/08

L'objet page a changé d'identifiant : `97466351829` (supprimé, l'API renvoie `null`) →
`712153596244`. Le handle et donc l'URL sont conservés, mais **tous les métachamps attachés
à l'ancien objet ont disparu**, dont `global.title_tag` et `global.description_tag` — d'où
l'absence de `<meta name="description">` constatée le 20/08. Ils ont été reposés sur le
nouvel identifiant.

Si la page est de nouveau supprimée/recréée, il faudra **repositionner les champs SEO** :
ils ne vivent pas dans le thème et aucune duplication de thème ne les restaure.

### Le nom du fichier de section

Le DOM expose `shopify-section-template--...__a_propos_daewoo`. `a_propos_daewoo` est la
**clé de l'instance de section** dans `templates/page.a-propos.json`, pas un nom de fichier.
Le fichier réel est `sections/page-a-propos-daewoo.liquid`. Un audit lisant le DOM conclut
à tort à l'existence de `sections/a_propos_daewoo.liquid` — la créer produirait une section
en double.

## Points d'attention

- **Ne pas remettre de retour à la ligne dans un `srcset`** (voir « Corrections notables »).
- **Title et meta description** sont appliqués depuis le 17/08 sur les métachamps de la page
  (`global.title_tag`, `global.description_tag`). Ces champs sont partagés entre tous les thèmes :
  les modifier agit immédiatement sur la page en ligne, quel que soit le thème utilisé.
- **Photos Mérignac** : les trois images par défaut sont celles déjà utilisées par l'ancienne page.
  Leurs attributs ALT annoncent locaux / équipe / préparation des commandes — à vérifier et à
  remplacer dans le personnalisateur si le contenu des photos ne correspond pas.
- **Bloc distributeurs** (section 11) : masqué tant que le réglage `resellers_text` est vide.
- **Dates.** Liz Invest SAS est immatriculée depuis **2013** (`foundingDate` sur le nœud
  `#liz-invest`) ; l'exploitation de Daewoo-Security.fr a démarré en **2020**
  (`copyrightYear` sur le nœud `WebSite`, et « depuis 2020 » en texte visible). Ne pas
  confondre les deux : mettre `foundingDate: 2020` sur Liz Invest serait faux et
  contredirait le SIREN.
- **Identifiants légaux dans le JSON-LD** : le node Liz Invest porte `vatID` FR45791022692 et
  les `identifier` RCS Bordeaux / SIREN 791022692. Ces valeurs correspondent aux mentions
  légales du site. La clé de contrôle 45 du numéro de TVA confirme arithmétiquement le SIREN
  791022692 : `(12 + 3 × (791022692 mod 97)) mod 97 = 45`. Un SIREN 792022692 donnerait FR29.
