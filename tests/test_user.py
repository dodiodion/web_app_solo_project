from lib.user import User
"""
Create an instance of User with the properties id, name, email, username, password
"""

def test_construct_user():
    user = User(3, "test name", "test@gmail.com", "test123", "testpassword")
    assert user.id == 3
    assert user.name == "test name"
    assert user.email == "test@gmail.com"
    assert user.username == "test123"
    assert user.password == "testpassword"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "test name", "test@email.com", "Test username", "Test password", )
    user2 = User(1, "test name", "test@email.com", "Test username", "Test password")
    assert user1 == user2

# This method makes it look nicer when we print an User
def __repr__(self):
    return f"User({self.id}, {self.name}, {self.email}, {self.username}, {self.password})"