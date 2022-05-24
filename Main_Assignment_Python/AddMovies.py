from _csv import writer


class AddMovies:

    def __init__(self):
        print("******Welcome Admin*******")
        # creating an empty list
        self.lst = []

        # number of elements as input
        title = str(input("Enter title:  "))
        self.lst.append(title)  # adding the element
        genre = str(input("Enter genre:  "))
        self.lst.append(genre)
        moviename = str(input("Enter length of Movie:  "))
        self.lst.append(moviename)
        castname = str(input("Enter cast Name:  "))
        self.lst.append(castname)
        directorname = str(input("Enter Director Name:  "))
        self.lst.append(directorname)
        ratings = str(input("Enter Admin Rating:  "))
        self.lst.append(ratings)
        language = str(input("Enter a movie Language:  "))
        self.lst.append(language)
        timing = str(input("Enter movie Timing:  "))
        self.lst.append(timing)
        firstshowtime = str(input("Enter First show:  "))
        self.lst.append(firstshowtime)
        intervaltime = str(input("Enter interval time:  "))
        self.lst.append(intervaltime)
        gapbetweenshows = str(input("Enter gap between shows:  "))
        self.lst.append(gapbetweenshows)
        numberofseats = str(input("Enter the capacity:  "))
        self.lst.append(numberofseats)

    def appendingMoviesfile(self, lst):
        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open('MovieList.csv', 'a', newline='') as f_object:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            writer_object.writerow(lst)
            print("Movie Added")

            # Close the file object
            f_object.close()
