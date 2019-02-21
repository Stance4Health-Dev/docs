import pyexcel as pe

fields_correspondences = {}

# values = ["food-name", "energy-kcal", "total-lipids-fats", "protein" ,"cholesterol",
# "carbohydrates", "starch"  , "sugars", "glucose", "galactose", "fructose", "maltose",
# "lactose", "retinol-equivalent", "retinol"   , "beta-carotene-equivalent", "vitamin-B1",
# "thiamin", "vitamin-B2", "riboflavin", "vitamin-C", "niacin", "vitamin-D", "vitamin-E",
#  "alpha-tocopherol", "vitamin-B12", "dietary-fibre-fiber", "water", "iron"  , "calcium",
#   "sodium", "potassium", "phosphorus"  , "zinc"  , "magnesium", "manganese", "copper"  ,
#    "saturated-fatty-acids","monounsaturated-fatty-acids","polyunsaturated-fatty-acids"]


def process_greek_db(filename = "hhf-greece.gr.xlsx"):

    ## Read the sheet
    sheet = pe.get_sheet(file_name=filename)

    correspondences_values = ["food-name","energy-kcal", "protein", "total-lipids-fats",
    "saturated-fatty-acids", "monounsaturated-fatty-acids", "polyunsaturated-fatty-acids",
    "carbohydrates", "dietary-fibre-fiber", "water", "sodium",  "potassium", "calcium",
     "magnesium", "phosphorus", "iron", "zinc","copper"]
    # create dictionary

    # In the case of the greek database, we take into consideration all the fields
    # We discriminate row 0 (spanish name fields) and column 0 (spanish name of foods)
    del sheet.column[0]
    del sheet.row[0]

    # We are going to adapt name fields in order to unify with the other databases

    # Get field names
    row_names = sheet.row[0]
    # # Then we modify them
    row_names[0]="Food name" # we modify it because it is ' '


    for i,name in enumerate(row_names):
        fields_correspondences[name] = correspondences_values[i]


    pass

def get_correspondences():

    process_greek_db()
    # call the other databases to complete correspondences.....
    return fields_correspondences
