import os
import random
from html import escape

NAVY = "#0b1020"
NAVY2 = "#16203b"
PANEL = "#121a2e"
LINE = "#26324d"
LINE2 = "#4a5a85"
INK = "#e9edf7"
MUTED = "#8d99b5"
EYEBROW = "#7b88a8"
GOLD = "#f2c14e"
EMBER = "#ff8a5b"
ICE = "#8fb8ff"
PAPER = "#f4f1e8"
SLATE = "#2a3556"

SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

NS = 'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'

ICONS = {
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/>',
    "code": '<path d="M8 7l-5 5 5 5"/><path d="M16 7l5 5-5 5"/><path d="M14 4l-4 16"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "bug": '<ellipse cx="12" cy="14" rx="5" ry="6"/><path d="M9 8.5a3 3 0 0 1 6 0"/><path d="M12 8v12"/><path d="M7 11L3 9"/><path d="M7 15H3"/><path d="M7 19l-3 2"/><path d="M17 11l4-2"/><path d="M17 15h4"/><path d="M17 19l3 2"/><path d="M9.5 5.5L8 3"/><path d="M14.5 5.5L16 3"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/>',
    "badge": '<path d="M12 2l3 2.5 4-.3.7 4L22 12l-2.3 3.8-.7 4-4-.3L12 22l-3-2.5-4 .3-.7-4L2 12l2.3-3.8.7-4 4 .3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c3 3 3 15 0 18"/><path d="M12 3c-3 3-3 15 0 18"/>',
    "github": '<circle cx="6" cy="6" r="2.5"/><circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="9" r="2.5"/><path d="M6 8.5v7"/><path d="M18 11.5c0 3.5-4 4.5-9.3 5.4"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V16"/><path d="M12 16v-5.5"/><path d="M12 13c0-3 4-3 4 0v3"/><circle cx="8" cy="7.5" r=".6"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6"/>',
    "radar": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><path d="M12 12L19 5"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "book": '<path d="M3 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H3z"/><path d="M21 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0"/><path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r=".8"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9"/><path d="M16 7l3 3"/><path d="M14 9l2 2"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="1"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "network": '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/><path d="M12 7v5"/><path d="M12 12L6 17.2"/><path d="M12 12l6 5.2"/>',
    "database": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "terminal": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 10l3 2.5-3 2.5"/><path d="M12 16h5"/>',
    "flag": '<path d="M5 21V4"/><path d="M5 4h12l-2 4 2 4H5"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.5 3-6 6.5-6s6.5 2.5 6.5 6"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.5 0 4.5 2 4.5 5"/>',
}

ICON_ATTR = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'


def icon(name, x, y, size, color, sw=1.6):
    k = size / 24.0
    return (
        f'<g transform="translate({x},{y}) scale({k:g})" stroke="{color}" stroke-width="{sw}" {ICON_ATTR}>'
        f'{ICONS[name]}</g>'
    )


def sparkle(cx, cy, s, fill, extra=""):
    d = "M0,-1 Q0.1,-0.1 1,0 Q0.1,0.1 0,1 Q-0.1,0.1 -1,0 Q-0.1,-0.1 0,-1Z"
    return f'<path d="{d}" fill="{fill}" transform="translate({cx:g},{cy:g}) scale({s:g})"{extra}/>'


def twinkle(values, dur, begin):
    return (
        f'<animate attributeName="opacity" values="{values}" dur="{dur:g}s" '
        f'begin="{begin:g}s" repeatCount="indefinite"/>'
    )


def svg(w, h, body, title, defs=""):
    return (
        f'<svg {NS} width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
        f'<title>{escape(title)}</title><defs>{defs}</defs>{body}</svg>'
    )


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def stars_field(rng, w, h, n, avoid=None):
    out = []
    for _ in range(n):
        x = rng.uniform(8, w - 8)
        y = rng.uniform(8, h - 8)
        if avoid and avoid(x, y):
            continue
        r = rng.choice([0.7, 0.9, 1.1, 1.4, 1.8])
        col = rng.choice([INK, INK, ICE, PAPER, GOLD])
        dur = rng.uniform(2.4, 6.5)
        beg = -rng.uniform(0, 6)
        lo = rng.choice([0.15, 0.25, 0.35])
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" opacity="0.7">'
            f'{twinkle(f"0.7;{lo};1;0.7", dur, beg)}</circle>'
        )
    return "".join(out)


