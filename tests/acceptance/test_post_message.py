class TestPostMessage:
    def test_user_can_post_message_to_timeline(self):
        user = "Alice"
        message_content = "I love the weather today"
        post_message_use_case.execute(user, message_content)

        # When we get Alice's timeline
        timeline = get_timeline_use_case.execute(user)

        assert len(timeline) == 1
        assert timeline[0].content == message_content
