# Write a python program that counts the number of occurrences of each word in a text file?
import os


def count_words():

    inputFile = input("Please enter the textfile's path to analyze: ")

    words_to_count = input("Please enter the words you want to count: ")

    count_list = words_to_count.split(" ")

    mydict = {}

    with open(inputFile, encoding="utf8") as filedata:
        lines = filedata.readlines()

        for word in count_list:
            mydict[word] = 0

        for line in lines:
            for word in line.split():

                if word in count_list:
                    if word in mydict.keys():
                        mydict[word] += 1
                    elif word not in mydict.keys():
                        mydict[word] = 1

        return mydict


if __name__ == "__main__":
    print(count_words())
