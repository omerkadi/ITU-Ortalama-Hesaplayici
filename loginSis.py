import requests
import bs4


def get_transcript_html(user_name, password, student_number, pin):
    sis_login_page_url = "https://girisv3.itu.edu.tr/Login.aspx"
    info_system_login_page_url = "http://ssb.sis.itu.edu.tr:9000/pls/PROD/twbkwbis.P_WWWLogin/"
    info_system_login_post_url = "http://ssb.sis.itu.edu.tr:9000/pls/PROD/twbkwbis.P_ValLogin"
    transcript_page_url = "http://ssb.sis.itu.edu.tr:9000/pls/PROD/p_transcript.p_id_response"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}

    session = requests.session()
    session.headers.update(headers)
    sis_login_page = session.get(sis_login_page_url)
    sis_login_soup = bs4.BeautifulSoup(sis_login_page.text, "html.parser")

    sis_login_data = {
        "__EVENTTARGET": sis_login_soup.find("input", attrs={"name": "__EVENTTARGET"}).attrs["value"],
        "__EVENTARGUMENT": sis_login_soup.find("input", attrs={"name": "__EVENTARGUMENT"}).attrs["value"],
        "__VIEWSTATE": sis_login_soup.find("input", attrs={"name": "__VIEWSTATE"}).attrs["value"],
        "__VIEWSTATEGENERATOR": sis_login_soup.find("input", attrs={"name": "__VIEWSTATEGENERATOR"}).attrs["value"],
        "__EVENTVALIDATION": sis_login_soup.find("input", attrs={"name": "__EVENTVALIDATION"}).attrs["value"],
        "ctl00$ContentPlaceHolder1$hfAppName": "Öğrenci Bilgi Sistemi",
        "ctl00$ContentPlaceHolder1$hfToken": "",
        "ctl00$ContentPlaceHolder1$hfVerifier": "",
        "ctl00$ContentPlaceHolder1$hfCode": "",
        "ctl00$ContentPlaceHolder1$hfState": "",
        "ctl00$ContentPlaceHolder1$tbUserName": user_name,
        "ctl00$ContentPlaceHolder1$tbPassword": str(password),
        "ctl00$ContentPlaceHolder1$btnLogin": "Giriş"
    }

    try:
        session.post(sis_login_page.url, data=sis_login_data)

        info_system_login_page = session.get(info_system_login_page_url)
        info_system_login_soup = bs4.BeautifulSoup(info_system_login_page.text, "html.parser")

        info_system_login_data = {
            "sid": str(student_number),
            "PIN": str(pin),
            "SessionId": info_system_login_soup.find("input", attrs={"name": "SessionId"}).attrs["value"]
            }

        session.post(info_system_login_post_url, data=info_system_login_data)

        transcript_html = session.get(transcript_page_url)
        if transcript_html.url.split("?")[0] == info_system_login_page_url:
            return 2

    except AttributeError:
        return 1

    return transcript_html


if __name__ == "__main__":
    pass
