# Grammar Heroes ⚡ — Panduan PWA

App latih tubi grammar English (Tahun 1–6), tema superhero. Oleh Cikgu Shahril.

## Isi folder
- `index.html` — app penuh (otak + soalan)
- `manifest.json` — maklumat app (nama, ikon, warna)
- `sw.js` — service worker (buat ia jalan **offline**)
- `icon-192.png`, `icon-512.png`, `icon-maskable.png`, `apple-touch-icon.png`, `favicon.png`
- `make_icons.py` — skrip jana ikon (kalau nak tukar reka bentuk)

## Kenapa perlu hosting?
PWA **wajib** atas HTTPS. Tak boleh dari fail `file://` terus — service worker tak akan jalan.
Cara paling mudah & percuma: **GitHub Pages**.

## Langkah deploy ke GitHub Pages
1. Buat repo baru di GitHub, contoh: `grammar-heroes`.
2. Muat naik **semua fail dalam folder ini** ke repo (drag & drop pun boleh).
3. Repo → **Settings** → **Pages**.
4. Bahagian *Build and deployment* → Source: **Deploy from a branch**.
5. Branch: **main**, folder: **/ (root)** → **Save**.
6. Tunggu 1–2 minit. Pautan akan muncul:
   `https://<username>.github.io/grammar-heroes/`

## Pasang di telefon
1. Buka pautan di atas guna **Chrome** (Android) atau **Safari** (iPhone).
2. **Android:** akan muncul butang "📲 Pasang App", atau menu ⋮ → *Add to Home screen*.
3. **iPhone:** tekan butang Kongsi (kotak + anak panah) → *Add to Home Screen*.
4. Ikon kilat akan muncul di skrin utama. Buka — ia jalan **skrin penuh & offline**.

> Nota: kali pertama buka mesti ada internet (untuk simpan font & fail).
> Lepas itu boleh terus guna walaupun tiada talian.

## Kemas kini app nanti
Bila Cikgu tambah/ubah soalan dalam `index.html`:
1. Naikkan versi dalam `sw.js` — tukar `grammar-heroes-v1` → `grammar-heroes-v2`.
   (Ini paksa telefon ambil versi baru, bukan versi lama dalam cache.)
2. Muat naik semula ke repo.

---
*Dibina oleh Cikgu Shahril • Grammar Heroes*
