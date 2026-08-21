OFFICIAL_LINKS_2026 = {
    "DE": {"country": "Almanya", "url": "https://idata.com.tr/de/tr", "provider": "iDATA", "note": "Tek yetkili - 18 Mart 2024"},
    "IT": {"country": "Italya", "url": "https://idata.com.tr/ita/tr", "provider": "iDATA"},
    "FR": {"country": "Fransa", "url": "https://visa.vfsglobal.com/tur/tr/fra", "provider": "VFS Global"},
    "NL": {"country": "Hollanda", "url": "https://visa.vfsglobal.com/tur/tr/nld", "provider": "VFS Global"},
}
def get_official_link(code):
    return OFFICIAL_LINKS_2026.get(code, {}).get("url", "")
