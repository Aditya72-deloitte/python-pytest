from _csv import reader

from AddMovies import AddMovies


class AdminLogin(AddMovies):
    def __init__(self):
        print("******Welcome to BookMyShow*******")
        print("Enter your credentials")
        self.adminname = str(input("Enter your User name:  "))
        self.adminpass = str(input("Enter your Password:  "))

    def verifyCredentials(self, adminname, adminpass):
        with open('adminCredentials.csv', 'r') as read_obj:
            i = 0
            flag = 0
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header is not None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    i = i + 1
                    # row variable is a list that represents a row in csv
                    if row[0] == adminname and row[1] == adminpass:
                        return 1
                    else:
                        flag = flag + 1
        if flag == i:
            print("Wrong Credentials")

    def insideAdminLogin(self):
        while True:
            print("******Welcome Admin*******")
            print("1. Add new Movie Info")
            print("2. Edit Movie Info")
            print("3. Delete Movie")
            print("4. Logout")
            choice = int(input("Enter your choice"))
            if choice == 4:
                return 0
            elif choice == 1:
                # addMovie()
                AddMovies.__init__(self)
                AddMovies.appendingMoviesfile(self, self.lst)
            elif choice == 2:
                # editMovie()
                print("Inside Edit movies")
            elif choice == 3:
                # deleteMovie()
                print("Inside delete Movies")
            else:
                print("Enter Valid Choice")
