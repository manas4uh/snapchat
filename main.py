#Here i started my very first python project.

from spy_details import spy_name,spy_age,spy_rating #Here i imported specific spy details from a file name spy_details.
print 'Hello' #greetings to the user
print 'Let\'s get started' #startup quote

def start_chat(spy_name,spy_age,spy_rating): #Here i created a user define function having some arguments.
    print 'Here are your options ' +spy_name
    show_menu = True #For displaying menu with default value true
    while show_menu: #using loop concept 'while'
        choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n0.Exit ') #asking for user choices to select.
        if choice ==1: #condition statement
            print 'This will add the status of the spy'
        elif choice==2: #condition statement
            print 'This will add a friend'
        elif choice==0: #condition statement
            show_menu=False
        else: #condition statement
            print 'Invalid option selected by you.!! '
spy_exist=raw_input('Are you an existing spy Y/N ') #asking user for their existence
if spy_exist.upper()=='Y': #condition statement
    print 'Welcome back %s age: %d having spy rating of %.1f' %(spy_name,spy_age,spy_rating)#printing user details using place holder format specifier.
    start_chat(spy_name,spy_age,spy_rating) #calling funtion start_chat
elif spy_exist.upper()=='N':#condition statement
    spy_name = raw_input('Enter Your Name ') #asking user to input their name
    spy_rating=0.0 #using duck typing feature of python to declare spy_rating data type that is 'float'
    spy_age=0 #using duck typing feature of python to declare age data type that is 'integer'
    if spy_name.isalpha(): #condition statement
        spy_salutation = raw_input('What should we call you(Mr. or Ms.)')  # asking user to enter their salutation
        if len(spy_name)>=2:#using len() function to specify the length of input string
            if spy_salutation.upper()=='MR.' or spy_salutation.upper()=='MS.': #conditional statement using 'or' keyword and upper() function to convert sting into upper case.
                spy_name = spy_salutation.upper() + '' + spy_name #concatenating two variables
                print 'Welcome '+spy_name +'. Glad to have you back with us'
                print 'Alright '+spy_name+'. '+'I\'d like to know a little bit more about you ...'
                spy_age=input('what is your age ') #using input
                if 50>spy_age>12: #condiotional statement for comparing age limit
                    print 'You are eligible for being a spy with an age: '+str(spy_age)
                elif spy_age>50:
                    print 'Sir you have exceeded the spy age limit!'
                    spy_rating=input('Please enter your rating ') #asking user for rating
                    if spy_rating>5.0: #conditional statement used for spy rating
                        print'Bravo! it looks like you are an expert.'
                    elif 3.5<spy_rating<=5.0: #conditional statement used for spy rating
                        print 'You are good and well! You will be assigned a task Soon.'
                    elif 2.5<spy_rating<=3.5: #conditional statement used for spy rating
                        print 'A long way to go! keep going.'
                        spy_is_online = True  # using boolean data type
                        print 'Authentication Completed! Welcome ' + spy_name + ' age: ' + str(
                            spy_age) + ' and your rating is ' + str(spy_rating)
                        start_chat(spy_name, spy_age, spy_rating)
                    else: #conditional statement
                        print 'Who hired You? you are not born to be a spy.Go do something else..!!!'
                else: #condition statement
                    print 'You are under age! Go n grow up first!!'
            else: #condition statement
                print 'oops!Wrong Salutation.'
        else: #condition statement
            print 'Enter a valid name.'
    else: #condition statement
        print 'Invalid name!'
else: #condition statement
    print 'Invalid Option.Please try again.'
