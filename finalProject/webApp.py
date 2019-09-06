import os
from flask import Flask, url_for, render_template, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/teamoffense')
def render_teamOffense():
    return render_template('team_offense.html')

@app.route('/team_offense_result')
def render_team_offense_result():
    try:
        offense_result = request.args['school']
        attack_result = getOffenseStats(offense_result)
        return render_template('team_offense_result.html', attack_form = attack_result)
    except ValueError:
        return "Sorry: invalid team"
"""
@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/mtokm')
def render_mtokm():
    return render_template('mtokm.html')
    
@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['fTemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', fTemp=ftemp_result, cTemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['cTemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', cTemp=ctemp_result, fTemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/mtokm_result')
def render_mtokm_result():
    try:
        # You'll need some code here, and maybe some extra parameters in render_template below...
        return render_template('mtokm.html')
    except ValueError:
        return "Sorry: something went wrong."

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)
    
def ctof(ftemp):
   return (ftemp*(9.0/5.0))+32.0

# You'll probably want a basic function here to convert miles to kilometers too...
"""
def getQBStats(qb):
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

    name = qb
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
def getOffenseStats(school): 
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
    name = school
    statsRows = int(statsSize//len(statsCols))
    while statsRows > 0:
        statsRows -= 1
        university = stats.loc[statsRows]['School']
        if university != None and university == name:
            index = 0
            string = ""
            string += otherTableHead[index]
            index += 1
            string += str(stats.iloc[statsRows,0:3])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index] +"\n"
            index += 1
            string += str(stats.iloc[statsRows,3:8])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index] +"\n"
            index += 1
            string += str(stats.iloc[statsRows,8:12])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index] +"\n"
            index += 1
            string += str(stats.iloc[statsRows,12:15])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index] +"\n"
            index += 1
            string += str(stats.iloc[statsRows,15:19])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index] +"\n"
            index += 1
            string += str(stats.iloc[statsRows,19:21])+"/\/\/\/\/\/\/\/\/"
            string += otherTableHead[index]+"\n"
            string += str(stats.iloc[statsRows,21:len(tableHead)])
            return string
getOffenseStats("UCLA")
def getDefenseStats(school): 
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
    name = school
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
def getRBStats(rb): 
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
    name = rb
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
def getWRStats(wr): 
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
    name = wr
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
#getWRStats()    
if __name__=="__main__":
    app.run(debug=False, port=5751)
