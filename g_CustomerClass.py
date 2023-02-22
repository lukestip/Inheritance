class Person():

    def __init__(self, name, address, phoneNum):
        self.__name = name
        self.__address = address
        self.__phoneNum = phoneNum

    def print_person(self):
        print(f'Name: {self.__name}')
        print(f'Addr: {self.__address}')
        print(f'Phone: {self.__phoneNum}')

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phoneNum


class Customer(Person):

    def __init__(self, name, address, phoneNum, custNum, mailList):
        Person.__init__(self, name, address, phoneNum)
        self.__custNum = custNum
        self.__mailList = mailList

    def print_person(self):
        Person.print_person(self)  # print_person()
        print(f'Cust Num: {self.__custNum}')
        if self.__mailList:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')

    def get_custNum(self):
        return self.__custNum

    def get_mailList(self):
        return self.__mailList
