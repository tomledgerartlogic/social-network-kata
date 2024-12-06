from unittest.mock import patch, Mock, call
from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.message_store import MessageStore
from social_network_kata.social_media_service import SocialMediaService
from social_network_kata.social_media import SocialMedia
from datetime import datetime

class TestPostMessage:
    @patch('builtins.input')
    def test_user_can_post_message_to_timeline(self, mocked_input):
        # Arrange
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)
        message_store = Mock(MessageStore)
        mocked_input.side_effect = ['Alice -> I love the weather today', 'Alice', 'exit']
        clock.now.side_effect = [datetime.strptime('2024-11-29T00:05:23', '%Y-%m-%dT%H:%M:%S'), datetime.strptime('2024-11-29T00:10:23', '%Y-%m-%dT%H:%M:%S')]
        expected_output = "I love the weather today (5 minutes ago)"

        social_media_service = SocialMediaService(clock, printer, message_store)
        ##accept command
        social_media = SocialMedia(social_media_service)
                
        # Act
        # > Alice -> I love the weather today 
        # > Alice
        # > exit

        social_media.run()

        # Assert
        # Test message equals message passed in to printer
        printer.print.assert_has_calls([call(expected_output), call("Good bye")])
        # printer.print.assert_called_once_with("Good bye")
