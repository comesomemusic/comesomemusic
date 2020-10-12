# -*- coding: UTF-8 -*-
import math
import sys
import random
import heapq
import re
from fractions import Fraction
import logging
if(sys.argv[1]!="-n"):
    print("参数错误")
if(sys.argv[3]!='-r'):
    print("参数错误")
n=int(sys.argv[2])
r=int(sys.argv[4])

def check(s):
    lst=list(s)
    i=0
    a=0
    b=0
    while(i<len(lst)):
        if(lst[i]=='('):
            a=a+1
        if(lst[i]==')'):
            b=b+1
        i=i+1
    return a==b


#测试 s="".join print(s)
#约分
def rdOfAFra(n,m):
    n=int(n)
    m=int(m)
    if n>m:
        t=n
        n=m
        m=t
    if n==1:
        return str(n)+'/'+str(m)
    elif n==2 or n==4:
        if m%2==0:
            return str(n//2)+'/'+str(m//2)
        elif m%4==0:
            return str(n//4)+'/'+str(m//4)
        else :
            return str(n)+'/'+str(m)
    else :
        t=int(n//2)
        for i in range(2,t):
            while (n%i==0 and m%i==0):
                n=n//i
                m=m//i
        return str(n)+'/'+str(m)

#生产运算数字 n表示范围 k表示类型2、3为整数、1为代分数、0为真分数
def prdctN(k,n):
    if (n==1):
        k=0
    if k>=2:
        return str(random.randint(0,n))
    elif k==1:
        if n==2:
            m=1
        else:
            m=random.randint(1,n-1)
        b=random.randint(1,n)
        a=random.randint(1,n)
        if a==b:
            return str(m)
        s=rdOfAFra(a,b)
        return '('+str(m)+"'"+'('+str(s)+')'')'
    elif k==0 : 
        b=random.randint(1,n)
        a=random.randint(1,n)
        if a==b:
            return str(1)
        s=rdOfAFra(a,b)
        return '('+s+')'
    else :
        print("数字类型错误")

#产生运算符 k：0 1 2 3 对应+ - * /
def prdctC(k):
    if k==0:
        return '+'
    elif k==1:
        return '-'
    elif k==2:
        return '*'
    elif k==3:
        return '/'
    else :
        print("符号类型错误")
        
def dlSmPrn(s):
    #去除重复括号
    lst=list(s)
    L=[]#用来储存读取到的符号所在的位置
    i=0
    while i<len(lst):
        if lst[i]=="(":
            if i==1:
                pass
            L.append(i)
        while lst[i]==")":#删除重复
            j=L.pop()
            if(j==len(lst)-1)and L[len(L)-1]==0:
                del lst[i+1]
                del lst[L.pop()]
                
            while lst[i+1]==')' and(j-1==L[(len(L)-1)]):
                del lst[i+1]
                i=i-1
                j=L.pop()
                del lst[j]
            else:
                pass
            i=i+1
        i+=1
    return ''.join(lst)
#s为没加括号的表达式 n为表达式数字的多少
def prdctPrn(s,n):
    lst=list(s)
        #随机数为0时产生括号
    r=1
    while(random.randint(0,2)==0 or r==1):
        r=0
        st=random.randint(1,n)
        lnth=random.randint(2,n-st+2)
        if st==1:
            lst.insert(0,'(')
            i=1
            if(lnth>=0):
                while(i<len(lst)-2 and lnth>=0):
                    if lst[i]==" " and (lst[i+1]=="+" or lst[i+1]=="-"or lst[i+1]=="*" or lst[i+1]=="/"or lst[i+1]=='=') and lst[i+2]==" "and st>=0:
                        
                        
                        if lnth==0:
                            while(lst[i]!=" "and (lst[i+1]=="+" or lst[i+1]=="-"or lst[i+1]=="*" or lst[i+1]=="/"or lst[i+1]=='=')):
                                i+=1
                            lst.insert(i,")")
                            s="".join(lst)
                            i+=1
                        lnth=lnth-1
                    i+=1
                else:
                    pass
            else:
                print("右括号生距离错误")
                return s

        else :
            st-=1
            i=0
            while (i<len(lst)-2):
                if lst[i]==" " and (lst[i+1]=="+"or lst[i+1]=="-"or lst[i+1]=="*" or lst[i+1]=="/"or lst[i+1]=='=') and lst[i+2]==" " and st>=0:
                    st-=1
                    if st==0:
                        lst.insert(i+3,'(')
                        i+=1
                        if(lnth>=0):
                            while(i<len(lst)-2 and lnth>=0):
                                if lst[i]==" " and (lst[i+1]=="+"or lst[i+1]=="-"or lst[i+1]=="*" or lst[i+1]=="/"or lst[i+1]=='=') and lst[i+2]==" "and st>=0:
                                    
                                    if lnth==0:
                                        lst.insert(i,")")
                                        i+=1
                                    lnth=lnth-1   
                                i+=1
                        else:
                            print("右括号生距离错误")
                            return s
                i+=1
    s=''.join(lst)
    return s
        
def do_math(s):
    S1=re.sub(r"'",'+',s)
    S2=re.sub(r'(\d+/\d+)',r'(\1)',S1)
    S3=re.sub(r"=",'',S2)
    S4=re.sub(r'(\d+)', r'Fraction("\1")',S3)
    
    try:
        answ=eval(S4)
        return answ
    except Exception as e:
        print(e)
        return -1
#n表示范围 默认取10，d是存题目的字典
def prdctE(n=10):
    NumOfC=random.randint(1,3)#随机生成符号数
    N=NumOfC
    s=''
    while NumOfC>=0:
        NumOfC-=1
        C=random.randint(0,3)#随机生成符号
        k=random.randint(0,2)     
        s=s+prdctN(k,n)+' '+prdctC(C)+' '
    k=random.randint(0,4)
    s=s+prdctN(k,n)+' '+'='+' '
    s=prdctPrn(s,N)
    s=dlSmPrn(s)
    return s



Sanswer=''
Sq=''
d={}
for i in range(1,n+1):
    s=prdctE(random.randint(1,r))
    #print(check(s))
    answ=do_math(s)
    while(answ in d.keys() or int(answ)<=0) :
        s=prdctE(random.randint(1,r))
        
        #print(check(s))
        answ=do_math(s)
    else :    
        a=int(answ)
        
        answ=answ-a
        if(a==0 or answ==0):    
            d[answ]=0
            Sq=Sq+str(i)+'.'+s+"\n"
            Sanswer=Sanswer+str(i)+'.'+str(answ)+"\n"
        else :
            
            answ=str(a)+"'"+str(answ)
            d[answ]=0
            
            Sq=Sq+str(i)+'.'+s+"\n"
            Sanswer=Sanswer+str(i)+'.'+str(answ)+"\n"


Exer=open('Exercise'+'.txt',"w",encoding='utf-8')    
Answ=open('Answers'+'.txt',"w",encoding='utf-8')   
Exer.write(Sq)
Answ.write(Sanswer)     


