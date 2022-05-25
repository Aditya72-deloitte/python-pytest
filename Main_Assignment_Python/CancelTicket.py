import csv

import pandas as pd


class CancelTicket:
    pass


def cancel(Movie, Name):
    with open("movieList.csv") as movieDetail:
        read = csv.DictReader(movieDetail)

        for row in read:
            if row['Title'] == Movie:
                availableSeats = int(row['Capacity'])

    cancelSeats = int(input("Enter the number of seats to be cancelled : "))
    if availableSeats > cancelSeats:
        seatLeft = availableSeats + cancelSeats
        remainingSeats = str(seatLeft)
        df = pd.read_csv('movieList.csv')
        df.loc[df['Title'] == Movie, 'Capacity'] = seatLeft
        df.to_csv('movieList.csv', index=False)
        print(df)

        print("Booking Cancelled Successfully!!!")

    else:
        print("Invalid Cancellation!!")