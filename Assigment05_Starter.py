# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JRushing-Crocker,11.14.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFileName = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here DONE
objFile=open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
print(objFile)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here DONE
        objFile = open(objFileName,'r')
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here DONE
        objFile = open('ToDoList.txt',"a")
        dicRow = {'task': 'Task', 'priority': 'Priority'}
        objFile.write(dicRow['task'] + "," + (dicRow['priority']) + "\n")
        lstTable = [dicRow]
        print(lstTable) # prints Table in long list
        strTask = input('input task:')
        strPriority = input("input priority:")
        dicRow = {'task':strTask, 'priority':strPriority}
        lstTable.append(dicRow)
        for objRow in lstTable:# prints list in neater stacked table1
            print(objRow)
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here DONE
        strKeyToRemove = input("Which  line do you want to delete? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here DONE
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"] + ",")
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()

         #Step 7 - Exit programcontinue

    elif (strChoice.strip() == '5'):

        # TODO: Add Code Here DONE
        quit()
        break  # and Exit the program
