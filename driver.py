def main():
    # 1. Name:
    #      -Tyler Elms-
    # 2. Assignment Name:
    #      Lab 03: Calendar
    # 3. Assignment Description:
    #      -It takes in any given month and year after 1753 and calculates the month days.-
    # 4. What was the hardest part? Be as specific as possible.
    #      -The assignment went well for me. I tried an object oriented approach at first but 3 functions is all this program really needs.
    #       I struggled with figuring out algorithms to calulate any given year with its month but luckily I found patterns. After  the intial calulations were 
    #       made, I just looked at the example for output format and went with a similar way-
    # 5. How long did it take for you to complete the assignment?
    #      -9 hours-
    handle_inputs()

def handle_inputs():
    while True:
        user_month = int(input("Type month value (1-12): "))
        if 0 < user_month < 13:
            break
    while True:
        user_year = int(input("Type year value (1753-2022): "))
        if 1752 < user_year < 2023:
            break
    
    handle_months_days(user_month,user_year)

def handle_months_days(user_month,user_year):
    month ={1:'January', 2:'February', 3:'March',
            4:'April', 5:'May', 6:'June', 7:'July',
            8:'August', 9:'September', 10:'October',
            11:'November', 12:'December'}

     
    day =(user_year-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7

    regular =[31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]
    leaped =[31, 29, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]
    
    placeholder = 0

    if user_year % 4 == 0:
        for i in range(user_month-1):
            placeholder+= leaped[i]
    else:
        for i in range(user_month-1):
            placeholder+= regular[i]

    day += placeholder % 7
    day = day % 7
    handle_output(user_month,user_year,month,day)


def handle_output(user_month,user_year,month,day):
    space =''
    space = space.rjust(2, ' ')

    print(month[user_month], user_year)
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')

    if user_month == 9 or user_month == 4 or user_month == 6 or user_month == 11:
        for i in range(31 + day):
            
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    elif user_month == 2:
        if user_year % 4 == 0:
            p = 30
        else:
            p = 29
            
        for i in range(p + day):
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    else:
        for i in range(32 + day):
            
            if i<= day:
                print(space, end =' ')
            else:
                print("{:02d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()

main()