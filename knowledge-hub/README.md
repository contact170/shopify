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

## À vérifier avant publication

Dans le thème, plusieurs pages se contredisent. Les moteurs génératifs ont besoin d'une source **cohérente**, donc la page retient les valeurs les plus sûres. Il reste à harmoniser le reste du site.

| Point | Constat dans le thème | Choix retenu ici |
|---|---|---|
| Accessoires max. Vigilia | 60 (collection, compare) vs 90 (accueil, comparatif) | 60 (modifiable dans les réglages de la section) |
| Durée de retour | 14 jours (CGV) vs « 30 jours » (badges accueil et collection Vigilia) | 14 jours, la valeur légale des CGV |
| Note moyenne | 4,6/5 (accueil) vs 4,7/5 (collections) | 4,6/5 sur plus de 900 avis (modifiable) |
| Puissance des sirènes | Vigilia 85 ou 90 dB ; Élite 85, 95-100 ou 110 dB | Non affichée |
| Adresse | 6 rue Léon Morane (siège) vs 15 allée James Watt (retours SAV) | Siège social uniquement |
| Horaires du support | Lun-ven 9h30-17h30 vs « 7j/7 » sur l'accueil | Lun-ven 9h30-17h30 (Franck 24h/24) |
| Année de création | « Depuis 2015 » (accueil) ; page À propos : Daewoo « fondée en 1971 » | Aucune date donnée (année à confirmer) |

Les **URLs** sont des réglages de la section, modifiables dans l'éditeur de thème. Les handles suivants ont été déduits des liens du thème et sont **à vérifier** : `/pages/configurateurs`, `/pages/sa501-4g`, `/pages/livraison-retour`, `/pages/questions-frequentes`, `/pages/notices`.
