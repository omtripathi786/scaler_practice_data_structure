class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def displayInfo(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")

    def getUsername(self):
        return self._username

    def getEmail(self):
        return self._email


class Student(User):
    def __init__(self, username, email, studentId, course):
        super().__init__(username, email)
        self._studentId = studentId
        self._course = course

    def displayInfo(self):
        super().displayInfo()
        print(f"Student ID: {self._studentId}")
        print(f"Course: {self._course}")

    def getStudentId(self):
        return self._studentId

    def getCourse(self):
        return self._course


class Employee(User):
    def __init__(self, username, email, employeeId, department):
        super().__init__(username, email)
        self._employeeId = employeeId
        self._department = department

    def displayInfo(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")
        print(f"Employee ID: {self._employeeId}")
        print(f"Department: {self._department}")

    def getEmployeeId(self):
        return self._employeeId

    def getDepartment(self):
        return self._department


# Example usage
if __name__ == "__main__":
    # Create a User object
    user = User("john_doe", "john.doe@example.com")
    print("User Info:")
    user.displayInfo()
    print()

    # Create a Student object
    student = Student("jane_smith", "jane.smith@example.com", "S12345", "Computer Science")
    print("Student Info:")
    student.displayInfo()
    print()

    # Create an Employee object
    employee = Employee("mike_jones", "mike.jones@example.com", "E54321", "IT")
    print("Employee Info:")
    employee.displayInfo()
