"""Bande-son synthétisée (musique + SFX) pour la vidéo Pack Sécurité Intégrale.

Tout est généré de façon déterministe (graine fixe) : même entrée -> même WAV.
Usage : python3 synth.py frame_starts.json out_dir
frame_starts.json = {"01-hook-0312": 0.0, "02-detecte": 4.0, ...} (secondes globales)
"""
import json
import sys
import wave

import numpy as np

SR = 48000
BPM = 124.0
BEAT = 60.0 / BPM
rng = np.random.default_rng(170)


# ----------------------------------------------------------------- utilitaires
def t_arr(dur):
    return np.arange(int(dur * SR)) / SR


def env_ad(n, a=0.005, d=0.3, curve=4.0):
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-6), np.exp(-(t - a) * curve / max(d, 1e-6)))
    return e


def noise(n):
    return rng.standard_normal(n)


def lowpass(x, fc):
    # one-pole, fc can be scalar or array
    fc = np.broadcast_to(np.asarray(fc, dtype=float), x.shape)
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc = (1 - a[i]) * x[i] + a[i] * acc
        y[i] = acc
    return y


def lp_fast(x, fc):
    """Scalar-cutoff one-pole low-pass via scipy if present (faster)."""
    try:
        from scipy.signal import lfilter
        a = np.exp(-2 * np.pi * fc / SR)
        return lfilter([1 - a], [1, -a], x)
    except Exception:
        return lowpass(x, fc)


def hp_fast(x, fc):
    return x - lp_fast(x, fc)


def bandpass(x, lo, hi):
    return lp_fast(hp_fast(x, lo), hi)


def sine_sweep(f0, f1, dur, curve="exp"):
    n = int(dur * SR)
    if curve == "exp":
        f = f0 * (f1 / f0) ** (np.arange(n) / max(n - 1, 1))
    else:
        f = np.linspace(f0, f1, n)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph), f


def saw(freq, dur):
    t = t_arr(dur)
    out = np.zeros_like(t)
    for k in range(1, 16):
        if freq * k > SR / 2.2:
            break
        out += ((-1) ** (k + 1)) * np.sin(2 * np.pi * freq * k * t) / k
    return out * 0.6


def reverb(x, secs=1.6, mix=0.25, damp=3500):
    n = int(secs * SR)
    ir = noise(n) * np.exp(-np.arange(n) / SR * (6.0 / secs))
    ir = lp_fast(ir, damp)
    ir /= np.sqrt((ir ** 2).sum()) + 1e-9
    try:
        from scipy.signal import fftconvolve
        wet = fftconvolve(x, ir)[: len(x) + n]
    except Exception:
        wet = np.convolve(x, ir)[: len(x) + n]
    dry = np.concatenate([x, np.zeros(n)])
    wet = np.pad(wet, (0, max(0, len(dry) - len(wet))))[: len(dry)]
    return dry * (1 - mix) + wet * mix * 1.4


def norm(x, peak=0.9):
    m = np.max(np.abs(x)) + 1e-9
    return x / m * peak


def note(name):
    names = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6,
             "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
    p, o = name[:-1], int(name[-1])
    return 440.0 * 2 ** ((names[p] + 12 * (o + 1) - 69) / 12)


def mixs(*xs):
    n = max(len(x) for x in xs)
    out = np.zeros(n)
    for x in xs:
        out[: len(x)] += x
    return out


# ----------------------------------------------------------------------- SFX
def sfx_impact(big=1.0):
    d = 1.4
    s, _ = sine_sweep(140, 38, d)
    body = s * env_ad(len(s), 0.002, 0.55 * big, 3.0)
    cr = hp_fast(noise(len(s)), 1200) * env_ad(len(s), 0.001, 0.12, 6)
    return norm(mixs(body, cr * 0.35), 0.95 * min(1, big))


def sfx_sub_boom():
    s, _ = sine_sweep(70, 28, 2.2)
    return norm(s * env_ad(len(s), 0.004, 1.4, 2.5), 0.95)


def sfx_whoosh(dur=0.6, up=True):
    n = int(dur * SR)
    x = noise(n)
    t = np.arange(n) / n
    fc = (300 + 5000 * t) if up else (5000 - 4600 * t)
    y = lowpass(x, fc) - lp_fast(x, 150)
    e = np.sin(np.pi * t) ** 1.5
    return norm(y * e, 0.6)


