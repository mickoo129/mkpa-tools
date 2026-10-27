#!/usr/bin/env python3
"""MKPA 工具 icon 產生器：一個圖形 → 全套 icon 檔案。

用法：
  pip install cairosvg pillow
  python3 make-icons.py <圖形名或 .svg 檔> <輸出 folder> --name "工具全名" --short "短名"

圖形用 32×32 網格、白色線條（stroke-width 2.5、圓角），唔使包底色。
現成圖形喺 _standard/icons/*.svg（例如 house、shield-check、trend-up）。

輸出：
  favicon.svg           瀏覽器分頁 icon（宏利綠圓角方塊 + 白色圖形），亦用喺標題旁邊
  favicon.ico           舊瀏覽器用（16/32/48）
  apple-touch-icon.png  iPhone／iPad「加至主畫面」（180×180，滿版，iOS 自己切圓角）
  icon-192.png / icon-512.png  Android／Chrome「安裝」用（滿版，可做 maskable）
  site.webmanifest      加至主畫面嘅名同 icon
"""
import argparse, io, json, os, re, sys

BRAND = "#00A758"   # 宏利綠：icon 底色
DEEP = "#0E5E57"    # 深青綠：theme-color
BG = "#F6F9F8"

def glyph_markup(arg):
    here = os.path.dirname(os.path.abspath(__file__))
    path = arg if arg.endswith(".svg") else os.path.join(here, "icons", arg + ".svg")
    s = open(path, encoding="utf-8").read()
    m = re.search(r"<svg[^>]*>(.*)</svg>", s, re.S)
    return m.group(1).strip()

def svg(glyph, rounded):
    rx = ' rx="7.5"' if rounded else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
            f'<rect width="32" height="32"{rx} fill="{BRAND}"/>'
            f'<g fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{glyph}</g></svg>')

def png(svg_text, size):
    import cairosvg
    return cairosvg.svg2png(bytestring=svg_text.encode(), output_width=size, output_height=size)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("glyph"); ap.add_argument("out")
    ap.add_argument("--name", required=True); ap.add_argument("--short", required=True)
    ap.add_argument("--prefix", default="", help="manifest 入面 icon 路徑前綴，例如 /icons/")
    a = ap.parse_args()
    from PIL import Image
    g = glyph_markup(a.glyph)
    os.makedirs(a.out, exist_ok=True)
    rounded, full = svg(g, True), svg(g, False)
    open(os.path.join(a.out, "favicon.svg"), "w", encoding="utf-8").write(rounded + "\n")
    ico = Image.open(io.BytesIO(png(rounded, 256))).convert("RGBA")
    ico.save(os.path.join(a.out, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    for name, size in [("apple-touch-icon.png", 180), ("icon-192.png", 192), ("icon-512.png", 512)]:
        open(os.path.join(a.out, name), "wb").write(png(full, size))
    p = a.prefix
    manifest = {
        "name": a.name, "short_name": a.short, "lang": "zh-HK",
        "start_url": ".", "display": "standalone",
        "background_color": BG, "theme_color": DEEP,
        "icons": [
            {"src": f"{p}icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
            {"src": f"{p}icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
        ],
    }
    json.dump(manifest, open(os.path.join(a.out, "site.webmanifest"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("done:", a.out)

if __name__ == "__main__":
    main()
