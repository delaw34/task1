
# Application that can check the age of a person
# user enter name 
# user enter year of birth age 
# application will calculate how old user is 
# 18 years below access will be denied
# 18 years above access will be approved

current_year = 2023 #int



def age_cal():
    name_of_student = (input("Enter Name:   "))
    age_calculation = int(input("Enter year of birth:   "))
    if  age_calculation <= 2005 :
        final_year  = current_year - age_calculation
        
        print("Hello", name_of_student , "your age is", final_year ,"years and qualified")
    else:
        final_year  = current_year - age_calculation
        print('Hello', name_of_student, 'your age is', final_year, "years, you are not qualified yet" )
  

age_cal()
