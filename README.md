# Social Network Kata

> Incremental Kata - no peeping ahead!
> This is an incremental kata to simulate a real business situation: work your way through the steps in order, but do not read the next requirement before you have finished your current one.


## Your Team
Is tired of all those boring tasks like bowling game scores, bank accounts, singing songs or commanding mars rovers. This time you want to do something truly innovative: A Social Network!

## Your Rules
Your team also decided for this project to not only apply TDD and pair-programming - this time you’re gonna use BDD to cover all important features.

## Your Backlog

- Posting: Alice can publish messages to a personal timeline
- Reading: Bob can view Alice’s timeline
- Wall: Charlie can see his timeline
- Following: Charlie can subscribe to Alice’s and Bob’s timelines, and view an aggregated list of all subscriptions in his timeline


Additional Challenge:

- Mentions: Bob can link to Charlie in a message using “@”
- Direct Messages: Mallory can send a private message to Alice
- Links: Alice can link to a clickable web resource in a message

Implement a console-based social networking application (similar to Twitter) satisfying the scenarios below.

### Scenarios

**Posting**: Alice can publish messages to a personal timeline

> \> Alice -> I love the weather today
> \> Bob -> Damn! We lost!
> \> Bob -> Good game though.

**Reading**: Bob can view Alice’s timeline

> \> Alice
> \> I love the weather today (5 minutes ago)
> \> Bob
> \> Good game though. (1 minute ago)
> \> Damn! We lost! (2 minutes ago)

**Following**: Charlie can subscribe to Alice’s and Bob’s timelines, and view an aggregated list of all subscriptions

> \> Charlie -> I'm in New York today! Anyone wants to have a coffee?
> \> Charlie follows Alice
> \> Charlie wall
> \> Charlie - I'm in New York today! Anyone wants to have a coffee? (2 seconds ago)
> \> Alice - I love the weather today (5 minutes ago)

> \> Charlie follows Bob
> \> Charlie wall
> \> Charlie - I'm in New York today! Anyone wants to have a coffee? (15 seconds ago)
> \> Bob - Good game though. (1 minute ago)
> \> Bob - Damn! We lost! (2 minutes ago)
> \> Alice - I love the weather today (5 minutes ago)


### General requirements

- Application must use the console for input and output;
- User submits commands to the application:
    - posting: \<user name> -> \<message>
    - reading: \<user name>
    - following: \<user name> follows \<another user>
    - wall: \<user name> wall
- Don't worry about handling any exceptions or invalid commands. Assume that the user will always type the correct commands. Just focus on the sunny day scenarios.
- Use whatever language and frameworks you want. (provide instructions on how to run the application)
- **NOTE:** "posting:", "reading:", "following:" and "wall:" are not part of the command. All commands start with the user name.

**IMPORTANT:**  Implement the requirements focusing on **writing the best code** you can produce.

**CODE SUBMISSION:** Add the code to your own Github account and share with your teammates.

### Hints:

- You may use [Click](https://click.palletsprojects.com/en/stable/) library to build the application. Click library to build the application.
