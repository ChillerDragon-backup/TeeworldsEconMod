#!/usr/bin/env python3
import sys
import time
from chiller_essential import *
from player import *
import global_settings

def HandleChatMessage(msg):
    msg_normal = msg
    msg = msg.lower()
    if (msg.find("/help") != -1 or msg.find("/info") != -1 or msg.find("/cmdlist") != -1):
        say("==== Teeworlds Econ Mod (TEM) ====")
        say("developed by ChillerDragon")
        say("https://github.com/ChillerDragon/TeeworldsEconMod")
        say("'/help' to show this help")
        say("'/stats' to show stats for all players")
        say("'/stats_all' to show all stats (a bit messy)")
    elif (msg.find("/stats_all") != -1):
        PrintStatsAll(True)
    elif (msg.find("/stats") != -1):
        #say("sample rank message...")
        PrintStatsAll()
    elif (msg.find("/dev") != -1):
        say("debug=" + global_settings.IsDebug + " stats=" + global_settings.StatsMode)
    elif (msg.find("/test3") != -1):
        say("test 3 failed")
    elif (msg.find("/test2") != -1):
        say("test 2 failed")
    elif (msg.find("/test") != -1):
        say("test failed")

