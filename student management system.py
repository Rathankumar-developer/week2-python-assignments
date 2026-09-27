"""
Mini Project (W2): Student Management System
Store student data (name, marks, roll number) in a CSV file.
Add/Delete/Search functions. Save changes permanently to file.
"""

import csv
import os

CSV_FILE = "students.csv"
FIELDNAMES = ["roll_number", "name", "marks"]


def ensure_file_exists(filepath):
    if not os.path.exists(filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_all_students(filepath):
    ensure_file_exists(filepath)
    with open(filepath, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_all_students(filepath, students):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student(filepath):
    roll_number = input("Enter roll number: ").strip()
    students = read_all_students(filepath)

    if any(s["roll_number"] == roll_number for s in students):
        print(f"A student with roll number '{roll_number}' already exists.")
        return

    name = input("Enter name: ").strip()
    marks = input("Enter marks: ").strip()

    students.append({"roll_number": roll_number, "name": name, "marks": marks})
    write_all_students(filepath, students)
    print(f"Student '{name}' added and saved to file.")


def search_student(filepath):
    roll_number = input("Enter roll number to search: ").strip()
    students = read_all_students(filepath)

    for s in students:
        if s["roll_number"] == roll_number:
            print(f"Roll Number: {s['roll_number']}")
            print(f"Name       : {s['name']}")
            print(f"Marks      : {s['marks']}")
            return

    print(f"No student found with roll number '{roll_number}'.")


def delete_student(filepath):
    roll_number = input("Enter roll number to delete: ").strip()
    students = read_all_students(filepath)

    remaining = [s for s in students if s["roll_number"] != roll_number]

    if len(remaining) == len(students):
        print(f"No student found with roll number '{roll_number}'.")
        return

    write_all_students(filepath, remaining)
    print(f"Student with roll number '{roll_number}' deleted and changes saved.")


def list_students(filepath):
    students = read_all_students(filepath)
    if not students:
        print("No student records found.")
        return

    print(f"{'Roll No.':<10}{'Name':<20}{'Marks':<10}")
    print("-" * 40)
    for s in students:
        print(f"{s['roll_number']:<10}{s['name']:<20}{s['marks']:<10}")


def main():
    ensure_file_exists(CSV_FILE)

    menu = """
--- Student Management System ---
1. Add Student
2. Search Student
3. Delete Student
4. List All Students
5. Exit
"""
    actions = {
        "1": add_student,
        "2": search_student,
        "3": delete_student,
        "4": list_students,
    }

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(CSV_FILE)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
