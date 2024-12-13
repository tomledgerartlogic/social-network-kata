from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
    author : str
    content: str
    timestamp: datetime