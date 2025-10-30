def add_student():
    with open("student.txt", "a") as f:
        name = input("Enter name:")
        roll = input("Eneter roll number: ")
        marks = input("Enter marks: ")
        f.write(f"{name},{roll},{marks}\n")
        print("Student added successfully")
        
def view_students():
    with open("student.txt", "r") as f:
        print("\nname\troll\tmarks")
        print("_" * 25)
        for line in f:
            data = line.strip().split(",")
            print("\t.join(data)")
            print()
            
def search_student():
    roll = input("enter roll number to search: ")
    with open("student.txt", "r") as f:
        found = False
        for line in f:
            name, r, marks = line.strip().split(",")
            if r == roll:
                print(f"found{name} - {marks}")
                found = True
                if not found:
                    print("student not found")
                    
while True:
    print("\n1. add student\n2. view all\n. search\n4. exit")
    ch = input("enter choice: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        search_student()
    elif ch == '4':
        break
    else:
        print("invalid choice")

        
    
    
    
    
