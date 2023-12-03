################################################################
# Project: Reading and Writing files using lists
# File: main.py
# Description: Use a small array to demonstrate writing records for a file
#              from parallel arrays, then reading them back into the list
#
# Note:        The two functions, writeToFile and readFromFile, should
#              be passed generic list names. This wasn't done, because it
#              would be too complex for a beginning class.
# Author: minassie ghebremicael
# Version: 1.0
# Date: March 12, 2023
 ################################################################
def main():
    ################################################################
    # Function: main()
    # Description: Process an array...
    # Parameters: null
    # Returns: null
    # Author: minassie ghebremicael
    ################################################################
    # BUILD ARRAY, TRAVERSE AND PRINT CONTENTS
    student_names = [""] * 20
    interests = [""] * 20
    height = [0] * 20
    native_country = [""] * 20
    distance_from_home = [0] * 20
    country_known_for = [""] * 20

    readFromFile(student_names,interests,height,native_country,
                 distance_from_home,country_known_for)
    # traverse the list names and country_known_for
    # and print each element
    print("Student Name            Country Known for\n")
    count_students = 0
    for i in range(0, len(student_names)):
        count_students = count_students + 1
        print(f"{count_students}){student_names[i]:18}\t{country_known_for[i]}")
    # print a blank line
    print("")
    # traverse the list native_country
    # print Vietnam occurrences
    vietnam_occurrences = 0
    for i in range(0, len(native_country)):
        if native_country[i] == "Vietnam":
            vietnam_occurrences = vietnam_occurrences + 1
    print(f"*** Vietnam has {vietnam_occurrences} occurrences on file")
    # traverse the list native_country
    # print USA occurrences
    usa_occurrences = 0
    for i in range(0, len(native_country)):
        if native_country[i] == "USA":
            usa_occurrences = usa_occurrences + 1
    print(f"*** USA has {usa_occurrences} occurrences on file")
    # traverse the list distance_from_home
    # print the largest distance 
    largest_distance = distance_from_home[0]
    for i in range(1, len(distance_from_home)):
        if distance_from_home[i] > largest_distance:
            largest_distance = distance_from_home[i]
            name_lrgst_distance = student_names[i]
    print(f"*** {name_lrgst_distance} has the largest"
          f" distance from home: {largest_distance:.2f} miles")
    #################################################
    # write records of 3 lists back to file
    # I made it 3 for the purpose of practise
    #################################################
    writeToFile(student_names, interests, height)


def writeToFile(list1,list2,list3):
    ################################################################
    # Function: writeToFile
    # Description: write records from parallel lists to a file
    # Parameters: three parallel lists
    # Returns: null
    # Author: minassie ghebremicael
    ################################################################
    student_file = open('NewStudents.txt', 'w')
    # put number of records at top of file
    str_len = str(len(list1))
    student_file.write(str_len + '\n')
    # write records from list to the file
    for i in range(0, len(list1)):
        student_file.write(list1[i] + '\n')
        student_file.write(str(list2[i]) + '\n')
        student_file.write(str(list3[i]) + '\n')
    # close the file
    student_file.close()
def readFromFile(list1,list2,list3,list4,list5,list6):
    ################################################################
    # Function: readFromFile
    # Description: read records from a file and write to parallel lists
    # Parameters: six parallel lists
    # Returns: null
    # Author: minassie ghebremicael
    ################################################################
    # open file for  input
    student_file = open('StudentsNight.txt', 'r')
    # read first record - containing number of records
    # int and float ignore \n - so no exception is thrown
    num_recs = int(student_file.readline())  # convert to int
    # initialize the lists
    for i in range(0,num_recs):
        list1[i] = ""
        list2[i] = ""
        list3[i] = 0
        list4[i] = ""
        list5[i] = 0
        list6[i] = ""
    # read records back into the list
    for i in range(0, num_recs):
        list1[i] = student_file.readline()
        list1[i] = list1[i].rstrip('\n')
        list2[i] = student_file.readline()
        list2[i] = list2[i].rstrip('\n')
        list3[i] = float(student_file.readline())
        list4[i] = student_file.readline()
        list4[i] = list4[i].rstrip('\n')
        list5[i] = float(student_file.readline())
        list6[i] = student_file.readline()
        list6[i] = list6[i].rstrip('\n')

    # close the file
    student_file.close()
main()