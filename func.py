import subprocess
import re
import math as m

def get_dataSignal() -> object:
    p = subprocess.Popen("netsh wlan show networks mode=Bssid", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode("unicode_escape").strip()
    m=re.findall("SSID.*?:.*?([\u0020-\u007e]{8,63}).*?Signal.*?:.*?([0-9]*)%",out,re.DOTALL)
    d={}
    for i in m:
        l=i[0].lstrip()
        d[l]=int(i[1])
    p.communicate()

    return(d)
def get_dataReception():
        p = subprocess.Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode("unicode_escape").strip()
        m=re.findall("R.ception.*?:.*?(\d{1,4}.\d{0,3})",out,re.DOTALL)
        p.communicate()
        return(m[0])
def get_dataSSID():
     p = subprocess.Popen("netsh wlan show networks", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     out = p.stdout.read().decode("unicode_escape").strip()
     m=re.findall("SSID.*?:.*?([\u0020-\u007e]{8,63})",out,re.DOTALL)
     p.communicate()
     l=[]
     for i in m:
          l.append(i.lstrip())
     return(l)


def get_distance(ssid):
    signal=get_dataSignal()[ssid]
    quality=(signal)/2-100
    """print(quality)"""
    if(signal>90):
        constant=(14-quality-(10*2.7*(m.log10(2.4))+30*2.7-32.44))/(10*2.7)
    elif (signal<=90):
        constant=(22-quality-(10*2.7*(m.log10(2.4))+30*2.7-32.44))/(10*2.7)
    return(m.pow(10,constant))
