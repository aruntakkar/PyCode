row_data = {}

with open('PaceData.csv') as paces:

    column_headings = paces.readline().strip().split(',')

    column_headings.pop(0)

    for each_line in paces:
        row = each_line.strip().split(',')
        row_label = row.pop(0)
        # Use the row label together with the
        # rest of the line's data to update
        # the dictionary
        # row_data[row_label] = row

        inner_dict = {}
        # with each iteration "i" is the
        # current column number.
        for i in range(len(column_headings)):
            # Associate the column heading
            # with the time value in the row
            inner_dict[row[i]] = column_headings[i]
            # with the dictionary populated assign it
            # to its label in row_data
        row_data[row_label] = inner_dict

    column_heading = row_data['15k']['43:24']
    print(column_heading)

# num_cols = len(column_headings)
# print(num_cols, end=' -> ')
# print(column_headings)

# num_2mi = len(row_data['2mi'])
# print(num_2mi, end=' -> ')
# print(row_data['2mi'])

# num_Marathon = len(row_data['Marathon'])
# print(num_Marathon, end=' -> ')
# print(row_data['Marathon'])
