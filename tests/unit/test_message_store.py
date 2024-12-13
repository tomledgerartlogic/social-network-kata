from social_network_kata.message import Message
from social_network_kata.message_store import MessageStore
from datetime import datetime

class TestMessageStore:
    def test_message_store_can_add(self):
        message_store = MessageStore()
        author = "Alice"
        content = "I love the weather today"
        message_timestamp = datetime.strptime('2024-11-29T00:05:23', '%Y-%m-%dT%H:%M:%S')
        message = Message(author,content,message_timestamp)
        expected_message_list = [message]

        message_store.add(message=message)

        assert message_store.get_all_messages() == expected_message_list

    