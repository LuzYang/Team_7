import json

class student:
    def __init__(self,name:str,age:int,gender:str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def dict_infor(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }
    
class studentManager:
    def __init__(self, file_name="roster.json"):
        self.file_name = file_name
        return None

    def read_file(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump([], file)
            return []
    
    def write_file(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        return None

    def add_student(self, student):
        data = self.read_file()
        data.append(student.dict_infor())
        self.write_file(data)
        return None
    
    def update_student(self, name, new_info):
        data = self.read_file()
        for student in data:
            if student["name"] == name:
                student.update(new_info)
                self.write_file(data)
                return None
        print('No student found.')

    def display_students(self):
        data = self.read_file()
        if not data:
            print("No infor.")
            return None
        else:
            print("students information：")
            for student in data:
                print(f"name: {student['name']}, age: {student['age']}, gender: {student['gender']}")
            return None
    
    def query_students_by_age(self, min_age, max_age):
        data = self.read_file()
        result = [student for student in data if min_age <= student["age"] <= max_age]###################
        if not result:
            print(f"No results found.")
            return None
        else:
            print(f"students information：")
            for student in result:
                print(f"name: {student['name']}, age: {student['age']}, gender: {student['gender']}")
            print(f"Total: {len(result)}")
            return None