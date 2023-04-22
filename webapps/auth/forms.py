from fastapi import Request
from typing import Optional, List


class LoginForm:
    def __init__(self, request):
        self.request: Request = request
        self.errors: List = []
        self.username: str = None
        self.password: str = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Valid Email is required")
        if not self.password or not len(self.password) >= 6:
            self.errors.append("Password must be at least 6 characters long")
        if not self.errors:
            return True
        return False
