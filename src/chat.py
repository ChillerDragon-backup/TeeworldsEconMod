#!/usr/bin/env python3
import sys
import time
from chiller_essential import *
import cbase
from player import *
import global_settings
import sql_stats
import version

def GetRankName(msg, rank_cmd):
    if not global_settings.StatsMode == "sql":
        say("not supported in file stats mode")
        return None
    msg_normal = msg
    msg = msg.lower()
    name_start = cbase.cfind(msg, ":", 3) + 1
    name_end = msg.find(rank_cmd, name_start)
    name_end = msg.rfind(": ", name_end)
    name = msg_normal[name_start:name_end]
    rankname_start = -1
    if (msg.find(rank_cmd + " ") != -1):
        rankname_start = msg.find(rank_cmd + " ", name_end) + len(rank_cmd + " ")
    rankname_end = len(msg) - 1 #cut off newline
    rankname = msg_normal[rankname_start:rankname_end]
    if not rankname or rankname == "" or rankname_start == -1:
        return name
    return rankname

def HandleChatMessage(msg):
    msg_normal = msg
    msg = msg.lower()
    if (msg.find("/help") != -1 or msg.find("/info") != -1 or msg.find("/cmdlist") != -1):
        say("==== Teeworlds Econ Mod (TEM) ====")
        say("developed by ChillerDragon version: " + str(version.VERSION))
        say("https://github.com/ChillerDragon/TeeworldsEconMod")
        say("'/help' to show this help")
        say("'/stats' to show stats for all players")
        say("'/stats_all' to show all stats (a bit messy)")
        if global_settings.StatsMode == "sql":
            say("'/top5' for all time stats commands")
            say("'/rank' for all rank commands")
    elif (msg.find("/top5") != -1):
        if global_settings.StatsMode == "sql":
            say("'/top_kills' to see top5 killers of all time")
        if global_settings.StatsMode == "sql":
            say("'/top_flags' to see top5 flag caps of all time")
        if global_settings.StatsMode == "sql":
            say("'/top_sprees' to see top5 killing sprees of all time")
        else:
            say("not supported in file stats mode")
    elif (msg.find("/stats_all") != -1):
        PrintStatsAll(True)
    elif (msg.find("/stats") != -1):
        #say("sample rank message...")
        PrintStatsAll()
    elif (msg.find("/top_flag") != -1):
        if global_settings.StatsMode == "sql":
            sql_stats.BestTimes()
        else:
            say("not supported in file stats mode")
    elif (msg.find("/top_kill") != -1):
        if global_settings.StatsMode == "sql":
            sql_stats.BestKillers()
        else:
            say("not supported in file stats mode")
    elif (msg.find("/top_spree") != -1):
        if global_settings.StatsMode == "sql":
            sql_stats.BestSprees()
        else:
            say("not supported in file stats mode")
    elif (msg.find("/rank_kill") != - 1):
        sql_stats.RankKills(GetRankName(msg_normal, ": /rank_kill"))
    elif (msg.find("/rank_flag") != - 1):
        sql_stats.RankFlagTime(GetRankName(msg_normal, ": /rank_flag"))
    elif (msg.find("/rank_spree") != - 1):
        sql_stats.RankSpree(GetRankName(msg_normal, ": /rank_spree"))
    elif (msg.find("/rank_all") != - 1):
        name = GetRankName(msg_normal, ": /rank_all")
        if not name:
            return
        say("=== '" + str(name) + "'s stats ===")
        sql_stats.RankKills(str(name))
        sql_stats.RankFlagTime(str(name))
        sql_stats.RankSpree(str(name))
    elif (msg.find("/rank") != - 1):
        if not global_settings.StatsMode == "sql":
            say("not supported in file stats mode")
            pass
        say("'/rank_kills' to show global kills rank")
        say("'/rank_spree' to show global spree rank")
        say("'/rank_flag' to show global flag time rank")
    elif (msg.find("/test") != - 1):
        echo(" hello test wolrd ")
        say("test failed")
