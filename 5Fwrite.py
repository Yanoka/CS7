# enter all names and split by whitespace
names  = input("Please, enter the names: ")
namesList = names.split()

# enter all scores and split by whitespace
scores  = input("Please, enter the scores: ")
scoresList = scores.split()

# open file and record the information
fileNamesScores = open('5Fgolf.txt','w')

# get the list length 
number = len (namesList)

# record the data
for i in range(number):
    fileNamesScores.write(namesList[i]+'\t')
    fileNamesScores.write(scoresList[i]+'\n')

# close the file
fileNamesScores.close()
