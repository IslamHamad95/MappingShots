#!/usr/bin/env python
# coding: utf-8

# In[356]:


import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


# In[357]:


conn = sqlite3.connect(r'C:\Users\Islam\.spyder-py3\ChelsesVsWesthamShots.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Shots')
data = cursor.fetchall()


# In[358]:


headers= ["shotId","playerId","name","isHome","position","shotType","situation","xg","bodyPart","time","addedTime",
          "startx","starty","endx","endy","blockx","blocky","goalx","goaly"]
df = pd.DataFrame(data,columns=headers)
df


# In[359]:



def createPitch(team,home,teamColor):
    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 7,
        }
    
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
   

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,90], color="black")
    plt.plot([0,130],[90,90], color="black")
    plt.plot([130,130],[90,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    

    
    #Upper Penalty Area
    plt.plot([40,40],[0,16],color="black")
    plt.plot([40,90],[16,16],color="black")
    plt.plot([90,90],[16,0],color="black")
    
    
    #UPPER 6-yard Box
    plt.plot([51,79],[6,6],color="black")
    plt.plot([51,51],[0,6],color="black")
    plt.plot([79,79],[0,6],color="black")
    
    #Prepare Circles
    centreSpot = plt.Circle((65,90),0.8,color="black")
    upperPenSpot = plt.Circle((65,11),0.8,color="black")
    
    #Draw Circles
    ax.add_patch(centreSpot)
    ax.add_patch(upperPenSpot)
    
    #Prepare Arcs
    rightArc = Arc((65,10),height=18.3,width=18.3,angle=270,theta1=130,theta2=230,color="black")
    cenArc=Arc((65,90),height=18.3,width=18.3,angle=180,theta1=0,theta2=180,color="black")
    #Draw Arcs
    ax.add_patch(rightArc)
    ax.add_patch(cenArc)
    
    #Tidy Axes
    plt.axis('off')
    plt.gca().invert_yaxis()
    


    for i, shot in df.iterrows():
        if shot["isHome"]==home:
            x= shot["startx"]+15
            y= shot["starty"]
            shotCircle=plt.Circle((x,y),2,color=teamColor)
            
            if shot["shotType"]=="goal":
                shotCircle.set_alpha(1)
                plt.text(x, y+3, f'{shot["name"]}', fontdict=font)
               
            else:
                 shotCircle.set_alpha(.2)
        else:
            continue
        
       
        ax.add_patch(shotCircle)
    
    fig.suptitle(f"{team}'s Shots", fontsize = 24)
    fig.set_size_inches(10, 7)
    #Display Pitch
    plt.show()

createPitch("Chelsea",0,"blue")


# In[ ]:





# In[ ]:





# In[ ]:




