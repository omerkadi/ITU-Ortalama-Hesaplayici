
def genel_ort_hesapla(veri: list, kredi=False):
    top_kredi = 0.0
    top_not = 0.0
    for ders_not in veri:
        top_kredi += float(ders_not["Kredi"])
        top_not += float(ders_not["Kredi"]) * not_coz(ders_not["Not"])
    if top_kredi == 0:
        ortalama = 0
    else:
        ortalama = round(top_not/top_kredi, 2)

    if kredi is True:
        return [ortalama, top_kredi]
    else:
        return ortalama


def not_coz(veri: str) -> [float, None]:

    if veri[:2] == "AA":
        return 4.00
    elif veri[:2] == "BA":
        return 3.50
    elif veri[:2] == "BB":
        return 3.00
    elif veri[:2] == "CB":
        return 2.50
    elif veri[:2] == "CC":
        return 2.00
    elif veri[:2] == "DC":
        return 1.50
    elif veri[:2] == "DD":
        return 1.00
    elif veri[:2] == "FF" or veri[:2] == "VF" or veri[:2] == "BL" or veri[:2] == "BZ":
        return 0.00
    else:
        return None
