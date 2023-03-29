from menus.menu import Menu
from models.todo_model import TodoModel

class MenuMain(Menu): # MenuMain inheriting Menu
    # help_menu: MenuHelp
    todo_model: TodoModel
    def __init__(self) -> None:
        super().__init__(options=[
            { "description": "Create new task", "action": self.createTask },
            { "description": "Show task", "action": self.showTask },
            { "description": "Update task status", "action": self.updateTask },
            { "description": "Delete task status", "action": self.deleteTask },
        ])
        self.todo_model = TodoModel()
        return None
    
    def createTask(self) -> None:
        print("Create task")
        return None
    
    def showTask(self) -> None:
        print("Tasks: ")
        print("Columns: t_name, t_status, update_at, created_at")
        tasks = self.todo_model.getTasks()
        for task in tasks:
            print(task.__str__())
        return None
    
    def updateTask(self) -> None:
        print("Update task")
        return None
    
    def deleteTask(self) -> None:
        print("Delete task")
        return None