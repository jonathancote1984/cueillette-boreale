#!/usr/bin/env python3
"""Icônes PWA Cueillette Boréale : 3 bleuets sur fond ivoire, contours noirs épais,
petites pointes rayonnantes et une feuille verte. Usage : python generer_icones.py"""
import os
from PIL import Image, ImageDraw

# Palette boréale (vert sapin)
IVOIRE = (239, 243, 236)      # #EFF3EC fond
BLEUET = (61, 90, 158)        # bleu des bleuets
BLEUET_CLAIR = (94, 120, 190) # reflet
VERT = (30, 77, 51)           # #1E4D33 feuille / contour
BLANC = (248, 251, 246)       # #F8FBF6
NOIR = (15, 36, 24)           # #0F2418 contour épais

def fond(d, taille):
    d.rectangle([0, 0, taille, taille], fill=IVOIRE)

def feuille(d, cx, cy, e, angle_deg):
    """Petite feuille ovale orientée."""
    import math
    img = Image.new('RGBA', (int(e*1.2), int(e*0.7)), (0, 0, 0, 0))
    dd = ImageDraw.Draw(img)
    dd.ellipse([0, 0, img.width - 1, img.height - 1], fill=VERT, outline=NOIR, width=max(2, int(e*0.09)))
    img = img.rotate(angle_deg, expand=True)
    d._image.alpha_composite(img, (int(cx - img.width/2), int(cy - img.height/2)))

def bleuet(d, cx, cy, e):
    """Baie de bleuet : cercle bleu + pointes rayonnantes + couronne + reflet blanc."""
    lw = max(3, int(e * 0.09))
    # corps
    d.ellipse([cx - e*0.5, cy - e*0.5, cx + e*0.5, cy + e*0.5], fill=BLEUET, outline=NOIR, width=lw)
    # pointes rayonnantes (le calice)
    for a in range(-40, 250, 25):
        import math
        rad = math.radians(a)
        x1 = cx + e*0.46*math.cos(rad); y1 = cy - e*0.46*math.sin(rad)
        x2 = cx + e*0.68*math.cos(rad); y2 = cy - e*0.68*math.sin(rad)
        d.line([x1, y1, x2, y2], fill=NOIR, width=max(1, int(e*0.05)))
    # couronne centrale
    cw = int(e*0.09)
    for a in range(-40, 250, 25):
        import math
        rad = math.radians(a)
        x1 = cx + e*0.14*math.cos(rad); y1 = cy - e*0.14*math.sin(rad)
        x2 = cx + e*0.30*math.cos(rad); y2 = cy - e*0.30*math.sin(rad)
        d.line([x1, y1, x2, y2], fill=NOIR, width=cw)
    # reflet blanc
    d.ellipse([cx - e*0.30, cy - e*0.24, cx - e*0.08, cy - e*0.05], fill=BLANC)

def generer(taille, nom, masquable=False):
    img = Image.new('RGBA', (taille, taille))
    d = ImageDraw.Draw(img)
    # attacher une image composite pour alpha_composite de feuille()
    d._image = img
    fond(d, taille)
    s = (0.34 if masquable else 0.46)   # taille des bleuets en fraction (masquable = plus petit pour marges)
    # Disposition 3 bleuets (2 dessus, 1 dessous-centre)
    bleuet(d, taille*0.36, taille*0.44, taille*s)
    bleuet(d, taille*0.64, taille*0.42, taille*s)
    bleuet(d, taille*0.50, taille*0.62, taille*s)
    # feuille verte en haut à droite
    feuille(d, taille*0.82, taille*0.20, taille*0.13, angle_deg=35)
    img.save(os.path.join('icons', nom))
    print('OK', nom, taille)

if __name__ == '__main__':
    os.makedirs('icons', exist_ok=True)
    generer(192, 'icon-192.png')
    generer(512, 'icon-512.png')
    generer(512, 'icon-maskable-512.png', masquable=True)
