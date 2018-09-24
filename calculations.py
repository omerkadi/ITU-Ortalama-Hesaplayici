
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
        return -1.00


def calculate_gpa(data):
    total_credits = 0
    total_points = 0

    for pair in data:
        total_credits += pair[0]
        total_points += pair[0] * pair[1]

    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = total_points/total_credits

    return gpa
