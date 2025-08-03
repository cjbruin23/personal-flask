import csv
import datetime
import os
import psycopg2

from dotenv import load_dotenv

with open('../assets/country_gdp.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    years = []
    final_csv_data = []

    for row in csv_reader:
        final_row = []

        ## We do not need the first several rows
        if len(row) < 4:
            continue

        relevant_year_data = row[44:69]

        ## Add years to their own row
        if relevant_year_data[0] == '2000':
            years = relevant_year_data
            print(years)
            continue

        ## Add the country name followed by the yearly gdp data
        relevant_year_data.insert(0, row[0])

        final_csv_data.append(relevant_year_data)

    print(final_csv_data[1])

    load_dotenv()
    SECRET_KEY = os.environ.get("CONNECTION_STRING")
    conn = psycopg2.connect(SECRET_KEY)

    country = final_csv_data[1][0]

    for i, item in enumerate(final_csv_data[1][1:]):
        gdp_date = datetime.date(int(years[i], 10), 1, 1)
        print(gdp_date)
        gdp = round(float(item), 3)
        print(gdp)
        curr = conn.cursor()
        curr.execute("""
            INSERT INTO country_gdp(name, ts, gdp)
            VALUES (%s, %s, %s);
            """,
            (country, gdp_date, gdp)
        )
        conn.commit()
        curr.close()

    conn.close()