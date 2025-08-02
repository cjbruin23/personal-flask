import csv

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
            years = row
            continue

        ## Add the country name and then the yearly gdp data
        relevant_year_data.insert(0, row[0])
        final_row.append(relevant_year_data)

        final_csv_data.append(final_row)

    print(years)
    print(final_csv_data)