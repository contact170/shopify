# E-mails de notification Shopify

Ces modèles se collent dans **Paramètres › Notifications › E-mails clients ›
Confirmation de commande › Modifier le code**. Shopify n'a pas d'API pour les
modifier : la mise en place est manuelle.

| Fichier | Rôle |
|---|---|
| `confirmation-commande.liquid` | Version à coller dans Shopify |
| `confirmation-commande.avant.liquid` | Version en place au 12/11/2026, à recoller pour revenir en arrière. Le bouton « Rétablir » de Shopify ramène au modèle Shopify d'origine, pas à celle-ci. |

## Changements du 12/11/2026

1. **Rappel point relais.** Si le mode de livraison contient « Point Relai »,
   un encadré « Action requise » s'affiche sous le titre, avec un bouton vers
   la page de commande. Une note sous l'adresse précise que le colis part au
   point relais. L'e-mail part avant que l'application Chronopost Officiel ne
   remplace l'adresse, soit environ 2 minutes après la commande.
2. **Délais concrets** dans « Et maintenant ? », selon le mode de livraison :
   48 à 72 h (Colissimo, point relais), le jour ouvré suivant (Chronopost 18),
   3 à 5 jours (DPD). Les délais viennent de la politique d'expédition de la
   boutique.
3. **Bon guide d'installation** dans « Besoin d'aide ? », reconnu au code
   produit (SKU) des alarmes et packs : Vigilia, Touch (AM301), Touch XL
   (AM302), Élite (PA501Z). Pour les accessoires seuls, le lien mène à la
   page des guides. Le téléphone du SAV est ajouté.
4. **Récapitulatif plus clair** : « dont TVA » sous le total quand les prix
   l'incluent, « Livraison Offerte » à 0 €, « Alma – paiement en 4 fois ».
5. **Finitions** : bouton « Voir ma commande », icônes de réassurance
   harmonisées, adresses non soulignées en bleu sur iPhone.

## Maintenance

- **Nouvelle alarme ou nouveau pack** : la détection repose sur le début du
  SKU. Elle se trouve en tête du fichier, dans le bloc
  `Daewoo Security : variables ajoutées`. Les codes reconnus sont `PK-…`,
  `PSI-…`, `VIG…`, `AM34x`/`AM35x`, `AM301…`/`AM302…`, `PA57x`,
  `PA501…` et `DAPA501Z…`. Un pack sans SKU reconnu est rattrapé par son
  titre s'il commence par « Pack alarme ».
- **Changement d'intitulé du mode point relais** dans l'application
  Chronopost : le rappel s'appuie sur les mots « point relai ». Il faut les
  garder dans l'intitulé, ou adapter la condition `dw_point_relais`.
- **Changement de numéro ou de pages** : le téléphone (05 47 74 29 40) et
  les adresses `/pages/...` sont écrits en clair dans le modèle.
