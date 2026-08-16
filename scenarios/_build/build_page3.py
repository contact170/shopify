#!/usr/bin/env python3
import base64, os
S = "/tmp/claude-0/-home-user-shopify/95706305-7fda-52f3-b4c4-6cba2e324986/scratchpad"
def b64(p, m): return f"data:{m};base64," + base64.b64encode(open(p, "rb").read()).decode()

# ---- media ----
PRISE_VID = b64(f"{S}/scenario_web.mp4", "video/mp4")
PRISE_POS = b64(f"{S}/web/poster.jpg", "image/jpeg")
PRISE_IMG = [b64(f"{S}/web/{i:02d}.jpg", "image/jpeg") for i in range(1, 16)]
CAM_VID   = b64(f"{S}/scenario_camera_web.mp4", "video/mp4")
CAM_POS   = b64(f"{S}/webcam/poster.jpg", "image/jpeg")
CAM_IMG   = [b64(f"{S}/webcam/{i:02d}.jpg", "image/jpeg") for i in range(1, 17)]
VP_IMG    = b64(f"{S}/webcam/vieprivee.jpg", "image/jpeg")
AL_VID    = b64(f"{S}/scenario_alarme_web.mp4", "video/mp4")
AL_POS    = b64(f"{S}/webalarm/poster.jpg", "image/jpeg")
AL_IMG    = [b64(f"{S}/webalarm/{i:02d}.jpg", "image/jpeg") for i in range(1, 13)]
AL_CAPS = ["Sur l'accueil, appuyez sur +","Choisissez « Créer une scène »",
 "« Lorsque le statut de l'appareil change »","Puis « Sélectionner un seul appareil »",
 "Choisissez la caméra IP506P (le déclencheur)","Choisissez « Mouvement détecté »",
 "Validez « Mouvement détecté » → Confirmer","Partie ALORS : appuyez sur +",
 "Sélectionnez « Appareil »","Choisissez l'alarme Vigilia",
 "Choisissez « SOS » puis Confirmer","Enregistrez, puis nommez la scène"]

PRISE_CAPS = ["Sur l'accueil, appuyez sur +","Choisissez « Créer une scène »",
 "« Lorsque le statut de l'appareil change »","Puis « Sélectionner un seul appareil »",
 "Choisissez votre alarme Vigilia","Ouvrez « Mode » → Armer → Confirmer",
 "Partie ALORS : appuyez sur +","Sélectionnez « Appareil »","Puis « Sélectionner un seul appareil »",
 "Choisissez la prise SP502F","Réglez « ON » puis Confirmer","Périmètre de validité → Terminé",
 "Nommez la scène → Confirmer","Test : armez votre Vigilia","La prise s'allume automatiquement"]
CAM_CAPS = ["Sur l'accueil, appuyez sur +","Choisissez « Créer une scène »",
 "« Lorsque le statut de l'appareil change »","Puis « Sélectionner un seul appareil »",
 "Choisissez votre alarme Vigilia","Ouvrez « Mode » → Armer → Confirmer",
 "Partie ALORS : appuyez sur +","Sélectionnez « Appareil »","Puis « Sélectionner un seul appareil »",
 "Choisissez la caméra IP506P Full HD","Choisissez « Détection de mouvement »",
 "Activez la détection : « On » puis Confirmer","Vérifiez le récapitulatif, puis Enregistrer",
 "Nommez la scène → Confirmer","Test : armez votre Vigilia","La détection de mouvement est bien active"]

GRID_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><rect x="3" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="14" y="3" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="3" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/><rect x="14" y="14" width="7" height="7" rx="1.5" stroke="currentColor" stroke-width="2"/></svg>'
SHIELD_SVG = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6l-8-4Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>'
SWAP_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 9a8 8 0 0 1 13-3l3 3M20 15a8 8 0 0 1-13 3l-3-3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 4v5h-5M4 20v-5h5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
EYE_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7Z" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/><path d="M4 4l16 16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
SHIELD_SVG_BIG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6l-8-4Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

