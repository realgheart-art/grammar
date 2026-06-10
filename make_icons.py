"""Jana ikon Grammar Heroes — perisai komik + kilat kuasa."""
from PIL import Image, ImageDraw

INK    = (20, 20, 43)
BLUE   = (37, 99, 235)
BLUE_D = (30, 58, 138)
YELLOW = (250, 204, 21)
PAPER  = (255, 247, 230)

def vgrad(size, top, bot):
    img = Image.new("RGB", (size, size), top)
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        px_row = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        for x in range(size):
            px[x, y] = px_row
    return img

def bolt(d, cx, cy, s, fill, outline=None, ow=0):
    # kilat ringkas, berpusat pada (cx,cy), skala s
    pts = [(-0.18,-0.55),(0.20,-0.55),(0.02,-0.10),(0.28,-0.10),
           (-0.18,0.58),(-0.05,0.08),(-0.30,0.08)]
    poly = [(cx + x*s, cy + y*s) for (x, y) in pts]
    if outline:
        d.polygon(poly, fill=outline)
        # lukis sedikit lebih kecil untuk kesan outline
        poly2 = [(cx + x*s*0.86, cy + y*s*0.86) for (x, y) in pts]
        d.polygon(poly2, fill=fill)
    else:
        d.polygon(poly, fill=fill)

def shield(size, pad_ratio, bg_full=False, square_bg=False):
    """Lukis ikon. pad_ratio = ruang selamat tepi (untuk maskable)."""
    SS = size * 4  # supersample untuk tepi licin
    if square_bg:
        img = vgrad(SS, BLUE, BLUE_D).convert("RGBA")
    else:
        img = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    m = int(SS * pad_ratio)
    box = (m, m, SS - m, SS - m)

    if not square_bg:
        # latar perisai bulat-segi (rounded square)
        r = int(SS * 0.22)
        # outline ink tebal
        d.rounded_rectangle(box, radius=r, fill=INK)
        inset = int(SS * 0.035)
        d.rounded_rectangle((box[0]+inset, box[1]+inset, box[2]-inset, box[3]-inset),
                            radius=r-inset, fill=BLUE)
        # kilauan atas
        d.rounded_rectangle((box[0]+inset, box[1]+inset, box[2]-inset, box[1]+int(SS*0.30)),
                            radius=r-inset, fill=(80, 130, 250))

    cx, cy = SS/2, SS/2 + (SS*0.01)
    bolt(d, cx, cy, SS*0.42, YELLOW, outline=INK, ow=1)

    img = img.resize((size, size), Image.LANCZOS)
    return img

# 192 & 512 — telus, perisai berkulit
shield(192, 0.06).save("icon-192.png")
shield(512, 0.06).save("icon-512.png")
# maskable — latar penuh biru hingga tepi, kandungan di zon selamat tengah
shield(512, 0.22, square_bg=True).save("icon-maskable.png")
# apple-touch — penuh segi empat (iOS bulatkan sendiri)
shield(180, 0.16, square_bg=True).save("apple-touch-icon.png")
# favicon kecil
shield(64, 0.06).save("favicon.png")
print("Ikon siap.")
