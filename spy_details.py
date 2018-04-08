from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=salutation +" " +name
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None

spy = Spy('Manas','Mr.',20,3.5)

class ChatMessage:
    def __init__(self,message,date,sent_by_me,receiver_name):
        date = datetime.now()
        self.message = message
        self.date = str(date)
        self.sent_by_me = sent_by_me
        self.receiver_name = receiver_name
