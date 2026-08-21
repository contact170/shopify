# Ménage des pages en double — préparation

Inventaire établi le 18/08/2026 en fin de session, pour le nettoyage prévu le 19/08.
Aucune modification n'a été faite : ce document ne contient que des constats et des
propositions. Les décisions déjà prises sont marquées comme telles.

---

## P1 — Doublons PageFly : RÉSOLU le 21/08/2026

Constat du 18/08 : une douzaine de gabarits `pf-*` existaient chacun en ~29 exemplaires
publiés (`-9` à `-37`), soit de l'ordre de 350 à 400 pages dupliquées et indexables.

**Vérification du 21/08 après mise à jour du thème : ces doublons ont disparu.**
La boutique ne compte plus que **26 pages publiées au total** (`hasNextPage: false`).
Aucune famille numérotée ne subsiste.

### Ce qui reste : 5 pages encore servies par PageFly

| Page | Gabarit | Réassignée le 21/08 à |
| --- | --- | --- |
| Livraison & Retour | `pf-2d5d5021` | 09:32:38 |
| RETOURS SAV | `pf-94ab49fb` | 09:32:41 |
| QUESTIONS FRÉQUENTES | `pf-48b7c494` | 09:32:52 |
| GUIDE | `pf-cc921caf` | 09:33:00 |
| Formulaire Contact assistance | `pf-c72fce5a` | — |

### Pourquoi PageFly reprend la main sur une page refaite sans lui

PageFly tient sa propre base des pages qu'il gère, chacune associée à un identifiant de
page Shopify et à un gabarit `pf-xxxxx`. À chaque synchronisation — mise à jour de l'app,
mise à jour ou publication de thème, publication depuis PageFly — l'app réécrit
`template_suffix` sur ces pages via l'API Admin. Le contenu du corps de la fiche n'est pas
touché : il est simplement **court-circuité**, puisque Shopify rend le gabarit PageFly au
lieu du corps.

Signature caractéristique : plusieurs pages modifiées à quelques secondes d'intervalle
(ici les 4 en 22 secondes), sans intervention humaine.

### Résolution durable

1. **Délier la page depuis PageFly**, pas depuis Shopify. Tant que le mappage existe côté
   app, réassigner le gabarit dans Shopify ne tient que jusqu'à la prochaine synchro.
   ⚠️ À la suppression, PageFly demande s'il faut aussi supprimer la page Shopify :
   répondre non. Sauvegarder le HTML du corps de la fiche avant, par précaution.
2. **Ensuite seulement**, remettre le gabarit voulu côté Shopify (ici : « Page par défaut »).
   L'ordre compte.
3. **Définitif** : une fois les 5 pages ci-dessus refaites, plus rien ne dépend de PageFly.
   L'app peut être désinstallée, et le thème « PageFly Assets - DO NOT DELETE » (2020)
   supprimé avec elle.

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

## P6 — Suppression/recréation de pages

La page « À propos » a été supprimée puis recréée le 20/08 (ancien id `97466351829`,
nouveau `712153596244`). L'URL survit, mais les métachamps SEO de la page sont perdus et
doivent être ressaisis. À garder en tête pendant le ménage : **dépublier n'est pas
supprimer**, et supprimer une page fait perdre ses champs SEO en plus de son URL.

## Règles de sécurité pour demain

1. **Jamais de suppression sans 301 préalable.**
2. **Vérifier le thème publié avant toute écriture** — il change souvent sur cette
   boutique. Voir la procédure dans `theme-src/README.md`.
3. **Aucune redirection créée sans validation explicite du client.**
4. Traiter famille par famille, en vérifiant après chacune, plutôt qu'un traitement
   global en une passe.
