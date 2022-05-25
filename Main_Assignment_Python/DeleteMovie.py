import csv

import pandas as pd


class DeleteMovie:
    def __init__(self):
        self.delMovie = input("Enter the movie to delete : ")

        try:
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] != self.delMovie:
                        continue

                    else:
                        df = pd.read_csv('MovieDetails.csv')
                        df.drop(df[df['Title'] == self.delMovie].index, inplace=True)
                        df.to_csv('MovieDetails.csv', index=False)
                        print("Movie is Deleted Successfully!!")
                        break
        except:
            print("No Such Movie present in the Database with name : ", self.delMovie)
