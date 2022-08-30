import Contests_Cleaner
import Choices_Cleaner
import BallotMapper_Cleaner

#Removes duplicate from contests.csv
#Writes cleaned data to new Contests_Output.csv file
Contests_Cleaner.cleanContests('contests.csv')

#Removes from choices.csv records that include illegal duplicate in contests.csv
#Writes cleaned data to new Choices_Output.csv file
Choices_Cleaner.cleanChoices('choices.csv')

#Corrects contestIDs and choiceIDs
#Writes cleaned data to new BallotMapper_Output.csv file
BallotMapper_Cleaner.cleanBallotMapper('ballotmapper.csv')
