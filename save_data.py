import curriculums
import csv
import os


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

    if not os.path.exists("Data/Cirriculums"):
        os.makedirs("Data/Cirriculums")

    if not data:
        return False
    else:
        fieldnames = data[0].keys()
        with open("Data/Cirriculums/"+code+".csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for lst in data:
                writer.writerow(lst)
    return True


def read_depatments_cirriculum(code: str) -> list:
    data = []
    if not os.path.exists("Data/Cirriculums/" + code + ".csv"):
        save_departments_curriculum(code)

    with open("Data/Cirriculums/" + code + ".csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
    return data


def save_secmeli_ders_urls(code: str) -> bool:
    data = curriculums.get_secmeli_ders_urls(code)

    if not os.path.exists("Data/SecmeliDers/Urls"):
        os.makedirs("Data/SecmeliDers/Urls")

    if not data:
        return False
    else:
        with open("Data/SecmeliDers/Urls/" + code + ".csv", "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    return True


def read_secmeli_ders_urls(code: str) -> list:
    data = []
    if not os.path.exists("Data/SecmeliDers/Urls/" + code + ".csv"):
        save_secmeli_ders_urls(code)

    with open("Data/SecmeliDers/Urls/" + code + ".csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data = row
    return data


def save_secmeli_ders(code: str) -> bool:
    data = curriculums.get_secmeli_ders(read_secmeli_ders_urls(code))

    if not os.path.exists("Data/SecmeliDers"):
        os.makedirs("Data/SecmeliDers")

    if not data:
        return False
    else:
        fieldnames = list(data[0].keys())
        with open("Data/SecmeliDers/" + code + ".csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for ders in data:
                writer.writerow(ders)
    return True


def read_secmeli_ders(code: str) -> list:
    data = []
    if not os.path.exists("Data/SecmeliDers/" + code + ".csv"):
        save_secmeli_ders(code)

    with open("Data/SecmeliDers/" + code + ".csv") as csvfile:
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


if __name__ == "__main__":
    a = read_departments_code()
    b = read_depatments_cirriculum("FIZ")
    c = read_secmeli_ders_urls("FIZ")
    d = read_secmeli_ders("FIZ")
    e = read_verify_departments_code()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