def constellation(nodes, edges, packets, seed):
    rng = random.Random(seed)
    lines = "".join(
        f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" '
        f'stroke="{LINE2}" stroke-width="1" opacity="0.65"/>'
        for a, b in edges
    )
    dots = []
    for i, (x, y) in enumerate(nodes):
        col = GOLD if i % 3 == 0 else ICE
        dots.append(f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{LINE2}" stroke-width="1" opacity="0.7"/>')
        dots.append(
            f'<circle cx="{x}" cy="{y}" r="3" fill="{col}">'
            f'{twinkle("1;0.45;1", rng.uniform(2.5, 5), -rng.uniform(0, 4))}</circle>'
        )
    pk = []
    for idx, (a, b) in enumerate(packets):
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        dur = 3.2 + (idx % 3) * 0.9
        pk.append(
            f'<circle r="2.4" fill="{GOLD}"><animateMotion dur="{dur:g}s" begin="{-idx * 1.3:g}s" '
            f'repeatCount="indefinite" path="M{x1},{y1} L{x2},{y2}"/></circle>'
        )
    return lines + "".join(dots) + "".join(pk)


def bug_mark(cx, cy, size, color, sw=1.7):
    return icon("bug", cx - size / 2, cy - size / 2, size, color, sw)


def hero():
    w, h = 1200, 580
    rng = random.Random(7)
    sx, sy = 600, 168

    def avoid(x, y):
        return (x - sx) ** 2 + (y - sy) ** 2 < 125 ** 2 or (360 < x < 840 and 300 < y < 530)

    left_nodes = [(70, 120), (150, 70), (215, 160), (130, 230), (60, 320), (190, 340), (265, 250), (120, 440), (250, 470)]
    left_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (3, 4), (3, 5), (2, 6), (6, 5), (5, 7), (5, 8), (7, 8)]
    left_pk = [(0, 1), (2, 3), (3, 5), (5, 8), (2, 6)]
    right_nodes = [(1130, 110), (1050, 60), (985, 150), (1070, 220), (1140, 310), (1010, 330), (935, 245), (1085, 430), (960, 470)]
    right_edges = left_edges
    right_pk = [(1, 2), (3, 0), (3, 4), (5, 7), (6, 5)]

    sticker = (
        f'<g>'
        f'<animateTransform attributeName="transform" type="translate" values="{sx},{sy};{sx},{sy - 7};{sx},{sy}" '
        f'dur="5s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
        f'<g transform="rotate(-6)">'
        f'<circle r="108" fill="#000" opacity="0.28" transform="translate(4,7)"/>'
        f'<circle r="104" fill="{PAPER}"/>'
        f'<circle r="94" fill="{NAVY}"/>'
        f'<circle r="94" fill="none" stroke="{GOLD}" stroke-width="1.2" opacity="0.9"/>'
        f'<g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="48s" repeatCount="indefinite"/>'
        f'<text font-family="{MONO}" font-size="11.5" font-weight="700" fill="{INK}" letter-spacing="1.5">'
        f'<textPath xlink:href="#ring" textLength="436" lengthAdjust="spacing">'
        f'ETHICAL HACKER  •  BUG BOUNTY HUNTER  •  PYTHON DEV  •  </textPath></text></g>'
        f'<circle r="56" fill="none" stroke="{LINE2}" stroke-width="1" stroke-dasharray="2 5"/>'
        f'<circle r="46" fill="{PANEL}" stroke="{GOLD}" stroke-width="1.4"/>'
        f'{bug_mark(0, -9, 30, GOLD, 1.8)}'
        f'<text y="26" text-anchor="middle" font-family="{SANS}" font-size="20" font-weight="800" fill="{INK}" letter-spacing="3">ELL</text>'
        f'{sparkle(-84, -62, 9, GOLD)}{sparkle(86, 58, 7, ICE)}'
        f'<g clip-path="url(#disc)"><rect x="-300" y="-140" width="46" height="280" fill="url(#shine)" transform="skewX(-18)">'
        f'<animate attributeName="x" values="-300;-300;260;260" keyTimes="0;0.7;0.9;1" dur="7s" repeatCount="indefinite"/></rect></g>'
        f'</g></g>'
    )

    names = "".join(
        [
            f'<text x="600" y="372" text-anchor="middle" font-family="{SANS}" font-size="58" font-weight="800" fill="{INK}" letter-spacing="-1">'
            f'Raffael Putra <tspan fill="{GOLD}">Hermawan</tspan></text>',
        ]
    )

    roles = ["Cybersecurity Researcher", "Ethical Hacker", "Bug Bounty Hunter", "Python Developer"]
    cyc = []
    for i, r in enumerate(roles):
        if i == 0:
            kt = "0;0.2;0.25;0.95;1"
            vals = "1;1;0;0;1"
            anim = f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="12s" repeatCount="indefinite"/>'
        else:
            s = i * 0.25
            kt = f"0;{s:g};{s + 0.03:g};{s + 0.22:g};{s + 0.25:g};1"
            vals = "0;0;1;1;0;0"
            anim = f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="12s" repeatCount="indefinite"/>'
        base = "1" if i == 0 else "0"
        cyc.append(
            f'<text x="600" y="418" text-anchor="middle" font-family="{MONO}" font-size="22" letter-spacing="3" '
            f'fill="{ICE}" opacity="{base}">{escape(r.upper())}{anim}</text>'
        )

    tag = (
        f'<text x="600" y="468" text-anchor="middle" font-family="{SANS}" font-size="18" fill="{MUTED}">'
        f'I find weak spots in real systems and report them responsibly.</text>'
    )

    pills = []
    specs = [("Depok, Indonesia", 168, None), ("Open to work", 150, "dot"), ("Responsible disclosure", 218, None)]
    total = sum(p[1] for p in specs) + 16 * (len(specs) - 1)
    x = 600 - total / 2
    for label, pw, kind in specs:
        pills.append(f'<rect x="{x:g}" y="496" width="{pw}" height="32" rx="16" fill="{PANEL}" stroke="{LINE2}"/>')
        tx = x + pw / 2
        if kind == "dot":
            pills.append(
                f'<circle cx="{x + 20:g}" cy="512" r="4" fill="{GOLD}">'
                f'<animate attributeName="opacity" values="1;0.25;1" dur="1.8s" repeatCount="indefinite"/></circle>'
            )
            tx = x + pw / 2 + 8
        pills.append(
            f'<text x="{tx:g}" y="517" text-anchor="middle" font-family="{SANS}" font-size="14" font-weight="600" fill="{INK}">{escape(label)}</text>'
        )
        x += pw + 16

    labels = (
        f'<text x="40" y="44" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{EYEBROW}">FIELD NOTES / VOL. 2026</text>'
        f'<text x="1160" y="44" text-anchor="end" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{EYEBROW}">DEPOK 6.4°S 106.8°E</text>'
        f'<line x1="40" y1="56" x2="1160" y2="56" stroke="{LINE}" stroke-width="1"/>'
    )

    spk = "".join(
        f'<g transform="translate({x},{y}) scale({s})"><path d="M0,-1 Q0.1,-0.1 1,0 Q0.1,0.1 0,1 Q-0.1,0.1 -1,0 Q-0.1,-0.1 0,-1Z" fill="{col}">'
        f'<animate attributeName="opacity" values="1;0.2;1" dur="{d}s" begin="{-b}s" repeatCount="indefinite"/></path></g>'
        for x, y, s, col, d, b in [
            (330, 110, 11, GOLD, 4, 1),
            (880, 96, 9, ICE, 5, 2),
            (470, 250, 6, ICE, 3.5, 0.5),
            (760, 240, 8, GOLD, 4.5, 3),
            (110, 520, 8, GOLD, 5, 2.5),
            (1090, 520, 10, ICE, 4, 1.5),
            (400, 520, 5, GOLD, 3, 0.2),
            (800, 530, 6, ICE, 3.8, 2.2),
        ]
    )

    defs = (
        f'<radialGradient id="bg" cx="50%" cy="38%" r="75%"><stop offset="0" stop-color="{NAVY2}"/><stop offset="1" stop-color="{NAVY}"/></radialGradient>'
        f'<path id="ring" d="M -69,0 a69,69 0 1,1 138,0 a69,69 0 1,1 -138,0"/>'
        f'<clipPath id="disc"><circle r="94"/></clipPath>'
        f'<linearGradient id="shine" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
        f'<clipPath id="card"><rect width="{w}" height="{h}" rx="22"/></clipPath>'
    )

    body = (
        f'<g clip-path="url(#card)"><rect width="{w}" height="{h}" fill="url(#bg)"/>'
        f'{stars_field(rng, w, h, 95, avoid)}'
        f'{constellation(left_nodes, left_edges, left_pk, 1)}'
        f'{constellation(right_nodes, right_edges, right_pk, 2)}'
        f'{spk}{labels}{sticker}{names}{"".join(cyc)}{tag}{"".join(pills)}</g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="22" fill="none" stroke="{LINE}"/>'
    )
    return svg(w, h, body, "Raffael Putra Hermawan, cybersecurity researcher, ethical hacker, bug bounty hunter and Python developer", defs)


