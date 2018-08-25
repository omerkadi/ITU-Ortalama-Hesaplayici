import curriculums
import os
from json import dump, load


def save_departments_code() -> bool:
    data = curriculums.get_departments_code()
    if not os.path.exists("Data"):
        os.makedirs("Data")

    with open("Data/departments.json", "w") as file:
        dump(data, file)
    return True


def read_departments_code() -> dict:
    if not os.path.exists("Data/departments.json"):
        save_departments_code()

    with open('Data/departments.json') as file:
        departments_code = load(file)
    return departments_code


def save_departments_curriculum(code: str) -> bool:
    data = curriculums.trim_mt_and_itb(curriculums.get_department_curriculum(code))

    if not os.path.exists("Data/Curriculum"):
        os.makedirs("Data/Curriculum")

    if not data:
        return False
    else:
        with open("Data/Curriculum/"+code+".json", "w") as file:
            dump(data, file)
    return True


def read_departments_curriculum(code: str) -> list:
    if not os.path.exists("Data/Curriculum/" + code + ".json"):
        save_departments_curriculum(code)

    with open("Data/Curriculum/" + code + ".json") as file:
        data = load(file)
    return data


def save_elective_courses_urls(code: str) -> bool:
    data = curriculums.get_elective_courses_urls(code)

    if not os.path.exists("Data/ElectiveCourses/Urls"):
        os.makedirs("Data/ElectiveCourses/Urls")

    if not data:
        return False
    else:
        with open("Data/ElectiveCourses/Urls/" + code + ".json", "w") as file:
            dump(data, file)
    return True


def read_elective_courses_urls(code: str) -> list:
    if not os.path.exists("Data/ElectiveCourses/Urls/" + code + ".json"):
        save_elective_courses_urls(code)

    with open("Data/ElectiveCourses/Urls/" + code + ".json") as file:
        data = load(file)
    return data


def save_elective_courses(code: str) -> bool:
    data = curriculums.get_elective_courses(read_elective_courses_urls(code))

    if not os.path.exists("Data/ElectiveCourses"):
        os.makedirs("Data/ElectiveCourses")

    if not data:
        return False
    else:
        with open("Data/ElectiveCourses/" + code + ".json", "w") as file:
            dump(data, file)
    return True


def read_elective_courses(code: str) -> list:
    if not os.path.exists("Data/ElectiveCourses/" + code + ".json"):
        save_elective_courses(code)

    with open("Data/ElectiveCourses/" + code + ".json") as file:
        data = load(file)
    return data


def save_verify_departments_code() -> bool:
    departments_code = read_departments_code()
    verified_departments = curriculums.verify_departments_code(departments_code)

    if not os.path.exists("Data/"):
        os.makedirs("Data")

    with open("Data/verified_departments.json", "w") as file:
        dump(verified_departments, file)
    return True


def read_verify_departments_code() -> dict:
    if not os.path.exists("Data/verified_departments.json"):
        save_verify_departments_code()

    with open('Data/verified_departments.json') as file:
        departments_code = load(file)
    return departments_code


def read_old_courses():
    with open("Data/old_courses.json") as file:
        old_courses = load(file)
    return old_courses


def read_non_english_courses():
    with open("Data/non-english_courses.json") as file:
        courses = load(file)
    return courses


def save_transcript(user_name, transcript_data):
    if not os.path.exists("Data/Transcripts"):
        os.makedirs("Data/Transcripts")

    with open("Data/Transcripts/" + str(user_name) + ".json", "w") as file:
        dump(transcript_data, file)

    return True


def read_transcript(user_name):
    path = "Data/Transcripts/" + str(user_name) + ".json"

    if not os.path.exists(path):
        return None

    with open(path, "r") as file:
        transcript_data = load(file)

    return transcript_data


if __name__ == "__main__":
    a = read_departments_code()
    b = read_departments_curriculum("FIZ")
    c = read_elective_courses_urls("FIZ")
    d = read_elective_courses("FIZ")
    e = read_verify_departments_code()
    f = read_old_courses()
    g = read_non_english_courses()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(read_transcript("test_data"))
