import requests
import bs4
import save_data


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}


def format_str(string: str) -> str:
    return string.replace("þ", "ş").replace("ð", "ğ").replace("ý", "ı").replace("Ý", "İ")


def make_departments_urls(code: list, root: bool=False) -> list:
    urls = []

    for dep_code in code:
        if root is True:
            urls.append("http://www.sis.itu.edu.tr/tr/dersplan/plan/" + dep_code)
        else:
            urls.append("http://www.sis.itu.edu.tr/tr/dersplan/plan/" + dep_code + "/201810.html")
    return urls


def trim_mt_and_itb(lesson_data: list) -> list:
    new_lesson_data = []

    for item in lesson_data:
        key = item["Ders Adı"]
        if "(MT)" in key or "(ITB)" in key or "(TM)" in key or "(TB)" in key or "(SNT)" in key:
            continue
        new_lesson_data.append(item)
    return new_lesson_data


def get_departments_code() -> dict:
    url = "http://www.sis.itu.edu.tr/tr/sistem/fak_bol_kodlari.html"

    response = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    name_and_code = soup.find_all("table")[2].find("table").find_all("tr")

    departments = {}
    for item in name_and_code:
        department = item.find_all("td")
        if len(department) > 1:
            departments[format_str(department[1].text[4:])] = department[0].text.rstrip()[1:]
        else:
            continue
    return departments


def get_department_curriculum(code: str) -> [list]:
    url = make_departments_urls([code])
    response = requests.get(*url, headers=headers)

    if response.status_code == 404:
        return None

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    plans = soup.find_all("table", attrs={"class": "plan"})

    dersler_data = []
    for plan in plans:
        for item in plan.find_all("tr")[1:]:
            ders_data = {}
            ders = item.find_all("td")

            kod = ders[0].text
            if len(kod) > 9:
                ders_data["Ders Kodu"] = kod[:7]
            else:
                ders_data["Ders Kodu"] = kod
            ders_data["Ders Adı"] = format_str(ders[1].text)
            ders_data["Kredi"] = ders[2].text
            dersler_data.append(ders_data)
    return dersler_data


def get_secmeli_ders_urls(bolum_code: str) -> list:
    root_url = make_departments_urls([bolum_code], root=True)[0]
    url = make_departments_urls([bolum_code])

    response = requests.get(*url, headers=headers)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    plans = soup.find_all("table", attrs={"class": "plan"})

    urls = []
    for plan in plans:
        for ders in plan.find_all("tr"):
            ders_data = ders.find_all("td")
            if ders_data[8].text == "S":
                urls.append(root_url + "/" + ders_data[1].contents[0].attrs["href"])
    return urls


def get_secmeli_ders(urls: list) -> list:
    dersler = []

    for url in urls:
        ders = {}
        response = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        ders_data = soup.find("table", class_="plan").find_all("tr")

        for data in ders_data[1:]:
            inf = data.find_all("td")
            ders["Ders Kodu"] = inf[0].text
            ders["Ders Adı"] = format_str(inf[1].text)
            ders["Kredi"] = inf[2].text
            dersler.append(ders)
            ders = {}
    return dersler


def verify_departments_code(departments_codes: dict) -> dict:
    dep_name = list(departments_codes.keys())
    dep_code = list(departments_codes.values())
    urls = make_departments_urls(dep_code)

    verified_code = {}
    for i, url in enumerate(urls):
        if requests.get(url, headers=headers).status_code == 200:
            verified_code[dep_name[i]] = dep_code[i]
    return verified_code


def parse_lessons_code(dep_code: str):
    dersler = save_data.read_depatments_cirriculum(dep_code) + save_data.read_secmeli_ders(dep_code)
    ingilizcesi_olmayan_dersler = save_data.read_non_english_course()

    lessons_data = {}
    for lesson in dersler:
        data = lesson["Ders Kodu"]
        if not data[:3] in lessons_data:
            lessons_data[data[:3]] = []

        if data[7:9] == "EL" or data[7:8] == "L" or data in ingilizcesi_olmayan_dersler:
            lessons_data[data[:3]].append(data[4:9])
        else:
            lessons_data[data[:3]].append(data[4:7])
            lessons_data[data[:3]].append(data[4:7] + "E")
    return lessons_data


if __name__ == "__main__":
    #a = get_department_curriculum("http://www.sis.itu.edu.tr/tr/dersplan/plan/INS/201810.html")
    #b = trim_mt_and_itb(a)
    #get_all_department_curriculum()
    #a = get_secmeli_ders_urls(["FIZ"])
    #b = get_secmeli_ders(a)
    #c = get_departments_code().values()
    #b = list(get_departments_code().values())
    #a = verify_departments_code(b)
    #print(a, b)
    a = parse_lessons_code("FIZ")
    #a = make_departments_urls("FIZ")
    #b = get_secmeli_ders_urls("FIZ")

    print(a)