CSS = """
<style>
  .sc-full .sc-media{display:grid;grid-template-columns:270px 1fr;gap:24px;align-items:start;margin-bottom:6px}
  .sc-full .video-wrap{border-radius:18px;overflow:hidden;border:1px solid var(--line);box-shadow:var(--shadow);background:#000}
  .sc-full .sc-video{display:block;width:100%;height:auto;background:#000}
  .sc-full .sc-aside .eyebrow{color:var(--accent)}
  .sc-full .sc-aside h4{font-size:19px;margin:10px 0 8px}
  .sc-full .sc-aside p{font-size:14.5px;color:var(--ink-2);margin-bottom:18px}
  .btn-steps{display:inline-flex;align-items:center;gap:11px;font-family:inherit;font-weight:600;font-size:15px;color:#fff;
    background:linear-gradient(135deg,var(--accent),var(--accent-deep));border:0;border-radius:12px;padding:14px 20px;cursor:pointer;box-shadow:var(--shadow-sm);transition:transform .15s}
  .btn-steps:hover{transform:translateY(-1px)}
  .btn-steps .ic{width:22px;height:22px;display:grid;place-items:center}
  .mini-logic{margin-top:18px;font-size:12.5px;font-weight:600;color:var(--accent);background:var(--surface-2);
    border:1px solid var(--line);border-radius:9px;padding:9px 13px;display:inline-flex;gap:8px;align-items:center}
  .gallery{margin-top:24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(188px,1fr));gap:16px}
  .gstep{margin:0;position:relative;background:var(--surface-2);border:1px solid var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--shadow-sm)}
  .gstep img{display:block;width:100%;height:auto}
  .gstep .gnum{position:absolute;top:9px;left:9px;width:27px;height:27px;border-radius:8px;
    background:linear-gradient(135deg,var(--accent),var(--accent-deep));color:#fff;display:grid;place-items:center;font-weight:700;font-size:13px;box-shadow:0 2px 6px rgba(12,30,74,.3)}
  .gstep figcaption{font-size:12.5px;color:var(--ink-2);padding:11px 13px 13px;line-height:1.4}
  .tip-inverse{margin-top:24px;display:grid;grid-template-columns:auto 1fr;gap:16px;align-items:start;
    background:color-mix(in srgb,var(--accent) 9%,var(--surface));border:1px solid color-mix(in srgb,var(--accent) 32%,var(--line));border-radius:16px;padding:20px 22px}
  .tip-inverse .ti-ic{width:44px;height:44px;flex:none;border-radius:12px;display:grid;place-items:center;background:var(--surface);border:1px solid var(--line);color:var(--accent);box-shadow:var(--shadow-sm)}
  .tip-inverse h4{font-size:16px;margin-bottom:6px}
  .tip-inverse p{font-size:14px;color:var(--ink-2)}
  .tip-inverse .swap{display:inline-flex;gap:8px;flex-wrap:wrap;margin-top:12px;font-size:12.5px;font-weight:600}
  .tip-inverse .swap span{padding:6px 11px;border-radius:999px;border:1px solid var(--line);background:var(--surface)}
  .tip-inverse .swap .off{color:var(--armed);border-color:color-mix(in srgb,var(--armed) 40%,transparent)}
  .tip-privacy{margin-top:20px;display:grid;grid-template-columns:132px 1fr;gap:20px;align-items:start;
    background:color-mix(in srgb,#f59e0b 9%,var(--surface));border:1px solid color-mix(in srgb,#f59e0b 42%,var(--line));border-radius:16px;padding:20px 22px}
  .tip-privacy .vp-fig{margin:0}
  .tip-privacy .vp-fig img{width:100%;border-radius:12px;border:1px solid var(--line);box-shadow:var(--shadow-sm)}
  .tip-privacy .vp-fig figcaption{font-size:11.5px;color:var(--muted);margin-top:7px;text-align:center}
  .tip-privacy h4{font-size:16px;margin-bottom:6px;display:flex;align-items:center;gap:9px}
  .tip-privacy h4 .b{color:#b45309}
  .tip-privacy p{font-size:14px;color:var(--ink-2);margin-bottom:6px}
  .warn{margin-top:12px;display:grid;gap:9px}
  .warn div{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start;font-size:13.5px;color:var(--ink)}
  .warn .bang{width:22px;height:22px;flex:none;border-radius:6px;background:#f59e0b;color:#fff;display:grid;place-items:center;font-weight:800;font-size:14px}
  .warn b{color:#b45309}
  .caveat{margin-top:24px;display:grid;grid-template-columns:auto 1fr;gap:16px;align-items:start;
    background:color-mix(in srgb,var(--armed) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--armed) 40%,var(--line));border-radius:16px;padding:20px 22px}
  .caveat .ci{width:44px;height:44px;flex:none;border-radius:12px;display:grid;place-items:center;background:color-mix(in srgb,var(--armed) 14%,transparent);color:var(--armed)}
  .caveat h4{font-size:16px;margin-bottom:6px;color:var(--armed);display:flex;align-items:center;gap:9px}
  .caveat p{font-size:14px;color:var(--ink-2)}
  .caveat .tag-nr{font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--armed);background:color-mix(in srgb,var(--armed) 14%,transparent);border:1px solid color-mix(in srgb,var(--armed) 34%,transparent);padding:3px 9px;border-radius:999px}
  @media(max-width:720px){.sc-full .sc-media{grid-template-columns:1fr;max-width:340px}.tip-privacy{grid-template-columns:1fr;max-width:340px}}
</style>
"""

