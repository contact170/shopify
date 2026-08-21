# Page « Caractéristiques techniques officielles des alarmes Daewoo Security »

Page de référence publique, non commerciale, destinée aux clients, à Google et aux
assistants IA. Elle réunit les caractéristiques des quatre centrales : **Vigilia**,
**Touch (AM301)**, **Touch XL (AM302)** et **Élite (PA501Z)**.

## Fichiers livrés

| Fichier | Rôle |
|---|---|
| `sections/caracteristiques-techniques.liquid` | Toute la page : données, mise en forme, données structurées |
| `templates/page.caracteristiques-techniques.json` | Template de page qui appelle la section |

## Installation

1. Dans l'admin Shopify : **Boutique en ligne → Thèmes → … → Modifier le code**.
2. Créer `sections/caracteristiques-techniques.liquid` et y coller le fichier livré.
3. Créer `templates/page.caracteristiques-techniques.json` et y coller le fichier livré.
4. Aller dans **Boutique en ligne → Pages → Ajouter une page**.
   - Titre : `Caractéristiques techniques officielles des alarmes Daewoo Security`
   - Contenu : laisser vide (tout le contenu est dans la section).
   - Modèle de page : `page.caracteristiques-techniques`
   - Handle recommandé : `caracteristiques-techniques`
     → URL finale : `https://daewoo-security.fr/pages/caracteristiques-techniques`
5. Référencement de la page : renseigner la balise titre et la méta-description dans
   l'encart **Référencement des moteurs de recherche** de la page.

Suggestion de méta-description :

> Caractéristiques techniques officielles des centrales d'alarme Daewoo Security :
> Vigilia, Touch AM301, Touch XL AM302 et Élite PA501Z. Connectivité, autonomie,
> sirène, capacités et compatibilité des accessoires. Source officielle mise à jour.

## Mettre à jour une caractéristique

Toutes les données sont regroupées en haut de la section, dans les blocs `capture rows_*`.

Format d'une ligne :

```
Libellé~Vigilia~Touch~Touch XL~Élite~code source
```

Codes source, affichés sous forme de pastille à côté du libellé :

| Code | Pastille | Signification |
|---|---|---|
| `M` | bleue **M** | Valeur issue du manuel officiel |
| `F` | grise **F** | Valeur issue de la fiche produit ou du catalogue |
| `X` | jaune **?** | Valeur en cours de vérification |

Les valeurs `Oui`, `Non`, `À confirmer` et `Non documenté…` sont colorées
automatiquement. Aucun autre fichier n'est à modifier.

**Après chaque correction**, mettre à jour les deux dates dans les réglages de la
section (personnalisateur de thème) :
- *Date affichée sur la page* — exemple : `4 septembre 2026`
- *Date au format ISO* — exemple : `2026-09-04` (lue par Google et les assistants IA)

## Origine des données

Les valeurs marquées `M` proviennent des manuels déjà publiés sur la boutique :

- `/pages/manuel-vigilia`
- `/pages/manuel-am301`
- `/pages/manuel-touch-xl-am302`
- `/pages/manuel-elite`

Les valeurs marquées `F` proviennent des fiches produits et pages de collection.

## Points à vérifier avant communication commerciale

Ces valeurs sont **contradictoires entre les documents existants du site**. La page les
affiche comme « à confirmer » plutôt que d'arbitrer à tort. À trancher en interne :

1. **Autonomie de la batterie Touch (AM301)** — le site indique selon les pages
   4 h, 3 à 6 h, ou 30 h.
2. **Autonomie de la batterie Touch XL (AM302)** — 20 h annoncées, non confirmées
   par le manuel.
3. **Autonomie de la centrale Élite (PA501Z)** — le manuel indique 3 à 24 h selon
   l'usage, plusieurs pages annoncent 12 h.
4. **Autonomie de la centrale Vigilia** — environ 4 h annoncées ; le manuel ne donne
   que la capacité de la batterie (1500 mAh).
5. **Nombre maximal d'accessoires** — le site annonce 60 accessoires pour Vigilia et
   90 pour Touch, alors que les manuels AM301 et AM302 documentent 160 capteurs,
   6 télécommandes, 6 sonnettes et 6 claviers. Il faut décider si les chiffres
   commerciaux correspondent à une limite recommandée ou s'ils sont à corriger.
6. **Génération du module mobile** des centrales Vigilia + et Touch : les documents
   parlent de GSM, les fiches produits de « GSM 4G ».

Une fois ces points tranchés, remplacer la valeur dans le bloc de données concerné et
faire passer le code source de `X` à `M` ou `F`.

## Liens internes recommandés

La page n'a pas vocation à figurer dans le menu principal. Pour qu'elle soit trouvée
par les clients et citée par les moteurs, ajouter un lien depuis :

- le comparatif des gammes (`/pages/comparatif-d-alarme`)
- les pages de collection de chaque gamme (Vigilia, Touch, Élite)
- les fiches produits des centrales
- la page d'assistance (`/pages/assistance-1`)
- le pied de page, dans la colonne « Aide » ou « À propos »
- les articles de blog traitant du choix d'une alarme

Libellé de lien suggéré : **« Voir les caractéristiques techniques officielles »**.

## Données structurées incluses

- `TechArticle` avec `dateModified` — identifie la page comme document technique daté.
- `FAQPage` avec 6 questions/réponses — Ethernet, fonctionnement sans Internet,
  compatibilité des accessoires, puissance des sirènes, Wi-Fi 5 GHz, application.

Ces deux blocs se mettent à jour automatiquement à partir des réglages de la section.
