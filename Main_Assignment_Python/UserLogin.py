from _csv import reader


class UserLogin:
    def __init__(self):
        print("******Welcome to BookMyShow*******")
        print("Enter your credentials")
        self.username = str(input("Enter your User name:  "))
        self.userpass = str(input("Enter your Password:  "))

    def verifyCredentials(self, username, userpass):
        i = 0
        flag = 0
        with open('User.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            header = next(csv_reader)
            # Check file as empty
            if header is not None:
                # Iterate over each row after the header in the csv
                for row in csv_reader:
                    i = i + 1
                    # row variable is a list that represents a row in csv
                    if row[0] == username and row[4] == userpass:
                        return 1
                    else:
                        flag = flag + 1
        if flag == i:
            print("Wrong Credentials")