def gallery(imgs, caps, gid):
    figs = "\n".join(
      f'<figure class="gstep"><span class="gnum">{i+1}</span>'
      f'<img loading="lazy" src="{imgs[i]}" alt="Étape {i+1}">'
      f'<figcaption><b>Étape {i+1}.</b> {caps[i]}</figcaption></figure>' for i in range(len(imgs)))
    return f'<div id="{gid}" class="gallery" hidden>\n{figs}\n</div>'

def toggle(gid, label):
    return (f"var g=document.getElementById('{gid}');var o=g.hasAttribute('hidden');"
            f"if(o){{g.removeAttribute('hidden');}}else{{g.setAttribute('hidden','');}}"
            f"this.setAttribute('aria-expanded',o);"
            f"this.querySelector('.lbl').textContent=o?'Masquer les étapes':'{label}';")

def article(cid, gid, badge, models, title, meta, dur, aside_h, aside_p, btn, logic, video, poster, imgs, caps, notes):
    return f"""
      <article class="scenario reveal sc-full" id="{cid}">
        <div class="sc-head">
          <span class="sc-badge k">{badge}</span>
          <div>
            <h3>{title}</h3>
            <div class="meta">{meta}</div>
          </div>
          <div class="sc-models">{models}</div>
        </div>
        <div class="sc-body">
          <div class="sc-media">
            <div class="video-wrap">
              <video class="sc-video" controls playsinline preload="metadata" poster="{poster}">
                <source src="{video}" type="video/mp4">
                Votre navigateur ne peut pas lire la vidéo.
              </video>
            </div>
            <aside class="sc-aside">
              <span class="eyebrow">En {dur}</span>
              <h4>{aside_h}</h4>
              <p>{aside_p}</p>
              <button class="btn-steps" type="button" aria-expanded="false" aria-controls="{gid}" onclick="{toggle(gid, btn)}">
                <span class="ic">{GRID_SVG}</span><span class="lbl">{btn}</span>
              </button>
              <div class="mini-logic">{SHIELD_SVG} {logic}</div>
            </aside>
          </div>
          {gallery(imgs, caps, gid)}
          {notes}
        </div>
      </article>"""

# ---- notes ----
def inverse_note(cond_off, act_off):
    return f"""<div class="tip-inverse">
            <span class="ti-ic">{SWAP_SVG}</span>
            <div>
              <h4>Astuce&nbsp;: créez le scénario inverse</h4>
              <p>Avec exactement les mêmes étapes, vous pouvez créer le scénario miroir&nbsp;: il suffit de choisir « Désarmer » comme condition et l'état inverse comme action.</p>
              <div class="swap"><span>SI la centrale est <b>{cond_off}</b></span><span class="off">→ ALORS {act_off}</span></div>
            </div>
          </div>"""

PRISE_NOTES = inverse_note("Désarmée", "la prise <b>OFF</b>")

CAM_NOTES = inverse_note("Désarmée", "la détection <b>OFF</b>") + f"""
          <div class="tip-privacy">
            <figure class="vp-fig">
              <img src="{VP_IMG}" alt="Mode Vie privée réglé sur On">
              <figcaption>Action « Mode Vie Privée » → On</figcaption>
            </figure>
            <div>
              <h4>{EYE_SVG}<span>Variante&nbsp;: le <span class="b">Mode Vie privée</span></span></h4>
              <p>Pour la IP506P, vous pouvez aussi créer&nbsp;: <b>SI la centrale est désarmée → ALORS Mode Vie privée ON</b>. La caméra <b>se referme physiquement</b> (l'objectif se masque) pour préserver votre intimité quand vous êtes chez vous.</p>
              <div class="warn">
                <div><span class="bang">!</span><span>Le Mode Vie privée <b>ne coupe PAS la détection de mouvement</b>&nbsp;: il masque seulement l'image. Pour réellement couper la détection, utilisez le scénario inverse ci-dessus (Désarmée → détection OFF).</span></div>
                <div><span class="bang">!</span><span>Avec le Mode Vie privée, <b>créez les deux sens à chaque fois</b>&nbsp;: un scénario pour l'<b>activer</b> (Désarmée → Vie privée ON) <b>et</b> un pour le <b>désactiver</b> (Armée → Vie privée OFF). Sinon la caméra reste fermée en permanence.</span></div>
              </div>
            </div>
          </div>"""

