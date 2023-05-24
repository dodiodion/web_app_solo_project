from lib.user_repository import UserRepository
from lib.user import User
"""
Get the author of the post with the user_id
"""
def test_get_user_with_post_id(db_connection):
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    user_repository = UserRepository(db_connection)
    user = user_repository.get_user_with_post_id(3)
    assert user == User(1, "Bob Builder", "bob@gmail.com", "bob_builder",  "123456")

"""
Create a new user, and add it to the database
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/book_store.sql")
    user_repository = UserRepository(db_connection)
    user = User(None, "Little Mermaid", "mermaid@sea.com", "98776534", "little_mermaid")
    user_repository.create(user)
    users = user_repository.all()
    assert users == [User(1, "Bob Builder", "bob@gmail.com", "bob_builder",  "123456"),
                    User(2, "Little Mermaid", "mermaid@sea.com", "98776534", "little_mermaid")]

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_users(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new BookRepository

    users = repository.all() # Get all books

    # Assert on the results
    assert users == [User(1, "Bob Builder", "bob@gmail.com", "bob_builder",  "123456"),
                    User(2, "Little Mermaid", "mermaid@sea.com", "98776534", "little_mermaid")]