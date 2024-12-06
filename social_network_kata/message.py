from dataclasses import dataclass

@dataclass
class Message:
    author: str
    content: str
    timestamp: str