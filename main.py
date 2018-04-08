# Here i started my very first python project.

from spy_details import spy,Spy,ChatMessage # Here i imported specific spy details from a file name spy_details.
from steganography.steganography import Steganography
import csv
from colorama import Fore,Style
from datetime import datetime
import time # current date and time
t = datetime.now()
print t.strftime('%b %d %Y %H:%M:%S')
print time #Display to the user
print 'Hello'  # greetings to the user
print 'Let\'s get started'  # startup quote
STATUS_MESSAGE = ['Be your Best!', 'What you allow is what will continue.', 'Busy']#predefined status
frnd1 = Spy('Manas','Mr.',20,3.5)
frnd2 = Spy('Faisal','Mr.',21,4.0)
friends=[frnd1,frnd2]

def load_frnds():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            spy= Spy(name=row[1],salutation=row[0],age=row[2],rating=row[3])
            friends.append(spy)
load_frnds()

def load_chats():#for loading all the chats
    with open('chat.csv') as chats_data:#opening chats.csv file
        reader = list(csv.reader(chats_data))#making this as a list
        print' Secret Text, ' + '(Date/Month/Hour), ' + 'Sender Name, ' + 'Receiver Name' #Displaying it to the user
        for message, date, sent_by_me, receiver_name in reader[1:]: #Extracting specific information
            print Fore.BLACK + message, Fore.BLUE + date, Fore.BLACK + sent_by_me, Fore.RED + receiver_name  # formaating it with a color
            print(Style.RESET_ALL)  # changes made by default

def specific_chats():#for particular friend
    specific_name = raw_input('Enter the Freind name')#asking for the user input name
    specific_sal = raw_input('What will you call Mr. or Ms.')#asking for the user input salutation
    specific_name=specific_sal.upper()+specific_name.upper()#converting for uppercase
    with open('chat.csv') as chats_data: #opening chats.csv file
        reader = list(csv.reader(chats_data)) #making this as a list
        print 'Secret Text,' + ' (Date/Month/Hour), ' + 'sender Name,' + 'Receiver Name'#Displaying the message for the user


    for message,date,sent_by_me,receiver_name in reader[1:]:  # The csv module already extracts the information for you
        if specific_name == receiver_name:
            print Fore.BLACK + message, Fore.BLUE + date, Fore.BLACK + sent_by_me, Fore.RED + receiver_name  # formaating it with a color
            print(Style.RESET_ALL)  # changes made by default

    if specific_name != receiver_name:  # conditional statemetn
        print 'You have not chated with that friend'  # displaying it for the user


def add_status(c_status):
    if c_status != None:
        print 'your current status is ' + c_status
    else:
        print 'you dont have any status currently.'
    existing_status = raw_input('Do you want to go for a old status? Y/N ')
    if existing_status.upper() == 'N':
        new_status = raw_input('Enter your new status ')
        if len(new_status) > 0:  # validating
            STATUS_MESSAGE.append(new_status)  # add the status in the list
    elif existing_status.upper() == 'Y':  # checking condition
        serial_no = 1  # initialising
        for old_status in STATUS_MESSAGE:  # traversing the list
            print str(serial_no) + '. ' + old_status  # displaying for the user
            serial_no = serial_no + 1  # incrementing
        user_choice = input('Enter your choice :')  # required input for the user
        new_status = STATUS_MESSAGE[user_choice - 1]  # Index value decremented not start with zero
    updated_status = new_status  # updating the status
    return updated_status  # returning back

def add_friend():
    new_frnd = Spy("","",0,0.0)
    new_frnd.name=raw_input('What is your name ? ') #required an input
    new_frnd.salutation=raw_input('what should we call you? (Mr. or Ms.)')
    new_frnd.age=input('What is your age ? ') #required an input
    new_frnd.rating=input('What is your rating ? ') #required an input
    new_frnd.spy_is_online=True
    if len(new_frnd.name)>2 and 12<new_frnd.age<50 and new_frnd.rating>=spy.rating and new_frnd.name.isalpha(): #checking for the condition
        new_frnd.salutation = new_frnd.salutation.upper()
        friends.append(new_frnd) #appending in the list
        with open('friends.csv', 'a') as friends_data:
            writer = (csv.writer(friends_data))
            writer.writerow([new_frnd.salutation, new_frnd.name, new_frnd.age, new_frnd.rating, new_frnd.spy_is_online])

    else:
        print 'Sorry! You are not eligible for being a spy friend'#displaying for the user
    return len(friends)#returning the value for the function

def select_frnd():#display all friend
    serial_no=1#initialising
    for frnd in friends:#showing all friends using loop
        print str(serial_no)+". "+frnd.name #displaying for the user
        serial_no=serial_no+1#incrementing
    user_selected_frnd=input("Enter a choice")#input from the user
    user_selected_frnd_index=user_selected_frnd-1#decrementing because list does not start with zero
    return user_selected_frnd_index #returning value to the function