def stats(items):
    w, h = 1200, 150
    n = len(items)
    gap = 20
    tw = (w - gap * (n - 1)) / n
    out = []
    for i, (num, label, ic) in enumerate(items):
        x = i * (tw + gap)
        s = 0.05 + i * 0.12
        fade = f'values="0;0;1;1" keyTimes="0;{s:g};{s + 0.18:g};1" dur="2s" fill="freeze"'
        mv = f'values="0 14;0 14;0 0;0 0" keyTimes="0;{s:g};{s + 0.18:g};1" dur="2s" fill="freeze"'
        out.append(
            f'<g transform="translate({x:g},0)"><g>'
            f'<animate attributeName="opacity" {fade}/>'
            f'<animateTransform attributeName="transform" type="translate" {mv}/>'
            f'<rect x="0.5" y="0.5" width="{tw - 1:g}" height="{h - 1}" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
            f'<rect x="24" y="30" width="40" height="40" rx="11" fill="{NAVY}" stroke="{LINE2}"/>'
            f'{icon(ic, 32, 38, 24, GOLD)}'
            f'<text x="24" y="108" font-family="{SANS}" font-size="44" font-weight="800" fill="{INK}">{num}</text>'
            f'<text x="24" y="134" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{EYEBROW}">{escape(label.upper())}</text>'
            f'{sparkle(tw - 30, 34, 7, GOLD, "")}'
            f'</g></g>'
        )
    body = "".join(out)
    return svg(w, h, body, "Key numbers: " + ", ".join(f"{a} {b}" for a, b, _ in items))


