from social_network_kata.social_media_service import SocialMediaService

class SocialMediaCLI:
    
    def __init__(self, social_media_service: SocialMediaService):
        self.social_media_service = social_media_service

    def run(self):
        self.running = True
        while self.running:
            user_input = input()
            self.parse_user_input(user_input)


    def parse_user_input(self, user_input):
        if user_input == "exit":
            self.social_media_service.exit()
            self.running = False
        elif "->" in user_input:
            # 'Alice -> I love the weather today'
            username, _, message = user_input.partition("->")
            self.social_media_service.post(username.strip(), message.strip())
        else:
            username = user_input
            self.social_media_service.print_timeline_for_username(username)
