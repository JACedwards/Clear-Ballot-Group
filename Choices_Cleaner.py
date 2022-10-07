import csv
import Contests_Cleaner

#Variable to hold the illegal ContestID returned from
    #cleanContests function in Contests_Cleaner module
il_id = Contests_Cleaner.cleanContests('contests.csv')


def cleanChoices(file):
    
    #Converts csv file to list of Python dictionaries
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lst_dict = list(csv_reader)

    #Removes records associated with illegal ContestID in contests.csv
    for i in range(len(lst_dict)-1):
        if lst_dict[i]['ContestID']==il_id:
            del lst_dict[i]
    if lst_dict[-1]['ContestID']==il_id:
        del lst_dict[-1]

    #Writes cleaned data to a new Choices_Output.csv file
    csv_columns = ['ChoiceID','ContestID','ChoiceName', 'ContestAndChoiceName', 'ChoiceFullName','ChoiceType']

    csv_file = "Choices_Output.csv"
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in lst_dict:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    return il_id

#git changes 2
#git diff staging test
