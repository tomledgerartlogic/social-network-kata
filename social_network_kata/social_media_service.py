from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message_store import MessageStore
from social_network_kata.message import Message


class SocialMediaService:
    
    def __init__(self, clock: MessageClock, printer: MessagePrinter, message_store: MessageStore):
        self.printer = printer
        self.message_clock = clock
        self.message_store = message_store

    def post(self, username, message_content):
        message = Message(username, message_content, self.message_clock.now())
        self.message_store.add(message)

    def print_timeline_for_username(self, username):
        timeline = self.message_store.get_timeline_for_username(username)
        formatted_messages = []
        for message in timeline:
            formatted_messages.append(self.format_message_for_printer(message))

        self.printer.print("\n".join(formatted_messages))

    def format_message_for_printer(self, message: Message):
        current_time = self.message_clock.now()
        message_time = message.timestamp
        time_difference = current_time - message_time
        time_difference_in_minutes = int(time_difference.total_seconds() / 60)
        if time_difference_in_minutes == 1:
            minute_label = "minute"
        else:
            minute_label = "minutes"
        formatted_message = f"{message.content} ({time_difference_in_minutes} {minute_label} ago)"

        return formatted_message


    def exit(self):
        self.printer.print("Good bye")