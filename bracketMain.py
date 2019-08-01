import bracket as br
import sys
import copy
import os
from bracketmodel import BracketModel


def newBracket(numTeams, teams, maxScore, numRounds, totalNumTeams, totalTeams, lineup, count, rounds, name):
    bracket = BracketModel(numTeams, teams, maxScore, numRounds, totalNumTeams, totalTeams, lineup, count, rounds, name)
    bracket = begin()
    update(bracket, 2)


"""def createDB(bracket, conn):
    cursor = conn.cursor()
    for i in range(1, bracket.totalNumTeams+1):
        cursor.execute("ALTER TABLE bracket ADD COLUMN team"+str(i)+" TEXT")
    for i in range(0, bracket.numRounds):
        columns = "('round',"
        for j in range(1, len(bracket.rounds[i])+1):
            columns += "'team"+str(j)+"',"
        columns = columns[:-1]+")"
        cursor.execute("INSERT INTO bracket "+columns+" VALUES ("+str(i+1)+",'" + "','".join(bracket.rounds[i])+"')")
    conn.commit()"""


def openBracket(bracket):
    if not bracket:
        print "bracket not found"
    q = BracketModel.query(BracketModel.name == bracket.name)
    users = q.fetch()
    teams = [x for x in list(users[0])[1:] if x[0] != "-"]
    temp = []
    for row in users:
        temp.append([str(x) for x in row if isinstance(x, unicode)])
    bracket = br.Bracket(teams)
    bracket.rounds = copy.deepcopy(temp)
    Round = bracket.numRounds
    for i in range(1, bracket.numRounds+1):
        if "-"*bracket.maxScore in bracket.rounds[i]:
            Round = i+1
            break
    update(bracket, Round)


def begin():
    numTeams = br.getNumTeams()
    teams = br.getTeamNames(numTeams)
    bracket = br.Bracket(teams)
    bracket.shuffle()
    return bracket


def update(bracket, Round):
    updated = False
    while not updated:
        bracket.show()
        teams = []  # html form for update bracket teams
        updated = bracket.update(Round, teams)
    if Round == bracket.numRounds:
        bracket.show()
        # html show win results
    else:
        update(bracket, Round+1)
        # html show next round results


"""def saveBracket(bracket, conn):
    for i in range(0, bracket.numRounds):
        keys = []
        for j in range(1, len(bracket.rounds[i])+1):
            keys.append("team"+str(j))
        results = ('UPDATE bracket SET '+','.join(key+' = ?' for key in keys)+' WHERE round = ?')
        args = bracket.rounds[i]+[i+1]
        return results


def closeBracket(bracket, conn):
    saveBracket(bracket, conn)
"""