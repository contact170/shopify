# Page « Daewoo Home Connect »

Page de présentation de l'application mobile, destinée à la page Shopify existante
`https://daewoo-security.fr/pages/daewoo-home-connect` (handle `daewoo-home-connect`,
actuellement masquée mais génératrice de trafic).

## Fichier

`daewoo-home-connect.html` — bloc HTML + CSS autonome, à coller dans le **corps de la page**
Shopify (éditeur en mode `<>` HTML), comme la page `comparateur-vigilia-touch-elite`.
Tous les styles sont préfixés `.dhc` : aucun risque de conflit avec le thème.

> Note : la page utilise actuellement le suffixe de template `daewoo-home-connect`, qui
> n'existe plus dans le thème principal. Le passer à « Default page » lors de la publication.

## Structure

1. **Hero** — accroche + boutons App Store / Google Play
2. **Télécharger & démarrer** — 3 étapes, captures d'installation, encart autorisations
3. **La page d'accueil** — présentation du dashboard de l'app
4. **Alarme Vigilia / Touch** — modes d'armement, accessoires, historique, réglages
5. **Alarme Élite PA501Z** — zones, Zigbee, supervision réseau, automatisations
6. **Caméras** — direct, PTZ, audio, relecture, détection, mosaïque
7. **Scénarios & tâches** — scénarios manuels vs automatisations « si / alors » + exemples
8. **Prises & objets connectés** — prises, interrupteurs, ampoules, Zigbee
9. **Tableau de compatibilité** — ce que chaque système permet
10. **FAQ** — 7 questions (accordéon natif `<details>`, aucun JavaScript)
11. **Réassurance** + **CTA final**

## Emplacements média (« slots »)

Chaque emplacement est un bloc `data-slot="..."` contenant un placeholder visuel.
Pour l'alimenter, remplacer le contenu du `<div class="slot">…</div>` par une `<img>`
ou une `<video>` (les styles `object-fit` sont déjà en place).

### Captures verticales (mockup téléphone, ratio 9:19.5)

| Slot | Contenu attendu |
|---|---|
| `install-1` … `install-4` | Création de compte · Ajouter un appareil · Choix du produit · Appairage réussi |
| `home-screen` | Page d'accueil de l'application |
| `alarme-vt-main` | Écran principal centrale Vigilia / Touch |
| `alarme-vt-1` … `alarme-vt-4` | Armement · Accessoires · Historique · Réglages |
| `alarme-elite-main` | Écran principal centrale PA501Z |
| `alarme-elite-1` … `alarme-elite-4` | Modes d'armement · Zones · Zigbee · Réseau & batterie |
| `camera-live` | Direct caméra |
| `camera-1` … `camera-4` | Liste caméras · Relecture · Détection · Notification |
| `scenario-1` … `scenario-3` | Liste scénarios · Création « si / alors » · Automatisations |
| `prise-main`, `prise-1` … `prise-3` | Écran prise · Marche/arrêt · Programmation · Consommation |

### Vidéos / visuels larges (ratio 16:9)

| Slot | Contenu attendu |
|---|---|
| `hero-video` | Vidéo de présentation générale de l'application |
| `home-video` | Navigation dans la page d'accueil (screen recording) |
| `alarme-vt-video` | Armement / désarmement Vigilia ou Touch |
| `alarme-elite-video` | Pilotage de la centrale Élite PA501Z |
| `camera-video` | Direct, PTZ et relecture |
| `scenario-video` | Création d'un scénario de A à Z |

### Exemple de remplacement

```html
<!-- avant -->
<div class="phone-screen" data-slot="home-screen">
  <div class="slot">…</div>
</div>

<!-- après -->
<div class="phone-screen" data-slot="home-screen">
  <img src="https://cdn.shopify.com/s/files/.../accueil-app.png" alt="Page d'accueil de l'application Daewoo Home Connect" loading="lazy">
</div>
```

Pour une vidéo :

```html
<div class="slot-wide" data-slot="camera-video">
  <video src="https://cdn.shopify.com/videos/.../cameras.mp4" autoplay muted loop playsinline></video>
</div>
```

## Liens vérifiés

- App Store : https://apps.apple.com/fr/app/daewoo-home-connect/id1491449350
- Google Play : https://play.google.com/store/apps/details?id=com.NewDeal.Homeconnect

## À valider

Les contenus fonctionnels décrits (modes d'armement, zones, suivi de consommation, détection
de silhouette, etc.) ont été rédigés à partir des manuels du site et des fiches produits.
À confirmer écran par écran au fur et à mesure de la réception des captures.
