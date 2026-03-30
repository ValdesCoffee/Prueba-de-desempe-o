## 𐙚 ‧₊˚ ⋅ Register of students

૮ ˶ᵔ ᵕ ᵔ˶ ა  
#### Hiii :D. Welcome to the Readme archive that develop the next functions:
##### * Register new students.
##### * View the student list.

##### * Search for a student by criteria (e.g., ID or name).

###### * Update a student's information.

##### * Delete students.
---
### Use of the for 
##### The `for` statement iterates over sequences such as lists or tuples. Its logic is "for each element in the collection." It is safer than `while` because the number of iterations is usually known beforehand, and it automatically terminates at the end of the sequence, preventing infinite loops. It is very readable because it automatically manages data access.
### some examples
```pythonfor student in students:
        if student["name"].lower() == name.strip().lower():
            return student
    return None
```
### Uso of While
##### The `while` statement repeats a block of code as long as a condition is true. It is used when you cannot predict how many times the action will be repeated. It is crucial that the code inside modifies the evaluated variable so that the condition becomes false at some point, thus preventing an infinite loop that would block your program.

```python
  valide = False
    while not valide:
        entrada = input(mensaje).strip()
        if permitir_none and entrada == "":
            return None
        try:
            valor = int(entrada)
            if valor < 0:
                print("This value is negative")
            else:
                valide = True
        except ValueError:
            print("This number is not valid")
```
##### We use while for making loops that would serve you as a infinite posibles to register that, if you want delete something you can use te option 4 that would encarges that. 
```python
elif sdk == "4":
        deleteoption()
```
#### THis option use the function deleteoption()
```python
def deleteoption(students):
    print("Staring system")
    print("\n-- Deleting students --")
    name = read_name("name to delete ")
    if optionsearch(students, name) is None:
        print("Student not found")
        return
```

### Uses of variables
##### I use the type variable int and string, that means strings and numbers that include enters