ALARM_NOTES = f"""<div class="caveat">
            <span class="ci"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 9v4m0 4h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            <div>
              <h4>Scénario fonctionnel <span class="tag-nr">Non préconisé</span></h4>
              <p>Ce scénario marche, mais nous ne le recommandons pas&nbsp;: une caméra peut générer des <b>fausses détections</b> (animaux, insectes, ombres, phares de voiture, changements de lumière…) et <b>déclencher l'alarme à tort</b>. Si vous l'utilisez, réservez-le à une zone bien maîtrisée et combinez-le avec l'armement (astuce ci-dessous) pour limiter les fausses alertes.</p>
            </div>
          </div>
          <div class="tip-inverse">
            <span class="ti-ic">{SHIELD_SVG_BIG}</span>
            <div>
              <h4>Astuce&nbsp;: combinez les scénarios</h4>
              <p>Créez d'abord « <b>Détection ON quand l'alarme est armée</b> », puis celui-ci. Ainsi la caméra ne déclenche l'alarme (SOS) <b>que lorsque vous êtes absent</b> (alarme armée) — et jamais quand vous êtes chez vous.</p>
              <div class="swap"><span>1&nbsp;· Détection ON si armée</span><span>2&nbsp;· Mouvement → SOS</span></div>
            </div>
          </div>"""

ALARM = article("sc-alarme","gallery-alarme","Vigilia · IP506P",
    '<span class="model">Caméra IP506P</span><span class="model">Alarme Vigilia</span><span class="model">SOS</span>',
    "Déclencher l'alarme quand la caméra détecte un mouvement",
    "<span>🎬 Vidéo ~24 s</span><span>🖼️ 12 étapes en images</span><span>⭐ Le plus important</span>",
    "24 secondes", "Regardez la vidéo…",
    "…ou déroulez le détail <b>image par image</b>. Ici la <b>caméra est le déclencheur</b> et l'<b>alarme l'action</b>.",
    "Voir les 12 étapes en images", "SI mouvement détecté&nbsp; →&nbsp; ALORS SOS",
    AL_VID, AL_POS, AL_IMG, AL_CAPS, ALARM_NOTES)

CAM = article("sc-camera","gallery-cam","Vigilia · IP506P",
    '<span class="model">VIGILIA</span><span class="model">Caméra IP506P</span>',
    "Activer la détection de la caméra IP506P quand l'alarme est armée",
    "<span>🎬 Vidéo ~30 s</span><span>🖼️ 16 étapes en images</span><span>⭐ Prioritaire</span>",
    "30 secondes", "Regardez la vidéo…",
    "…ou déroulez le détail <b>image par image</b>. Une flèche indique où appuyer à chaque étape.",
    "Voir les 16 étapes en images", "SI armée&nbsp; →&nbsp; ALORS détection ON",
    CAM_VID, CAM_POS, CAM_IMG, CAM_CAPS, CAM_NOTES)

PRISE = article("sc-prise-on","gallery-prise","Vigilia · Prise",
    '<span class="model">VIGILIA</span><span class="model">Prise SP502F</span>',
    "Allumer une prise connectée quand l'alarme est armée",
    "<span>🎬 Vidéo ~30 s</span><span>🖼️ 15 étapes en images</span><span>⭐ Niveau : facile</span>",
    "30 secondes", "Regardez la vidéo…",
    "…ou déroulez le détail <b>image par image</b>, avec la zone à toucher fléchée à chaque étape.",
    "Voir les 15 étapes en images", "SI armée&nbsp; →&nbsp; ALORS prise ON",
    PRISE_VID, PRISE_POS, PRISE_IMG, PRISE_CAPS, PRISE_NOTES)

# ---- inject: replace everything from inside data-panel="key" up to Scenario 2 ----
html = open(f"{S}/scenarios.html", encoding="utf-8").read()
anchor = '<div data-panel="key">'
a = html.index(anchor) + len(anchor)
b = html.index("<!-- Add more -->")
new = html[:a] + "\n\n" + CSS + ALARM + "\n" + CAM + "\n" + PRISE + "\n\n      " + html[b:]
open(f"{S}/scenarios.html", "w", encoding="utf-8").write(new)
print("rebuilt:", len(new), "bytes")
