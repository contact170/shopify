# Ménage des pages en double — préparation

Inventaire établi le 18/08/2026 en fin de session, pour le nettoyage prévu le 19/08.
Aucune modification n'a été faite : ce document ne contient que des constats et des
propositions. Les décisions déjà prises sont marquées comme telles.

---

## P1 — Doublons PageFly : le vrai problème

Le catalogue contient des **familles de pages publiées quasi identiques**, générées par
PageFly. Chaque gabarit `pf-*` existe en une trentaine d'exemplaires publiés, numérotés
en suffixe de `-9` à `-37`.

Familles confirmées par requête API :

| Gabarit | Famille | Copies publiées observées |
| --- | --- | --- |
| `pf-fafd78ec` | Assistance AM301 | `-9` à `-37` (29) |
| `pf-1f5b15c1` | Assistance AM302 | `-9` à `-37` (29) |
| `pf-f38cd714` | Assistance Maison connectée | `-9` à `-37` (29) |
| `pf-32de21c8` | Assistance OCT 2023 | `oct-2032` à `oct-2042`+ |

Familles repérées lors d'un inventaire antérieur, à recompter :
`pf-a805143d` (Assistance PA501Z), `pf-194b31cc` (Assistance SA501),
`pf-55a110eb` (Assistance caméras), `pf-b22bc537` (La sécurité n'attend pas),
`pf-f10041b4` (Offre expirée), `pf-48b7c494` (Questions fréquentes),
`pf-cc921caf` (Guide), `pf-13f1764b` (Notre offre),
`pf-c72fce5a` (Formulaire contact assistance).

**Ordre de grandeur : une douzaine de familles × ~29 copies ≈ 350 à 400 pages publiées
en double.** Chiffre à confirmer — l'inventaire n'a pas été mené jusqu'au bout.

C'est de très loin le premier poste : du contenu dupliqué massif, publié, donc
indexable, qui dilue le budget de crawl et brouille la page canonique de chaque sujet.

### Méthode pour l'inventaire complet

```graphql
query {
  pages(first: 50, query: "published_status:published", sortKey: TITLE, after: "<cursor>") {
    nodes { id handle title templateSuffix updatedAt }
    pageInfo { hasNextPage endCursor }
  }
}
```

Paginer jusqu'à `hasNextPage: false`, puis grouper par `templateSuffix`.

### À vérifier avant toute suppression

1. **Laquelle de chaque famille est la bonne ?** Comparer les `updatedAt` et les contenus :
   la copie la plus récente n'est pas forcément celle qui est liée.
2. **Qui pointe vers elles ?** Menus, boutons de fiches produits, e-mails, campagnes,
   QR codes sur les notices papier. Une page d'assistance produit est souvent imprimée
   sur un manuel — supprimer sans redirection casserait le support client.
3. **Sont-elles indexées ?** Vérifier dans Search Console avant/après.

### Action proposée

Pour chaque famille : garder **une** page, rediriger les autres en **301** vers elle,
puis les dépublier. Ne pas supprimer avant d'avoir posé les redirections — une page
supprimée sans 301 renvoie un 404 et perd tout signal.

---

## P2 — Comparateurs : 3 pages, même intention

| URL | État | Détail |
| --- | --- | --- |
| `/pages/comparateur-am301-sa501-pa501z` | **Retenue comme canonique** (décision client, 18/08) | Publiée, gabarit `comparatif-d-alarme`, liée par le menu principal et par les 3 liens de la page À propos |
| `/pages/comparateur-vigilia-touch-elite` | À rediriger | Publiée, sans gabarit — contenu HTML+CSS collé dans le corps de la fiche. Créée le 08/08/2026 à 16:05, jamais modifiée. N'est plus liée depuis À propos |
| `/pages/product-compare` | À examiner | Publiée, gabarit `compare`, intitulée « Product Compare (ne pas supprimer) ». Le nom suggère une dépendance à une application — **vérifier avant toute action** |

Le handle retenu contient `sa501`, référence de la gamme Key qui est arrêtée. Sans effet
technique, mais l'URL décrit une gamme qui n'existe plus. Un renommage poserait une 301
automatique côté Shopify.

---

## P3 — Liens du menu vers des ressources absentes

- `/pages/configurateurs` : **dépubliée**, alors que le menu principal pointe dessus.
  La page vivante est `/pages/configurateur_2` (« Configurez votre alarme »), celle
  qu'utilise la page À propos.
- Collections `systemes-elite` et `offres-du-mois-1` : référencées par les mega-menus,
  **absentes du catalogue** (24 collections au total, aucune ne porte ces handles).

---

## P4 — Anciennes mentions légales

Trois pages, **toutes dépubliées** — donc sans risque immédiat, mais à supprimer pour
éviter une republication accidentelle :

- `mentions-legales`
- `mentions-legales-off`
- `mentions-legales-1` (gabarit `pf-9d6cdb2b`, contient l'ancienne adresse
  *6 rue Léon Morane* et l'ancien téléphone *05 56 31 57 17*)

La source qui fait foi est la politique boutique `/policies/legal-notice`, à jour :
LIZ INVEST – DAEWOO SECURITY, SAS au capital de 10 000 €, 15 Allée James Watt –
Immeuble 2000 Watt, 33700 Mérignac, RCS Bordeaux 791 022 692, TVA FR45791022692,
05 47 74 29 40, contact@daewoo-security.fr, directeur de la publication David Haddad.

---

## P5 — Divers, déjà documentés ailleurs

- `snippets/header-logo.liquid` : microdata `Organization` sans `name` sur toutes les
  pages. Voir `theme-src/README.md`.
- `/pages/daewoo-home-connect` : dépubliée. À republier si on veut la lier depuis la
  page À propos.
- `snippets/vital.liquid` : application d'optimisation chargeant du JavaScript depuis le
  CDN d'une autre boutique, avec du code obfusqué en base64. Suspect n°1 pour les
  `srcset` cassés. À auditer.
- Anciens thèmes à supprimer : les copies `OBSOLETE - *` et les brouillons `(Claude)`
  qui ne servent plus. `themeDelete` est bloqué côté API, à faire depuis l'admin.

---

## Règles de sécurité pour demain

1. **Jamais de suppression sans 301 préalable.**
2. **Vérifier le thème publié avant toute écriture** — il change souvent sur cette
   boutique. Voir la procédure dans `theme-src/README.md`.
3. **Aucune redirection créée sans validation explicite du client.**
4. Traiter famille par famille, en vérifiant après chacune, plutôt qu'un traitement
   global en une passe.
