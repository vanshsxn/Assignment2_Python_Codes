class StudentRecord:
    def __init__(self, student_id, name, internal_marks, medical_leaves, disciplinary_notes):
        self.student_id = student_id
        self.name = name
        self.__internal_marks = internal_marks
        self.__medical_leaves = medical_leaves
        self.__disciplinary_notes = disciplinary_notes

    def get_marks(self, role):
        if role not in ("instructor","admin"):
            raise PermissionError("Access denied")
        return self.__internal_marks

    def set_marks(self, role, new_marks):
        if role != "instructor":
            raise PermissionError("Only instructor can set marks")
        if not all(0 <= m <= 100 for m in new_marks):
            raise ValueError("Marks must be between 0 and 100")
        self.__internal_marks = new_marks

    def view_sensitive(self, role):
        if role == "admin":
            return {"medical_leaves": self.__medical_leaves, "discipline": self.__disciplinary_notes}
        raise PermissionError("Access denied")

s = StudentRecord("S1001","Raj",[78,85,90], 2, "None")
try:
    print(s.get_marks("student"))
except Exception as e:
    print(e)
print(s.get_marks("instructor"))
try:
    s.set_marks("student",[80,80,80])
except Exception as e:
    print(e)
s.set_marks("instructor",[80,80,80])
print(s.get_marks("instructor"))
print(s.view_sensitive("admin"))
