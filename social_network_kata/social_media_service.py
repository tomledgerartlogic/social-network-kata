from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message_store import MessageStore
from social_network_kata.message import Message


class SocialMediaService:
    
    def __init__(self, clock: MessageClock, printer: MessagePrinter, message_store: MessageStore):
        self.printer = printer
        self.message_store = message_store
        self.clock = clock

    def post(self, username, user_message):
        message = Message(author=username, content=user_message, timestamp=self.clock.now())
        self.message_store.add(message=message)

    def exit(self):
        self.printer.print("Good bye")