def send_message():#sending a message
    select_friend=select_frnd()#index value
    original_image = raw_input('What is the name of your original image ? ')  # asking the user for an input of image
    secret_text = raw_input('What is your secret text message ? ')# secret text to be entered
    list = ['SOS', 'HELP ME', 'SAVE ME']  # if message is these words it will not be encoded
    if secret_text.upper() in list:
        print Fore.RED + 'Inappropriate message..'
        print(Style.RESET_ALL)
    else:
        output_path = "secret.jpg"#predefined name of an image
        secret_text=str(select_friend)+secret_text #assigning the index with the text for reading a message validation
        Steganography.encode(original_image, output_path, secret_text)  # encoding the message with image
        print 'Your message has been successfully encoded..'#displaying for the user
        print'Your secret message is ready.'#displaying for the user

    with open('chat.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([secret_text, time.strftime("%d %m %H"), spy.name, friends[select_friend].name])

def read_message():#reading a message
    select_friend=select_frnd()#index value
    output_path = raw_input('Enter the name of your image which you want to decode ? ')# asking the user for an input of image
    secret_text = Steganography.decode(output_path)#decoding message
    print'Secret text is:' + secret_text
    new_chat = ChatMessage(secret_text, time.strftime("%d %m %H"), spy.name, friends[select_friend].name)
    friends[select_friend].chats.append(new_chat)  # appending the friend chat detail
    print'Your secret message has been saved...'  # Displaying for the user



def start_chat(spy_name, spy_age, spy_rating):  # Here i created a user define function having some arguments.
    print 'Here are your options ' + spy_name
    current_status = None
    show_menu = True  # For displaying menu with default value true
    while show_menu:  # using loop concept 'while'
        choice = input(
            'What do you want to do ?\n1.Add a status\n2.Add a friend\n3.Send a secret message\n4.Read a secret message\n5.Read all chat History\n6.Read specific chat of a user\n0.logout ')  # asking for user choices to select.
        if choice == 1:  # condition statement
            current_status = add_status(current_status)  # calling add  status function
            print 'Updated status is ' + current_status  # displaying for the user

        elif choice == 2:  # condition statement
            no_of_friends = add_friend()  # calling the add friend function
            print 'You have ' + str(no_of_friends) + ' friends.'  # displaying for the user
        elif choice == 3:
            send_message()  # calling send function for encoding
        elif choice == 4:
            read_message()  # calling read function for decoding
        elif choice == 5:
            chat = raw_input('Do you want to load all chats? Y/N')
            if chat.upper()=='Y':
                load_chats()
            elif chat.upper()=='N':
                print'Then try for specific chat.'
            else:
                print 'Please select the right option'
        elif choice==6:
            specific_chats()
        elif choice == 0:  # condition statement
            show_menu = False
        else:  # condition statement
            print 'Invalid option selected by you.!! '


spy_exist = raw_input('Are you an existing spy Y/N ')  # asking user for their existence
if spy_exist.upper() == 'Y':  # condition statement
    print'Welcome back ' + spy.name + ' age :' + str(spy.age) + ' having rating of ' + str(spy.rating)

    start_chat(spy.name, spy.age, spy.rating)  # calling function


elif spy_exist.upper() == 'N': #condition statement
    spy = Spy("","",0,0.0)
    spy.name = raw_input('Enter Your Name ')  # asking user to input their name
    spy.rating = 0.0 # using duck typing feature of python to declare spy_rating data type that is 'float'
    spy.age = 0  # using duck typing feature of python to declare age data type that is 'integer'
    if spy.name.isalpha():  # condition statement
        spy_salutation = raw_input('What should we call you(Mr. or Ms.)')  # asking user to enter their salutation
        if len(spy.name) >= 2:  # using len() function to specify the length of input string
            if spy_salutation.upper() == 'MR.' or spy_salutation.upper() == 'MS.':  # conditional statement using 'or' keyword and upper() function to convert sting into upper case.
                spy.name = spy_salutation.upper() + '' + spy.name # concatenating two variables
                print 'Welcome ' + spy.name + '. Glad to have you back with us'
                print 'Alright ' + spy.name + '. ' + 'I\'d like to know a little bit more about you ...'
                spy.age = input('what is your age ')  # using input
                if 50 > spy.age > 12:  #condiotional statement for comparing age limit
                    print 'You are eligible for being a spy with an age: ' + str(spy.age)
                    spy.rating = input('Please enter your rating ') # asking user for rating
                    if spy.rating > 5.0:  # conditional statement used for spy rating
                        print'Bravo! it looks like you are an expert.'
                    elif 3.5 < spy.rating <= 5.0:  # conditional statement used for spy rating
                        print 'You are good and well! You will be assigned a task Soon.'
                    elif 2.5 < spy.rating <= 3.5:  # conditional statement used for spy rating
                        print 'A long way to go! keep going.'
                    else:  # conditional statement
                        print 'Who hired You? you are not born to be a spy.Go do something else..!!!'
                    spy_is_online = True  # using boolean data type
                    print 'Authentication Completed! Welcome ' + spy.name + ' age: ' +str(spy.age) + ' and your rating is ' +str(spy.rating)
                    start_chat(spy.name,spy.age,spy.rating)
                elif str(spy.age) > 50: #elif condition statement
                    print 'Sir you have exceeded the spy age limit!'
                else:  # condition statement
                    print 'You are under age! Go n grow up first!!'
            else:  # condition statement
                print 'oops!Wrong Salutation.'
        else:  # condition statement
            print 'Enter a valid name.'
    else:  # condition statement
        print 'Invalid name!'
else:  # condition statement
    print 'Invalid Option.Please try again.'