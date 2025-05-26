def calculate_solar_output(area_m2, irradiance=5.5, efficiency=0.18):
    kWh_per_year = area_m2 * irradiance * 365 * efficiency
    return round(kWh_per_year, 2)

def estimate_roi(cost, savings_per_year):
    payback = round(cost / savings_per_year, 2)
    roi = round((savings_per_year * 25 - cost) / cost * 100, 2)
    return payback, roi

def recommend_system(usable_area_m2):
    panel_area = 1.7  # m²/panel
    panel_count = int(usable_area_m2 / panel_area)
    system_kw = round(panel_count * 0.4, 2)  # ~400W per panel
    return panel_count, system_kw
