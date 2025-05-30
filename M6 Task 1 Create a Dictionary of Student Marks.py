stud_mark = {"Ram": 27,"Laxman": 84,"Bheem": 47,"Khuldeep": 71}
stud_name = input("Enter a student's name: ")
if stud_name in stud_mark:
    mark = stud_mark[stud_name]
    print(stud_name+"'s marks:",mark)
else:
    print("Student not found.")