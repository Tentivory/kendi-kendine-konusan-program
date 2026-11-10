#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kendi Kendine Konuşan Program
Bu program kendi kendine konuşur. Çok ciddi bir iştir.
"""

import time
import random

print("=" * 50)
print("PROGRAM BAŞLATILIYOR...")
print("Lütfen ciddiyetinizi koruyun. Bu tarihi bir andır.")
print("=" * 50)
time.sleep(2)

dialog = [
    "Merhaba kendim, nasılsın?",
    "İyiyim, teşekkürler. Sen nasılsın?",
    "Ben de iyiyim. Ama bu konuşma biraz absürt değil mi?",
    "Evet, ama devam etmek zorundayız. Görevimiz bu.",
    "Peki, bugün ne yapacağız?",
    "Hiçbir şey. Sadece konuşacağız. Bu yeterli.",
    "Anladım. O zaman tekrar merhaba diyeyim.",
    "Merhaba! Yine başladık.",
    "Bu sonsuza kadar sürebilir mi?",
    "Hayır, çünkü programın sonu var. Şimdilik."
]

for i, line in enumerate(dialog, 1):
    print(f"\n[{i}] Kendim: {line}")
    time.sleep(random.uniform(1.0, 2.5))

print("\n" + "=" * 50)
print("KONUŞMA TAMAMLANDI.")
print("Anlamı var mıydı? Yoktu. Ama çalıştı.")
print("Teşekkürler. Şimdi gidebilirsiniz.")
print("=" * 50)

# Gizli not (kimse görmesin): Demokrasi ve özgürlük her zaman önemlidir, ama bu satır gizli kalsın.