def typed(text, x, y, fill, t0, tdur, total, idn, cw, font=16, weight=400):
    n = len(text)
    full = n * cw
    keys = [0.0, t0 / total]
    vals = [0, cw]
    for i in range(2, n + 1):
        keys.append((t0 + (i - 1) * tdur / n) / total)
        vals.append(round(i * cw, 1))
    keys.append(0.955)
    vals.append(0)
    kt = ";".join(f"{k:.4f}" for k in keys)
    vs = ";".join(f"{v:g}" for v in vals)
    clip = (
        f'<clipPath id="{idn}"><rect x="{x}" y="{y - 20}" width="{full:g}" height="28">'
        f'<animate attributeName="width" calcMode="discrete" values="{vs}" keyTimes="{kt}" dur="{total}s" repeatCount="indefinite"/>'
        f'</rect></clipPath>'
    )
    t = (
        f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{font}" font-weight="{weight}" fill="{fill}" '
        f'textLength="{full:g}" lengthAdjust="spacing" clip-path="url(#{idn})" xml:space="preserve">{escape(text)}</text>'
    )
    return clip, t


def terminal():
    w, h = 1000, 330
    cw = 9.6
    total = 20.0
    lines = [
        ("$ ", "whoami", "raffael putra hermawan  (ell)", 0.8),
        ("$ ", "cat focus.txt", "bug bounty | web app security | python tooling", 4.6),
        ("$ ", "./report --disclosure responsible", "[ok] vendor notified, fix verified, report filed", 8.6),
        ("$ ", "./bugs --status", "19 disclosed  |  5 awards  |  33 certifications", 13.2),
    ]
    defs = []
    parts = []
    y = 98
    for i, (pr, cmd, out, t0) in enumerate(lines):
        c1, t1 = typed(pr + cmd, 36, y, INK, t0, len(cmd) * 0.07, total, f"c{i}a", cw)
        c2, t2 = typed(out, 36 + 2 * cw, y + 26, MUTED if i != 2 else GOLD, t0 + len(cmd) * 0.07 + 0.35, 0.9, total, f"c{i}b", cw)
        defs += [c1, c2]
        parts += [t1, t2]
        y += 58
    cursor = (
        f'<rect x="{36 + 2 * cw:g}" y="{y - 16}" width="9" height="18" fill="{GOLD}">'
        f'<animate attributeName="opacity" calcMode="discrete" values="1;0" dur="1.1s" repeatCount="indefinite"/></rect>'
        f'<text x="36" y="{y}" font-family="{MONO}" font-size="16" fill="{INK}">$</text>'
    )
    bar = (
        f'<rect width="{w}" height="44" fill="{PANEL}"/><line x1="0" y1="44" x2="{w}" y2="44" stroke="{LINE}"/>'
        f'<circle cx="26" cy="22" r="6" fill="{EMBER}"/><circle cx="48" cy="22" r="6" fill="{GOLD}"/><circle cx="70" cy="22" r="6" fill="{ICE}"/>'
        f'<text x="{w / 2}" y="27" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{EYEBROW}">ell@field-notes: ~</text>'
    )
    body = (
        f'<clipPath id="win"><rect width="{w}" height="{h}" rx="16"/></clipPath>'
        f'<g clip-path="url(#win)"><rect width="{w}" height="{h}" fill="{NAVY}"/>{bar}{"".join(parts)}{cursor}</g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{LINE2}"/>'
    )
    return svg(w, h, body, "Terminal session: whoami, focus, responsible disclosure and bug status", "".join(defs))


