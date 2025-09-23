
def filter_by_date(submissions: list[dict[str, any]], submitted_date: str) -> list[dict[str, any]]:
    """
    Filters submissions by provided submitted date.
    Parameters:
        submissions (list[dict[str, any]]): A list of submissions to filter.
        submitted_date (str): The submission date to filter by.
    Returns:
        list[dict]: A the filtered submissions list.
    """

    return [s for s in submissions if s.get("submissionDate") == submitted_date]


def filter_by_student_id(submissions: list[dict[str, any]], student_id: int) -> list[dict[str, any]]:
    """
    Filter submissions by provided student id.

    Parameters:
        submissions (list[dict[str, any]]): _description_
        student_id (int): _description_

    Returns:
        list[dict[str, any]]: _description_
    """
    return [s for s in submissions if s.get("studentId") == student_id]


def find_unsubmitted(submitted_date: str, student_names: list[str], submissions: list[dict[str, any]]) -> list[str]:
    """
    Filter submissions by finding unsubmitted data

    Parameters:
        submitted_date (str): _description_
        student_names (list[str]): _description_
        submissions (list[dict[str, any]]): _description_

    Returns:
        list[str]: _description_
    """
    submitted = {s["studentName"] for s in submissions if s.get("submissionDate") == submitted_date}
    return [name for name in student_names if name not in submitted]

