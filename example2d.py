""" Example 2d: Using code features """

def compute_grade_average(grades_file_path):
    grades = read_grades(grades_file_path)
    return compute_average(grades)


def read_grades(grades_file_path):
    with open(grades_file_path, "r") as the_file:
        grades = the_file.readlines()
    return [float(g) for g in grades]


def compute_average(array):
    return sum(array)/len(array)
