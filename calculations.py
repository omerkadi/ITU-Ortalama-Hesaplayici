
def calculate_gpa(data: list, credit=False):
    credit_sum = 0.0
    point_sum = 0.0
    for course in data:
        grade = solve_grade(course["Not"])
        if grade is not None:
            credit_sum += float(course["Kredi"])
            point_sum += float(course["Kredi"]) * grade
    if credit_sum == 0:
        gpa = 0
    else:
        gpa = round(point_sum/credit_sum, 2)

    if credit is True:
        return [gpa, credit_sum]
    else:
        return gpa


def solve_grade(data: str) -> [float, None]:

    if data[:2] == "AA":
        return 4.00
    elif data[:2] == "BA":
        return 3.50
    elif data[:2] == "BB":
        return 3.00
    elif data[:2] == "CB":
        return 2.50
    elif data[:2] == "CC":
        return 2.00
    elif data[:2] == "DC":
        return 1.50
    elif data[:2] == "DD":
        return 1.00
    elif data[:2] == "FF" or data[:2] == "VF" or data[:2] == "BL" or data[:2] == "BZ":
        return 0.00
    else:
        return None
