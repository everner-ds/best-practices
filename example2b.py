""" Example 2b: Good documentation """

def compute_grade_average(grades_file_path):
    """ Computes average of grades from a file.

    Args:
        grades_file_path (string): path to file containing grades

    Returns:
        avg_grade (float): average of grades
    """

    # Read grades from file
    with open(grades_file_path, "r") as the_file:
        grades = list()
        for grade in the_file:
            grades.append(grade)

    # Compute average
    grade_sum = 0
    for grade in grades:
        grade_as_num = float(grade)
        grade_sum = grade_sum + grade_as_num

    len_grades = len(grades)
    avg_grade = grade_sum / len_grades

    return avg_grade
