import hashlib
from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_user_with_post_id(self, post_id):
        rows = self._connection.execute('SELECT users.* FROM users '\
                                    'JOIN posts ON posts.user_id = users.id '\
                                    'WHERE posts.id = %s', [post_id])
        return User(rows[0]["id"], rows[0]["name"], rows[0]["email"], rows[0]["username"], rows[0]["password"])
    
    def create(self, user):
        binary_password = user.password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute('INSERT INTO users (name, email, username, password)'\
                                'VALUES(%s, %s, %s, %s)', [user.name, user.email, user.username, hashed_password])
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row["id"], row["name"], row["email"], row["username"], row["password"])
            users.append(user)
        return users
    
    def check_password(self, email, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])

        return len(rows) > 0