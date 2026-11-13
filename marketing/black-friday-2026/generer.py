# -*- coding: utf-8 -*-
"""Génère les 3 e-mails HTML de la campagne Black Friday 2026.

Pour changer l'offre (pourcentage, code, date de fin), modifier les
constantes ci-dessous puis relancer :  python3 generer.py
Les fichiers .html du dossier sont alors réécrits.
"""
from pathlib import Path

# --- Offre (à valider par le dirigeant) ------------------------------------
REMISE = "-10&nbsp;%"
CODE = "BLACKFRIDAY26"
FIN = "lundi 30&nbsp;novembre à&nbsp;23h59"
FIN_COURT = "jusqu'au 30/11 à&nbsp;23h59"

SITE = "https://daewoo-security.fr"
EMAIL_CONTACT = "contact@daewoo-security.fr"
LOGO = ("https://cdn.shopify.com/s/files/1/0326/3132/4811/files/"
        "daewoo-Correct_logo_8e380760-43ca-4080-b60d-5338106491e2.jpg"
        "?v=1680770505&width=360")

# Couleurs du thème Shopify (config/settings_data.json)
MARINE = "#0c1e4a"
FOND = "#f2f3ff"
BLEU_PRIX = "#1a4fab"
ROUGE = "#e11d48"
TEXTE = "#1f2a44"
GRIS = "#5b6582"
BORDURE = "#e1e5f5"

DOSSIER = Path(__file__).resolve().parent


def lien_remise(chemin="/"):
    """Lien qui applique le code automatiquement puis redirige."""
    return f"{SITE}/discount/{CODE}?redirect={chemin}"


PRODUITS = [
    {
        "titre": "Pack Alarme Vigilia avec caméra",
        "accroche": "L'essentiel pour démarrer, piloté depuis votre smartphone",
        "prix": "dès 139,90&nbsp;€",
        "barre": "",
        "image": "https://cdn.shopify.com/s/files/1/0326/3132/4811/files/958b5e1e-36cd-47db-93da-efc4b7f2d77c.jpg?v=1770108516&width=480",
        "chemin": "/products/daewoo-vigilia-starter-pack",
    },
    {
        "titre": "Système d'alarme Touch",
        "accroche": "Centrale à écran tactile, Wi-Fi et 4G",
        "prix": "dès 199,90&nbsp;€",
        "barre": "",
        "image": "https://cdn.shopify.com/s/files/1/0326/3132/4811/files/AM302_TouchXL_Starter_Pack.jpg?v=1787740224&width=480",
        "chemin": "/products/alarme-daewoo-wifi-gsm-4g-starter-pack-am301",
    },
    {
        "titre": "Pack Sécurité Intégrale",
        "accroche": "Alarme + caméra extérieure solaire rotative",
        "prix": "369,90&nbsp;€",
        "barre": "",
        "image": "https://cdn.shopify.com/s/files/1/0326/3132/4811/files/PSI-VIGILIA-1WRC-W512MW-agrandie.webp?v=1790686139&width=480&format=jpg",
        "chemin": "/products/pack-alarme-securite-integrale",
    },
    {
        "titre": "Pack ÉLITE",
        "accroche": "Offre exclusive, compatible animaux",
        "prix": "593,90&nbsp;€",
        "barre": "794,20&nbsp;€",
        "image": "https://cdn.shopify.com/s/files/1/0326/3132/4811/files/PA5012601-003_1.png?v=1770973567&width=480",
        "chemin": "/products/offre-exclusive-pack-elite-compatible-animaux-sans-abonnement",
    },
]

POLICE = "'Poppins', Arial, Helvetica, sans-serif"
SALUTATION = ("Bonjour{% if customer.first_name != blank %} "
              "{{ customer.first_name }}{% endif %},")


