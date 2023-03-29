from models.base_model import BaseModel


class TodoModel(BaseModel):
    def __init__(self) -> None:
        super().__init__("todo")
        return None
    
    def getTasks(self) -> list[tuple[str, int, int, int]]:
        records = self.read()
        return records