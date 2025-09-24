
def filter_by_date(submissions, date):
    """
    Filters submissions by provided submitted date. 
    Parameters:
        submissions (list): A list of submission dictionaries.
        date (str): The date you want to filter by (example: "2025-09-01").
    
    Returns:
        list: A list of submissions that match the given date.
    """
    result = []
    for s in submissions:
        if s["submissionDate"] == date:
            result.append(s)
    return result


def filter_by_student_id(submissions, student_id):
    """
    Filter submissions by provided student id. 
    Parameters:
        submissions (list): A list of submission dictionaries.
        student_id (int): The ID of the student you want to filter by.
    
    Returns:
        list: A list of submissions that belong to the given student ID.
    """
    result = []
    for s in submissions:
        if s["studentId"] == student_id:
            result.append(s)
    return result


def find_unsubmitted(date, student_names, submissions):
    """
    Filter submissions by finding unsubmitted data 
    Parameters:
        date (str): The date to check (example: "2025-09-01").
        student_names (list): A list of all student names (strings).
        submissions (list): A list of submission dictionaries.
    
    Returns:
        list: A list of student names who did not submit on the given date.
    """
    submitted_students = []
    for s in submissions:
        if s["submissionDate"] == date:
            submitted_students.append(s["studentName"])

    not_submitted = []
    for name in student_names:
        found = False
        for submitted in submitted_students:
            if name == submitted:
                found = True
        if found == False:
            not_submitted.append(name)
    return not_submitted



def get_average_score(submissions):
    """

    Parameters:
        submissions (list): A list of submission dictionaries.
    
    Returns:
        float: The average score of all submissions, rounded to 1 decimal place.
               If there are no submissions, returns 0.0.
    """
    if len(submissions) == 0:
        return 0.0

    total = 0
    count = 0
    for s in submissions:
        total = total + s["quizScore"]
        count = count + 1

    avg = total / count
    return round(avg, 1)


def get_average_score_by_module(submissions):
    """
   collect scores of module and compute averages
    Parameters:
        submissions (list): A list of submission dictionaries.
    
    Returns:
        dict: A dictionary where the keys are module names (strings),
              and the values are the average scores for that module,
              rounded to 1 decimal place.
    """
    module_scores = {}

