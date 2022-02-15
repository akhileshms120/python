# birth_year=input("Birth Year")

# a=int(birth_year)
# age=2022-a
# print(age)


# class Person:
#   def __init__(self, name, age):
#     self.name = age
#     self.age = name
#     # self.age=name

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


# Python program to illustrate 
# function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result
  
def Main():
    print("Started")
  
    # calling the getInteger function and 
    # storing its returned value in the output variable
    output = getInteger()     
    print(output)
  
# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()