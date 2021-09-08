from typing import List
from typing import Optional

from fastapi import Request


class JobCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.adhar: Optional[str] = None
        self.pen: Optional[str] = None
       

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.adhar = form.get("adhar")
  
        self.pen = form.get("pen")
   

    def is_valid(self):
        if not self.name or not len(self.name) >= 4:
            self.errors.append("A valid name is required")
        if not self.adhar or not len(self.adhar) >= 1:
            self.errors.append("A valid Adhar Number is required")
        if not self.errors:
            return True
        return False
