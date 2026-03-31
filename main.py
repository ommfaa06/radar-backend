from fastapi import FastAPI
import uvicorn

app = FastAPI()

# SAHTE RADAR VERİLERİ (Ankara Koordinatları)
radarlar = [
    {"id": 1, "tip": "Sabit Radar", "enlem": 39.9207, "boylam": 32.8541, "hiz_siniri": 82},
    {"id": 2, "tip": "Hız Koridoru", "enlem": 39.9531, "boylam": 32.8368, "hiz_siniri": 110}
]

# Kullanıcı Listesi (1=Normal, 2=Premium)
kullanicilar = {
    "omer": {"ad": "Ömer Faruk", "premium": False},
    "test_user": {"ad": "Deneme Kullanıcı", "premium": True}
}

@app.get("/")
def ana_sayfa():
    return {"mesaj": "Radar API Sunucusu GitHub ve Render Üzerinden Aktif!"}

@app.get("/api/radarlar")
def radarlari_getir(kullanici_adi: str = "misafir"):
    user = kullanicilar.get(kullanici_adi)
    
    # NORMAL KULLANICI SENARYOSU
    if not user or user["premium"] == False:
        return {
            "durum": "kısıtlı_erişim",
            "mesaj": "Normal üyelik: Sadece bölge uyarısı aktif.",
            "uyari": "Yakınınızda radar bölgeleri bulunmaktadır!",
            "veriler": "Tam koordinatlar için Premium üye olmalısınız."
        }
    
    # PREMIUM KULLANICI SENARYOSU
    return {
        "durum": "tam_erişim",
        "mesaj": f"Hoş geldin {user['ad']}! Tüm radarlar listeleniyor.",
        "veriler": radarlar 
    }

# Render için port ayarı (Otomatik algılar)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