# --- Briques communes ------------------------------------------------------
def page(titre, preheader, contenu):
    return f"""<!DOCTYPE html>
<html lang="fr" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{titre}</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  body {{ margin:0; padding:0; background:{FOND}; }}
  a {{ color:{BLEU_PRIX}; }}
  @media only screen and (max-width:620px) {{
    .conteneur {{ width:100% !important; }}
    .marge {{ padding-left:20px !important; padding-right:20px !important; }}
    .col {{ display:block !important; width:100% !important; padding:0 0 16px 0 !important; }}
    .titre-hero {{ font-size:38px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background:{FOND};">
<!-- Texte d'aperçu (affiché sous l'objet dans la boîte de réception) -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{FOND};">{preheader}{'&zwnj;&nbsp;' * 60}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{FOND};">
<tr><td align="center" style="padding:24px 12px;">
<table role="presentation" class="conteneur" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;background:#ffffff;border-radius:12px;overflow:hidden;">
<tr><td align="center" style="padding:28px 32px 24px 32px;">
  <a href="{SITE}" style="text-decoration:none;"><img src="{LOGO}" width="180" alt="Daewoo Security" style="display:block;width:180px;height:auto;border:0;"></a>
</td></tr>
{contenu}
</table>
<table role="presentation" class="conteneur" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
<tr><td class="marge" align="center" style="padding:24px 32px;font-family:{POLICE};font-size:12px;line-height:1.6;color:{GRIS};">
  Daewoo Security · Alarmes et caméras connectées sans abonnement<br>
  <a href="{SITE}" style="color:{GRIS};">daewoo-security.fr</a> · <a href="mailto:{EMAIL_CONTACT}" style="color:{GRIS};">{EMAIL_CONTACT}</a><br>
  * Livraison offerte dès 50&nbsp;€ d'achat en France métropolitaine et en Belgique.<br>
  Vous recevez cet e-mail car vous avez accepté de recevoir les offres de Daewoo Security.
  <!-- Shopify Email ajoute automatiquement le lien de désinscription et l'adresse de la boutique.
       Avec un autre outil (Klaviyo, Brevo…), insérez ici sa balise de désinscription. -->
</td></tr>
</table>
</td></tr>
</table>
</body>
</html>
"""


def hero(etiquette, sous_titre):
    return f"""<tr><td class="marge" align="center" style="background:{MARINE};padding:40px 32px 36px 32px;font-family:{POLICE};">
  <div style="font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#b9c6ec;font-weight:600;">{etiquette}</div>
  <div class="titre-hero" style="font-size:46px;line-height:1.1;font-weight:700;color:#ffffff;margin:12px 0 16px 0;letter-spacing:1px;">BLACK FRIDAY</div>
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tr>
    <td style="background:{ROUGE};border-radius:999px;padding:8px 20px;font-size:20px;font-weight:700;color:#ffffff;">{REMISE} sur tout le site</td>
  </tr></table>
  <div style="font-size:15px;line-height:1.5;color:#dfe6fb;margin-top:16px;">{sous_titre}</div>
</td></tr>"""


def paragraphe(html, haut=0, bas=16):
    return (f'<p style="margin:{haut}px 0 {bas}px 0;font-family:{POLICE};'
            f'font-size:16px;line-height:1.65;color:{TEXTE};">{html}</p>')


def bloc_texte(*paragraphes, haut=32):
    return (f'<tr><td class="marge" style="padding:{haut}px 40px 8px 40px;">'
            + "\n".join(paragraphes) + "</td></tr>")


def boite_code(note=None):
    note = note or f"{REMISE} sur toute la commande, sans minimum d'achat · {FIN_COURT}"
    return f"""<tr><td class="marge" style="padding:8px 40px 8px 40px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{FOND};border:2px dashed {MARINE};border-radius:10px;">
  <tr><td align="center" style="padding:20px 16px;font-family:{POLICE};">
    <div style="font-size:13px;color:{GRIS};letter-spacing:1px;text-transform:uppercase;">Votre code</div>
    <div style="font-size:28px;font-weight:700;color:{MARINE};letter-spacing:3px;margin:6px 0;">{CODE}</div>
    <div style="font-size:13px;line-height:1.5;color:{GRIS};">{note}</div>
  </td></tr></table>
</td></tr>"""


