#!/usr/bin/env python3
"""Página de entrega: 30 posts animados (video + imagen + copy) con descarga ZIP."""
import json, html, sys
sys.path.insert(0, '/opt/data/donpunto-facebook')
from spec import POSTS
cal = {p['day']: p for p in json.load(open('/opt/data/donpunto-facebook/calendar.json'))['posts']}
V = sys.argv[1] if len(sys.argv) > 1 else '1'
cards = []
for p in POSTS:
    d = p['d']; c = cal[d]; dd = f'd{d:02d}'
    ratio = '1 / 1' if p['fmt'] == '1x1' else '4 / 5'
    fmt = '1:1 · 1080×1080' if p['fmt'] == '1x1' else '4:5 · 1080×1350'
    voz = 'Voz masculina' if p['voice'] == 'M' else 'Voz femenina'
    cards.append(f"""<article class=card>
<div class=meta><b>Día {d}</b><span>{c['weekday']} {c['date'][8:]}/{c['date'][5:7]}</span><span class=tag>{fmt}</span><span class=tag>{voz}</span></div>
<video src="posts/{dd}.mp4?v={V}" poster="posts/{dd}.png?v={V}" controls playsinline preload="none" style="aspect-ratio:{ratio}"></video>
<div class=dl><a href="posts/{dd}.mp4?v={V}" download="DonPunto_dia{d:02d}.mp4">⬇ Video</a><a href="posts/{dd}.png?v={V}" download="DonPunto_dia{d:02d}.png">⬇ Imagen</a></div>
<pre>{html.escape(c['copy'])}

{c['hashtags']}</pre>
<button onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent);this.textContent='¡Copiado!'">Copiar copy</button>
<details><summary>Narración</summary><p>{html.escape(' '.join(p['vo']))}</p></details>
</article>""")
page = f"""<!doctype html><html lang=es><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>Don Punto · 30 posts animados con voz</title>
<script src="https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js"></script>
<style>
body{{font-family:system-ui,-apple-system,sans-serif;background:#FAFAF7;color:#0f1d18;margin:0;padding:20px}}
header{{max-width:1200px;margin:0 auto 20px}} h1{{margin:0 0 6px;font-size:26px}} .sub{{color:#5b6b64}}
.zip{{margin-top:12px;border:0;background:#0f6b4f;color:#fff;border-radius:99px;padding:12px 20px;font-size:15px;cursor:pointer}}
.grid{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:18px}}
.card{{background:#fff;border:1px solid #e3e7e4;border-radius:16px;padding:14px}}
.meta{{display:flex;flex-wrap:wrap;gap:6px;font-size:12px;color:#5b6b64;margin-bottom:8px}} .meta b{{color:#0f6b4f}}
.tag{{background:#eef2f0;border-radius:6px;padding:1px 6px}}
video{{width:100%;border-radius:12px;background:#04211A;display:block}}
.dl{{display:flex;gap:8px;margin:8px 0}} .dl a{{flex:1;text-align:center;background:#e7efe9;color:#0f6b4f;text-decoration:none;border-radius:99px;padding:8px;font-size:14px;font-weight:600}}
pre{{white-space:pre-wrap;font-family:inherit;font-size:13.5px;line-height:1.45;background:#f6f8f7;padding:10px;border-radius:10px;margin:0;max-height:180px;overflow:auto}}
button{{margin-top:8px;border:0;background:#0f6b4f;color:#fff;border-radius:99px;padding:8px 14px;cursor:pointer}}
details{{font-size:13px;color:#46554f;margin-top:8px}}
</style>
<header><h1>Don Punto · 30 posts animados con voz</h1>
<div class=sub>21 oct → 19 nov 2026 · 15 en 1:1 y 15 en 4:5 · voz masculina y femenina intercaladas · cada post trae video con narración y la imagen fija.</div>
<button class=zip id=zip>⬇ Descargar todo (ZIP)</button> <span id=st class=sub></span></header>
<main class=grid>{''.join(cards)}</main>
<script>
document.getElementById('zip').onclick=async()=>{{const z=new JSZip(),st=document.getElementById('st');
for(let d=1;d<=30;d++){{const dd='d'+String(d).padStart(2,'0');for(const ext of ['mp4','png']){{st.textContent='Preparando día '+d+'…';const b=await (await fetch('posts/'+dd+'.'+ext+'?v={V}')).blob();z.file('DonPunto_dia'+String(d).padStart(2,'0')+'.'+ext,b)}}}}
st.textContent='Comprimiendo…';const blob=await z.generateAsync({{type:'blob'}});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='DonPunto_30_posts.zip';a.click();st.textContent='Listo'}};
</script></html>"""
open('/opt/data/donpunto-facebook/posts.html', 'w').write(page)
print('ok', len(cards))
