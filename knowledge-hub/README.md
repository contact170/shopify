# Knowledge Hub Daewoo Security

Page de référence **« Tout savoir sur les alarmes Daewoo Security »**.
Elle sert d'abord à décrire l'entité Daewoo Security aux moteurs de recherche et aux moteurs génératifs (SEO / GEO). La conversion vient en second.

## Fichiers

| Fichier | Rôle |
|---|---|
| `sections/knowledge-hub.liquid` | Section autonome : contenu factuel rendu côté serveur, sommaire à ancres, tableaux, FAQ et JSON-LD |
| `templates/page.knowledge-hub.json` | Template de page qui utilise la section |

## Contenu de la page

1. Fiche d'identité, sous forme de liste de définitions (le format le plus simple à extraire pour un LLM)
2. Qui distribue la marque en France : Liz Invest SAS, sous licence officielle Daewoo
3. Où se trouve l'équipe : Mérignac, métropole bordelaise
4. Les gammes : Vigilia, Touch AM301, Touch XL AM302, Élite PA501Z, Key SA501 et passage à la 4G, caméras, domotique
5. L'application Daewoo Home Connect
6. Le modèle sans abonnement, avec les options facultatives SIM Afone et Cloud présentées en toute transparence
7. Les technologies : 433/868 MHz, Wi-Fi, 4G, RJ45, Zigbee 3.0, batterie de secours
8. Les compatibilités : Alexa, Google Home, Zigbee, accessoires
9. Le support : formulaire, e-mail, WhatsApp, Franck, SAV
10. Les garanties : 2 ans, rétractation de 14 jours
11. La documentation : notices, vidéos, FAQ, assistance
12. Les liens vers le comparateur, le configurateur, le quiz et le guide
13. Une FAQ « entité » de 7 questions

**Données structurées (JSON-LD `@graph`) :** `Organization` (raison sociale, RCS, TVA, adresse, contactPoint, sameAs), `Brand`, `MobileApplication`, `AboutPage` (avec `about` et `mainEntity` qui pointent vers l'organisation) et `FAQPage`.
Le thème ne contenait jusqu'ici **aucun JSON-LD Organization**. Seule une microdonnée existait sur le logo.

## Installation

1. Ajouter les deux fichiers au thème : Boutique en ligne → Thèmes → `…` → Modifier le code.
   - Dans **Sections**, ajouter une section `knowledge-hub`.
   - Dans **Templates**, ajouter un template `page` nommé `knowledge-hub`.
2. Créer la page : Boutique en ligne → Pages → Ajouter une page.
   - Titre : `Tout savoir sur les alarmes Daewoo Security`
   - Template : `page.knowledge-hub`
   - Handle conseillé : `tout-savoir-daewoo-security`
   - Méta-description conseillée : *« Daewoo Security : alarmes sans abonnement sous licence Daewoo, distribuées par Liz Invest (Mérignac, Bordeaux). Gammes, application, garanties, support. »*
3. Ajouter un lien vers la page dans le footer (par exemple « À propos de Daewoo Security »). Sans lien interne, la page sera mal découverte.
4. Tester la page avec l'outil Google *Rich Results Test* et le *Schema Markup Validator*.

## Valeurs validées (à reporter sur le reste du site)

| Point | Valeur officielle |
|---|---|
| Accessoires max. | Vigilia 60 · Touch/Touch XL 90 · Élite 200 |
| Retours | 14 jours |
| Note moyenne | 4,6/5 |
| Sirène intégrée | 85-90 dB (Vigilia, Touch, Élite) |
| Sirène extérieure (option) | 105-110 dB |
| Adresse | 15 allée James Watt, Immeuble 2000 Watt, 33700 Mérignac |
| Support humain | Lundi-vendredi, 9h30-17h30 |
| Assistant IA (Franck) | 7j/7, 24h/24 |

Pages du thème encore en contradiction : badges « Retours 30 jours » (accueil, collection Vigilia), « jusqu'à 90 accessoires » pour Vigilia (accueil, comparatif d'alarme), 4,7/5 (collections, comparatif), dB des sirènes (collections, compare), « Support technique 7j/7 » sur l'accueil (à reformuler en « Assistant IA 7j/7 »), adresse Léon Morane dans les mentions légales et la page Livraison & Retour.

Année de création : non indiquée (« depuis 2015 » sur l'accueil, à confirmer).

Les **URLs** sont des réglages de la section, modifiables dans l'éditeur de thème. Handles déduits des liens du thème, **à vérifier** : `/pages/configurateurs`, `/pages/sa501-4g`, `/pages/livraison-retour`, `/pages/questions-frequentes`, `/pages/notices`.
