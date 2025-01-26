from student import student, studentManager

def main():
    manager = studentManager()

    while True:
        print("\nStudent Information Management System")
        print("1. add students infor")
        print("2. edit students infor")
        print("3. show the list")
        print("4. inquire age group(enter min and max age)")
        print("5. Exit")
        choice = input("choice：")

        if choice == "1":
            name = input("name：")
            age = int(input("age："))
            gender = input("gender：")
            student1 = student(name, age, gender)
            manager.add_student(student1)
        
        elif choice == "2":
            name = input("who needs to modify：")
            print("space = not modify：")
            new_name = input("new name：").strip()
            new_age = input("new age：").strip()
            new_gender = input("new gender：").strip()

            new_info = {}
            if new_name:
                new_info["name"] = new_name
            if new_age:
                new_info["age"] = int(new_age)
            if new_gender:
                new_info["gender"] = new_gender

            manager.update_student(name, new_info)

        elif choice == "3":
            manager.display_students()

        elif choice == "4":
            min_age = int(input("min age："))
            max_age = int(input("max age："))
            manager.query_students_by_age(min_age, max_age)

        elif choice == "5":
            print("Exit")
            break

        else:
            print("error! choose again.")

if __name__ == '__main__':
    app = main()