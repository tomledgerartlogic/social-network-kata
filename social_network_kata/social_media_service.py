from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message_store import MessageStore


class SocialMediaService:
    
    def __init__(self, clock: MessageClock, printer: MessagePrinter, message_store: MessageStore):
        self.printer = printer

    def post(self, username, content):
        raise NotImplementedError

    def exit(self):
        self.printer.print("Good bye")