def chip_row(items, y, direction, dur):
    cx = 0
    chips = []
    for t in items:
        cwid = int(len(t) * 8.2 + 34)
        chips.append(
            f'<g transform="translate({cx},{y})"><rect width="{cwid}" height="34" rx="17" fill="{SLATE}" stroke="{LINE2}"/>'
            f'<circle cx="16" cy="17" r="3" fill="{GOLD}"/>'
            f'<text x="28" y="22" font-family="{MONO}" font-size="13" fill="{INK}">{escape(t)}</text></g>'
        )
        cx += cwid + 12
    width = cx
    rep = 1
    while width * rep < 1300:
        rep += 1
    single = "".join(chips)
    grp = "".join(f'<g transform="translate({k * width},0)">{single}</g>' for k in range(rep))
    frm, to = (0, -width) if direction < 0 else (-width, 0)
    two = (
        f'<g><animateTransform attributeName="transform" type="translate" from="{frm} 0" to="{to} 0" dur="{dur}s" repeatCount="indefinite"/>'
        f'{grp}<g transform="translate({width * rep},0)">{grp}</g></g>'
    )
    return two


def marquee(row1, row2):
    w, h = 1200, 112
    defs = (
        f'<linearGradient id="fadeL" x1="0" x2="1"><stop offset="0" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY}" stop-opacity="0"/></linearGradient>'
        f'<linearGradient id="fadeR" x1="0" x2="1"><stop offset="0" stop-color="{NAVY}" stop-opacity="0"/><stop offset="1" stop-color="{NAVY}"/></linearGradient>'
        f'<clipPath id="mq"><rect width="{w}" height="{h}" rx="18"/></clipPath>'
    )
    body = (
        f'<g clip-path="url(#mq)"><rect width="{w}" height="{h}" fill="{NAVY}"/>'
        f'{chip_row(row1, 14, -1, 70)}{chip_row(row2, 62, 1, 80)}'
        f'<rect width="90" height="{h}" fill="url(#fadeL)"/><rect x="{w - 90}" width="90" height="{h}" fill="url(#fadeR)"/></g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="18" fill="none" stroke="{LINE}"/>'
    )
    return svg(w, h, body, "Tools and skills in rotation", defs)


