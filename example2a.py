""" Example 2a: Bad documentation """

def compute_grade_average(grades_file):
    """ This function computes average of grades from a file.
        It first opens the file and then reads every grade individually,
        appending it to the grades list.
        After that, the average is computed. In a for loop, each grade
        from the list is converted into a float and added to the sum of
        grades.
        Finally, the average is computed by dividing the sum of grades
        by the number of grades and returned.
        Author: Eric Verner
        Date: Nov 15, 2018
        Company: Mind Research Network
        License: MIT
    """

    # Read grades from file
    with open(grades_file, "r") as the_file:
        grades = list()                         # Initialize grade list
        for grade in the_file:                  # Loop through lines in file
            grades.append(grade)               # Add each grade to the list

    # Compute average
    grade_sum = 0                               # Initialize sum of grades
    for grade in grades:                        # Loop through grades
        grade_as_num = float(grade)             # Convert grade to float
        grade_sum = grade_sum + grade_as_num    # Add to sum of grades

    len_grades = len(grades)                    # Compute length of grades
    avg_grade = grade_sum / len_grades          # Compute average

    return avg_grade
