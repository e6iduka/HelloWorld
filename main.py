for x in range(0 ,151):
    print(x)




for x in range(5 ,1001 ,5):
    print(x)



def counting_dojo():
    for x in range (1,101):
        if x % 5 == 0:
            print('Coding')
        if x % 10 == 0:
            print ('Dojo')
        else:
             print(x)

counting_dojo()



def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()   



minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))




def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()   


def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)