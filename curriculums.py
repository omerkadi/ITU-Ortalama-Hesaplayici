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


def trim_mt_and_itb(course_data: list) -> list:
    new_course_data = []

    for item in course_data:
        key = item["Ders Adı"]
        if "(MT)" in key or "(ITB)" in key or "(TM)" in key or "(TB)" in key or "(SNT)" in key:
            continue
        new_course_data.append(item)
    return new_course_data


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

    courses_data = []
    for plan in plans:
        for item in plan.find_all("tr")[1:]:
            course_data = {}
            course = item.find_all("td")

            code = course[0].text
            if len(code) > 9:
                course_data["Ders Kodu"] = code[:7]
            else:
                course_data["Ders Kodu"] = code
            course_data["Ders Adı"] = format_str(course[1].text)
            course_data["Kredi"] = course[2].text
            courses_data.append(course_data)
    return courses_data


def get_elective_courses_urls(bolum_code: str) -> list:
    root_url = make_departments_urls([bolum_code], root=True)[0]
    url = make_departments_urls([bolum_code])

    response = requests.get(*url, headers=headers)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    plans = soup.find_all("table", attrs={"class": "plan"})

    urls = []
    for plan in plans:
        for course in plan.find_all("tr"):
            course_data = course.find_all("td")
            if course_data[8].text == "S":
                urls.append(root_url + "/" + course_data[1].contents[0].attrs["href"])
    return urls


def get_elective_courses(urls: list) -> list:
    courses = []

    for url in urls:
        course = {}
        response = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        course_data = soup.find("table", class_="plan").find_all("tr")

        for data in course_data[1:]:
            inf = data.find_all("td")
            course["Ders Kodu"] = inf[0].text
            course["Ders Adı"] = format_str(inf[1].text)
            course["Kredi"] = inf[2].text
            courses.append(course)
            course = {}
    return courses


def verify_departments_code(departments_codes: dict) -> dict:
    dep_name = list(departments_codes.keys())
    dep_code = list(departments_codes.values())
    urls = make_departments_urls(dep_code)

    verified_code = {}
    for i, url in enumerate(urls):
        if requests.get(url, headers=headers).status_code == 200:
            verified_code[dep_name[i]] = dep_code[i]
    return verified_code


def parse_courses_code(dep_code: str):
    courses = save_data.read_departments_curriculum(dep_code) + save_data.read_elective_courses(dep_code)
    non_english_courses = save_data.read_non_english_courses()

    courses_data = {}
    for course in courses:
        data = course["Ders Kodu"]
        if not data[:3] in courses_data:
            courses_data[data[:3]] = []

        if data[7:9] == "EL" or data[7:8] == "L" or data in non_english_courses:
            courses_data[data[:3]].append(data[4:9])
        else:
            courses_data[data[:3]].append(data[4:7])
            courses_data[data[:3]].append(data[4:7] + "E")
    return courses_data


if __name__ == "__main__":
    pass
