import pandas as pd
import datetime

#####
# Chybí mi tady komentáře
#####


"""
Zase, napsal bych k čemu to slouží a co to dělá, odkud se ty funkce volají a jak je to důležité.
Pro mě je tohle dost nečitelné, zkus mi to tím textem jakoby vysvětlit
Klidně bych zase popsal co dělají importované moduly, pokud tam je něco zásadního
"""


df = pd.read_csv('data.csv')
count = df.shape[0]

def readDF():
    temp = df.at[0, 'Teplota']
    volt = df.at[0, 'Napětí']
    df.drop([0])
    df.reset_index()
    return temp, volt

def readDF2():
    j = 0
    while j <= df.shape[0]:
        temp = df.at[j, 'Teplota']
        volt = df.at[j, 'Napětí']
        j += 1
        return temp, volt

def readDF3():
    global df
    temp = df.at[0, 'Teplota']
    volt = df.at[0, 'Napětí']
    df = df.drop([0]).reset_index().drop(columns=['index'])
    return temp, volt



#print(type(df.shape[0]))
# print(readDF())
# print(readDF())
# print(readDF())
# print(readDF())
# print(readDF())

# print(readDF3())
# print(readDF3())
# print(readDF3())
# print(readDF3())
# print(readDF3())

time = datetime.datetime.now()
str = str(time)
stime = datetime.datetime.strptime(str, '%Y-%m-%d %H:%M:%S.%f')

print(time)
print(type(time))
print(str)
print(type(str))
print(stime)
print(type(stime))

print(time == stime)