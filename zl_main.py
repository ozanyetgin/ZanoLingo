#!/usr/bin/env python3

import speech_recognition as sr
from recognize_speech import recognize_speech
import time
import random

seviyeler = {
    "kolay": ["Dairy", "Mouse", "Computer"],
    "orta": ["Programming", "Algorithm", "Developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

seviye_secimi = input("Seviyenizi seçin (kolay/orta/zor): ")

if seviye_secimi in seviyeler:
    secilen_kelime = random.choice(seviyeler[seviye_secimi])
    print("")
    print(f"Seçilen kelime: {secilen_kelime}, konuşmaya başla!")

    speech_sonuc2 = recognize_speech()

    if speech_sonuc2 == secilen_kelime:
        print("")
        print(f"Tebrikler, {seviye_secimi} seviyesiden {secilen_kelime} kelimesini başarıyla telaffuz ettin!")
        print("")
    else:
        print("")
        print(f"Üzgünüm, {seviye_secimi} seviyeden {secilen_kelime} kelimesini {speech_sonuc2} olarak telaffuz ettin... Lütfen tekrar dene!")
        print("")

else:
    print("")
    print("Geçersiz seviye seçimi. Lütfen 'kolay', 'orta' veya 'zor' seçeneklerinden birini yazınız.")
    print("")