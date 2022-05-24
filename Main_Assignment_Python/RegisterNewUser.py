class RegisterNewUser:
    def __init__(self):
        print("******Create New Account******:  ")
        name = str(input("Enter your name:  "))
        email = str(input("Enter your email:  "))
        phone = str(input("Enter your Phone number:  "))
        age = str(input("Enter your Age:  "))
        password = str(input("Enter your password:  "))

        self.credentials = str(name + ',' + email + ',' + phone + ',' + age + ',' + password)

    def appendingInFile(self, credentials):
        with open('User.csv', 'a') as f_object:
            # and get a writer object
            f_object.write(credentials)
            f_object.write("\n")
