import hashlib
from lib.user_repository import UserRepository
from lib.user import User
"""
Get the author of the post with the user_id
"""
def test_get_user_with_post_id(db_connection):
    db_connection.seed("seeds/post_user.sql") # Seed our database with some test data
    user_repository = UserRepository(db_connection)
    user = user_repository.get_user_with_post_id(3)
    assert user == User(1, "Bob Builder", "bob@gmail.com", "bob_builder",  "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92")

"""
Create a new user, and add it to the database
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/post_user.sql")
    user_repository = UserRepository(db_connection)
    plain_password = "98776534"
    user = User(None, "Little Mermaid", "mermaid@sea.com", "little_mermaid", plain_password)
    user_repository.create(user)
    binary_password = plain_password.encode("utf-8")
    hashed_password = hashlib.sha256(binary_password).hexdigest()
    users = user_repository.all()
    assert users == [User(1, "Bob Builder", "bob@gmail.com", "bob_builder", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
                    User(2, "Bob Gratton", "bob_gratton@hotmail.com", "bob_gratton", "ba28e715bb87f8126262007fd9651d3cae6a60faa48ccf8b62124b0fb7f6e01b"),
                    User(3, "Little Mermaid", "mermaid@sea.com", "little_mermaid", hashed_password)]

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/post_user.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)

    users = repository.all()
    # Assert on the results
    assert users == [User(1, "Bob Builder", "bob@gmail.com", "bob_builder", "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"),
                    User(2, "Bob Gratton", "bob_gratton@hotmail.com", "bob_gratton", "ba28e715bb87f8126262007fd9651d3cae6a60faa48ccf8b62124b0fb7f6e01b")]
    
"""
Test if the test password works with an existing email and password combination
"""
def test_check_password(db_connection):
    db_connection.seed("seeds/post_user.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    assert True == repository.check_password("bob_gratton@hotmail.com", "0987654")
    assert False == repository.check_password("bob@gmail.com", "falseemail")