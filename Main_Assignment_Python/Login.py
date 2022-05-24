
from AdminLogin import AdminLogin
from UserLogin import UserLogin


class Login(AdminLogin, UserLogin):
    def __init__(self):
        # ******Welcome to BookMyShow *******
        # User: Admin
        # Password: ** ** ** ** **
        print("******Welcome to BookMyShow*******")
        print("1. Admin login")
        print("2. User login")
        print("3. Previous option")

        self.input_choice = int(input("Enter your choice"))

    def choiceAgain(self, input_choice):
        if input_choice == 3:
            return
        elif input_choice == 1:
            # admin_login
            AdminLogin.__init__(self)
            var = AdminLogin.verifyCredentials(self, self.adminname, self.adminpass)
            if var == 1:
                AdminLogin.insideAdminLogin(self)

        elif input_choice == 2:
            # user_login()
            UserLogin.__init__(self)
            var = UserLogin.verifyCredentials(self, self.username, self.userpass)
            if var == 1:
                UserLogin.insideUserLogin(self)

        else:
            print("Enter the valid choice")
