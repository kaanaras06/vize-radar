
"""
GÜNCEL ALARM KONFİGÜRASYONU - 20 Ağustos 2026
Almanya & İtalya -> iDATA (VFS değil!)
Diğer ülkeler -> VFS Global
"""

ALARM_CONFIG = [
    {
        "id": "de_istanbul",
        "provider": "iDATA",
        "country": "Almanya",
        "country_code": "DE",
        "city": "İstanbul",
        "visa_types": ["Turistik", "Ticari", "Aile Birleşimi", "Öğrenci"],
        "priority": "YÜKSEK",
        "check_interval": 45,
        "link": "https://idata.com.tr/de/tr",
        "login_required": True,
        "system": "Bekleme Listesi - Kronolojik tahsis",
        "note": "18 Mart 2024'ten beri sadece iDATA üzerinden"
    },
    {
        "id": "de_ankara",
        "provider": "iDATA",
        "country": "Almanya", 
        "country_code": "DE",
        "city": "Ankara",
        "visa_types": ["Turistik", "Öğrenci", "Ticari"],
        "priority": "YÜKSEK",
        "check_interval": 60,
        "link": "https://idata.com.tr/de/tr",
        "login_required": True
    },
    {
        "id": "de_izmir",
        "provider": "iDATA",
        "country": "Almanya",
        "country_code": "DE", 
        "city": "İzmir",
        "visa_types": ["Turistik"],
        "priority": "ORTA",
        "check_interval": 90,
        "link": "https://idata.com.tr/de/tr"
    },
    {
        "id": "it_istanbul",
        "provider": "iDATA",
        "country": "İtalya",
        "country_code": "IT",
        "city": "İstanbul", 
        "visa_types": ["Turistik", "Ticari"],
        "priority": "YÜKSEK",
        "check_interval": 60,
        "link": "https://idata.com.tr/ita/tr",
        "login_required": True
    },
    {
        "id": "it_ankara",
        "provider": "iDATA",
        "country": "İtalya",
        "country_code": "IT",
        "city": "Ankara",
        "visa_types": ["Turistik"],
        "priority": "ORTA", 
        "check_interval": 90,
        "link": "https://idata.com.tr/ita/tr"
    },
    # VFS Global - Fransa, Hollanda vb için
    {
        "id": "fr_istanbul",
        "provider": "VFS Global",
        "country": "Fransa",
        "country_code": "FR",
        "city": "İstanbul",
        "visa_types": ["Turistik", "Ticari"],
        "priority": "ORTA",
        "check_interval": 120,
        "link": "https://visa.vfsglobal.com/tur/tr/fra"
    },
    {
        "id": "nl_istanbul",
        "provider": "VFS Global",
        "country": "Hollanda",
        "country_code": "NL",
        "city": "İstanbul",
        "visa_types": ["Turistik"],
        "priority": "DÜŞÜK",
        "check_interval": 180,
        "link": "https://visa.vfsglobal.com/tur/tr/nld"
    }
]
