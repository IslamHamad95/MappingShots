import sys
import sqlite3
sys.path.append(r'C:\Users\Islam\.spyder-py3/WebScarbSofa.py')  
from WebScarbSofa import shots


conn = sqlite3.connect('ChelsesVsWesthamShots.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Shots;

CREATE TABLE Shots (
    ShotID    INTEGER NOT NULL PRIMARY KEY  UNIQUE,
    PlayerID  INTEGER,
    Name Text,
    Position Text,
    shotType Text,
    Situation Text,
    XG float,
    bodyPart Text,
    time Integer,
    addedTime Integer
);
''')

players_shots= shots['shotmap']

for player in players_shots:
    shotId=player['id']
    playerId=player['player']['id']
    name=player['player']["name"]
    position=player['player']["position"]
    shotType=player["shotType"]
    situation=player["situation"]
    xg=player["xg"]
    bodyPart=player["bodyPart"]
    time=player["time"]
    addedTime=player.get("addedTime",0)
    
    #print(shotId,playerId,name,position,shotType,xg,situation,bodyPart,time,addedTime)
    
    cur.execute('''INSERT OR IGNORE INTO Shots (ShotID,PlayerID,Name,Position,ShotType,XG,Situation,BodyPart,Time,AddedTime)
       VALUES ( ?,?,?,?,?,?,?,?,?,? )''', ( shotId,playerId,name,position,shotType,xg,situation,bodyPart,time,addedTime ) )
    cur.execute('SELECT ShotId FROM Shots WHERE name = ? ', (name, ))
    shotId = cur.fetchone()[0]
    conn.commit()