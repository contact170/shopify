# Refonte de la page collection ÉLITE (PA501Z)

Page concernée : <https://daewoo-security.fr/collections/systeme-dalarme-pa501z>
(collection « Système d'alarme ÉLITE », gabarit `collection-elite-2`).

Même méthode que la refonte Touch : le HTML/CSS vit dans des fichiers de section
(`sections/el-*.liquid`), le gabarit ne contient plus que des références de type.
L'ancien gabarit faisait 63 Ko de `custom-liquid` en dur ; le nouveau fait 6,3 Ko.

## Angle éditorial

La gamme Élite n'a pas de « duel » à raconter comme Touch / Touch XL : il n'y a
qu'une centrale, la **PA501Z**. L'angle retenu est sa particularité réelle :

> **la centrale qu'on n'a pas besoin de voir** — ni écran, ni clavier sur le boîtier,
> donc un hub qu'on peut cacher, et tout le pilotage dans l'application.

Les trois autres piliers : la **triple connexion** (Wi-Fi / Ethernet / 4G avec
bascule automatique), la **passerelle Zigbee intégrée** (200 accessoires, radio
chiffrée, compatible périphériques Zigbee tiers), et la **confidentialité**
(volontairement incompatible Alexa / Google Home).

## Différenciation visuelle

Pour éviter l'effet copier-coller avec Vigilia et Touch :

| | Touch / Touch XL | Élite |
|---|---|---|
| Accents | bleu `#1c5fd0` + ambre `#8f5d0c` | quasi-monochrome + **teal** `#0a6068` / `#12a0ad` |
| Encre / texte | `#0b1220` / `#4a5a75` | `#0d1520` / `#4b5a63` |
| Bande alternée | froide `#eef2f8` | neutre verte `#f1f3f2` |
| Structures | duel 2 panneaux, tableau comparatif, rail numéroté, frise horaire, bento | chaîne de secours 3 nœuds, schéma Zigbee en SVG, tuiles 3×2, stepper vertical, fiche technique en 6 blocs |

Police commune au thème : **Poppins**. Contraste vérifié : **0 élément sous le
seuil WCAG AA** (le gris secondaire a dû passer de `#6a7883` à `#5c6a75` pour
tenir 4,5:1 sur la bande `#f1f3f2`).

## Structure de la page

1. **Hero** — « La centrale qu'on n'a pas besoin de voir », 4 chiffres clés, CTA packs + centrale seule.
2. **Bandeau de confiance** (fond sombre) — installation 30 min, sans abonnement, SAV France, garantie.
3. **Triple connexion** — Wi-Fi / Ethernet / 4G en chaîne de secours, + batterie de secours et rappel « les caméras ont besoin du Wi-Fi ».
4. **Zigbee** — 4 arguments + **schéma SVG** de la centrale et de ses accessoires (aucune image externe).
5. **Packs** — 3 cartes de hauteur égale : Starter 299,90 € / **Offre exclusive 593,90 €** (mise en avant) / Double caméra 809,90 €.
6. **Anatomie** — bandeau photo + 6 tuiles (ni écran ni clavier, sirène, batterie, arrachement, 4 liaisons, modes + SOS).
7. **Pilotage app** — ce que fait l'application + carte sombre « armer sans téléphone » (télécommande, badge, clavier).
8. **Confidentialité** — pas d'Alexa ni Google Home, par choix ; renvoi vers Touch / Vigilia et le comparateur.
9. **Installation** — stepper vertical 3 étapes + pré-requis + liens manuel et guide d'installation.
10. **Accessoires** — grille de 12 références compatibles, 4 colonnes, **sans défilement horizontal**.
11. **Configurateur** — bandeau sombre horizontal avec **« jusqu'à −25 % »**.
12. **Témoignage** — section partagée `tc-temoignage`.
13. **Avis Judge.me** *(section existante conservée)*.
14. **Fiche technique** — 6 blocs thématiques.
15. **FAQ** — 12 questions, accordéon + balisage `FAQPage` (JSON-LD). CTA vers le formulaire de contact.
16. **CTA final**.

Les sections d'origine remplacées ont été retirées du gabarit ; leur contenu reste
consultable dans `theme-src/collection-elite.base.json` et dans le thème publié.

## Données utilisées

- Centrale **PA501Z** à 199,90 € (SKU DAPA501Z), 4,52/5 sur 152 avis
- Wi-Fi 2,4 GHz, Ethernet RJ45, **module GSM 4G intégré** (carte SIM en option)
- Passerelle **Zigbee** intégrée, jusqu'à **200 accessoires**
- Batterie de secours intégrée, sirène intégrée, détection d'arrachement
- Modes Total / Partiel (Maison) / Désarmé, temporisation, fonction SOS
- **Non compatible Alexa ni Google Home** (choix de conception, mentionné sur la fiche produit)
- Carte SIM M2M Afone 1 an : 85 €
- 12 accessoires actifs de la collection « Compatible gamme Élite »

### Points de vigilance factuels

- **Batterie de secours : la fiche produit annonce 10 h, l'ancienne FAQ 12 h.**
  La page retient **≈ 10 h** dans la fiche technique et dit « une dizaine d'heures »
  ailleurs. À trancher côté produit.
- **Sirène intégrée : 85 dB**, valeur reprise de l'ancienne FAQ de la page.
  Non confirmée par la fiche produit — à valider.
- **Nombre d'accessoires : 200** d'après la fiche de la centrale. Les descriptions
  des deux packs « Offre exclusive » annoncent « jusqu'à 100 accessoires
  supplémentaires ». La page retient 200.
- **Les anciens packs de la page (PA570 Zenguard, PA574 Tranquillité) n'existent
  plus** : les produits correspondants sont archivés. Les trois packs affichés
  sont les produits actifs.
- **Remise configurateur de 25 %** : reprise de la page Touch, le configurateur
  étant le même outil. À confirmer si elle diffère pour l'Élite.
- **La section témoignage parle du système Touch XL** — c'est le contenu existant,
  repris tel quel. À adapter si vous voulez un témoignage Élite.
- **Disponibilité du support** : assistant en ligne 7j/7, équipe 5j/7. Ne jamais
  écrire que l'équipe est joignable au téléphone 7j/7.

## Modifier la page

```bash
python3 theme-src/build-collection-elite.py
```

Le script écrit `sections/el-*.liquid` et
`templates/collection.collection-elite-2.json` à partir de
`theme-src/collection-elite/*.liquid` et de `theme-src/collection-elite.base.json`.

## Aperçu

Thème non publié **« Page ÉLITE PA501Z - refonte (Claude) »** (id `202210017620`),
dupliqué depuis le thème de la refonte Touch — il contient donc **les deux pages** :

<https://daewoo-security.fr/collections/systeme-dalarme-pa501z?preview_theme_id=202210017620>

Le thème publié n'est pas modifié.
