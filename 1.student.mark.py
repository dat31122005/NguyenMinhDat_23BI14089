class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        self.num_students = int(input("Enter the number of students: "))

    def input_student_information(self):
        for _ in range(self.num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            self.students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})

    def input_number_of_courses(self):
        self.num_courses = int(input("Enter the number of courses: "))

    def input_course_information(self):
        for _ in range(self.num_courses):
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append({"id": course_id, "name": course_name})

    def select_course_and_input_marks(self):
        course_id = input("Enter the course ID to input marks: ")
        selected_course = next((course for course in self.courses if course["id"] == course_id), None)
        if not selected_course:
            print("Course not found.")
            return

        for student in self.students:
            mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
            student['marks'][course_id] = mark

    def list_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(f"ID: {course['id']}, Name: {course['name']}")

    def list_students(self):
        print("\nStudents:")
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

    def show_student_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        selected_course = next((course for course in self.courses if course["id"] == course_id), None)
        if not selected_course:
            print("Course not found.")
            return

        print(f"\nMarks for course {selected_course['name']} (ID: {course_id}):")
        for student in self.students:
            mark = student['marks'].get(course_id, "N/A")
            print(f"{student['name']} (ID: {student['id']}): {mark}")

if __name__ == "__main__":
    smm = StudentMarkManagement()

    smm.input_number_of_students()
    smm.input_student_information()

    smm.input_number_of_courses()
    smm.input_course_information()

    while True:
        print("\nOptions:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            smm.list_courses()
        elif choice == 2:
            smm.list_students()
        elif choice == 3:
            smm.select_course_and_input_marks()
        elif choice == 4:
            smm.show_student_marks()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
