import curriculums
import csv
import os
import json


def save_departments_code() -> bool:
    data = curriculums.get_departments_code()
    fieldnames = list(data.keys())
    if not os.path.exists("Data"):
        os.makedirs("Data")

    with open("Data/departments.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
    return True


def read_departments_code() -> dict:
    if not os.path.exists("Data/departments.csv"):
        save_departments_code()

    with open('Data/departments.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        departments_code = {}
        for row in reader:
            departments_code = dict(row)
    return departments_code


def save_departments_curriculum(code: str) -> bool:
    data = curriculums.trim_mt_and_itb(curriculums.get_department_curriculum(code))

    if not os.path.exists("Data/Curriculum"):
        os.makedirs("Data/Curriculum")

    if not data:
        return False
    else:
        fieldnames = data[0].keys()
        with open("Data/Curriculum/"+code+".csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for lst in data:
                writer.writerow(lst)
    return True


def read_departments_curriculum(code: str) -> list:
    data = []
    if not os.path.exists("Data/Curriculum/" + code + ".csv"):
        save_departments_curriculum(code)

    with open("Data/Curriculum/" + code + ".csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data


def save_elective_courses_urls(code: str) -> bool:
    data = curriculums.get_elective_courses_urls(code)

    if not os.path.exists("Data/ElectiveCourses/Urls"):
        os.makedirs("Data/ElectiveCourses/Urls")

    if not data:
        return False
    else:
        with open("Data/ElectiveCourses/Urls/" + code + ".csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    return True


def read_elective_courses_urls(code: str) -> list:
    data = []
    if not os.path.exists("Data/ElectiveCourses/Urls/" + code + ".csv"):
        save_elective_courses_urls(code)

    with open("Data/ElectiveCourses/Urls/" + code + ".csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data = row
    return data


def save_elective_courses(code: str) -> bool:
    data = curriculums.get_elective_courses(read_elective_courses_urls(code))

    if not os.path.exists("Data/ElectiveCourses"):
        os.makedirs("Data/ElectiveCourses")

    if not data:
        return False
    else:
        fieldnames = list(data[0].keys())
        with open("Data/ElectiveCourses/" + code + ".csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ders in data:
                writer.writerow(ders)
    return True


def read_elective_courses(code: str) -> list:
    data = []
    if not os.path.exists("Data/ElectiveCourses/" + code + ".csv"):
        save_elective_courses(code)

    with open("Data/ElectiveCourses/" + code + ".csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data


def save_verify_departments_code() -> bool:
    departments_code = read_departments_code()
    verified_departments = curriculums.verify_departments_code(departments_code)

    if not os.path.exists("Data/"):
        os.makedirs("Data")

    fieldnames = list(verified_departments.keys())
    with open("Data/verified_departments.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(verified_departments)
    return True


def read_verify_departments_code() -> dict:
    if not os.path.exists("Data/verified_departments.csv"):
        save_verify_departments_code()

    with open('Data/verified_departments.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        departments_code = {}
        for row in reader:
            departments_code = dict(row)
    return departments_code


def read_old_courses():
    with open("Data/old_courses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        old_courses = {}
        for row in reader:
            old_courses = dict(row)
        return old_courses


def read_non_english_courses():
    courses = []
    with open("Data/Non-English Courses.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            courses = row
    return courses


def save_transcript(user_name, transcript_data):
    if not os.path.exists("Data/Transcripts"):
        os.makedirs("Data/Transcripts")

    with open("Data/Transcripts/" + str(user_name) + ".json", "w") as file:
        json.dump(transcript_data, file)

    return True


def read_transcript(user_name):
    path = "Data/Transcripts/" + str(user_name) + ".json"

    if not os.path.exists(path):
        return None

    with open(path, "r") as file:
        transcript_data = json.load(file)

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
