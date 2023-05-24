from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._conection = connection

    def get_user_with_post_id(self, post_id):
        rows = self._conection.execute('SELECT users.* FROM users '\
                                    'JOIN posts ON posts.user_id = users.id '\
                                    'WHERE posts.id = %s', [post_id])
        return User(rows[0]["id"], rows[0]["name"], rows[0]["email"], rows[0]["username"], rows[0]["password"])
    
    def create(self, user):
        self._conection.execute('INSERT INTO users (name, email, username, password)'\
                                'VALUES(%s, %s, %s, %s)', [user.name, user.email, user.username, user.password])
        
    def all(self):
        rows = self._conection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row["id"], row["name"], row["email"], row["username"], row["password"])
            users.append(user)
        return users