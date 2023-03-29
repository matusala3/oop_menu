from db_conn import DB_CONN

class BaseModel:
    table_name: str 

    def __init__(self, table_name: str) -> None:
        self.table_name = table_name
        return None
    
    def create(self) -> None:
        #Create
        #INSERT INTO todo (t_name, t_status) VALUES ('Jump', 1);
        #INSERT INTO todo (t_name, t_status) VALUES ('Crouch', 0);
        return None
    
    def read(self) -> list[tuple]:
        #Read
        #SELECT * FROM todo;
        # tuplle -> {t_name, t_status, update_at, created_at}
        #list of tuples
            # ("Jump", t_status, update_at, created_at)
            # ("Crouch", t_status, update_at, created_at)
        cursor = DB_CONN.cursor()
        statement = f"SELECT * FROM {self.table_name};"
        cursor.execute(statement)
        records: list[tuple] = cursor.fetchall()
        DB_CONN.commit()
        return records
    
    # def update(self) -> None:
    #     print("Update")
    #     #Update
    #     #UPDATE todo SET t_status = 1 WHERE t_name = 'Jump';
    #     return None
    
    # def delete(self) -> None:
    #     print("Delete")
    #     #Delete
    #     #DELETE FROM todo WHERE t_name = 'Jump';
    #     return None
    