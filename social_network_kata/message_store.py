from social_network_kata.message import Message

class MessageStore:
    def __init__(self):
        self.__message_list = []
    
    def add(self, message: Message):
        self.__message_list.insert(0, message)
    
    def get_all_messages(self):
        return self.__message_list
    
    def get_timeline_for_username(self, username):
        raise NotImplementedError