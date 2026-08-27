"""
Vize Radar V6.1 - 2026 Resmi Linkler - TÜM ÜLKELER - OTOMATİK TELEGRAM BİLDİRİMLİ
Tek yetkili kaynaklar - 2026 güncel - 20 ülke
Kaynaklar: tuerkei.diplo.de, VFS Global, TLScontact, BLS, Kosmos, US Travel Docs
Son güncelleme: 27 Ağustos 2026 - V6.1 GET+POST Fix
Versiyon: 6.1.0 - Canlı: https://vize-radar-production-3237.up.railway.app
"""

OFFICIAL_LINKS_2026 = {
    # iDATA Ülkeleri (Almanya & İtalya - 18 Mart 2024'ten beri tek yetkili)
    "DE": {
        "country": "Almanya",
        "url": "https://idata.com.tr/de/tr",
        "provider": "iDATA",
        "authority": "Tek yetkili",
        "since": "2024-03-18",
        "source": "https://tuerkei.diplo.de/tr-tr/service/05-VisaEinreise/-/2650620",
    },
    "IT": {
        "country": "İtalya",
        "url": "https://idata.com.tr/ita/tr",
        "provider": "iDATA",
        "authority": "Tek yetkili",
    },

    # VFS Global Ülkeleri
    "FR": {
        "country": "Fransa",
        "url": "https://visa.vfsglobal.com/tur/tr/fra",
        "provider": "VFS Global",
        "authority": "Tek yetkili",
    },
    "NL": {
        "country": "Hollanda",
        "url": "https://visa.vfsglobal.com/tur/tr/nld",
        "provider": "VFS Global",
        "authority": "Tek yetkili",
    },
    "BE": {
        "country": "Belçika",
        "url": "https://visa.vfsglobal.com/tur/tr/bel",
        "provider": "VFS Global",
    },
    "AT": {
        "country": "Avusturya",
        "url": "https://visa.vfsglobal.com/tur/tr/aut",
        "provider": "VFS Global",
    },
    "SE": {
        "country": "İsveç",
        "url": "https://visa.vfsglobal.com/tur/tr/swe",
        "provider": "VFS Global",
    },
    "NO": {
        "country": "Norveç",
        "url": "https://visa.vfsglobal.com/tur/tr/nor",
        "provider": "VFS Global",
    },
    "DK": {
        "country": "Danimarka",
        "url": "https://visa.vfsglobal.com/tur/tr/dnk",
        "provider": "VFS Global",
    },
    "FI": {
        "country": "Finlandiya",
        "url": "https://visa.vfsglobal.com/tur/tr/fin",
        "provider": "VFS Global",
    },
    "PL": {
        "country": "Polonya",
        "url": "https://visa.vfsglobal.com/tur/tr/pol",
        "provider": "VFS Global",
    },
    "CZ": {
        "country": "Çekya",
        "url": "https://visa.vfsglobal.com/tur/tr/cze",
        "provider": "VFS Global",
    },
    "HU": {
        "country": "Macaristan",
        "url": "https://visa.vfsglobal.com/tur/tr/hun",
        "provider": "VFS Global",
    },
    "PT": {
        "country": "Portekiz",
        "url": "https://visa.vfsglobal.com/tur/tr/prt",
        "provider": "VFS Global",
    },
    "GR": {
        "country": "Yunanistan",
        "url": "https://visa.vfsglobal.com/tur/tr/grc",
        "provider": "VFS Global / Kosmos",
    },
    "CH": {
        "country": "İsviçre",
        "url": "https://visa.vfsglobal.com/tur/tr/che",
        "provider": "VFS Global / TLScontact",
    },

    # BLS Spain - İspanya
    "ES": {
        "country": "İspanya",
        "url": "https://turkey.blsspainvisa.com/",
        "provider": "BLS Spain",
        "authority": "Tek yetkili",
    },

    # TLScontact Ülkeleri
    "GB": {
        "country": "Birleşik Krallık (İngiltere)",
        "url": "https://visas-immigration.service.gov.uk/product/turkey",
        "provider": "TLScontact / UKVI",
        "authority": "Tek yetkili",
    },
    "US": {
        "country": "Amerika (ABD)",
        "url": "https://ais.usvisa-info.com/tr-tr/niv",
        "provider": "US Travel Docs",
        "authority": "Tek yetkili",
    },
    "CA": {
        "country": "Kanada",
        "url": "https://visa.vfsglobal.com/tur/tr/can",
        "provider": "VFS Global",
    },
}

# Eski linkler için uyumluluk
OFFICIAL_LINKS = OFFICIAL_LINKS_2026

def get_link(country_code):
    """Ülke koduna göre resmi linki döndür"""
    return OFFICIAL_LINKS_2026.get(country_code.upper(), {}).get("url")

def get_all_links():
    """Tüm resmi linkleri döndür"""
    return OFFICIAL_LINKS_2026

def get_by_provider(provider_name):
    """Sağlayıcıya göre filtrele (iDATA, VFS Global, BLS, TLScontact)"""
    provider_name = provider_name.lower()
    return {k: v for k, v in OFFICIAL_LINKS_2026.items() if provider_name in v.get("provider", "").lower()}
