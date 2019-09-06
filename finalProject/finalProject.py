from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
#url = "https://www.sports-reference.com/cbb/seasons/2019-school-stats.html"
#url = "https://www.sports-reference.com/cfb/years/2018-team-offense.html"
def getQBStats():
    url = "https://www.sports-reference.com/cfb/years/2018-passing.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
#Use findAll() to get the column headers
    soup.findAll('tr')
#Use getText()to get the text and put it into a list
    tableHead = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    otherTableHead = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
#Exclude the first column since rank is not useful info
    tableHead = tableHead[1:]
    #otherTableHead = otherTableHead[1:]
#print(tableHead)
    #print(otherTableHead)
#From 1 in order to avoid the first row which doesn't contain any info(kind of like hurricane tracker)
    rows = soup.findAll('tr')[1:]
    teamStats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    stats = pd.DataFrame(teamStats, columns = tableHead)
#stats.head(1i
    #print(stats)
    statsCols = stats.columns
    statsSize = stats.size
#print (statsCols)
#print (int(statsSize)/int(len(statsCols)))
#statsRows = int(statsSize//len(statsCols))
#print (statsRows)

    name = input("Enter QB Name: ")
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        player = stats.loc[statsRows]['Player']
        if player != None and player.split("*")[0] == name:
            index = 0
            #while index < len(tableHead)-1:
                #print (tableHead[index] + ": " + stats.loc[statsRows][tableHead[index]])
                #index += 1
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,0:3])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,3:4])
            print (otherTableHead[index])
            index +=1 
            print (stats.iloc[statsRows,4:13])
            print (otherTableHead[index])
            print (stats.iloc[statsRows,13:len(tableHead)])
#getQBStats()
def getOffenseStats(): 
    url = "https://www.sports-reference.com/cfb/years/2018-team-offense.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    soup.findAll('tr')
    tableHead = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    otherTableHead = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    tableHead = tableHead[1:]
    #print(otherTableHead)
    rows = soup.findAll('tr')[1:]
    teamStats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    stats = pd.DataFrame(teamStats, columns = tableHead)
    #print(stats)
    statsCols = stats.columns
    statsSize = stats.size
    name = input("Enter School Name: ")
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        university = stats.loc[statsRows]['School']
        if university != None and university == name:
            index = 0
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,0:3])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,3:8])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,8:12])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,12:15])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,15:19])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,19:21])
            print (otherTableHead[index])
            print (stats.iloc[statsRows,21:len(tableHead)])
#getOffenseStats()
def getDefenseStats(): 
    url = "https://www.sports-reference.com/cfb/years/2018-team-defense.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    soup.findAll('tr')
    tableHead = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    otherTableHead = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    tableHead = tableHead[1:]
    print(otherTableHead)
    rows = soup.findAll('tr')[1:]
    teamStats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    stats = pd.DataFrame(teamStats, columns = tableHead)
    print(stats)
    statsCols = stats.columns
    statsSize = stats.size
    name = input("Enter School Name: ")
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        university = stats.loc[statsRows]['School']
        if university != None and university == name:
            index = 0
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,0:3])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,3:8])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,8:12])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,12:15])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,15:19])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,19:21])
            print (otherTableHead[index])
            print (stats.iloc[statsRows,21:len(tableHead)])
#getDefenseStats()
def getRBStats(): 
    url = "https://www.sports-reference.com/cfb/years/2018-rushing.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    soup.findAll('tr')
    tableHead = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    otherTableHead = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    tableHead = tableHead[1:]
    print(otherTableHead)
    rows = soup.findAll('tr')[1:]
    teamStats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    stats = pd.DataFrame(teamStats, columns = tableHead)
    print(stats)
    statsCols = stats.columns
    statsSize = stats.size
    name = input("Enter RB Name: ")
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        player = stats.loc[statsRows]['Player']
        if player != None and player.split("*")[0] == name:
            index = 0
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,0:3])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,3:4])
            print (otherTableHead[index])
            index +=1 
            print (stats.iloc[statsRows,4:8])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,8:12])
            print (otherTableHead[index])
            print (stats.iloc[statsRows,12:len(tableHead)])
#getRBStats()
def getWRStats(): 
    url = "https://www.sports-reference.com/cfb/years/2018-receiving.html"
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    soup.findAll('tr')
    tableHead = [th.getText() for th in soup.findAll('tr')[1].findAll('th')]
    otherTableHead = [th.getText() for th in soup.findAll('tr')[0].findAll('th')]
    tableHead = tableHead[1:]
    print(otherTableHead)
    rows = soup.findAll('tr')[1:]
    teamStats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    stats = pd.DataFrame(teamStats, columns = tableHead)
    print(stats)
    statsCols = stats.columns
    statsSize = stats.size
    name = input("Enter WR Name:")
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        player = stats.loc[statsRows]['Player']
        if player != None and player.split("*")[0] == name:
            index = 0
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,0:3])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,3:4])
            print (otherTableHead[index])
            index +=1 
            print (stats.iloc[statsRows,4:8])
            print (otherTableHead[index])
            index += 1
            print (stats.iloc[statsRows,8:12])
            print (otherTableHead[index])
            print (stats.iloc[statsRows,12:len(tableHead)])
getWRStats()
