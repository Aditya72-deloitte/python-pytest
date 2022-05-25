import csv

import BookingTickets
import CancelTicket
import FeedBack
import Login


def user_Login(name):
    try:
        DataFile = open("movieList.csv", "r+")
        readFile = csv.reader(DataFile)
        value = len(list(readFile))
        if value > 1:
            with open("movieList.csv") as userDetails:
                read = csv.DictReader(userDetails)
                i = 0
                for row in read:
                    i = i + 1
                    print(i, ". Details of ", row['Title'], ".")

            i = i + 1
            print("1. Enter movie name")
            print("2. Logout")

            choiceMovie = input("Enter choice : ")
            if choiceMovie == 2:
                print("Logged out successfully")
                LoginObj = Login
                LoginObj.LoginPage()

            else:
                with open("movieList.csv") as movieList:
                    read = csv.DictReader(movieList)
                    for row in read:
                        if row['Title'] == choiceMovie:
                            print("Title : ", row['Title'])
                            print("Genre : ", row['Genre'])
                            print("Length : ", row['Length'])
                            print("Cast : ", row['Cast'])
                            print("Director : ", row['Director'])
                            print("Admin Rating : ", row['Admin Rating'])
                            print("Timings : ", row['Timings'])
                            break

                while True:

                    print("1. Book Ticket")
                    print("2. Cancel Ticket")
                    print("3. Give User Feedback")
                    print("4. Logout")

                    ch = int(input("Enter Option : "))
                    if ch == 1:
                        bookObject = BookingTickets
                        bookObject.book(name)

                    elif ch == 2:
                        cancelObj = CancelTicket
                        cancelObj.cancel(choiceMovie, name)

                    elif ch == 3:
                        feedbackObj = FeedBack
                        feedbackObj.rating(choiceMovie, name)

                    elif ch == 4:
                        print("Logged Out Successfully!!")
                        loginObj = Login
                        loginObj.LoginPage()
                        break

                    else:
                        print("Invalid Choice!!!")
                        break
    except:
        print("No movies found.")
