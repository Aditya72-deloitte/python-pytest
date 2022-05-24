from Login import Login
from RegisterNewUser import RegisterNewUser


class HomePage(RegisterNewUser, Login):
    def __init__(self):
        print('******Welcome to BookMyShow*******')
        print('1. Login')
        print('2. Register new user')
        print('3. Exit')

        self.choice = int(input("Enter your option: "))

    def numbers_To_Strings(self, choice):
        if choice == 1:
            Login.__init__(self)
            Login.choiceAgain(self, self.input_choice)

        elif choice == 2:
            RegisterNewUser.__init__(self)
            RegisterNewUser.appendingInFile(self, self.credentials)

        else:
            print(choice)
            print("Enter valid Choice")


while True:
    obj = HomePage()
    if obj.choice == 3:
        exit()
    else:
        obj.numbers_To_Strings(obj.choice)
