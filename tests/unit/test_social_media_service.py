from unittest.mock import patch, Mock
from datetime import datetime
from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message import Message
from social_network_kata.message_store import MessageStore
from social_network_kata.social_media import SocialMedia
from social_network_kata.social_media_service import SocialMediaService

class TestSocialMediaService:
    def test_social_media_service_can_exit(self):
        #arrange
        expected_output = "Good bye"
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)
        
        social_media_service = SocialMediaService(clock, printer)

        #act
        social_media_service.exit()

        #assert
        printer.print.assert_called_once_with(expected_output)

    def test_social_media_service_can_add_message_to_username(self):
        #arrange
        clock = Mock(MessageClock)
        clock.now.return_value = datetime.strptime('2024-11-29T00:05:23')
        printer = Mock(MessagePrinter)
        message_store = Mock(MessageStore)
        
        
        social_media_service = SocialMediaService(clock, printer, message_store)
        username = 'SomeUser'
        user_message = 'I like chocolate'
        expected_output = Message(author=username, content=user_message, timestamp=datetime.strptime('2024-11-29T00:05:23'))

        #act
        social_media_service.post(username, user_message)


        #assert
        message_store.add.assert_called_once_with(expected_output)
