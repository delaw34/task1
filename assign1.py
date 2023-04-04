#Write a function that return bool type
# functions that return bool type

x = 50
y = 79
print(x==y)
print(x>y)
print(x<y)
print(x!=y)

#assigment 1 ends here

#assigment 2 starts here

#Write a Python function that takes 10 lists and returns True if they have
#at least one common member

colors = ["red", "white", "champagne", "cherry", "orange"]
fruits = ["orange", "cherry", "mango", "apple", "banana"]
phones = ["apple", "samsung", "vivo", "tecno", "orange"]
wine = ["vodka", "champagne","spirit", "amarula", "orange"]

coment_element = set(colors).intersection(fruits,wine,phones) 

def cohort_4():
    if coment_element:
        print("TRUE!, the common elements are:", coment_element)
    else:
        print("FALSE!", "there are no common element")
cohort_4()

#assigment 2 starts ends here

#assigment 3 starts here

# Application that can check the age of a person
# Input name and age in the application
# 18 years below access will be denied

current_year = 2023 #int



def age_cal():
    name_of_student = (input("Enter Name:   "))
    age_calculation = int(input("Enter year of birth:   "))
    if  age_calculation <= 2005 :
        final_year  = current_year - age_calculation
        
        print("hello", name_of_student , "your age is", final_year ,"years and qualified")
    else:
        final_year  = current_year - age_calculation
        print('hello', name_of_student, 'your age is', final_year, "years, you are not qualified yet" )
  

age_cal()
