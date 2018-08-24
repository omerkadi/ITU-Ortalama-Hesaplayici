import bs4
from save_data import read_transcript


def parse_transcript_data(raw_transcript_data):
    soup = bs4.BeautifulSoup(raw_transcript_data, "html.parser")

    season_data = soup.find("div", class_="pagebodydiv").find("tr").find_all("table")[1].\
        find_all("td", attrs={"colspan": "2"})
    courses_data = soup.find("div", class_="pagebodydiv").find("tr").find_all("table")[1].\
        find_all("td", attrs={"width": "400"})

    return [courses_data, season_data]


def parse_season_name(season_name):
    parsed = season_name.split(" / ")

    years = parsed[0].split("-")
    years = [int(years[0]), int(years[1])]

    season = parsed[1]
    return [years, season]


def edit_transcript_data(courses_data, seasons_names):
    edited_transcript_data = {}

    for i, season in enumerate(courses_data):
        season_name = seasons_names[i].text
        edited_transcript_data[season_name] = []
        for course in season.find_all("tr"):
            one_course = {}
            course_data = course.find_all("td")

            if course_data[0].text == "Ders Kodu":
                continue

            one_course["Ders Kodu"] = course_data[0].text
            one_course["Ders Adı"] = course_data[1].text
            one_course["Kredi"] = course_data[2].text.strip()
            one_course["Not"] = course_data[3].text

            edited_transcript_data[season_name].append(one_course)
    return edited_transcript_data


def get_seasons_names(user_name):
    seasons_data = parse_transcript_data(read_transcript(user_name))
    seasons_name = []
    for season in seasons_data[0]:
        seasons_name.append(season.text)
    return seasons_name


def get_last_season(user_name):
    seasons_name = get_seasons_names(user_name)
    return parse_season_name(seasons_name[-1])


if __name__ == "__main__":
    pass
