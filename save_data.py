import sqlite3
import os
from json import dump, load

import curriculums
import calculations


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


def save_transcript(transcript_data, user_name=None, directory=None):
    if directory is not None:
        with open(directory, "w") as file:
            dump(transcript_data, file)
    else:
        if not os.path.exists("Data/Transcripts"):
            os.makedirs("Data/Transcripts")

        with open("Data/Transcripts/" + str(user_name) + ".json", "w") as file:
            dump(transcript_data, file)

    return True


def read_transcript(user_name=None, directory=None):
    if directory is not None:
        with open(directory, "r") as file:
            transcript_data = load(file)
    else:
        path = "Data/Transcripts/" + str(user_name) + ".json"

        if not os.path.exists(path):
            return None

        with open(path, "r") as file:
            transcript_data = load(file)

    return transcript_data


def save_transcript_to_db(transcript_data, user_name):
    path = "Data/Transcripts/" + user_name + ".dp"

    if os.path.exists(path):
        os.remove(path)

    connection = sqlite3.connect(path)
    cursor = connection.cursor()

    sql_create_season_table = """
        CREATE TABLE seasons ( 
            Season_Name VARCHAR(24) NOT NULL, 
            Editable TINYINT NOT NULL, 
            GPA FLOAT(3,2) DEFAULT 0.0,
            Total_Credit FLOAT(2,1) DEFAULT 0.0,
            PRIMARY KEY (Season_Name) 
        )"""

    sql_create_course_table = """
        CREATE TABLE courses ( 
            Season_Name VARCHAR(24) NOT NULL, 
            Course_Code VARCHAR(9) NOT NULL,
            English_Course TINYINT NOT NULL, 
            Title VARCHAR(50) NOT NULL, 
            Credit FLOAT(2,1) NOT NULL, 
            Grade VARCHAR(4) NOT NULL, 
            Grade_Numeric FLOAT(2,1) NOT NULL,
            Passive TINYINT NOT NULL, 
            PRIMARY KEY (Season_Name, Course_Code) 
        )"""

    gpa_trigger_insert = """
            CREATE TRIGGER insert_gpa AFTER INSERT ON courses
                BEGIN
                    UPDATE seasons SET 
                        GPA = (GPA * Total_Credit + NEW.Credit * NEW.Grade_Numeric) / (Total_Credit + NEW.Credit),
                        Total_Credit = Total_Credit + NEW.Credit 
                        WHERE Season_Name == NEW.Season_Name AND NEW.Grade_Numeric != -1.0 AND NEW.Credit != 0;
                END"""

    cursor.execute(sql_create_season_table)
    cursor.execute(sql_create_course_table)

    cursor.execute(gpa_trigger_insert)

    for i, season_courses in enumerate(transcript_data[0]):
        season_name = transcript_data[1][i]
        sql_insert_season = "INSERT INTO seasons (Season_Name, Editable) VALUES (?,?)"
        cursor.execute(sql_insert_season, (season_name, 0))
        for course in season_courses:
            english_course = 0
            passive = 0
            if course[0][-1] == "E":
                english_course = 1
                course[0] = course[0][:-1]

            if course[3][-1] == "*":
                passive = 1

            sql_insert_course = "INSERT INTO courses VALUES (?,?,?,?,?,?,?,?)"
            course_params = (season_name, course[0], english_course, course[1], float(course[2][3:6]), course[3],
                             calculations.solve_grade(course[3]), passive)
            cursor.execute(sql_insert_course, course_params)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    a = read_old_courses()
    print(a)