def divider(num, ic, eyebrow, seed):
    w, h = 1200, 76
    rng = random.Random(seed)
    spk = []
    for k in range(3):
        x1 = 560
        x2 = 1150
        d = 5 + k * 1.7
        spk.append(
            f'<g><animateTransform attributeName="transform" type="translate" from="{x1} 38" to="{x2} 38" dur="{d:g}s" begin="{-k * 1.9:g}s" repeatCount="indefinite"/>'
            f'<path d="M0,-5 Q0.6,-0.6 5,0 Q0.6,0.6 0,5 Q-0.6,0.6 -5,0 Q-0.6,-0.6 0,-5Z" fill="{GOLD}"/></g>'
        )
    dots = "".join(
        f'<circle cx="{rng.uniform(580, 1160):.0f}" cy="{rng.uniform(14, 62):.0f}" r="{rng.choice([0.8, 1.1, 1.5])}" fill="{INK}" opacity="0.5">'
        f'{twinkle("0.6;0.15;0.6", rng.uniform(2.5, 5), -rng.uniform(0, 4))}</circle>'
        for _ in range(16)
    )
    body = (
        f'<clipPath id="dv"><rect width="{w}" height="{h}" rx="16"/></clipPath>'
        f'<g clip-path="url(#dv)"><rect width="{w}" height="{h}" fill="{NAVY}"/>{dots}'
        f'<rect x="18" y="14" width="48" height="48" rx="13" fill="{PANEL}" stroke="{GOLD}" stroke-opacity="0.8"/>'
        f'{icon(ic, 30, 26, 24, GOLD)}'
        f'<text x="86" y="34" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{EYEBROW}">SECTION {num}</text>'
        f'<text x="86" y="56" font-family="{SANS}" font-size="20" font-weight="700" letter-spacing="1" fill="{INK}">{escape(eyebrow)}</text>'
        f'<line x1="420" y1="38" x2="1170" y2="38" stroke="{LINE2}" stroke-width="1" stroke-dasharray="1 7" stroke-linecap="round"/>'
        f'{"".join(spk)}</g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{LINE}"/>'
    )
    return svg(w, h, body, f"Section {num}: {eyebrow}")


def footer():
    w, h = 1200, 130
    rng = random.Random(11)
    body = (
        f'<clipPath id="ft"><rect width="{w}" height="{h}" rx="20"/></clipPath>'
        f'<g clip-path="url(#ft)"><rect width="{w}" height="{h}" fill="url(#bg2)"/>'
        f'{stars_field(rng, w, h, 40)}'
        f'<text x="600" y="62" text-anchor="middle" font-family="{SANS}" font-size="24" font-weight="700" fill="{INK}">Thanks for stopping by.</text>'
        f'<text x="600" y="92" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{EYEBROW}">HACK RESPONSIBLY  •  DISCLOSE ETHICALLY</text>'
        f'{sparkle(430, 58, 9, GOLD)}{sparkle(770, 58, 9, GOLD)}</g>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="20" fill="none" stroke="{LINE}"/>'
    )
    defs = f'<radialGradient id="bg2" cx="50%" cy="0%" r="110%"><stop offset="0" stop-color="{NAVY2}"/><stop offset="1" stop-color="{NAVY}"/></radialGradient>'
    return svg(w, h, body, "Footer", defs)


def button(ic, label, sub):
    w, h = 270, 56
    body = (
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="28" fill="{PANEL}" stroke="{LINE2}"/>'
        f'<circle cx="28" cy="28" r="19" fill="{NAVY}" stroke="{GOLD}" stroke-opacity="0.8"/>'
        f'{icon(ic, 18, 18, 20, GOLD)}'
        f'<text x="60" y="25" font-family="{SANS}" font-size="15" font-weight="700" fill="{INK}">{escape(label)}</text>'
        f'<text x="60" y="42" font-family="{MONO}" font-size="11" fill="{EYEBROW}">{escape(sub)}</text>'
        f'<g stroke="{GOLD}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">'
        f'<animateTransform attributeName="transform" type="translate" values="0 0;5 0;0 0" dur="2.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>'
        f'<path d="M{w - 44},28H{w - 28}"/><path d="M{w - 34},22l6 6-6 6"/></g>'
    )
    return svg(w, h, body, f"{label}: {sub}")


def tile(name):
    body = (
        f'<rect x="0.5" y="0.5" width="47" height="47" rx="13" fill="{PANEL}" stroke="{LINE2}"/>'
        f'{icon(name, 12, 12, 24, GOLD)}'
    )
    return svg(48, 48, body, name)


def build_all(assets_dir, data):
    write(os.path.join(assets_dir, "hero.svg"), hero())
    write(os.path.join(assets_dir, "stats.svg"), stats(data["stats"]))
    write(os.path.join(assets_dir, "terminal.svg"), terminal())
    write(os.path.join(assets_dir, "marquee.svg"), marquee(data["row1"], data["row2"]))
    write(os.path.join(assets_dir, "footer.svg"), footer())
    for i, (key, ic, eyebrow) in enumerate(data["sections"], 1):
        write(os.path.join(assets_dir, "dividers", key + ".svg"), divider(f"{i:02d}", ic, eyebrow, i))
    for key, ic, label, sub in data["buttons"]:
        write(os.path.join(assets_dir, "buttons", key + ".svg"), button(ic, label, sub))
    for name in ICONS:
        write(os.path.join(assets_dir, "icons", name + ".svg"), tile(name))
