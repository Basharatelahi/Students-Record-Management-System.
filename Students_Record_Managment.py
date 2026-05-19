print("------welcome to the Students Record Managment system------!")
print()

info_store = {}

def add_student_information(info_store): 
    while True:
        while True:
            student_name = input(f"enter student name: ").strip()
            if student_name == "":
                print("student name cannot be empty. please enter a valid name.")
            elif any(char.isdigit() for char in student_name):
                print("student name cannot contain numbers. please enter a valid name.")
            else:
                break

        while True:
            try:
                sub = int(input("enter total subjects: "))
                break
            except ValueError:
                print("invalid input. please enter a valid number.")
                print()    
    
        paper_with_marks = {}
            
        for i in range(sub):
            while True:
                subject_name = input(f"enter name of subject {i+1}: ")
                if subject_name == "": 
                    print("subject name cannot be empty. please enter a valid name.")
                elif any(char.isdigit() for char in subject_name):
                    print("subject name cannot contain numbers. please enter a valid name.")
                else:
                    break

            while True:
                try:
                    marks = int(input(f"enter marks for subject {i+1}: "))
                    if 0 <= marks <= 100:
                        break
                    else:
                        print("marks should be between 0 and 100. please enter a valid numbers.")
                except ValueError:
                    print("invalid input. please enter a valid number.")
                    continue

            paper_with_marks[subject_name] = marks

            info_store[student_name] = paper_with_marks

        print(f"marks of '{student_name}' added successfully.")
        print()
        
        choice = input("do you want to add more students? (yes/no): ")
        if choice.lower() != "yes":
            break
        print()

    return info_store

def students_record(info_store):
    print("------All students & Paper records------")
    print("-" * 40)

    for name,record in info_store.items():
        print(f"Student Name: {name.upper()}")
        print("-" * 30)
        for paper_name,marks in record.items():
            clear_paper_name = paper_name.replace("_"," ")
            print(f"{clear_paper_name} : {marks}")
        print("-" * 20) 

    print("=" * 40)     


percentage_record = {}
def find_percentage(info_store):
    for std_name,std_marks in info_store.items():
        total_marks = sum(std_marks.values())
        percentage = (total_marks * 100) / (len(std_marks) * 100)
        percentage_record[std_name] = round(percentage, 2)
    
    print("------Students name with Percentage------")

    print("-" * 40)
    for name,pct in percentage_record.items():
        print(f"Name: {name} | Percentage:{pct}%.")
    print("=" * 40)    

    return percentage_record  


def high_to_low_performance(percentage_record):
    sorted_record_tuples = sorted(percentage_record.items(),key=lambda x: x[1],reverse = True)
    
    final_sorted_record = {}
    for name,percentage in sorted_record_tuples:
        final_sorted_record[name] = percentage
    
    print("------From Top performer students to low in Class------")

    print("-" * 20)
    for std_name,pct in final_sorted_record.items():
        print(f"{std_name}: {pct}%")
    print("=" * 20)    

    return final_sorted_record  
    

while True:
    print("choose one option in below...")
    print("1.Adding students marks. \n2.Show all students records. \n3.Show percentage of each students.\
      \n4.Show student records from high to low performance in class. \n5.exit")
    
    try:
        option = int(input("enter your option: "))
    except ValueError:
        print("invalid input. please enter a valid number.")
        print()
        continue

    if option == 1:
        print()
        add_student_information(info_store)
        print()    

    elif option == 2:
        print()
        if info_store == {}:
            print("No students records found. please first select option (1) to add students information.")
        else:
            students_record(info_store)
        print()    

    elif option == 3:
        print()
        if info_store == {}:
            print("No students records found. please first select option (1) to add students information.")
        else:
            find_percentage(info_store)  
        print()

    elif option == 4:
        print()
        if info_store == {}:
            print("No students records found. please first select option (1) to add students information.")
        elif percentage_record == {}:
            print("plz First select option 3 For find percentage.high to low performance are find through percentage")
        else:
            high_to_low_performance(percentage_record)
        print()

    elif option == 5:
        print("thanks for using the Studends Record managment system. goodbye!")
        break   
    else:
        print("invalid option") 
        print()   