def sfx_beep(f=2600, dur=0.09, vol=0.45):
    t = t_arr(dur)
    return np.sin(2 * np.pi * f * t) * env_ad(len(t), 0.002, dur * 0.8, 3) * vol


def sfx_key(f=1450):
    return mixs(sfx_beep(f, 0.07, 0.4), sfx_beep(f * 2, 0.05, 0.08))


def sfx_zap():
    s, _ = sine_sweep(4200, 380, 0.28)
    sq = np.sign(s) * 0.4 + s * 0.6
    return norm(sq * env_ad(len(s), 0.001, 0.25, 3) , 0.4)


def sfx_glass():
    t = t_arr(1.2)
    out = np.zeros_like(t)
    for f, a in [(2793, 1), (4186, .6), (5274, .4), (6645, .25)]:
        out += np.sin(2 * np.pi * f * t) * a * np.exp(-t * (5 + f / 1500))
    buzz = np.sin(2 * np.pi * 115 * t) * (np.sin(2 * np.pi * 23 * t) > 0) * np.exp(-t * 2.5) * 0.35
    return norm(out * 0.5 + buzz, 0.5)


def sfx_heartbeat():
    t = t_arr(0.5)
    def thump(delay, amp):
        s, _ = sine_sweep(75, 40, 0.22)
        y = np.zeros_like(t)
        i = int(delay * SR)
        y[i:i + len(s)] += (s * env_ad(len(s), 0.004, 0.18, 4) * amp)[: len(t) - i]
        return y
    return norm(thump(0, 1.0) + thump(0.17, 0.7), 0.85)


def sfx_tick():
    n = int(0.03 * SR)
    return hp_fast(noise(n), 3500) * env_ad(n, 0.0005, 0.02, 6) * 0.35


def sfx_siren(dur):
    t = t_arr(dur)
    f = 760 + 380 * (0.5 - 0.5 * np.cos(2 * np.pi * t / (BEAT * 2)))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.15 * np.sign(np.sin(ph))
    e = np.minimum(1, t / 0.5) * np.minimum(1, (dur - t) / 0.4)
    return norm(lp_fast(x, 5000) * e, 0.32)


def sfx_flash_hit():
    n = int(0.25 * SR)
    a = lp_fast(noise(n), 2500) * env_ad(n, 0.001, 0.12, 5)
    s, _ = sine_sweep(180, 60, 0.25)
    return norm(mixs(a * 0.5, s * env_ad(len(s), 0.001, 0.15, 4)), 0.55)


def sfx_ding(f1=1318.5, f2=1975.5):
    t = t_arr(0.9)
    a = np.sin(2 * np.pi * f1 * t) * np.exp(-t * 6)
    b = np.zeros_like(t)
    i = int(0.09 * SR)
    b[i:] = np.sin(2 * np.pi * f2 * t[: len(t) - i]) * np.exp(-t[: len(t) - i] * 5)
    return norm(a + b + 0.2 * np.sin(2 * np.pi * f2 * 2 * t) * np.exp(-t * 9), 0.5)


def sfx_tap():
    n = int(0.06 * SR)
    return lp_fast(noise(n), 2200) * env_ad(n, 0.0005, 0.03, 6) * 0.5


def sfx_pop():
    s, _ = sine_sweep(900, 320, 0.09)
    c = hp_fast(noise(len(s)), 2500) * env_ad(len(s), 0.0005, 0.01, 8) * 0.4
    return norm(mixs(s * env_ad(len(s), 0.001, 0.07, 4), c), 0.5)


def sfx_ping_up():
    s, _ = sine_sweep(600, 2400, 0.35)
    t = t_arr(0.35)
    m_ = min(len(s), len(t)); return norm((s[:m_] + 0.3 * np.sin(2 * np.pi * 3600 * t[:m_])) * env_ad(m_, 0.004, 0.33, 2.5), 0.45)


def sfx_powerdown():
    d = 0.9
    n = int(d * SR)
    f = 220 * (0.12 ** (np.arange(n) / n))
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = (2 * ((ph / (2 * np.pi)) % 1) - 1)
    hum = np.sin(2 * np.pi * 50 * t_arr(d)) * 0.4
    m_ = min(len(x), len(hum)); return norm(lp_fast(x[:m_] + hum[:m_], 2200) * np.linspace(1, 0, m_) ** 1.3, 0.6)