def bouton(texte, lien, haut=24, bas=8):
    return f"""<tr><td align="center" style="padding:{haut}px 40px {bas}px 40px;">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
    <td align="center" bgcolor="{ROUGE}" style="background:{ROUGE};border-radius:8px;">
      <a href="{lien}" style="display:inline-block;padding:16px 32px;font-family:{POLICE};font-size:16px;font-weight:700;color:#ffffff;text-decoration:none;border-radius:8px;">{texte}</a>
    </td>
  </tr></table>
</td></tr>"""


def lien_secondaire(texte, lien):
    return f"""<tr><td align="center" style="padding:4px 40px 8px 40px;font-family:{POLICE};font-size:15px;">
  <a href="{lien}" style="color:{BLEU_PRIX};font-weight:600;">{texte}</a>
</td></tr>"""


def reassurance():
    points = [
        ("Sans abonnement", "Vous payez votre matériel une fois, c'est tout"),
        ("Garantie 2&nbsp;ans", "Sur tous nos produits achetés neufs"),
        ("Livraison offerte*", "Dès 50&nbsp;€, expédiée sous 24 à 48&nbsp;h ouvrées"),
        ("14&nbsp;jours pour changer d'avis", "Retour et rétractation faciles"),
    ]
    cellules = []
    for titre, texte in points:
        cellules.append(
            f'<td class="col" width="50%" valign="top" style="padding:0 8px 16px 8px;font-family:{POLICE};">'
            f'<div style="font-size:15px;font-weight:600;color:{MARINE};">'
            f'<span style="color:{ROUGE};">&#10003;</span>&nbsp; {titre}</div>'
            f'<div style="font-size:13px;line-height:1.5;color:{GRIS};padding-left:22px;">{texte}</div></td>')
    lignes = f"<tr>{cellules[0]}{cellules[1]}</tr><tr>{cellules[2]}{cellules[3]}</tr>"
    return f"""<tr><td class="marge" style="padding:24px 32px 8px 32px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid {BORDURE};padding-top:24px;">
  <tr><td style="padding-top:24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{lignes}</table></td></tr>
  </table>
</td></tr>"""


def signature(texte_avant=""):
    avant = paragraphe(texte_avant) if texte_avant else ""
    return f"""<tr><td class="marge" style="padding:16px 40px 36px 40px;">
  {avant}
  {paragraphe("À très vite,<br><strong>L'équipe Daewoo Security</strong>", bas=0)}
</td></tr>"""


def carte_produit(p):
    barre = (f' <span style="font-size:13px;font-weight:400;color:#8a93ad;'
             f'text-decoration:line-through;">{p["barre"]}</span>') if p["barre"] else ""
    lien = lien_remise(p["chemin"])
    return f"""<td class="col" width="50%" valign="top" style="padding:0 8px 16px 8px;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid {BORDURE};border-radius:10px;">
  <tr><td align="center" style="padding:12px 12px 0 12px;">
    <a href="{lien}"><img src="{p['image']}" width="220" alt="{p['titre']}" style="display:block;width:100%;max-width:220px;height:auto;border:0;"></a>
  </td></tr>
  <tr><td style="padding:12px 16px 16px 16px;font-family:{POLICE};">
    <div style="font-size:15px;font-weight:600;line-height:1.35;color:{MARINE};">{p['titre']}</div>
    <div style="font-size:13px;line-height:1.45;color:{GRIS};margin:4px 0 10px 0;">{p['accroche']}</div>
    <div style="font-size:17px;font-weight:700;color:{BLEU_PRIX};">{p['prix']}{barre}</div>
    <div style="margin-top:10px;"><a href="{lien}" style="font-size:14px;font-weight:600;color:{ROUGE};text-decoration:none;">Voir le pack &rarr;</a></div>
  </td></tr></table>
</td>"""


