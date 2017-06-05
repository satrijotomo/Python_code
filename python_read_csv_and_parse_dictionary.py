# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "rb") as f:
        header = f.readline().split(',')
        count = 0
        for line in f:
            if count == 10:
                break
            
            fields = line.split(',')
            entry ={}
            
            for i, value in enumerate(fields):
                entry[header[i].strip()]=value.strip()
            
            data.append(entry)
            count = count + 1


    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()


# beatles-diskography.csv
# Title,Released,Label,UK Chart Position,US Chart Position,BPI Certification,RIAA Certification
# Please Please Me,22 March 1963,Parlophone(UK),1,-,Gold,Platinum
# With the Beatles,22 November 1963,Parlophone(UK),1,-,Platinum,Gold
# Beatlemania! With the Beatles,25 November 1963,Capitol(CAN),-,-,,
# Introducing... The Beatles,10 January 1964,Vee-Jay(US),-,2,,
# Meet the Beatles!,20 January 1964,Capitol(US),-,1,,5xPlatinum
# Twist and Shout,3 February 1964,Capitol(CAN),-,-,,
# The Beatles' Second Album,10 April 1964,Capitol(US),-,1,,2xPlatinum
# The Beatles' Long Tall Sally,11 May 1964,Capitol(CAN),-,-,,
# A Hard Day's Night,26 June 1964,United Artists(US)[C],-,1,,4xPlatinum
# ,10 July 1964,Parlophone(UK),1,-,Gold,
# Something New,20 July 1964,Capitol(US),-,2,,Platinum
# Beatles for Sale,4 December 1964,Parlophone(UK),1,-,Gold,Platinum
# Beatles '65,15 December 1964,Capitol(US),-,1,,3xPlatinum
# Beatles VI,14 June 1965,"Parlophone(NZ), Capitol(US)",-,1,,Platinum
# Help!,6 August 1965,Parlophone(UK),1,-,Platinum,
# ,13 August 1965,Capitol(US)[C],-,1,,3xPlatinum
# Rubber Soul,3 December 1965,Parlophone(UK),1,-,Platinum,
# ,6 December 1965,Capitol(US)[C],-,1,,6xPlatinum
# Yesterday and Today,15 June 1966,Capitol(US),-,1,,2xPlatinum
# Revolver,5 August 1966,Parlophone(UK),1,-,Platinum,
# ,8 August 1966,Capitol(US)[C],-,1,,5xPlatinum
# Sgt. Pepper's Lonely Hearts Club Band,1 June 1967,"Parlophone(UK), Capitol(US)",1,1,3xPlatinum,11xPlatinum
# Magical Mystery Tour,27 November 1967,"Parlophone(UK), Capitol(US)",31[D],1,Platinum,6xPlatinum
# The Beatles,22 November 1968,"Apple(UK), Capitol(US)",1,1,Platinum,19xPlatinum
# Yellow Submarine,13 January 1969,"Apple(UK), Capitol(US)",3,2,Silver,Platinum
# Abbey Road,26 September 1969,"Apple(UK), Capitol(US)",1,1,2xPlatinum,12xPlatinum
# Let It Be,8 May 1970,"Apple(UK),United Artists(US)",1,1,Gold,4xPlatinum