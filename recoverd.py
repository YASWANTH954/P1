# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:58:17 2022

@author: hp
"""

def rec(c,v,n):
    #dic={}
    l=[]
    z=len(c)
    x=z-n;                                #total uncorrupted letters
    for i in range (len(v)):        
        if c[0]==v[i][0]:
            if len(c)==len(v[i]):
                count=0
                
                for j in range (len(c)):
                    if c[j]==v[i][j]:
                        count+=1
                if count-x == 0:
                    
                    l.append(v[i])
                    
                  
    return l

def cnt(c):                         #count of the corrupted letters
    count=0
    for i in range (len(c)):
        if c[i]=='#':
            count+=1
    return count
   
        
                                   #main function block
voc=[]
with open("vocabulary_list.txt","r") as f:
    for line in f:
        tok=line.strip()
        voc.append(tok)


corr=[]
with open("corrupted_tokens.txt","r") as g:
    for line in g:
        tok=line.strip()
        corr.append(tok)
        
z=corr[:40]
#for i in range (len(z)):
    #print(z[i])
reco=[]
for i in range (len(z)):
    
    x=cnt(z[i])
    a=rec(z[i].lower(),voc,x)
        #print(a.values())
    reco.append(a)
    
d={}
for i in range(len(reco)):
    d[z[i]]=list(set(reco[i]))
print(d)

with open("recovery_list.txt","w") as h:
   
    for i in range (len(reco)):
        h.write(f'\n{z[i]} :{reco[i]}')
