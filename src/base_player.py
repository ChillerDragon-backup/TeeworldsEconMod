#!/usr/bin/env python3
from chiller_essential import *
import datetime

aPlayers=[]

def CalcKD(k, d):
    if k == 0:
        return str(0)
    if d == 0:
        return str(k)
    return str("%.2f" % (k / d))

def BestTime(t1, t2):
    t = min(t1,t2)
    if t == 0:
        return max(t1, t2) #if no time yet --> set the highest
    return t #if captured already use lowest time

def A_Best(a1, a2):
    if a1 == "":
        return a2
    elif a2 == "":
        return a1
    if a1 < a2:
        return a1 # use oldest time
    return a2

class Player:
    #def __init__(self, name, time=0.0, spree=0, team="", a_haxx0r = "", a_blazeit = "", a_satan = "", a_virgin = ""):
    def __init__(self, name, time=0.0, spree=0, team=""):
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.flag_grabs = 0
        self.flag_caps_red = 0
        self.flag_caps_blue = 0
        self.flag_time = time
        self.flagger_kills = 0
        self.best_spree = spree
        self.wins = 0
        self.looses = 0
        self.a_haxx0r = ""
        self.a_blazeit = ""
        self.a_satan = ""
        self.a_virgin = ""
        '''
        self.a_haxx0r = a_haxx0r
        self.a_blazeit = a_blazeit
        self.a_satan = a_satan
        self.a_virgin = a_virgin
        '''
        #round variables (not saved)
        self.killingspree = 0
        self.IsFlagger = False
        self.team = team
        self.LastChat = datetime.datetime.now()
        self.MuteScore = 0
        self.IsMuted = False
    def __add__(self, other):
        tmp_player = Player(self.name)
        tmp_player.kills = self.kills + other.kills
        tmp_player.deaths = self.deaths + other.deaths
        tmp_player.flag_grabs = self.flag_grabs + other.flag_grabs
        tmp_player.flag_caps_red = self.flag_caps_red + other.flag_caps_red
        tmp_player.flag_caps_blue = self.flag_caps_blue + other.flag_caps_blue
        tmp_player.flag_time = BestTime(self.flag_time, other.flag_time)
        tmp_player.flagger_kills = self.flagger_kills + other.flagger_kills
        tmp_player.best_spree = max(self.best_spree, other.best_spree)
        tmp_player.wins = self.wins + other.wins
        tmp_player.looses = self.looses + other.looses
        tmp_player.a_haxx0r = A_Best(self.a_haxx0r, other.a_haxx0r)
        tmp_player.a_blazeit = A_Best(self.a_blazeit, other.a_blazeit)
        tmp_player.a_satan = A_Best(self.a_satan, other.a_satan)
        tmp_player.a_virgin = A_Best(self.a_virgin, other.a_virgin)
        """
        say("== merging '" + other.name + "' -> into -> '" + self.name + "' ===")
        say("src: ")
        say("k/d: " + str(other.kills) + " g/r/b/t: " + str(other.flag_grabs) + "/" + str(other.flag_caps_red) + "/" + str(other.flag_caps_blue) + "/" + str(other.flag_time))
        say("dst: ")
        say("k/d: " + str(self.kills) + " g/r/b/t: " + str(self.flag_grabs) + "/" + str(self.flag_caps_red) + "/" + str(self.flag_caps_blue) + "/" + str(self.flag_time))
        say("merge: ")
        say("k/d: " + str(tmp_player.kills) + " g/r/b/t: " + str(tmp_player.flag_grabs) + "/" + str(tmp_player.flag_caps_red) + "/" + str(tmp_player.flag_caps_blue) + "/" + str(tmp_player.flag_time))
        """
        return tmp_player
    def ShowStats(self):
        say("[stats] '" + str(self.name) + "' kills: " + str(self.kills) + " deaths: " + str(self.deaths) + " killingspree: " + str(self.best_spree))
        #say("[stats] '" + self.name + "' flagtime: " + str(self.flag_time))
    def ShowStatsRound(self):
        say("[round-stats] '" + str(self.name) + "' kd: " + CalcKD(self.kills,self.deaths) + " (" + str(self.kills) + "/" + str(self.deaths) + ")")

