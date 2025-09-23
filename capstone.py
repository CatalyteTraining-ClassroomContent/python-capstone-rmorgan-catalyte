# Filter By Date Feature

def filter_by_date(submissions: List[Dict[str, Any]], date: str) -> List[Dict[str, Any]]:
    """
    Returns all submissions with a submissionDate equal to the given date.
    """
    return [s for s in submissions if s.get("submissionDate") == date]


# Filter By StudentId Feature

def filter_by_student_id(submissions: List[Dict[str, Any]], student_id: int) -> List[Dict[str, Any]]:
    """
    Returns all submissions with a studentId equal to the given student_id.
    """
    return [s for s in submissions if s.get("studentId") == student_id]

