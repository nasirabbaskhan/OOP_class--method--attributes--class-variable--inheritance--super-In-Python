class Teacher(): # class Name
    counter :int= 10 #clss_varible 1
    help_line:str ="0303-6702180" #clss_varible 2
    def __init__(self,teacher_name:str,teacher_id:int) -> None: # constructor
        self.id= teacher_id # attributes
        self.name= teacher_name
        
obj1= Teacher("nasir",1)
obj2= Teacher("Qasim",2)
obj3= Teacher("aneela",3)

print("Here obj1 data:")
print(obj1.id)
print(obj1.name)
print(obj1.counter) # class variable
print(obj1.help_line) # class variablev
print("\nHere obj2 data:")
print(obj2.id)
print(obj2.name)
print(obj2.counter) # class variable
print(obj2.help_line) # class variable
print("\nHere obj3 data:")
print(obj3.id)
print(obj3.name)
print(obj3.counter) # class variable
print(obj3.help_line) # class variable

# here class varible are same for all objects