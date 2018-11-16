""" Example 2c: Modularity """

def compute_grade_average(grades_file_path):
    grades = read_grades(grades_file_path)
    return compute_average(grades)


def read_grades(grades_file_path):
    with open(grades_file_path, "r") as the_file:
        grades = list()
        for grade in the_file:
            grade_as_num = float(grade)
            grades.append(grade_as_num)
    return grades


def compute_average(array):
    the_sum = 0
    for el in array:
        the_sum = the_sum + el
    avg = the_sum / len(array)
    return avg
