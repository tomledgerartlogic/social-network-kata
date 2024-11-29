from unittest.mock import patch, Mock
from social_network_kata.message_clock import MessageClock
from social_network_kata.message_printer import MessagePrinter
from social_network_kata.social_media_service import SocialMediaService
from social_network_kata.social_media import SocialMedia

class TestPostMessage:
    @patch('builtins.input')
    def test_user_can_post_message_to_timeline(self, mocked_input):
        # Arrange
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)
        mocked_input.side_effect = ['Alice -> I love the weather today', 'Alice', 'exit']
        expected_output = "I love the weather today (5 minutes ago)"

        social_media_service = SocialMediaService(clock, printer)
        ##accept command
        social_media = SocialMedia(social_media_service)
                
        # Act
        # > Alice -> I love the weather today 
        # > Alice
        # > exit

        social_media.run()

        # Assert
        # Test message equals message passed in to printer
        printer.print.assert_called_once_with(expected_output)
