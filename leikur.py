# -*- coding: utf-8 -*-
"""

@author: Axel Thor
"""

"this is a commit"







vbakki=["m","m","m","n","n","n"]

hbakki=[]

batur=[]

ferd=0

#slett tala; fara frá vinstri til hægri
counter=0

adgerdir=[]

while not(hbakki.count("m")==3 and hbakki.count("n")==3):
    print("ferð númer:",counter)
    if counter%2==0:
        print("fara frá vinstri bakka til hægri")
        print("vinstri bakki:",vbakki)
        print("hægri bakki:",hbakki)
        
        safe=False
        while not safe:
            while len(batur)!=2:
                inp=str(input("veldu mann í bátinn (0 fyrir engan):"))

                if inp=="0":
                    batur.append(inp)
                elif inp not in vbakki:
                    print("þessi maður er ekki á bakkanum reyndu aftur")
                else:
                    batur.append(inp)
                if batur == ["0","0"]:
                    print("einhver þarf að vera í bátnum, reyndu upp á nýtt")
                    batur=[]

            
            if (batur.count("m")+hbakki.count("m")>batur.count("n")+hbakki.count("n") and
                hbakki.count("n")+batur.count("n")!=0) or (vbakki.count("m")-batur.count("m")>vbakki.count("n")-batur.count("n") and
                vbakki.count("n")-batur.count("n")!=0):
                print("ekki safe, reyndu aftur")
                safe=False
                batur=[]

                
            else:
                safe=True
            
        
        print("í bátnum eru",batur)
        print("\n")
        adgerdir.append("bátur með {} og {} fóru frá vinstri til hægri".format(batur[0],batur[1]))
        for i in batur:
            if i!= "0":
                hbakki.append(i)
                vbakki.remove(i)

            else:
                pass
            batur=[]

    
    #fra hægri til vinstri
    if counter%2==1:
        print("fara frá hægri bakka til vinstri")
        print("vinstri bakki:",vbakki)
        print("hægri bakki:",hbakki)
        safe=False
        while not safe:
            while len(batur)!=2:
                inp=str(input("veldu mann í bátinn(0 fyrir engan):"))
                
                if inp=="0":
                    batur.append(inp)
                
                elif inp not in hbakki:
                     print("þessi maður er ekki á bakkanum reyndu aftur")
                else:
                    batur.append(inp)
                if batur == ["0","0"]:
                    print("einhver þarf að vera í bátnum, reyndu upp á nýtt")
                    batur=[]
            
            if (batur.count("m")+vbakki.count("m")>batur.count("n")+vbakki.count("n") and
                vbakki.count("n")+batur.count("n")!=0) or (hbakki.count("m")-batur.count("m")>hbakki.count("n")-batur.count("n") and
                hbakki.count("n")-batur.count("n")!=0):
                print("ekki safe, reyndu aftur")
                safe=False
                batur=[]
            else:
                safe=True
        print("í bátnum eru:",batur)  
        print("\n")
        adgerdir.append("bátur með {} og {} fóru frá hægri til vinstri".format(batur[0],batur[1]))
        for i in batur:
            if i!= "0":
                vbakki.append(i)
                hbakki.remove(i)
            else:
                pass
            batur=[]
    
    counter+=1
        
print("til hamingju þú hefur leyst þrautina")
print(adgerdir)
