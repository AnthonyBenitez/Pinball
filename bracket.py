import random
import math
import sys
import copy
# import os


class Bracket:
    def __init__(self, teams):
        self.numTeams = 1
        # self.numTeams = len(teams)
        self.teams = list(teams)
        self.maxScore = len(max(["Round "]+teams, key=len))
        self.numRounds = int(math.ceil(math.log(self.numTeams, 2)) + 1)
        self.totalNumTeams = int(2**math.ceil(math.log(self.numTeams, 2)))
        self.totalTeams = self.addTeams()
        self.lineup = ["bye" if "-" in str(x) else x for x in self.totalTeams]
        self.numToName()
        self.count = 0
        self.rounds = []
        for i in range(0, self.numRounds):
            self.rounds.append([])
            for _ in range(0, 2**(self.numRounds-i-1)):
                self.rounds[i].append("-"*self.maxScore)
        self.rounds[0] = list(self.totalTeams)

    def numToName(self):
        for i in range(0, self.numTeams):
            self.totalTeams[self.totalTeams.index(i+1)] = self.teams[i]

    def shuffle(self):
        random.shuffle(self.teams)
        self.totalTeams = self.addTeams()
        self.numToName()
        self.rounds[0] = list(self.totalTeams)

    def update(self, rounds, teams):
        lowercase = [team.lower() for team in self.rounds[rounds-2]]
        for team in teams:
            try:
                index = lowercase.index(team.lower())
                self.rounds[rounds-1][int(index/2)] = self.rounds[rounds-2][index]
            except:
                return False
        if "-"*self.maxScore in self.rounds[rounds-1]:
            return False
        return True

    def show(self):
        self.count = 0
        self.temp = copy.deepcopy(self.rounds)
        self.tempLineup = list(self.lineup)
        sys.stdout.write("Seed ")
        for i in range(1, self.numRounds+1):
            sys.stdout.write(("Round "+str(i)).rjust(self.maxScore+3))
        print ""
        self.recurse(self.numRounds-1, 0)

    def recurse(self, num, tail):
        if num == 0:
            self.count += 1
            if tail == -1:
                print str(self.tempLineup.pop(0)).rjust(4)+self.temp[0].pop(0).rjust(self.maxScore+3)+" \\"
            elif tail == 1:
                print str(self.tempLineup.pop(0)).rjust(4)+self.temp[0].pop(0).rjust(self.maxScore+3)+" /"
        else:
            self.recurse(num-1, -1)
            if tail == -1:
                print "".rjust(4)+"".rjust((
                    self.maxScore+3)*num)+self.temp[num].pop(0).rjust(self.maxScore+3)+" \\"
            elif tail == 1:
                print "".rjust(4)+"".rjust((self.maxScore+3)*num)+self.temp[num].pop(0).rjust(self.maxScore+3)+" /"
            else:
                print "".rjust(4)+"".rjust((self.maxScore+3)*num)+self.temp[num].pop(0).rjust(self.maxScore+3)
            self.recurse(num-1, 1)

    def addTeams(self):
        x = self.numTeams
        teams = [1]
        temp = []
        count = 0
        for i in range(2, x+1):
            temp.append(i)
        for i in range(0, int(2**math.ceil(math.log(x, 2))-x)):
            temp.append("-"*self.maxScore)
        for _ in range(0, int(math.ceil(math.log(x, 2)))):
            high = max(teams)
            for i in range(0, len(teams)):
                index = teams.index(high)+1
                teams.insert(index, temp[count])
                high -= 1
                count += 1
        return teams


def getNumTeams():
    print "How many players?",
    numTeams = 2
    try:
        x = int(numTeams)
        if x > 1:
            return x
        else:
            print "Must be at least two players"
            return getNumTeams()
    except:
        return getNumTeams()


def getTeamNames(numTeams):
    teams = []
    for i in range(0, numTeams):
        correct = False
        """while not correct:
            print "Name of player "+str(i+1)+"?",
            teams.append(name)
            correct = True"""
    return teams


def run():
    numTeams = getNumTeams()
    teams = getTeamNames(numTeams)
    bracket = Bracket(teams)
    bracket.shuffle()
    bracket.show()
    for i in range(2, bracket.numRounds+1):
        updated = False
        while not updated:
            teams = []
            updated = bracket.update(i, teams)
            bracket.show()
    print ""
    print bracket.rounds[-1][0]+" won!"
