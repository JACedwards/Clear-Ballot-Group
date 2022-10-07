import csv

def cleanContests(file):

    #Converts csv file to list of Python dictionaries
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lst_dict = list(csv_reader)

   
    #Identifies duplicated record
    stack = []
    dup = []
    for contest in lst_dict:
        for c_name in lst_dict:
            if contest['ContestName'] == c_name['ContestName']:
                if contest['ContestName'] not in stack:
                    stack.append(contest['ContestName'])
                else:
                    dup.append(contest['ContestName'])
    dup = set(dup)
    non_dup = ''.join(dup)
    
    #Removes second copy of duplicated record
    count = 1
    for i in range(len(lst_dict)):
        if lst_dict[i]['ContestName']==non_dup:
            if count <= 1:
                count += 1
            else:
                il_id = lst_dict[i]['ContestID']
                del lst_dict[i]
        else:
            continue

    #Writes Python dictionary to new csv file

    #commented out for testing related to bird on the brain
    # csv_columns = ['ContestID','ContestName', 'ContestShortName', 'ContestFullName','VoteRule', 'ContestType']

    # csv_file = "Contests_Output.csv"
    # try:
    #     with open(csv_file, 'w', newline='') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #         writer.writeheader()
    #         for data in lst_dict:
    #             writer.writerow(data)
    # except IOError:
    #     print("I/O error")
    # return il_id

cleanContests('contests.csv')

#git test 2
