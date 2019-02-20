import pyexcel as pe


def process_greek_db(filename = "hhf-greece.gr.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)

    # In the case of the greek database, we take into consideration all the fields
    # We discriminate row 0 (spanish name fields) and column 0 (spanish name of foods)
    del sheet.column[0]
    del sheet.row[0]

    # We are going to adapt name fields in order to unify with the other databases

    # Get field names
    row_names = sheet.row[0]

    # Then we modify them
    row_names[0]="Food name"
    row_names[4]="Total lipids/fats (g)"
    row_names[5]="Saturated fatty acids (SFA) (g)"
    row_names[6]="Monounsaturated fatty acids (g)"
    row_names[7]="Polyunsaturated fatty acids (g)"
    row_names[9]="Dietary Fiber/Fibre (g)"

    # Replace the values in the first row (it's the one with the field names)
    sheet.row[0] = row_names

    # Save all the changes
    sheet.save_as("processed-greek-db.xlsx")

    pass



process_greek_db()
