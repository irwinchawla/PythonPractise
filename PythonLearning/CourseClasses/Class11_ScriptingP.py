# testing for try catch & showing how to implement logic in py file
# to run file, open terminal i.e cmd
# we have to change directory using cmd <Folder name>, we have to do it one by one
# Then when we are in the folder where our py file is present.
# run file by python filename.py
try:
    val1=int(input('Enter Value1: '))
except:
    print('You have entered wrong value, it will be treated as 0')
    val1=0

try:
    val2=int(input('Enter Value2: '))
except:
    print('You have entered wrong value, it will be treated as 0')
    val2=0

try:
    val3=int(input('Enter Value3: '))
except:
    print('You have entered wrong value, it will be treated as 0')
    val3=0

def funcadd(val1,val2):
    c=(val1+val2)
    print('We are printing sum of Value1 :',val1,' & Value2 :',val2,' = ',c)
    return c

c=funcadd(val1,val2)

def funcadd2(c,val3):
    d=(c+val3)
    print('We are printing sum of Value1 , Value2 , Value3 :',d)

funcadd2(c,val3)
    
