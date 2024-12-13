from unittest.mock import patch, Mock
from datetime import datetime
from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message import Message
from social_network_kata.message_store import MessageStore
from social_network_kata.social_media_cli import SocialMediaCLI
from social_network_kata.social_media_service import SocialMediaService

class TestSocialMediaService:
    def test_social_media_service_can_exit(self):
        #arrange
        expected_output = "Good bye"
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)
        message_store = Mock(MessageStore)
        
        social_media_service = SocialMediaService(clock, printer, message_store)

        #act
        social_media_service.exit()

        #assert
        printer.print.assert_called_once_with(expected_output)

    def test_social_media_service_can_add_message_to_username(self):
        #arrange
        clock = Mock(MessageClock)
        clock.now.return_value = datetime.strptime('2024-11-29T00:05:23','%Y-%m-%dT%H:%M:%S')
        printer = Mock(MessagePrinter)
        message_store = Mock(MessageStore)
        
        
        social_media_service = SocialMediaService(clock, printer, message_store)
        username = 'SomeUser'
        user_message = 'I like chocolate'
        expected_output = Message(author=username, content=user_message, timestamp=datetime.strptime('2024-11-29T00:05:23', '%Y-%m-%dT%H:%M:%S'))

        #act
        social_media_service.post(username, user_message)


        #assert
        message_store.add.assert_called_once_with(expected_output)

    def test_social_media_service_can_print_user_timeline(self):
        username = "Alice"
        message_store = Mock(MessageStore)
        clock = Mock(MessageClock)
        clock.now.return_value = datetime.strptime('2024-11-29T00:10:23','%Y-%m-%dT%H:%M:%S')
        message_list = [Message('Alice', 'I love the weather today', datetime.strptime('2024-11-29T00:05:23', '%Y-%m-%dT%H:%M:%S'))]
        message_store.get_timeline_for_username.return_value = message_list
        printer = Mock(MessagePrinter)
        social_media_service = SocialMediaService(clock, printer, message_store)

        expected_timeline = "I love the weather today (5 minutes ago)"

        #Act
        social_media_service.print_timeline_for_username(username=username)
        printer.print.assert_called_once_with(expected_timeline)


