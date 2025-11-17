class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def details(self):
        return f"{self.staff_id} - {self.name}"

class Doctor(Staff):
    def diagnose(self, patient):
        return f"Dr.{self.name} diagnosing {patient}"

class Nurse(Staff):
    def assist(self, procedure):
        return f"Nurse {self.name} assisting in {procedure}"

class Surgeon(Doctor):
    def operate(self, procedure):
        return f"Surgeon {self.name} performing {procedure}"

class LabTechnician(Staff):
    def run_test(self, test):
        return f"LabTech {self.name} running {test}"

d = Doctor("Reema", "D101")
n = Nurse("Sam", "N201")
s = Surgeon("Irfan", "S301")
l = LabTechnician("Kiran", "L401")
print(d.details(), d.diagnose("patient A"))
print(n.details(), n.assist("blood draw"))
print(s.details(), s.operate("appendectomy"))
print(l.details(), l.run_test("CBC"))
