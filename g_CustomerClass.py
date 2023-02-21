class Person():

    def __init__(self, name, address, phoneNum):
        self.__name = name
        self.__address = address
        self.__phoneNum = phoneNum

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phoneNum)


class Customer(Person):

    def __init__(self, name, address, phoneNum, custNum, mailList):
        Person.__init__(self, name, address, phoneNum)
        self.__custNum = custNum
        self.__mailList = mailList

    def print_person(self):
        Person.print_person(self)
        print(self.__custNum)
        print(self.__mailList)
