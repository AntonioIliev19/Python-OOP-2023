from typing import List


class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books: List[str] = []      # [Java, Python, Clean code]

    def info(self) -> str:
        return ', '.join(sorted(self.books))        # alphabetically

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
