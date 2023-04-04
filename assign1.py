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

Colors = ['blue', 'hisense', 'white', 'champagne', 'orange']
Fruits = ['cherry', 'tangerine','orange', 'apple', 'hisense']
Phone = ['hisense', 'infinix','orange','samsung', 'tecno']
Drinks = ['vodka', 'orange','champagne', 'hisense', 'liquor']
Laptop = ['samsung', 'apple','hisense', 'orange', 'hp']
Makeup = ['mascara','orange','eyeliner', 'hisense','blush']
Coffee = ['black', 'nescafe','orange', 'tetley','hisense']
Software = ['python', 'orange', 'html', 'hisense', 'javascript']
Tablet = ['hisense', 'android', 'xiaomi', 'orange', 'infinix']
Conditioner = ['thermocool', 'orange', 'scanfrost', 'hisense']
               


common_elements = set(Colors).intersection(Fruits,Phone,Drinks,Laptop,Makeup,Coffee,Softwara,Tablets,Conditioner)

def cohort_four():
    if common_elements:
        print('True!', 'The common elements are', common_elements)
    else:
        print('False!', 'There are no common elements')
    
cohort_four()
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
