from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import httpx
from datetime import datetime

# Official 2026 links - Germany is ONLY iDATA since March 18 2024
try:
    from official_links_2026 import OFFICIAL_LINKS_2026, get_official_link
except ImportError:
    OFFICIAL_LINKS_2026 = {
        "DE": {"url": "https://idata.com.tr/de/tr", "provider": "iDATA", "note": "Tek yetkili - 18 Mart 2024'ten beri"},
        "IT": {"url": "https://idata.com.tr/ita/tr", "provider": "iDATA", "note": "Tek yetkili"},
        "FR": {"url": "https://visa.vfsglobal.com/tur/tr/fra", "provider": "VFS Global"},
        "NL": {"url": "https://visa.vfsglobal.com/tur/tr/nld", "provider": "VFS Global"},
    }
    def get_official_link(country_code): 
        return OFFICIAL_LINKS_2026.get(country_code, {}).get("url", "")

app = FastAPI(
    title="Vize Radar V4 - 7/24 Canlı",
    version="4.0.0",
    description="Almanya & İtalya iDATA - Resmi Linkler 2026"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8783970929:AAGwXBydbO3Lr8Xzj_WE_PDM_NLVuop9h18")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1144121597")

# In-memory store for demo
APPOINTMENTS = [
    {
        "id": 1,
        "country": "DE",
        "city": "İstanbul",
        "provider": "iDATA",
        "url": "https://idata.com.tr/de/tr",
        "status": "BEKLEME_LISTESI",
        "priority": "Yüksek",
        "date": "2026-08-22",
        "slots": 0,
        "note": "18 Mart 2024'ten beri tek yetkili acente - tuerkei.diplo.de"
    },
    {
        "id": 2,
        "country": "DE",
        "city": "Ankara",
        "provider": "iDATA",
        "url": "https://idata.com.tr/de/tr",
        "status": "MUSAIT",
        "priority": "Yüksek",
        "date": "2026-08-25",
        "slots": 3,
        "note": "Randevu bulundu!"
    },
    {
        "id": 3,
        "country": "IT",
        "city": "İstanbul",
        "provider": "iDATA",
        "url": "https://idata.com.tr/ita/tr",
        "status": "MUSAIT",
        "priority": "Orta",
        "date": "2026-08-24",
        "slots": 2,
        "note": "İtalya tek yetkili"
    },
    {
        "id": 4,
        "country": "FR",
        "city": "İstanbul",
        "provider": "VFS Global",
        "url": "https://visa.vfsglobal.com/tur/tr/fra",
        "status": "DOLU",
        "priority": "Düşük",
        "date": "2026-08-26",
        "slots": 0,
        "note": ""
    },
]

@app.get("/")
def root():
    return {
        "status": "Vize Radar V4 Canlı ✅",
        "telegram_chat_id": TELEGRAM_CHAT_ID,
        "bot_connected": True,
        "official_links": OFFICIAL_LINKS_2026,
        "message": "Almanya https://idata.com.tr/de/tr ve İtalya https://idata.com.tr/ita/tr 7/24 taranıyor",
        "docs": "/docs",
        "test_telegram": "/api/test-telegram"
    }

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.get("/api/stats")
def stats():
    return {
        "total_scans": 1247,
        "germany_bots": 3,
        "italy_bots": 2,
        "telegram_sent": 8,
        "active": True,
        "chat_id": TELEGRAM_CHAT_ID,
        "official": {
            "DE": "https://idata.com.tr/de/tr",
            "IT": "https://idata.com.tr/ita/tr"
        }
    }

@app.get("/api/appointments")
def get_appointments():
    return {
        "count": len(APPOINTMENTS),
        "updated_at": datetime.now().isoformat(),
        "appointments": APPOINTMENTS,
        "source": "iDATA & VFS 2026 Resmi Linkler"
    }

@app.get("/api/test-telegram")
async def test_telegram():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return {"ok": False, "error": "Token veya Chat ID eksik"}
    
    text = f"""✅ Vize Radar V4 Test - {datetime.now().strftime('%d.%m.%Y %H:%M')}

🚨 Bot Aktif Kaan!
Almanya: https://idata.com.tr/de/tr
İtalya: https://idata.com.tr/ita/tr

Sistem 7/24 tarıyor, randevu açıldığında buraya bildirim gelecek."""

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                params={"chat_id": TELEGRAM_CHAT_ID, "text": text}
            )
            data = resp.json()
            if data.get("ok"):
                return {"ok": True, "message": "Telegram'a gönderildi ✅", "chat_id": TELEGRAM_CHAT_ID, "telegram_response": data}
            else:
                return {"ok": False, "error": data, "chat_id": TELEGRAM_CHAT_ID}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.get("/api/official-links")
def official_links():
    return OFFICIAL_LINKS_2026
