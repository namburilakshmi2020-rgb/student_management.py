import json
import os

DATA_FILE = "data.json"


def load_data():
    """Load student data from JSON file if available."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_data():
    """Save student data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)


def add_student():
    roll = input("Roll no: ").strip()
    if any(s['roll_no'] == roll for s in students):
        print("⚠ Roll no already exists.")
        return
    name = input("Name: ").strip()
    grade = input("Grade: ").strip()
    age = input("Age (optional): ").strip()

    student = {"roll_no": roll, "name": name, "grade": grade}
    if age:
        student["age"] = age

    students.append(student)
    print("✅ Student added.")


def view_students():
    if not students:
        print("No records found.")
        return
    print(f"\n{'Roll':<10}{'Name':<20}{'Grade':<6}{'Age':<5}")
    print("-" * 45)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['grade']:<6}{s.get('age','-'):<5}")
    print()


def search_student():
    roll = input("Enter roll no to search: ").strip()
    for s in students:
        if s['roll_no'] == roll:
            print("✅ Found:", s)
            return s
    print("⚠ Student not found.")
    return None


def update_student():
    roll = input("Roll no to update: ").strip()
    student = next((s for s in students if s['roll_no'] == roll), None)
    if not student:
        print("⚠ Student not found.")
        return

    new_name = input(f"Name [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name

    new_grade = input(f"Grade [{student['grade']}]: ").strip()
    if new_grade:
        student['grade'] = new_grade

    new_age = input(f"Age [{student.get('age','-')}]: ").strip()
    if new_age:
        student['age'] = new_age

    print("✅ Student updated.")


def delete_student():
    roll = input("Roll no to delete: ").strip()
    student = next((s for s in students if s['roll_no'] == roll), None)
    if not student:
        print("⚠ Student not found.")
        return
    confirm = input("Are you sure you want to delete? (y/N): ").strip().lower()
    if confirm == 'y':
        students.remove(student)
        print("✅ Student deleted.")
    else:
        print("❌ Delete cancelled.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1) Add Student")
        print("2) View Students")
        print("3) Search Student")
        print("4) Update Student")
        print("5) Delete Student")
        print("6) Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()
            print("💾 Data saved. Exiting...")
            break
        else:
            print("⚠ Invalid choice. Try again.")
if __name__=="__main__":
    students=load_data()
    main()