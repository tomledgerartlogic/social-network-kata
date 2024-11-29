import MessagePrinter
import MessageClock

class TestPostMessage:
    def test_user_can_post_message_to_timeline(self):
        # Arrange
        clock = Mock(MessageClock)
        printer = Mock(MessagePrinter)

        test_message = "I love the weather today (5 minutes ago)"

        # Act
        # > Alice -> I love the weather today 
        # > Alice

        # Assert
        # Test message equals message passed in to printer
        printer.print.assert_called_once_with(test_message)