def grille_produits():
    c = [carte_produit(p) for p in PRODUITS]
    return f"""<tr><td class="marge" style="padding:16px 32px 0 32px;">
  <div style="font-family:{POLICE};font-size:20px;font-weight:700;color:{MARINE};padding:0 8px 16px 8px;">Nos packs les plus choisis</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    <tr>{c[0]}{c[1]}</tr>
    <tr>{c[2]}{c[3]}</tr>
  </table>
  <div style="font-family:{POLICE};font-size:12px;line-height:1.5;color:{GRIS};padding:0 8px;">Prix affichés avant remise. Les {REMISE} s'appliquent au panier avec le code {CODE} (automatiquement si vous passez par les liens de cet e-mail).</div>
</td></tr>"""


# --- E-mail 1 : devis non finalisés (accès anticipé) ------------------------
def email_devis():
    mailto = (f"mailto:{EMAIL_CONTACT}?subject=Mon%20devis%20au%20prix%20Black%20Friday")
    etapes = f"""<tr><td class="marge" style="padding:24px 40px 0 40px;">
  <div style="font-family:{POLICE};font-size:20px;font-weight:700;color:{MARINE};margin-bottom:12px;">Comment en profiter&nbsp;?</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
    {''.join(
        f'<tr><td valign="top" width="36" style="padding:0 0 14px 0;">'
        f'<div style="width:26px;height:26px;line-height:26px;border-radius:13px;background:{MARINE};color:#ffffff;'
        f'font-family:{POLICE};font-size:13px;font-weight:700;text-align:center;">{n}</div></td>'
        f'<td valign="top" style="padding:2px 0 14px 0;font-family:{POLICE};font-size:15px;line-height:1.6;color:{TEXTE};">{t}</td></tr>'
        for n, t in [
            (1, "<strong>Répondez simplement à cet e-mail.</strong> Nous vous renvoyons votre devis recalculé au prix Black Friday, avec un lien de paiement sécurisé."),
            (2, "<strong>Ou commandez directement sur le site</strong> avec le code ci-dessus&nbsp;: le bouton plus bas l'applique automatiquement."),
            (3, "<strong>Votre projet a évolué&nbsp;?</strong> Une pièce en plus, un garage, un animal à la maison… Nos techniciens ajustent votre configuration gratuitement."),
        ])}
  </table>
</td></tr>"""
    contenu = "\n".join([
        hero("Accès anticipé · Réservé à nos demandes de devis",
             f"Votre configuration à prix réduit jusqu'au {FIN}"),
        bloc_texte(
            paragraphe(SALUTATION),
            paragraphe("Il y a quelque temps, vous nous avez demandé un devis pour protéger votre logement. "
                       "Nous espérons que votre réflexion avance bien."),
            paragraphe("Avant l'ouverture officielle du Black Friday vendredi, nous vous réservons un "
                       f"<strong>accès anticipé</strong>&nbsp;: dès aujourd'hui et jusqu'au {FIN}, "
                       f"votre configuration bénéficie de <strong>{REMISE}</strong>, sans minimum d'achat."),
        ),
        boite_code(),
        etapes,
        bouton("Recevoir mon devis au prix Black Friday", mailto, haut=16),
        lien_secondaire("Ou commander directement sur le site &rarr;", lien_remise("/")),
        reassurance(),
        signature("Une question avant de vous décider&nbsp;? Notre équipe technique, basée près de "
                  "Bordeaux, connaît bien votre devis et vous répond avec plaisir."),
    ])
    return page("Black Friday : votre devis en accès anticipé",
                f"Votre devis à {REMISE} avant tout le monde, {FIN_COURT}. Sans abonnement, garantie 2 ans.",
                contenu)


