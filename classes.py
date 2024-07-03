from management import database
class User:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def select():
        query = "SELECT * FROM user"
        data = database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO user(name) VALUES('{self.name}')
        """
        return database.connect(query, "insert")


    def update(self):
        query = f"""
                UPDATE user(name) SET VALUES('{self.name}')
        """
        return database.connect(query, "update")
    def delete(self):
        query = f"DELETE FROM user(name) WHERE name = '{self.name}'"
        return database.connect(query, "delete")

