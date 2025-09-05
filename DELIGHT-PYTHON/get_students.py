class Student:
    def __init__(self, username, name, age, city, zip_code, courses):
        self.username = username
        self.name = name
        self.age = age
        self.city = city
        self.zip = zip_code
        self.courses = courses

students = []
courses_offered = [
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
]

def add_student():
    username = input("Enter username: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")
    course_input = input("Enter courses (comma-separated): ")
    courses = [course.strip() for course in course_input.split(",")]
    new_student = Student(username, name, age, city, zip_code, courses)
    students.append(new_student)
    print("Student added successfully!")

def find_student(username):
    for student in students:
        if student.username == username:
            return student
    return None

def display_student():
    username = input("Enter username to display: ")
    student = find_student(username)
    if student:
        print(f"Name: {student.name}, Age: {student.age}, City: {student.city}, Zip: {student.zip}, Courses: {', '.join(student.courses)}")
    else:
        print("Student not found.")

def add_course():
    username = input("Enter username: ")
    course = input("Enter course to add: ")
    student = find_student(username)
    if student:
        if course not in courses_offered:
            print("Course not offered.")
        elif course in student.courses:
            print("Course already exists.")
        else:
            student.courses.append(course)
            print(f"{course} added successfully!")
    else:
        print("Student not found.")

def update_course():
    username = input("Enter username: ")
    old_course = input("Enter course to replace: ")
    new_course = input("Enter new course: ")
    student = find_student(username)
    if student:
        if old_course in student.courses and new_course in courses_offered:
            index = student.courses.index(old_course)
            student.courses[index] = new_course
            print(f"{old_course} updated to {new_course}")
        else:
            print("Invalid course update.")
    else:
        print("Student not found.")

def update_student():
    username = input("Enter username: ")
    student = find_student(username)
    if student:
        name = input("Enter new name (or leave blank): ")
        age_input = input("Enter new age (or leave blank): ")
        city = input("Enter new city (or leave blank): ")
        zip_code = input("Enter new zip (or leave blank): ")

        if name: student.name = name
        if age_input: student.age = int(age_input)
        if city: student.city = city
        if zip_code: student.zip = zip_code

        print("Student updated!")
    else:
        print("Student not found.")

def total_students():
    print(f"Total students: {len(students)}")

# Menu loop
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Add Course")
    print("4. Update Course")
    print("5. Update Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        add_course()
    elif choice == "4":
        update_course()
    elif choice == "5":
        update_student()
    elif choice == "6":
        total_students()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
