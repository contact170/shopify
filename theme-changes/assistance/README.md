# Page Assistance — refonte de la présentation

Cible : `https://daewoo-security.fr/pages/assistance-1` (page Shopify `assistance-1`,
template `page.assistance-2`).

## Ce que contient ce dossier

| Fichier | Rôle |
| --- | --- |
| `sections/assistance-intro.liquid` | Nouvelle section « Assistance – Introduction » : message d'explication en haut de page, 3 étapes (Franck / base de connaissances / technicien) et encadré « munissez-vous de votre référence produit ». |
| `sections/assistance-franck.liquid` | Nouvelle section « Assistance – Franck (IA) » : présentation retravaillée de Franck (badge **Assistant IA**, mention explicite qu'il ne s'agit pas d'un technicien humain), checklist « pour une réponse précise, indiquez-lui… », comparaison mauvais / bon exemple de question, bloc WhatsApp + QR Code, et fenêtre de chat Chatbase dans une carte. |
| `templates/page.assistance-2.json` | Nouveau contenu du template : intro → Franck → base de connaissances Gorgias → bandeau W512MW → bandeau prise connectée → bloc « contactez le support ». |

## Bandeaux publicitaires

Les deux bandeaux réutilisent la section **`camera-promo-banner`** déjà présente dans le
thème (celle utilisée sur la collection Caméras), pour rester cohérent avec le reste du site.

1. **W512MW – la 2ᵉ à -50 %** — la remise automatique
   « W512MW – La 2ème à -50% » est active côté Shopify (Achetez 1 article, obtenez 1 article
   avec 50 % de réduction), d'où la mention « sans code à saisir ».
2. **Pack de 3 prises connectées SP502F** — 49,90 € au lieu de 69,90 €
   (prix et prix barré réels de la variante `DASP502FP3`).

## Bloc contact en bas de page

La section native `rich-text` (`rich_text_x8yKyV`), auparavant désactivée, est réactivée
en fin de page : « Votre problème n'est toujours pas résolu ? », explication de ce qu'il
faut mettre dans la demande (référence produit, numéro de commande, ce qui a déjà été
essayé), puis deux boutons — **Ouvrir le formulaire de contact**
(`/pages/nous-contacter`) et **Envoyer une vidéo sur WhatsApp**.

## Hauteur des bandeaux

Les deux bandeaux réutilisent `camera-promo-banner`, partagée avec la collection Caméras :
leur hauteur est réduite via les réglages de l'instance (`min_height: 280`) et un
`custom_css` propre à chaque instance (padding vertical, taille du titre, hauteur d'image).
La section elle-même n'est pas modifiée, la collection Caméras n'est donc pas impactée.

Les prix des bandeaux utilisent des espaces insécables (`&nbsp;`) avant le `€` pour que
le symbole ne parte pas à la ligne.

## Sections conservées

Les anciennes sections de la page sont conservées dans le template mais désactivées
(`"disabled": true`), pour pouvoir revenir en arrière depuis l'éditeur de thème :

- `custom_liquid_6dHA47` — ancienne présentation de Franck ;
- `rich_text_x8yKyV` — bloc « Envoyer une vidéo via WhatsApp » (déjà désactivé auparavant).

## Déploiement

Les fichiers ont été déposés sur un thème **non publié** dupliqué depuis le thème principal,
pour prévisualisation avant mise en ligne.

## Où prévisualiser

- Thème (non publié) : **Assistance v2 - Franck IA + promos (Claude)** — `201716007252`
- Aperçu : `https://daewoo-security.fr/pages/assistance-1?preview_theme_id=201716007252`
- Éditeur : `https://admin.shopify.com/store/daewoo-security/themes/201716007252/editor?previewPath=%2Fpages%2Fassistance-1`

> Le rendu n'a pas pu être vérifié depuis la session (le proxy réseau bloque
> `daewoo-security.fr` et `cdn.shopify.com`) : merci de contrôler l'aperçu avant publication.