# --- E-mail 2 : comptes créés sans achat ------------------------------------
def email_comptes():
    atouts = f"""<tr><td class="marge" style="padding:8px 40px 0 40px;">
  <div style="font-family:{POLICE};font-size:20px;font-weight:700;color:{MARINE};margin:16px 0 12px 0;">Pourquoi choisir Daewoo Security&nbsp;?</div>
  {''.join(
      f'<div style="font-family:{POLICE};font-size:15px;line-height:1.6;color:{TEXTE};margin-bottom:12px;">'
      f'<span style="color:{ROUGE};font-weight:700;">&#10003;</span>&nbsp; <strong>{t}</strong> {d}</div>'
      for t, d in [
          ("Aucun abonnement.", "Vous achetez votre matériel une fois, puis vous gardez la main sur votre sécurité depuis votre smartphone."),
          ("Sans fil, sans travaux.", "Vous installez vous-même votre alarme, sans faire venir de technicien."),
          ("Une équipe à vos côtés.", "Nos techniciens, basés près de Bordeaux, vous conseillent avant l'achat et vous accompagnent après."),
      ])}
</td></tr>"""
    contenu = "\n".join([
        hero(f"Du vendredi 27 au {FIN.split(' à')[0]}",
             "Alarmes et caméras connectées, sans abonnement"),
        bloc_texte(
            paragraphe(SALUTATION),
            paragraphe("Vous avez créé votre compte sur notre site&nbsp;: peut-être êtes-vous encore en train "
                       "de comparer les solutions pour protéger votre logement."),
            paragraphe(f"Bonne nouvelle&nbsp;: pendant le Black Friday, <strong>tout le site est à {REMISE}</strong>, "
                       "sans minimum d'achat. C'est le bon moment pour vous équiper avant les départs des fêtes."),
        ),
        boite_code(),
        bouton("Je découvre les offres", lien_remise("/"), haut=24, bas=16),
        atouts,
        grille_produits(),
        bloc_texte(
            paragraphe("<strong>Vous ne savez pas quelle configuration choisir&nbsp;?</strong> "
                       "Notre configurateur vous guide pièce par pièce selon votre logement. "
                       "Et si vous préférez en parler, répondez simplement à cet e-mail."),
            haut=24),
        bouton("Composer mon alarme", lien_remise("/pages/configurateur_2"), haut=0, bas=8),
        reassurance(),
        signature(),
    ])
    return page("Black Friday Daewoo Security",
                f"{REMISE} sur tout le site, {FIN_COURT}. Livraison offerte dès 50 €, garantie 2 ans.",
                contenu)


# --- E-mail 3 : relance commune, dernier jour (Cyber Monday) ---------------
def email_relance():
    contenu = "\n".join([
        hero("Dernier jour", f"L'offre se termine ce soir à&nbsp;23h59"),
        bloc_texte(
            paragraphe(SALUTATION),
            paragraphe("Le Black Friday se termine ce soir à minuit. Si vous pensiez sécuriser votre "
                       f"logement avant l'hiver, c'est le dernier moment pour profiter de <strong>{REMISE}</strong> "
                       "sur tout le site, sans minimum d'achat."),
        ),
        boite_code(f"{REMISE} sur toute la commande · <strong>se termine ce soir à&nbsp;23h59</strong>"),
        bouton("J'en profite avant minuit", lien_remise("/"), haut=24, bas=8),
        lien_secondaire("Composer mon alarme avec le configurateur &rarr;", lien_remise("/pages/configurateur_2")),
        bloc_texte(
            paragraphe("<strong>Vous aviez demandé un devis&nbsp;?</strong> Répondez à cet e-mail avant ce soir&nbsp;: "
                       "nous vous le renvoyons au prix Black Friday, avec un lien de paiement sécurisé."),
            haut=24),
        reassurance(),
        signature("Une dernière question avant de commander&nbsp;? Répondez à cet e-mail, notre équipe vous répond."),
    ])
    return page("Black Friday : dernier jour",
                f"Le Black Friday se termine ce soir à minuit. Votre code : {CODE}",
                contenu)


if __name__ == "__main__":
    fichiers = {
        "1-devis-acces-anticipe.html": email_devis(),
        "2-comptes-sans-achat.html": email_comptes(),
        "3-relance-dernier-jour.html": email_relance(),
    }
    for nom, html in fichiers.items():
        (DOSSIER / nom).write_text(html, encoding="utf-8")
        print(f"{nom} : {len(html.encode('utf-8')) // 1024} Ko")
