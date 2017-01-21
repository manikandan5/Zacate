# Automatic Zacate game player
# B551 Fall 2015
# Manikandan Murugesan - murugesm
#
# Based on skeleton code by D. Crandall
#
# The program written here plays the Zacate game at an Optimum level and tries to reach a good score
# The average score is in the range of 185-195
# The Minimum score varies between 90-130
# The Maximum score is in the range of 270-330
# The program takes the decision based on the Expectation and tries to reach the maximum possible score
# It compromises the category to take the decision
# The category that is being compromised is decided by the probability
# The category with the least probability is dropped first while the category with the highest probability is dropped last
# The program takes less time to run

#
#
# This is the file you should modify to create your new smart Zacate player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from ZacateState import Dice
from ZacateState import Scorecard
import random

class ZacateAutoPlayer:


    def __init__(self):
        pass

    #Call to reroll the dice after the first roll
    def first_roll(self, dice, scorecard):
        return self.ReRoll(dice,scorecard)

    #Call to reroll the dice after the second roll
    def second_roll(self, dice, scorecard):
        return self.ReRoll(dice,scorecard)

    #Call to select the Category after the final roll
    def third_roll(self, dice, scorecard):
        return  self.CalcScore(dice, scorecard)

    #Function which puts the dice values into a Dictionary which is easier to find the values
    def dice_into_dict(self, dice):
        diceDict={1:0,2:0,3:0,4:0,5:0,6:0}          #Initializing the dictionary
        for iDiceList in dice.dice:                 #Loop to assign the values into the Dictionary
              if diceDict.has_key(iDiceList):
                    diceDict[iDiceList] +=1
              else:
                    diceDict[iDiceList] = 1
        return diceDict                             #The final dictionary which contains the face of the dice and the occurences in key and values respectively

    #Function to try to increase the score when the program compromises and chooses pupusaDeQueso as the Category
    def pupusaDeQueso(self,dice):
        rerollList=[]
        if ((dice.dice.count(1)==2) or (set(dice.dice)==[1,3,4,5,6])):
            for i in range(0,5):
                for j in range(0,6):
                    if (dice.dice[i]==j or (set(dice.dice)==[1,2,3,4,6])):
                        if rerollList == []:
                            rerollList.append(i)
        return rerollList

    #Function to try to increase the score when the program compromises and chooses cuadruple as the Category
    def cuadruple(self,dice):
        rerollList=[]
        diceDict = self.dice_into_dict(dice)
        flag=0
        for j in range(1,7):
            if ((diceDict[j] == 4) or (diceDict[j] == 3)):
                for i in range(0,5):
                    if(dice.dice[i]!=j):
                        rerollList.append(i)
                        flag=1
            elif(diceDict[j] == 2):
                for i in range(0,5):
                    if(dice.dice[i]!=j):
                        rerollList.append(i)
                        flag=1

        if flag==0:
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        return rerollList

    #Function to try to increase the score when the program compromises and chooses quintupulo as the Category
    def quintupulo(self,dice):
        rerollList=[]
        diceDict = self.dice_into_dict(dice)
        if ((diceDict[1] == 4) or (diceDict[1] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=1):
                    rerollList.append(i)
        elif ((diceDict[2] == 4) or (diceDict[2] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=2):
                    rerollList.append(i)
        elif ((diceDict[3] == 4) or (diceDict[3] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=3):
                    rerollList.append(i)
        elif ((diceDict[4] == 4) or (diceDict[4] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=4):
                    rerollList.append(i)
        elif ((diceDict[5] == 4) or (diceDict[5] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=5):
                    rerollList.append(i)
        elif ((diceDict[6] == 4) or (diceDict[6] == 3)):
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        elif (diceDict[1] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=1):
                    rerollList.append(i)
        elif (diceDict[2] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=2):
                    rerollList.append(i)
        elif (diceDict[3] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=3):
                    rerollList.append(i)
        elif (diceDict[4] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=4):
                    rerollList.append(i)
        elif (diceDict[5] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=5):
                    rerollList.append(i)
        elif (diceDict[6] == 2):
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        elif (diceDict[1]!=5 or diceDict[2]!=5 or diceDict[3]!=5 or diceDict[4]!=5 or diceDict[5]!=5 or diceDict[6]!=5):
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        return rerollList

    #Function to try to increase the score when the program compromises and chooses pupusaDeFrijol as the Category
    def pupusaDeFrijol(self,dice):
        rerollList=[]
        if ((dice.dice.count(1)==2) or (set(dice.dice)==[1,3,4,5,6])):
            for i in range(0,5):
                if dice.dice[i]==1:
                    if rerollList == []:
                        rerollList.append(i)
        elif (dice.dice.count(2)==2):
            for i in range(0,5):
                if dice.dice[i]==2:
                    if rerollList == []:
                        rerollList.append(i)
        elif (dice.dice.count(3)==2):
            for i in range(0,5):
                if dice.dice[i]==3:
                    if rerollList == []:
                        rerollList.append(i)
        elif (dice.dice.count(4)==2):
            for i in range(0,5):
                if dice.dice[i]==4:
                    if rerollList == []:
                        rerollList.append(i)
        elif (dice.dice.count(5)==2):
            for i in range(0,5):
                if dice.dice[i]==5:
                    if rerollList == []:
                        rerollList.append(i)
        elif ((dice.dice.count(6)==2) or (set(dice.dice)==[1,2,3,4,6])):
            for i in range(0,5):
                if dice.dice[i]==6:
                    if rerollList == []:
                        rerollList.append(i)
        return rerollList

    #Function to try to increase the score when the program compromises and chooses elote as the Category
    def elote(self,dice):
        rerollList=[]
        diceDict = self.dice_into_dict(dice)
        if ((diceDict[1] == 2 and (diceDict[2] <2 and diceDict[3]<2 and diceDict[4]<2 and diceDict[5]<2 and diceDict[5]<2))):
            for i in range(0,5):
                if(dice.dice[i]!=1):
                    rerollList.append(i)
        elif ((diceDict[2] == 2) and (diceDict[1] <2 and diceDict[3]<2 and diceDict[4]<2 and diceDict[5]<2 and diceDict[5]<2)):
            for i in range(0,5):
                if(dice.dice[i]!=2):
                    rerollList.append(i)
        elif ((diceDict[3] == 2) and (diceDict[1] <2 and diceDict[2]<2 and diceDict[4]<2 and diceDict[5]<2 and diceDict[5]<2)):
            for i in range(0,5):
                if(dice.dice[i]!=3):
                    rerollList.append(i)
        elif ((diceDict[4] == 2) and (diceDict[1] <2 and diceDict[2]<2 and diceDict[3]<2 and diceDict[5]<2 and diceDict[5]<2)):
            for i in range(0,5):
                if(dice.dice[i]!=4):
                    rerollList.append(i)
        elif ((diceDict[5] == 2) and (diceDict[1] <2 and diceDict[2]<2 and diceDict[3]<2 and diceDict[4]<2 and diceDict[5]<2)):
            for i in range(0,5):
                if(dice.dice[i]!=5):
                    rerollList.append(i)
        elif ((diceDict[6] == 2) and (diceDict[1] <2 and diceDict[2]<2 and diceDict[3]<2 and diceDict[4]<2 and diceDict[5]<2)):
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        else:
            for i in range(0,5):
                if(dice.dice[i]!=6):
                    rerollList.append(i)
        return rerollList

    #Function to choose which dice to reroll
    def ReRoll(self,dice,scoreboard):
        rerollList=[]
        score = self.CalcScore(dice, scoreboard)
        print score

        if score=="quintupulo":
            rerollList=self.quintupulo(dice)
        elif score=="pupusa de frijol":
            rerollList = self.pupusaDeFrijol(dice)
        elif score=="pupusa de queso":
            rerollList = self.pupusaDeQueso(dice)
        elif score=="cuadruple":
            rerollList = self.cuadruple(dice)
        #elif score=="elote":
        #    rerollList = self.elote(dice)
        elif(score!="pupusa de frijol" and score!="elote"):
            for i in range(0,5):
                #print dice.dice[i]
                if score=="unos":
                    if(dice.dice[i]!=1):
                        rerollList.append(i)
                elif score=="doses":
                    if(dice.dice[i]!=2):
                        rerollList.append(i)
                elif score=="treses":
                    if(dice.dice[i]!=3):
                        rerollList.append(i)
                elif score=="cuatros":
                    if(dice.dice[i]!=4):
                        rerollList.append(i)
                elif score=="cincos":
                    if(dice.dice[i]!=5):
                        rerollList.append(i)
                elif score=="seises":
                    if(dice.dice[i]!=6):
                        rerollList.append(i)
                elif(dice.dice[i]==1 or dice.dice[i]==2 or dice.dice[i]==3):
                    rerollList.append(i)
        elif (score!="pupusa de queso"):
            rerollList = self.pupusaDeQueso(dice)


        return rerollList

    #Function which calculates the score for each category and assigns into a dictionary and returns the dictionary
    def valForCategory(self, roll, scorecard):
        dice = roll.dice

        counts = [dice.count(i) for i in range(1,7)]

        category={}

        category["unos"] = counts[0] * 1
        category["doses"] = counts[1] * 2 if category["unos"] < (counts[1]*2) else 0
        category["treses"] = counts[2] * 3 if (category["unos"] and category["doses"]) < (counts[2]*3) else 0
        category["cuatros"] = counts[3] * 4 if (category["unos"] and category["doses"] and category["treses"]) < (counts[3]*4) else 0
        category["cincos"] = counts[4] * 5 if (category["unos"] and category["doses"] and category["treses"] and category["cuatros"]) < (counts[4]*5) else 0
        category["seises"] = counts[5] * 6 if (category["unos"] and category["doses"] and category["treses"] and category["cuatros"] and category["cincos"]) < (counts[5]*6) else 0
        category["pupusa de queso"] = 40 if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6] else 0
        category["pupusa de frijol"] = 30 if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0) else 0
        category["elote"] = 25 if (2 in counts) and (3 in counts) else 0
        category["triple"] = sum(dice) if max(counts) >= 3 else 0
        category["cuadruple"] = sum(dice) if max(counts) >= 4 else 0
        category["quintupulo"] = 50 if max(counts) == 5 else 0
        category["tamal"] = sum(dice)

        return category

    #Function which calculates the expectation and makes a better decision to choose the proper category
    def CalcScore(self, roll, scorecard):
        category={}
        category = self.valForCategory(roll,scorecard)
        chosenCategory = self.chooseCategory(category,scorecard)
        return chosenCategory

    #Function to choose from the remaining category and compromises based on probability of the category
    def chooseCategory(self, category, scorecard):
        chosenCategory = ""
        if category["quintupulo"] != 0 and "quintupulo" not in scorecard.scorecard.keys():
            chosenCategory = "quintupulo"
        elif category["pupusa de queso"]!= 0 and "pupusa de queso" not in scorecard.scorecard.keys():
            chosenCategory = "pupusa de queso"
        elif category["pupusa de frijol"] and "pupusa de frijol" not in scorecard.scorecard.keys():
            chosenCategory = "pupusa de frijol"
        elif category["elote"] != 0 and "elote" not in scorecard.scorecard.keys():
            chosenCategory = "elote"
        elif category["cuadruple"] !=0 and "cuadruple" not in scorecard.scorecard.keys():
            chosenCategory = "cuadruple"
        elif category["triple"] !=0 and "triple" not in scorecard.scorecard.keys():
            chosenCategory = "triple"
        elif category["seises"] >6 and "seises" not in scorecard.scorecard.keys():
            chosenCategory = "seises"
        elif category["cincos"] >5 and "cincos" not in scorecard.scorecard.keys():
            chosenCategory = "cincos"
        elif category["cuatros"] >4 and "cuatros" not in scorecard.scorecard.keys():
            chosenCategory = "cuatros"
        elif category["treses"] >3 and "treses" not in scorecard.scorecard.keys():
            chosenCategory = "treses"
        elif category["doses"] >2 and "doses" not in scorecard.scorecard.keys():
            chosenCategory = "doses"
        elif category["unos"] !=0 and "unos" not in scorecard.scorecard.keys():
            chosenCategory = "unos"
        else:
            if "unos" not in scorecard.scorecard.keys():
                chosenCategory = "unos"
            elif "doses" not in scorecard.scorecard.keys():
                chosenCategory = "doses"
            elif "treses" not in scorecard.scorecard.keys():
                chosenCategory = "treses"
            elif "cuatros" not in scorecard.scorecard.keys():
                chosenCategory = "cuatros"
            elif "cincos" not in scorecard.scorecard.keys():
                chosenCategory = "cincos"
            elif "seises" not in scorecard.scorecard.keys():
                chosenCategory = "seises"
            elif "quintupulo" not in scorecard.scorecard.keys():
                chosenCategory = "quintupulo"
            elif "pupusa de queso" not in scorecard.scorecard.keys():
                chosenCategory = "pupusa de queso"
            elif "pupusa de frijol" not in scorecard.scorecard.keys():
                chosenCategory = "pupusa de frijol"
            elif "elote" not in scorecard.scorecard.keys():
                chosenCategory = "elote"
            elif "cuadruple" not in scorecard.scorecard.keys():
                chosenCategory = "cuadruple"
            elif "triple" not in scorecard.scorecard.keys():
                chosenCategory = "triple"
            else:
                chosenCategory = "tamal"
        return chosenCategory
