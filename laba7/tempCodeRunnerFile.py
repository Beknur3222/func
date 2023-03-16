def create_students_dict():
    students_dict = {}
    while True:
        name = input("Введите имя студента: ")
        if not name:
            break
        age = int(input("Введите возраст студента: "))
        major = input("Введите специализацию студента: ")
        students_dict[name] = {"age": age, "major": major}
    return students_dict