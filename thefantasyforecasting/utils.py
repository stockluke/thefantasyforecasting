import csv
import os
from thefantasyforecasting import db
from thefantasyforecasting.models import Location


def update_icao_list():
    print(os.getcwd())

    with open('thefantasyforecasting/static/icao_list.csv', 'r') as file:
        reader = csv.reader(file)
        db.session.query(Location).delete()
        for row in reader:
            state = row[0]
            city = row[1]
            icao = row[2]
            country = 'USA'
            location = Location(state=state, icao=icao, city=city, country=country)
            db.session.add(location)
        db.session.commit()
    print('ICAO list updated')

    return
