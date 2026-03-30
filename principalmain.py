students = []
def read_int(mensaje, permitir_none=False):
    valor = None
    valido = False
    while not valido:
        entrada = input(mensaje).strip()
        if permitir_none and entrada == "":
            return None
        try:
            valor = int(entrada)
            if valor < 0:
                print("This value is negative")
            else:
                valido = True
        except ValueError:
            print("This number is not valid")
    return valor
def searching_student(students, name):
    for student in students:
        if student["name"].lower() == name.strip().lower():
            return student
    return None
def update_info(name,new_student,new_count):
      print("\n-- Update student--")
      name = read_name("Student name:  ")
      if searching_student(students, name) is None:
        print("Student not found")
        return
      print("Please just get a blanck space")
      new_student = read_name("New student: ", permitir_none=True)
      new_count = read_int("New count ", permitir_none=True)
      if new_student is None and new_count is None:
        print("No se realizaron cambios.")
def showmenu():
      print("Welcome :)\n 1) Register new students\n 2) Search for students\n 3) Update student information\n 4) Delete\n")
      print("\n 5) Out of system (❁´◡`❁)")

def register(name,age,IDnumbers,sbjname,readyornot,list):
        new_student ={
        "Student": name, 
        "Age": age,
        "ID": IDnumbers,
        "Subject": sbjname,
        "Estatus": readyornot,
    }
        students.append(new_student)

def showstudents(students):
    for idx, show in enumerate(students):
        print(f"{idx+1}. Student: {show['Student']} | Age: {show['Age']} | ID: {show['ID']} | Subject: {show['Subject']} | Estatus: {show['Estatus']}")
    print("Done ☆")
def deleteoption(students):
    print("Staring system")
    print("\n-- Deleting students --")
    name = read_name("name to delete ")
    if optionsearch(students, name) is None:
        print("Student not found")
        return
    Check = input("Check elimination " + name + " (si/no): ").strip()
    if Check == "si" or Check == "Si":
        deleteoption(students, name)
    else:
        print("Operacion cancelada.")

def optionsearch(students):
    print("\n-- Buscar student --")
    nombre = read_name("Student a buscar: ")
    student = searching_student(students, nombre)
    if student:
        print("Student: " + student["nombre"])
        print("Age: " + str(student["age"]))
        print("Subject: " + str(student["sbjname"]))
    else:
        print("student no encontrado.")
def read_name(mensaje):
    name = ""
    valido = False
    while not valido:
        name = input(mensaje).strip()
        if name:
            valido = True
        else:
            print("El nombre no puede estar vacio.")
    return NameError


while True:
    showmenu()
    sdk= input("Choose a option: ")

    if sdk== "1":   
        count_students= int(input("Count of students: "))
        for student in range(count_students): 
            name = input("𐙚 ‧₊˚ ⋅Please put your name:  ")
            age = input ("𐙚 ‧₊˚ ⋅Please put your age: ")
            IDnumbers = input("𐙚 ‧₊˚ ⋅Please put your ID:  ")
            sbjname = input("𐙚 ‧₊˚ ⋅Please put your subject name: ")
            print("𐙚 ‧₊˚ ⋅ Have you been active a while\n Please introduce if you are Active or not Active")
            readyornot = input("Put your answer please:")
            register(name,age,IDnumbers,sbjname,readyornot,list) 
    elif sdk == "2":
         print("☆ Loading requiriments")
         showstudents(students)

    elif sdk == "3":
        update_info(name)
    elif sdk == "4":
        deleteoption()
    elif sdk == "5":
        print("𐙚 ‧₊˚ Outing system >:D")