import csv
import Contests_Cleaner

#Variable to hold the illegal ContestID returned from
    #cleanContests function in Contests_Cleaner module
il_id = Contests_Cleaner.cleanContests('contests.csv')

def cleanBallotMapper(file):

    #Converts csv file to list of Python dictionaries
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lst_dict = list(csv_reader)

    #Changes illegal contest Id's to legal equivalent
    for i in range(len(lst_dict)-1):
        if lst_dict[i]['ContestID']==il_id:
            lst_dict[i]['ContestID'] = '8'

    #Changes illegal choice Id's to legal equivalent
    for i in range(len(lst_dict)-1):
        if lst_dict[i]['ChoiceID']=='20':
            lst_dict[i]['ChoiceID'] = '15'
        elif lst_dict[i]['ChoiceID']=='21':
            lst_dict[i]['ChoiceID'] = '16'
        elif lst_dict[i]['ChoiceID']=='22':
            lst_dict[i]['ChoiceID'] = '17'

    #Writes dictionary back to csv file
    csv_columns = ['BallotStyleID','Side','vx', 'vy', 'ContestID','ChoiceID']
    csv_file = "BallotMapper_Output.csv"
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in lst_dict:
                writer.writerow(data)
    except IOError:
        print("I/O error")