def sfx_crackle(dur=0.5):
    n = int(dur * SR)
    x = hp_fast(noise(n), 2000)
    gate = (np.sin(np.arange(n) / SR * 2 * np.pi * 37) * np.sin(np.arange(n) / SR * 2 * np.pi * 11.3)) > 0.35
    return norm(x * gate * np.linspace(1, 0.4, n), 0.35)


def sfx_glitch(dur=0.35):
    n = int(dur * SR)
    out = np.zeros(n)
    seg = int(0.03 * SR)
    for k in range(0, n, seg):
        f = [180, 2400, 640, 3900, 90, 1200][(k // seg) % 6]
        tt = np.arange(min(seg, n - k)) / SR
        out[k:k + len(tt)] = np.sign(np.sin(2 * np.pi * f * tt)) * (0.6 if (k // seg) % 3 else 0.2)
    crushed = np.round(out * 4) / 4
    return norm(crushed * np.linspace(1, 0.5, n), 0.35)


def sfx_vibrate(dur=0.45):
    t = t_arr(dur)
    x = np.sin(2 * np.pi * 150 * t) * (np.sin(2 * np.pi * 7 * t) > -0.2)
    return norm(lp_fast(x + 0.3 * noise(len(t)), 600) * np.minimum(1, (dur - t) / 0.05), 0.4)


def sfx_ring():
    t = t_arr(0.6)
    tone = np.sin(2 * np.pi * 1046.5 * t) + np.sin(2 * np.pi * 1318.5 * t)
    gate = ((t % 0.15) < 0.11)
    return norm(tone * gate * np.exp(-t * 1.5), 0.32)


def sfx_drop():
    s, _ = sine_sweep(110, 35, 1.6)
    body = s * env_ad(len(s), 0.003, 1.0, 2.6)
    crash = hp_fast(noise(int(2.0 * SR)), 4000) * env_ad(int(2.0 * SR), 0.002, 1.6, 2.5) * 0.35
    y = np.zeros(int(2.0 * SR))
    y[: len(body)] += body
    y += crash
    return norm(y, 0.95)


def sfx_shimmer():
    t = t_arr(1.4)
    out = np.zeros_like(t)
    for i, f in enumerate([2093, 2637, 3136, 4186, 5274]):
        d = i * 0.06
        m = t >= d
        out[m] += np.sin(2 * np.pi * f * (t[m] - d)) * np.exp(-(t[m] - d) * 4)
    return norm(out, 0.25)


def sfx_ticker(dur=0.9):
    out = np.zeros(int(dur * SR))
    tt = 0.0
    k = 0
    while tt < dur - 0.03:
        i = int(tt * SR)
        tk = sfx_tick() * 1.3
        out[i:i + len(tk)] += tk[: len(out) - i]
        tt += 0.11 * (0.86 ** k) + 0.018
        k += 1
    return out


def sfx_slam():
    a = sfx_impact(1.0)
    n = int(0.6 * SR)
    clap = bandpass(noise(n), 800, 5000) * env_ad(n, 0.001, 0.12, 5)
    y = np.zeros(max(len(a), n))
    y[: len(a)] += a
    y[:n] += clap * 0.6
    return norm(y, 0.95)


def sfx_check_ding():
    return mixs(sfx_ding(1567.98, 2349.3) * 0.9, sfx_pop() * 0.5)


def sfx_strike():
    n = int(0.35 * SR)
    t = np.arange(n) / n
    x = bandpass(noise(n), 1500, 7000) * (np.sin(np.pi * t) ** 0.6)
    return norm(x, 0.4)


def sfx_cash():
    t = t_arr(1.0)
    bell = sum(np.sin(2 * np.pi * f * t) * np.exp(-t * dcy) for f, dcy in [(2637, 4), (3520, 5), (5274, 7)])
    i = int(0.05 * SR)
    clank = np.zeros_like(t)
    c = hp_fast(noise(int(0.08 * SR)), 2500) * env_ad(int(0.08 * SR), 0.001, 0.05, 6)
    clank[:len(c)] += c
    y = np.zeros_like(t)
    y[i:] += bell[: len(t) - i] * 0.5
    return norm(y + clank * 0.6, 0.6)


def sfx_riser(dur):
    n = int(dur * SR)
    t = np.arange(n) / n
    x = lowpass(noise(n), 200 + 9000 * t ** 2)
    s, _ = sine_sweep(110, 880, dur)
    m_ = min(len(x), len(s)); return norm((x[:m_] * 0.7 + s[:m_] * 0.3) * t[:m_] ** 2, 0.5)


def sfx_click():
    n = int(0.05 * SR)
    return mixs(hp_fast(noise(n), 1800) * env_ad(n, 0.0003, 0.015, 7), sfx_beep(1800, 0.05, 0.2)) * 0.8


def sfx_rec_beep():
    return sfx_beep(1000, 0.12, 0.35)


def sfx_drone(dur):
    t = t_arr(dur)
    x = (np.sin(2 * np.pi * 43.65 * t) + 0.5 * np.sin(2 * np.pi * 87.3 * t + 0.3)
         + 0.25 * lp_fast(noise(len(t)), 120))
    e = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.4)
    return norm(x * e, 0.45)


# --------------------------------------------------------------------- musique
def kick():
    s, _ = sine_sweep(150, 45, 0.35)
    return s * env_ad(len(s), 0.001, 0.28, 3.5) * 0.9


def snare():
    n = int(0.25 * SR)
    t = np.arange(n) / SR
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 25)
    nz = bandpass(noise(n), 1500, 8000) * np.exp(-t * 18)
    return (body * 0.5 + nz * 0.8) * 0.6


def hat(open_=False):
    n = int((0.18 if open_ else 0.05) * SR)
    t = np.arange(n) / SR
    return hp_fast(noise(n), 7000) * np.exp(-t * (14 if open_ else 60)) * 0.22


def bass_note(f, dur):
    x = saw(f, dur) + 0.6 * np.sin(2 * np.pi * f / 2 * t_arr(dur))
    x = lp_fast(x, 420)
    return x * env_ad(len(x), 0.004, dur * 0.9, 2.2) * 0.55


def pad(freqs, dur, bright=1800):
    t = t_arr(dur)
    x = np.zeros_like(t)
    for f in freqs:
        for det in (-0.6, 0.0, 0.7):
            x += saw(f * 2 ** (det / 1200 * 10), dur) * 0.18
    x = lp_fast(x, bright)
    e = np.minimum(1, t / 0.25) * np.minimum(1, (dur - t) / 0.3)
    return x * e


def pluck(f, dur=0.22):
    x = saw(f, dur)
    x = lp_fast(x, 3200)
    return x * env_ad(len(x), 0.002, 0.16, 4) * 0.35


def add(buf, sig, at, gain=1.0):
    i = int(round(at * SR))
    if i < 0:
        sig = sig[-i:]
        i = 0
    j = min(len(buf), i + len(sig))
    if j > i:
        buf[i:j] += sig[: j - i] * gain


def build_music(total, fs):
    m = np.zeros(int((total + 3) * SR))
    f = lambda k: fs[k]
    night_end = f("06-le-pack")
    drop = f("06-le-pack")
    f5 = f("05-box-coupee")
    f8 = f("08-offre")
    Fm = [note("F2"), note("Ab2"), note("C3")]
    Db = [note("Db2"), note("F2"), note("Ab2")]
    Eb = [note("Eb2"), note("G2"), note("Bb2")]
    Ab = [note("Ab2"), note("C3"), note("Eb3")]
    # --- partie nuit : battement de cœur, basse pulsée, pad sombre
    t0 = 0.45
    beat_i = 0
    t = t0
    while t < night_end - 0.05:
        bar_pos = beat_i % 4
        in_cut = f5 + 0.5 <= t < f5 + 1.15  # coupure de courant : la musique tombe
        if not in_cut:
            if t >= f("02-detecte") - 0.01:
                add(m, kick(), t, 0.8)
                if bar_pos in (1, 3):
                    add(m, snare(), t, 0.35 if t < f("03-riposte") else 0.55)
            # basse en croches
            root = [note("F1"), note("F1"), note("Db1"), note("Eb1")][(beat_i // 4) % 4]
            for h in (0, 0.5):
                add(m, bass_note(root * (2 if h else 1), BEAT * 0.45), t + h * BEAT, 0.7)
            add(m, hat(), t + 0.5 * BEAT, 0.8)
            if t >= f("03-riposte"):
                add(m, hat(), t + 0.25 * BEAT, 0.5)
                add(m, hat(), t + 0.75 * BEAT, 0.5)
        t += BEAT
        beat_i += 1
    # pad sombre sur la nuit
    chords = [Fm, Fm, Db, Eb]
    tt = 0.0
    k = 0
    while tt < night_end:
        d = min(BEAT * 4, night_end - tt)
        if not (f5 + 0.5 <= tt + d * 0.5 < f5 + 1.15):
            add(m, pad(chords[k % 4], d + 0.05, 900 + 300 * (tt / night_end)), tt, 0.5)
        tt += BEAT * 4
        k += 1
    # --- montée avant le drop
    add(m, sfx_riser(1.6), drop - 1.6, 0.6)
    # --- DROP : beat complet, accords lumineux, arpège
    prog = [Db, Ab, Eb, Fm]
    t = drop
    beat_i = 0
    while t < f8 + 1.9:
        add(m, kick(), t, 1.0)
        if beat_i % 2 == 1:
            add(m, snare(), t, 0.7)
        add(m, hat(True), t + 0.5 * BEAT, 0.7)
        add(m, hat(), t + 0.25 * BEAT, 0.5)
        add(m, hat(), t + 0.75 * BEAT, 0.5)
        ch = prog[(beat_i // 4) % 4]
        for h in (0, 0.5):
            add(m, bass_note(ch[0] / 2 * (2 if h else 1), BEAT * 0.45), t + h * BEAT, 0.8)
        arp = [ch[0] * 4, ch[1] * 4, ch[2] * 4, ch[1] * 4]
        for q in range(4):
            add(m, pluck(arp[q]), t + q * BEAT / 4, 0.55)
        if beat_i % 4 == 0:
            add(m, pad(ch, BEAT * 4 + 0.05, 2600), t, 0.45)
        t += BEAT
        beat_i += 1
    # --- final : grand accord tenu + réverbe
    end_ch = [note("Db2"), note("F2"), note("Ab2"), note("C3"), note("F3")]
    add(m, pad(end_ch, 3.6, 3000), f8 + 1.9, 0.7)
    add(m, bass_note(note("Db1"), 2.5), f8 + 1.9, 0.9)
    add(m, sfx_sub_boom(), f8 + 1.9, 0.6)
    return m


def build_sfx(total, fs):
    s = np.zeros(int((total + 3) * SR))
    F = fs

    def at(frame, local):
        return F[frame] + local

    # F1 — 03:12
    add(s, sfx_drone(F["02-detecte"] + 0.3), at("01-hook-0312", 0.0), 0.7)
    for hb in (0.0, 0.75, 1.5, 2.25, 3.0, 3.6):
        add(s, sfx_heartbeat(), at("01-hook-0312", hb), 0.75)
    add(s, sfx_impact(0.9), at("01-hook-0312", 0.45), 0.9)
    tk = 0.45
    while tk < 1.6:
        add(s, sfx_tick(), at("01-hook-0312", tk), 1.0)
        tk += 0.24
    add(s, sfx_glass(), at("01-hook-0312", 1.95), 0.9)
    add(s, sfx_impact(1.0), at("01-hook-0312", 2.9), 0.9)
    add(s, sfx_glitch(0.2), at("01-hook-0312", 2.9), 0.6)
    add(s, sfx_whoosh(0.5), at("02-detecte", -0.35), 0.8)
    # F2 — détecté
    add(s, sfx_beep(2600, 0.12, 0.5), at("02-detecte", 0.25))
    add(s, sfx_beep(2600, 0.12, 0.4), at("02-detecte", 0.42))
    add(s, sfx_zap(), at("02-detecte", 0.55), 0.9)
    add(s, sfx_key(), at("02-detecte", 1.45))
    add(s, sfx_key(1650), at("02-detecte", 1.6))
    add(s, sfx_whoosh(0.4), at("02-detecte", 1.6), 0.6)
    add(s, sfx_impact(0.8), at("02-detecte", 2.2), 0.85)
    # F3 — riposte
    add(s, sfx_siren(F["04-telephone"] - F["03-riposte"] + 0.3), at("03-riposte", 0.0), 1.0)
    for fl in (0.3, 0.78, 1.26, 1.74, 2.22, 2.7, 3.18):
        add(s, sfx_flash_hit(), at("03-riposte", fl), 0.7)
    add(s, sfx_slam(), at("03-riposte", 1.3), 0.75)
    add(s, sfx_slam(), at("03-riposte", 2.3), 0.85)
    add(s, sfx_sub_boom(), at("03-riposte", 2.3), 0.6)
    # F4 — téléphone
    add(s, sfx_whoosh(0.5), at("04-telephone", 0.05), 0.8)
    add(s, sfx_ding(), at("04-telephone", 0.7), 0.9)
    add(s, sfx_vibrate(0.35), at("04-telephone", 0.75), 0.6)
    add(s, sfx_tap(), at("04-telephone", 1.5), 1.0)
    add(s, sfx_whoosh(0.35), at("04-telephone", 1.55), 0.6)
    add(s, sfx_rec_beep(), at("04-telephone", 1.9))
    add(s, sfx_pop(), at("04-telephone", 2.9), 0.9)
    add(s, sfx_impact(0.6), at("04-telephone", 3.4), 0.7)
    # F5 — box coupée
    add(s, sfx_crackle(0.5), at("05-box-coupee", 0.0), 0.9)
    add(s, sfx_powerdown(), at("05-box-coupee", 0.5), 0.9)
    add(s, sfx_glitch(0.35), at("05-box-coupee", 0.55), 0.8)
    add(s, sfx_ping_up(), at("05-box-coupee", 1.2), 1.0)
    add(s, sfx_vibrate(0.4), at("05-box-coupee", 1.7), 0.7)
    add(s, sfx_ding(1760, 2349.3), at("05-box-coupee", 1.72), 0.5)
    add(s, sfx_ring(), at("05-box-coupee", 2.15), 0.8)
    add(s, sfx_slam(), at("05-box-coupee", 2.5), 0.7)
    # F6 — le pack (le drop est dans la musique)
    add(s, sfx_drop(), at("06-le-pack", 0.0), 0.8)
    add(s, sfx_whoosh(0.45), at("06-le-pack", 0.35), 0.6)
    add(s, sfx_impact(0.5), at("06-le-pack", 1.0), 0.55)
    for c in (1.55, 1.85, 2.15, 2.45, 2.75, 3.05, 3.35, 3.65):
        add(s, sfx_pop(), at("06-le-pack", c), 0.85)
        add(s, sfx_click(), at("06-le-pack", c + 0.01), 0.5)
    add(s, sfx_slam(), at("06-le-pack", 4.2), 0.6)
    add(s, sfx_shimmer(), at("06-le-pack", 5.0), 0.8)
    # F7 — sans abonnement
    add(s, sfx_ticker(0.9), at("07-sans-abonnement", 0.0), 1.0)
    add(s, sfx_slam(), at("07-sans-abonnement", 0.95), 0.95)
    add(s, sfx_impact(0.6), at("07-sans-abonnement", 1.45), 0.6)
    for c in (2.2, 2.7, 3.2):
        add(s, sfx_check_ding(), at("07-sans-abonnement", c), 0.75)
    # F8 — l'offre
    add(s, sfx_riser(1.9), at("08-offre", 0.0), 0.7)
    add(s, sfx_whoosh(0.5), at("08-offre", 0.3), 0.7)
    add(s, sfx_strike(), at("08-offre", 1.3), 0.9)
    add(s, sfx_slam(), at("08-offre", 1.9), 1.0)
    add(s, sfx_cash(), at("08-offre", 1.95), 0.8)
    add(s, sfx_pop(), at("08-offre", 2.6), 0.9)
    add(s, sfx_tick(), at("08-offre", 3.2), 2.0)
    add(s, sfx_click(), at("08-offre", 3.8), 1.0)
    add(s, sfx_shimmer(), at("08-offre", 3.85), 0.6)
    return s


def write_wav(path, x):
    x = np.clip(x, -1, 1)
    st = np.stack([x, x], -1)
    data = (st * 32767).astype("<i2").tobytes()
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data)


def soft_limit(x, drive=1.4):
    return np.tanh(x * drive) / np.tanh(drive)


if __name__ == "__main__":
    fs = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    total = float(fs.pop("_total"))
    music = build_music(total, fs)
    music = reverb(music, 1.2, 0.18)[: len(music)]
    sfx = build_sfx(total, fs)
    sfx = reverb(sfx, 1.0, 0.12)[: len(sfx)]
    n = int(total * SR)
    music, sfx = music[:n], sfx[:n]
    # fondu de sortie
    fade = int(0.6 * SR)
    music[-fade:] *= np.linspace(1, 0, fade)
    sfx[-fade:] *= np.linspace(1, 0, fade)
    mix = norm(music, 0.55) + norm(sfx, 0.85) * 0.95
    mix = soft_limit(mix, 1.6) * 0.92
    write_wav(f"{out}/soundtrack.wav", mix)
    write_wav(f"{out}/music.wav", soft_limit(norm(music, 0.8)))
    write_wav(f"{out}/sfx.wav", soft_limit(norm(sfx, 0.85)))
    print("ok", total, "s")
