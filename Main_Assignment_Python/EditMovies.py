import pandas as pd


class EditMovies:
    def __init__(self):
        self.moviename = input("Enter movie name which has to be updated : ")

    def editingCredentials(self, moviename):
        while True:
            print("1. title")
            print("2. genres")
            print("3. length")
            print("4. cast")
            print("5. derector")
            print("6. rating")
            print("7. Language")
            print("8. Timing")
            print("9. number of shows")
            print("10. first show")
            print("11. interval time")
            print("12. gap between show")
            print("13. capacity")
            print("14. Don't wanna update")

            choice = int(input("Enter the updation choice : "))

            if choice == 1:
                newmoviename = input("Enter new movie name : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Title'] = newmoviename
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 2:
                newGenre = input("Enter New Genre : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Genre'] = newGenre
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 3:
                newLength = input("Enter New Length : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Length'] = newLength
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 4:
                newCast = input("Enter New Cast : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Cast'] = newCast
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 5:
                newDir = input("Enter New Director : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Director'] = newDir
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 6:
                newAdminRating = input("Enter New Rating : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Admin Rating'] = newAdminRating
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 7:
                newLanguage = input("Enter New Language : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Language'] = newLanguage
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 8:
                newTiming = input("Enter New Timing : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Timings'] = newTiming
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 9:
                newNum = input("Enter Number of Shows : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Number of Shows in a day'] = newNum
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 10:
                newFirstShow = input("Enter New time of the First Show : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'First Show'] = newFirstShow
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 11:
                newIntervalTime = input("Enter New Interval Time : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Interval Timing'] = newIntervalTime
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 12:
                newGap = input("Enter New Gap time : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Gap Between Shows'] = newGap
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 13:
                newCapacity = input("Enter New Capacity : ")
                df = pd.read_csv('movieList.csv')
                df.loc[df['Title'] == moviename, 'Capacity'] = newCapacity
                df.to_csv('movieList.csv', index=False)
                print(df)

            elif choice == 14:
                break

            else:
                print("Enter a valid Choice!")
                break

            print("Updated Successfully!!")
