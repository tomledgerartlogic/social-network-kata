import MessagePrinter
import MessageClock
import SocialMediaService
import SocialMedia
from unittest import patch

class TestPostMessage:
    @patch('builtins.input', side_effect=['Alice -> I love the weather today', 'Alice', 'exit'])
    def test_user_can_post_message_to_timeline(self):
        # Arrange
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)

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
