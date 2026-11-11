# -*- coding: utf-8 -*-
"""Kit de componentes: gráficos SVG temáticos, documento HTML e renderizador."""
import os, math, html, random
E = html.escape

def brl(v, sym=True):
    s = f"{abs(v):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return (("-" if v < 0 else "") + ("R$ " if sym else "") + s)
def mi(v): return f"R$ {v:.1f} mi".replace(".", ",")
def mil(v): return f"R$ {v:,.0f} mil".replace(",", ".")
def n0(v): return f"{v:,.0f}".replace(",", ".")
def pc(v, d=1): return f"{v:.{d}f}%".replace(".", ",")

BASE_CSS = ("*{box-sizing:border-box;margin:0;padding:0}"
            "body{font-family:'Liberation Sans','Segoe UI',Arial,sans-serif;-webkit-font-smoothing:antialiased;position:relative;overflow:hidden}"
            "table{border-collapse:collapse}")

def doc(body, css="", w=1400, h=860):
    return (f"<html><head><meta charset='utf-8'><style>{BASE_CSS}body{{width:{w}px;height:{h}px}}{css}</style></head><body>{body}</body></html>", w, h)

def svg(w, h, inner): return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'
def txt(x, y, s, fill="#64748b", size=10, anchor="middle", weight="400", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" {extra}>{E(str(s))}</text>'
def grid(w, h, l=30, t=10, b=28, n=4, gc="#e5e7eb"):
    return "".join(f'<line x1="{l}" x2="{w}" y1="{t+(h-t-b)*i/(n-1):.1f}" y2="{t+(h-t-b)*i/(n-1):.1f}" stroke="{gc}"/>' for i in range(n))
def legend(items, cols, x, y, tc="#64748b", step=130, size=10):
    return "".join(f'<rect x="{x+i*step}" y="{y-9}" width="10" height="10" rx="3" fill="{cols[i]}"/>' + txt(x + i * step + 15, y, n, tc, size, "start") for i, n in enumerate(items))

def bars(data, cols, w=520, h=200, tc="#64748b", gc="#e5e7eb", r=5, stacked=False, series=None, bw=.62, gap=3, vals=None):
    n = len(data); ns = len(data[0]) - 1
    mx = (max(sum(d[1:]) for d in data) if stacked else max(max(d[1:]) for d in data)) * 1.12
    l = 30; slot = (w - l) / n; bot = 34 if series else 28
    o = [grid(w, h, l, 10, bot, 4, gc)]
    base = h - bot
    for i, d in enumerate(data):
        x0 = l + i * slot + slot * (1 - bw) / 2
        if stacked:
            y = base
            for s in range(ns):
                bh = (base - 10) * d[1 + s] / mx; y -= bh
                o.append(f'<rect x="{x0:.1f}" y="{y:.1f}" width="{slot*bw:.1f}" height="{max(bh-1,0):.1f}" fill="{cols[s]}" rx="{r if s==ns-1 else 0}"/>')
        else:
            bwid = slot * bw / ns
            for s in range(ns):
                bh = (base - 10) * d[1 + s] / mx
                o.append(f'<rect x="{x0+s*bwid:.1f}" y="{base-bh:.1f}" width="{bwid-gap:.1f}" height="{max(bh,1):.1f}" rx="{r}" fill="{cols[s]}"/>')
                if vals: o.append(txt(x0 + s * bwid + (bwid - gap) / 2, base - bh - 5, vals(d[1 + s]), tc, 9))
        o.append(txt(l + i * slot + slot / 2, base + 15, d[0], tc, 10))
    if series: o.append(legend(series, cols, l, h - 2, tc))
    return svg(w, h, "".join(o))

def _path(pts, smooth=True):
    if not smooth or len(pts) < 3: return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    p = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        dx = (x1 - x0) / 2.4
        p += f" C{x0+dx:.1f},{y0:.1f} {x1-dx:.1f},{y1:.1f} {x1:.1f},{y1:.1f}"
    return p

_uid = [0]
def line(data, cols, w=520, h=200, tc="#64748b", gc="#e5e7eb", area=True, dashed=(), smooth=True, markers=True, series=None, ymin=None, sw=2.6, mfill="#fff"):
    _uid[0] += 1; u = _uid[0]
    ns = len(data[0]) - 1; n = len(data)
    mx = max(max(d[1:]) for d in data) * 1.1
    mn = ymin if ymin is not None else min(min(d[1:]) for d in data) * .85
    l = 30; step = (w - l - 12) / (n - 1); bot = 34 if series else 28; base = h - bot
    o = ["<defs>" + "".join(f'<linearGradient id="g{u}{s}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{cols[s]}" stop-opacity=".30"/><stop offset="1" stop-color="{cols[s]}" stop-opacity="0"/></linearGradient>' for s in range(ns)) + "</defs>", grid(w, h, l, 10, bot, 4, gc)]
    for s in range(ns):
        pts = [(l + i * step, 10 + (base - 10) * (1 - (d[1 + s] - mn) / (mx - mn))) for i, d in enumerate(data)]
        if area and s not in dashed:
            o.append(f'<path d="{_path(pts, smooth)} L{pts[-1][0]:.1f},{base} L{pts[0][0]:.1f},{base} Z" fill="url(#g{u}{s})"/>')
        dash = ' stroke-dasharray="6 5"' if s in dashed else ""
        o.append(f'<path d="{_path(pts, smooth)}" fill="none" stroke="{cols[s]}" stroke-width="{sw}" stroke-linecap="round"{dash}/>')
        if markers and s not in dashed:
            for x, y in pts: o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.4" fill="{mfill}" stroke="{cols[s]}" stroke-width="2"/>')
    for i, d in enumerate(data): o.append(txt(l + i * step, base + 15, d[0], tc, 10))
    if series: o.append(legend(series, cols, l, h - 2, tc))
    return svg(w, h, "".join(o))

def donut(data, cols, size=170, hole=.62, tc="#334155", center=None, w=None, cc="#0f172a", lw=140):
    tot = sum(v for _, v in data); cx = cy = size / 2; r = size / 2 * (1 + hole) / 2 - 2; sw = size / 2 * (1 - hole)
    circ = 2 * math.pi * r; off = 0; o = [f'<g transform="rotate(-90 {cx} {cy})">']
    for i, (l, v) in enumerate(data):
        ln = circ * v / tot
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{cols[i%len(cols)]}" stroke-width="{sw:.1f}" stroke-dasharray="{max(ln-2.5,1):.1f} {circ:.1f}" stroke-dashoffset="{-off:.1f}"/>')
        off += ln
    o.append("</g>")
    if center: o.append(txt(cx, cy + 7, center, cc, 22, "middle", "700"))
    ww = w or size + lw + 20
    for i, (l, v) in enumerate(data):
        o.append(f'<rect x="{size+14}" y="{size/2-len(data)*12+i*24}" width="10" height="10" rx="3" fill="{cols[i%len(cols)]}"/>' + txt(size + 30, size / 2 - len(data) * 12 + i * 24 + 9, f"{l} ({v*100//tot}%)", tc, 11, "start"))
    return svg(ww, size, "".join(o))

def hbars(data, w=520, color="#3b82f6", tc="#334155", track="#eef2f8", fmt=None, rowh=28, labw=110, barh=14, colors=None):
    mx = max(abs(v) for _, v in data) or 1; fmt = fmt or (lambda v: f"{v:,.0f}".replace(",", "."))
    o = []; bwmax = w - labw - 74
    for i, (l, v) in enumerate(data):
        y = i * rowh; c = (colors[i] if colors else color)
        o.append(txt(0, y + 16, l, tc, 11, "start"))
        o.append(f'<rect x="{labw}" y="{y+5}" width="{bwmax}" height="{barh}" rx="{barh/2}" fill="{track}"/>')
        o.append(f'<rect x="{labw}" y="{y+5}" width="{max(bwmax*abs(v)/mx,6):.1f}" height="{barh}" rx="{barh/2}" fill="{c}"/>')
        o.append(txt(labw + bwmax + 8, y + 16, fmt(v), tc, 10.5, "start"))
    return svg(w, rowh * len(data) + 6, "".join(o))

def waterfall(items, w=720, h=340, up="#16a34a", down="#ef4444", total="#2563eb", tc="#475569", gc="#e5e7eb", fmt=None, fs=11):
    fmt = fmt or (lambda v: f"{v:,.0f}")
    run = 0; segs = []
    for l, v, k in items:
        if k == "t": segs.append((l, 0, v, "t", v)); run = v
        else: segs.append((l, run, run + v, "d", v)); run += v
    mx = max(max(a, b) for _, a, b, _, _ in segs) * 1.15
    left = 20; base = h - 34; slot = (w - left) / len(segs); bw = slot * .58; o = [grid(w, h, left, 14, 34, 4, gc)]
    prev = None
    for i, (l, a, b, k, v) in enumerate(segs):
        x = left + i * slot + (slot - bw) / 2
        lo, hi = min(a, b), max(a, b)
        y1 = base - (base - 14) * hi / mx; y2 = base - (base - 14) * lo / mx
        c = total if k == "t" else (up if v >= 0 else down)
        o.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{bw:.1f}" height="{max(y2-y1,2):.1f}" rx="5" fill="{c}"/>')
        o.append(txt(x + bw / 2, y1 - 7, (("+" if v > 0 else "") if k == "d" else "") + fmt(v), tc, fs, "middle", "700"))
        o.append(txt(x + bw / 2, base + 18, l, tc, fs - 1))
        if prev is not None:
            yy = base - (base - 14) * prev / mx
            o.append(f'<line x1="{x-(slot-bw):.1f}" x2="{x:.1f}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="{tc}" stroke-dasharray="3 3" opacity=".5"/>')
        prev = b if k == "d" else v
    return svg(w, h, "".join(o))

def gauge(pct, w=240, color="#22d3ee", track="#1e293b", tc="#e2e8f0", label=""):
    r = w / 2 - 18; cx = w / 2; cy = w / 2 - 6; L = math.pi * r
    d = f"M{cx-r:.1f},{cy:.1f} A{r:.1f},{r:.1f} 0 0 1 {cx+r:.1f},{cy:.1f}"
    return svg(w, int(w / 2 + 24), f'<path d="{d}" stroke="{track}" stroke-width="16" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{color}" stroke-width="16" fill="none" stroke-linecap="round" stroke-dasharray="{L*pct/100:.1f} {L:.1f}"/>' + txt(cx, cy - 6, pc(pct), tc, 30, "middle", "700") + txt(cx, cy + 16, label, tc, 11, "middle", "400", 'opacity=".7"'))

def heat(matrix, rl, cl, w, h, colorfn, tc="#cbd5e1", fs=14, gap=4, vfmt=None, lab_w=110):
    R = len(matrix); C = len(matrix[0]); cw = (w - lab_w) / C; ch = (h - 26) / R; o = []
    for i in range(R):
        o.append(txt(lab_w - 10, i * ch + ch / 2 + 4, rl[i], tc, 11, "end"))
        for j in range(C):
            v = matrix[i][j]; x = lab_w + j * cw
            o.append(f'<rect x="{x+gap/2:.1f}" y="{i*ch+gap/2:.1f}" width="{cw-gap:.1f}" height="{ch-gap:.1f}" rx="8" fill="{colorfn(i,j,v)}"/>')
            o.append(txt(x + cw / 2, i * ch + ch / 2 + fs / 3, (vfmt(v) if vfmt else v), "#fff", fs, "middle", "700"))
    for j in range(C): o.append(txt(lab_w + j * cw + cw / 2, h - 6, cl[j], tc, 10.5))
    return svg(w, h, "".join(o))

def treemap(items, w, h, gap=4, fs=13, tc="#fff"):
    items = sorted(items, key=lambda x: -x[1]); out = []
    def rec(its, x, y, ww, hh):
        if len(its) == 1:
            l, v, c, sub = its[0]
            out.append(f'<rect x="{x+gap/2:.1f}" y="{y+gap/2:.1f}" width="{ww-gap:.1f}" height="{hh-gap:.1f}" rx="10" fill="{c}"/>')
            out.append(txt(x + 14, y + 26, l, tc, fs, "start", "700")); out.append(txt(x + 14, y + 44, sub, tc, fs - 2, "start", "400", 'opacity=".85"')); return
        tot = sum(i[1] for i in its); acc = 0; k = 0
        for k, i in enumerate(its):
            acc += i[1]
            if acc >= tot / 2: break
        k = max(0, min(k, len(its) - 2)); a = its[:k + 1]; b = its[k + 1:]; sa = sum(i[1] for i in a) / tot
        if ww >= hh: rec(a, x, y, ww * sa, hh); rec(b, x + ww * sa, y, ww * (1 - sa), hh)
        else: rec(a, x, y, ww, hh * sa); rec(b, x, y + hh * sa, ww, hh * (1 - sa))
    rec(items, 0, 0, w, h); return svg(w, h, "".join(out))

def spark(color, n=9, seed=1, w=64, h=26):
    r = random.Random(seed); pts = [r.uniform(.3, 1) for _ in range(n)]; mx = max(pts)
    d = " ".join(f"{i*(w-4)/(n-1)+2:.0f},{h-3-(h-6)*p/mx:.1f}" for i, p in enumerate(pts))
    return f'<svg width="{w}" height="{h}"><polyline fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" points="{d}"/></svg>'

def render_all(items, out_dir, scale=1.4):
    from playwright.sync_api import sync_playwright
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME_PATH") or None, args=["--no-sandbox"])
        for name, (h, w, ht) in items.items():
            pg = b.new_page(viewport={"width": w, "height": ht}, device_scale_factor=scale)
            pg.set_content(h); pg.wait_for_timeout(60)
            pg.screenshot(path=f"{out_dir}/{name}.jpg", type="jpeg", quality=88); pg.close()
        b.close()
