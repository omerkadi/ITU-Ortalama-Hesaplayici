import sqlite3
import calculations
from save_data import read_old_courses
from shutil import copy2, rmtree
from os import path, makedirs


class Transcript:
    def __init__(self):
        self.user_name = ""
        self.path = ""
        self.temp_path = ""
        self.temp_root_path = ""
        self.connection = None
        self.cursor = None

    def set_user_name(self, user_name):
        if self.user_name == "":
            self.user_name = user_name
            return True
        else:
            return False

    def set_path(self, path):
        if self.path == "":
            self.path = path
            self.set_temp_path()
            self.open_connection()
            return True
        else:
            return False

    def set_temp_path(self):
        self.temp_root_path = self.path.split(".")[0]
        if not path.exists(self.temp_root_path):
            makedirs(self.temp_root_path)

        self.temp_path = self.temp_root_path + "/" + self.user_name + ".dp"

    def get_transcript_data(self):
        seasons = self.cursor.execute("SELECT * FROM seasons").fetchall()
        seasons = self.sort_season(seasons)

        transcript_data = []
        for row in seasons:
            courses = self.cursor.execute("SELECT * FROM courses WHERE Season_Name == '" + row[0] + "'")

            transcript_data.append([row[0][:9], row[0][12:], row[3], round(row[2], 2), row[1], "Season", row[0], 0])
            for course in courses:
                if course[2]:
                    course_code = course[1] + "E"
                else:
                    course_code = course[1]

                transcript_data.append([course_code, course[3], course[4], course[5], row[1], "Course", row[0],
                                        course[7]])

        return transcript_data

    def get_editable_data(self):
        seasons = self.cursor.execute("SELECT * FROM seasons").fetchall()
        seasons = self.sort_season(seasons)

        editable_seasons = []
        for row in seasons:
            if row[1]:
                editable_seasons.append(row[0])

        courses = self.cursor.execute("SELECT * FROM courses").fetchall()

        editable_courses = []
        for course in courses:
            editable_courses.append([course[1], course[5]])

        return editable_courses

    def get_last_season(self):
        seasons = self.cursor.execute("SELECT * FROM seasons").fetchall()
        seasons = self.sort_season(seasons)

        last_season = ""
        for season in reversed(seasons):
            if not season[1]:
                last_season = season[0]
                break

        return last_season

    def get_gpa(self):
        data = self.cursor.execute("SELECT Credit, Grade_Numeric FROM courses WHERE Passive == 0")
        gpa = calculations.calculate_gpa(data)

        return gpa

    def get_season_gpa(self, season_name):
        gpa = self.cursor.execute("SELECT GPA FROM seasons WHERE Season_Name == '" + season_name + "'").fetchone()

        return round(gpa[0], 2)

    def get_course(self, course_code):
        course = self.cursor.execute("SELECT * FROM seasons WHERE Course_Code == '" + course_code + "'").fetchall()

        return course

    def update_course(self, season_name, course_code, new_grade, passive=None):
        if passive is None:
            self.cursor.execute("UPDATE courses SET Grade = '" + new_grade + " ', Grade_Numeric = " +
                                str(calculations.solve_grade(new_grade)) + " WHERE Season_Name == '" + season_name +
                                "' AND Course_Code == '" + course_code + "'")
        else:
            self.cursor.execute("UPDATE courses SET Grade = '" + new_grade + " ', Passive = " + passive +
                                " WHERE Season_Name == '" + season_name + "' AND Course_Code == '" + course_code + "'")

    def update_season_gpa(self, season_name):
        data = self.cursor.execute("SELECT Credit, Grade_Numeric FROM courses WHERE Season_Name == '"
                                   + season_name + "'")
        self.cursor.execute("UPDATE seasons SET GPA = " + str(calculations.calculate_gpa(data)) +
                            " WHERE Season_Name == '" + season_name + "'")

    def update_season_credit(self, season_name):
        credit = self.cursor.execute("SELECT Credit FROM courses WHERE Season_Name == '" + season_name + "'").fetchall()
        total_credit = 0.0
        for data in credit:
            total_credit += data[0]

        self.cursor.execute("UPDATE seasons SET Total_Credit = " + str(total_credit) +
                            " WHERE Season_Name == '" + season_name + "'")

    def add_season(self, season_name):
        self.cursor.execute("INSERT INTO seasons (Season_Name, Editable) VALUES (?,?)", [season_name, 1])

    def add_course(self, course_data):
        if course_data[0][-1] == "E":
            course_code = course_data[0][:-1]
            english_course = 1
        else:
            course_code = course_data[0]
            english_course = 0

        self.cursor.execute("INSERT INTO courses VALUES (?,?,?,?,?,?,?,?)", [course_data[5], course_code,
                                                                             english_course, course_data[1],
                                                                             course_data[2], course_data[3],
                                                                             calculations.solve_grade(course_data[3]),
                                                                             course_data[4]])

        courses = self.cursor.execute("SELECT Season_Name, Course_Code, Passive FROM courses").fetchall()

        for course in courses:
            if course[1] == course_code and course[0] != course_data[5]:
                self.cursor.execute("UPDATE courses SET Passive = 1 WHERE Season_Name == '" + course[0] +
                                    "' AND Course_Code == '" + course_code + "'")

    def check_course_before_added(self, course_code):
        if course_code[-1] == "E":
            course_code = course_code[:-1]

        course = self.cursor.execute("SELECT * FROM courses WHERE Course_Code == '" + course_code + "'").fetchall()

        if course:
            if course[-1][7] == 0:
                self.update_course(course[-1][0], course[-1][1], course[-1][5] + "*", '1')
                return
            else:
                self.update_course(course[-1][0], course[-1][1], course[-1][5][:-2], '0')
                return

        old_courses = read_old_courses()

        if course_code in old_courses:
            self.check_course_before_added(old_courses[course_code])
            return

    def delete_course(self, season_name, course_code, check=True):
        if course_code[-1] == "E":
            course_code = course_code[:-1]

        self.cursor.execute("DELETE FROM courses WHERE Season_Name == '" + season_name + "' AND Course_Code == '"
                            + course_code + "'")

        if check is True:
            self.check_course_before_added(course_code)

    def delete_season(self, season_name):
        courses = self.cursor.execute("SELECT * FROM courses WHERE  Season_Name == '" + season_name + "'").fetchall()
        self.cursor.execute("DELETE FROM seasons WHERE Season_Name == '" + season_name + "'")

        for course in courses:
            if not course[7]:
                self.delete_course(season_name, course[1])

    @staticmethod
    def sort_season(seasons):
        for i in reversed(range(len(seasons))):
            for j in range(i):
                if seasons[j][0][:9] > seasons[j+1][0][:9]:
                    seasons[j], seasons[j+1] = seasons[j+1], seasons[j]
                elif seasons[j][0][:9] == seasons[j+1][0][:9]:
                    if seasons[j][0][12:] == "Yaz Öğretimi":
                        seasons[j], seasons[j + 1] = seasons[j + 1], seasons[j]
                    elif seasons[j][0][12:] == "Bahar" and seasons[j+1][0][12:] == "Güz":
                        seasons[j], seasons[j + 1] = seasons[j + 1], seasons[j]
        return seasons

    def save_connection(self):
        self.connection.commit()
        self.connection.close()
        copy2(self.temp_path, self.path)
        self.open_connection()

    def close_connection(self):
        self.connection.close()
        rmtree(self.temp_root_path)

    def open_connection(self):
        copy2(self.path, self.temp_path)
        self.connection = sqlite3.connect(self.temp_path)
        self.cursor = self.connection.cursor()


if __name__ == "__main__":
    tr = Transcript()
    tr.set_user_name("kadio")
    tr.set_path("Data/Transcripts/kadio.dp")
    tr_data = tr.get_transcript_data
    print(tr.get_last_season())
    print(tr.get_gpa())
