from db_conn import DB_CONN
from menus.main_menu import MenuMain


class Main:
    def __init__(self):
        #1 Initialize 
        print("Program starting.")
        self.initDB()
        main_menu = MenuMain()
        #2 operate
        main_menu.start()
        #3 clean up
        DB_CONN.close()
        print("Program ending.")
        return None
    
    def initDB(self) -> None:
        with open("init.sql", "r", encoding="utf-8") as file_handel:
            sql_script = file_handel.read() #\n
            cursor = DB_CONN.cursor()
            cursor.executescript(sql_script)
            DB_CONN.commit()
        return None
    
if __name__ == "__main__":
    main = Main()