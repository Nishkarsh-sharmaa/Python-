import CSV
def write_info_csv(info_list):
    with open('student_info.csv','a+', newline=' ') as csv_file:
         writer = CSV.writer(csv_file)
         if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact No.","E-Mail"])
         writer.writerow(info_list)
if __name__ =='__main__':
     condition = True
     #student_num = 1
     while (condition):
           student_info = input ("Enter student info in foll format for student(Name Age Contact Email id):")
           # #{}.format(student_num)

           student_info_list= student_info.split(' ')
           print ("Split up formation" +str(student_info_list))  
           print ("Entered into is-\nName: {}\nAge: {}\nContact_No: {}\nEmail Id {}"
           choice_check = input("Is the entered into correct(y/n):")
           if choice_check =='y':
              write_info_csv(student_info_list)



              condition_check = input("Enter(y/n) if you want to enter information for another student")
              if condition_check =="y":
                 condition = True
              #student_num = student_num + 1
 
            elif condition_check == "n"
                 condition = False
        elif choice_check == "n":
             print("\n Please re-enter the values")
