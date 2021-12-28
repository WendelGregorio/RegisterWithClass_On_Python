#coding: utf-8
#
#Program: Register 

"""Register"""

class Person(object):
    """Class Person: Resposible for storing a person's data """
    
    __name = ""
    __age = -1
    __sex = ""
    
    def __init__(self):
        """ constructor Python """
        
    def register(self):
        """ register method: allows to recive a data from a person """
        self.__name = input("Type your name: ")
        while self.__age < 0:
            try:
                self.__age= int(input("Type your age: "))
            except ValueError:
                print("Type an integer number!")
        self.__sex = input("Sex: M to masculine and F to feminine: ")
        self.__sex = self.__sex.upper()
        if self.__sex != 'F':
            self.__sex = 'M'
    def show(self):
        """ method show: show all registered data from person """
        if self.__sex == 'F' and self.__age > 30:
            print(self.__name + ' secret age ' + self.__sex)
        else:
            print(self.__name + ' ' + str(self.__age) + ' ' + self.__sex)
            
PEOPLE = list()
for i in range(0,3):
    OBJ = Person()
    OBJ.register()
    PEOPLE.append(OBJ)
    
for PERSON in PEOPLE:
    PERSON.show()
    
    #Changing Atributes and methods of the class
    print ('Line 46 ' + str(PEOPLE))
    print ('Line 47 ' + str(PEOPLE[0]))
    print ('Line 48 ' + str(PEOPLE[0].__dict__))
    print ('Line 49 ' + str(PEOPLE[0].__dict__.keys()))
    print ('Line 50 ' + str(PEOPLE[0].__dict__.values))
    PEOPLE[0]._Person__age = 'BlaBlaBla'
    print ('Line 51 ' + str(PEOPLE[0]._Person__age))
    PEOPLE[0]._Person__Nickname = 'CoolPerson'
    print ('Line 52 ' + str(PEOPLE[0].__dict__))
