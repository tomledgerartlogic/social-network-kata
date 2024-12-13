
from unittest.mock import patch, Mock
from social_network_kata.social_media_cli import SocialMediaCLI
from social_network_kata.social_media_service import SocialMediaService


class TestSocialMediaCLI:
    @patch('builtins.input')
    def test_user_can_exit(self, mocked_input):
        #Arrange
        mock_social_media_service = Mock(SocialMediaService)
        social_media = SocialMediaCLI(mock_social_media_service)
        mocked_input.return_value = "exit"
        
        #Act
        social_media.run()

        #Assert
        mock_social_media_service.exit.assert_called_once()

    @patch('builtins.input')
    def test_user_can_post(self, mocked_input):
        #Arrange
        mock_social_media_service = Mock(SocialMediaService)
        social_media = SocialMediaCLI(mock_social_media_service)
        mocked_input.side_effect = ['Alice -> I love the weather today', "exit"]

        #Act
        social_media.run()
        
        #Assert
        mock_social_media_service.post.assert_called_once_with("Alice", "I love the weather today")

    @patch('builtins.input')
    def test_can_read_user_timeline(self, mocked_input):
        #Arrange
        mock_social_media_service = Mock(SocialMediaService)
        social_media = SocialMediaCLI(mock_social_media_service)
        mocked_input.side_effect = ["Alice", "exit"]

        #Act
        social_media.run()

        #Assert
        mock_social_media_service.print_timeline_for_username.assert_called_once_with('Alice')

