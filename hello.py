import datetime   
print ("hello world ")
# this output let it say hello world
name = input(' whats your name? ') 
print("nice to meet you " +  name)

age = input('how old are you ')
if age >= "16" and age <= "22": 
    print("that is a nice age")
else: 
    print('oke good ')
x = datetime.datetime.now()
x = str(x)
print('the date is ' + x)

car = input('what is your favorite car? ')
if car == ('mustang'):
    print("good your doing good ")
else:
    print("trash")