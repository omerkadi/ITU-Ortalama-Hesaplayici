import bs4


import data


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}


def parse_transcript_data(raw_transcrip_data, only_season=False, only_lessons=False):
    soup = bs4.BeautifulSoup(raw_transcrip_data, "html.parser")

    season_data = soup.find("div", class_="pagebodydiv").find("tr").find_all("table")[1].\
        find_all("td", attrs={"colspan": "2"})
    lessons_data = soup.find("div", class_="pagebodydiv").find("tr").find_all("table")[1].\
        find_all("td", attrs={"width": "400"})

    if only_season is True and only_lessons is False:
        return season_data
    elif only_season is False and only_lessons is True:
        return lessons_data
    else:
        return [lessons_data, season_data]


def parse_season_name(season_name):
    parsed = season_name.split(" / ")

    years = parsed[0].split("-")
    years = [int(years[0]), int(years[1])]

    season = parsed[1]
    return [years, season]


def edit_transcript_data(donemler, donem_names):
    edited_transcript_data = {}

    for i, donem in enumerate(donemler):
        donem_name = donem_names[i].text
        edited_transcript_data[donem_name] = []
        for ders in donem.find_all("tr"):
            bir_ders = {}
            ders_veri = ders.find_all("td")

            if ders_veri[0].text == "Ders Kodu":
                continue

            bir_ders["Ders Kodu"] = ders_veri[0].text
            bir_ders["Ders Adı"] = ders_veri[1].text
            bir_ders["Kredi"] = ders_veri[2].text.strip()
            bir_ders["Not"] = ders_veri[3].text

            edited_transcript_data[donem_name].append(bir_ders)
    return edited_transcript_data


def get_seasons_names():
    seasons_data = parse_transcript_data(data.site_data, only_season=True)
    seasons_name = []
    for season in seasons_data:
        seasons_name.append(season.text)
    return seasons_name

def get_last_season():
    seasons_name = get_seasons_names()
    return parse_season_name(seasons_name[-1])

if __name__ == "__main__":
    season_data = parse_transcript_data(data.site_data, only_season=True)
    season_names = get_seasons_names()
    transcript_data = edit_transcript_data(*parse_transcript_data(data.site_data))
    print(transcript_data)
