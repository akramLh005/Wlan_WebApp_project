import func as f
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import math as m

from sympy import Symbol, solve
import random
def get_distances():
    wifi=f.get_dataSignal()
    wifi_dict={}
    wifimax_dict={}
    for i in wifi:
        distance=f.get_distance(i)
        wifi_dict[i]=distance
    for j in range(3):
        i_max=""
        d_min=200
        for i in wifi_dict:
            if(d_min>=wifi_dict[i]):
                d_min=wifi_dict[i]
                i_max=i
        wifi_dict[i_max]=400
        wifimax_dict[i_max]=d_min
    print(wifimax_dict)
    return(wifimax_dict) 
def get_point( x0, y0,  r0, x1, y1,r1,r2):
    g=[]
    dx = x1 - x0
    dy = y1 - y0
    d = m.sqrt((dy*dy) + (dx*dx))
    if((d <= (r0 + r1))and(d >= abs(r0 - r1))):
        a = ((r0*r0) - (r1*r1) + (d*d)) / (2.0 * d) 
        point2_x = x0 + (dx * a/d)
        point2_y = y0 + (dy * a/d)
        h = m.sqrt((r0*r0) - (a*a))
        rx = -dy * (h/d)
        ry = dx * (h/d)
        intersectionPoint1_x = point2_x + rx
        intersectionPoint1_y = point2_y + ry
        x2 = Symbol('x2')
        y2= Symbol('y2')
        dx1 = intersectionPoint1_x - x2;
        dy1 = intersectionPoint1_y - y2;
        dx2=x1-x2
        dy2=y1-y2
        l=solve((dx1**2+dy1**2-r2**2,dx2**2+dy2**2-(random.uniform((r1+r2)/2,r1+r2))**2),(x2,y2))
        d=(intersectionPoint1_x,intersectionPoint1_y)
        g.append(d)
        g.append(l[0])
        return(g)
    
def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def get_graph():
    plt.clf()
    wifi=get_distances()
    distance_liste=[]
    wifi_liste=[]
    for i in wifi:
        distance_liste.append(truncate(wifi[i],2))
        wifi_liste.append(i)
    r0=distance_liste[0]
    r1=distance_liste[1]
    r2=distance_liste[2]
    y0=random.uniform(6,10)
    y1=y0
    alpha=random.uniform(0,r1+r0)
    x0=random.uniform(0,alpha)
    x1=alpha-x0
    l=get_point(x0,y0,r0,x1,y1,r1,r2)
    plt.axis([-100,100,-100,100])
    plt.axis("equal")
    c1=plt.Circle((x0,y0),radius=r0,color='red',alpha=0.3)
    c2=plt.Circle((x1,y1),radius=r1, color='green',alpha=0.3)
    c3=plt.Circle((l[1][0],l[1][1]),radius=r2, color="blue",alpha=0.3)
    circles=[c1,c2,c3]
    coll = PatchCollection(circles, match_original=True, zorder=0)
    plt.gca().add_collection(coll)
    plt.text(x0,y0+random.uniform(0,r0/2),wifi_liste[0],color="firebrick",weight="bold")
    plt.text(x1,y1-random.uniform(0,r1/2),wifi_liste[1],color="forestgreen",weight="bold")
    plt.text(l[1][0],l[1][1],wifi_liste[2],color="teal",weight="bold")
    plt.plot([l[0][0],x0], [l[0][1],y0],'o-',color="blueviolet")
    plt.plot([l[0][0],x1], [l[0][1],y0],'o-',color="blueviolet")
    plt.plot([l[0][0],l[1][0]], [l[0][1],l[1][1]],'o-',color="blueviolet")
    plt.xlabel("x en m")
    plt.ylabel("y en m")
    plt.title("graph localisation")
    return plt


