
# Enter minefield: A minefield design can be entered. Mines are represebted as "#". Safe space are "-" Its size is calculated for use in later functions.

minefield = [ ["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "#", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"] ]

num_of_rows = len(minefield)
num_of_columns = len(minefield[0])

# Define Functions

# Function to "Count nearby mines": 
# This code checks for "#" in row/column locations next to the "current location" which is input as x and y coordinates. 
# It checks the cells in all relative compass directions. NW,N,NE,E,W,SW,S,SE and returns the count of nearby mines.
# The count is only carried out if the "current location" is itself not a mine.

def check_for_mines(x,y):
    current_location_row = x
    current_location_col = y

# Check if current location is a mine: If it is a mine, no nearby mines are counted, and "#" is returned. 
    if(minefield[current_location_row][current_location_col]) == "#":
        return("#")

    else:

        relative_coordinates_to_check = [
        ["NW",-1,-1],
        ["N",-1,0],
        ["NE",-1,1],
        ["W",0,-1],
        ["E",0,1],
        ["SW",1,-1],
        ["S",1,0],
        ["SE",1,1],
        ]

        count_of_mines_nearby = 0

        for coordinate_pair in relative_coordinates_to_check:

            check_row = current_location_row + coordinate_pair[1]
            check_col = current_location_col + coordinate_pair[2]

            if check_row >=0 and check_row <=(num_of_rows-1) and check_col>=0 and check_col<=(num_of_columns-1) and minefield[check_row][check_col] == "#": 
                count_of_mines_nearby +=1

    return(str(count_of_mines_nearby))

# Programme

# Check if minefield rows all have same number of columns. Return error if not.
row_lengths = []
for row in minefield:
    row_lengths.append(len(row))
if sum(row_lengths)/len(row_lengths)!=len(minefield[0]):
    print("Error: Rows are not the same length")

else:
# Loop though each "cell" and check for nearby mines using check_for_mines function
    for row_index,row in enumerate(minefield):
        new_row=[]
        for col_index,col in enumerate(row):
            new_row.append(check_for_mines(row_index,col_index))
        print(new_row)
