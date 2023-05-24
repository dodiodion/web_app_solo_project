from lib.post_repository import PostRepository
from lib.post import Post
"""
When we call PostRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_posts(db_connection):
    db_connection.seed("seeds/post_user.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) 

    posts = repository.all()

    # Assert on the results
    assert posts == [
        Post(1, "2021-12-09 15:45:21", "There are pinguins on the beach", 1),
        Post(2, "2022-02-08 18:45:21", "Am i really all the things that are outside of me", 1),
        Post(3, "2022-12-08 13:45:21", "Smoking so much I cant breathe", 1),
    ]

"""
Create a new post, and add it to the database
"""
def test_create_post(db_connection):
    db_connection.seed("seeds/book_store.sql")
    post_repository = PostRepository(db_connection)
    post = Post(None, "2023-05-09 05:45:21", "Les oiseaux chantonnaient dans la jungle maudite", 1)
    post_repository.create(post)
    posts = post_repository.all()
    assert posts == [
        Post(1, "2021-12-09 15:45:21", "There are pinguins on the beach", 1),
        Post(2, "2022-02-08 18:45:21", "Am i really all the things that are outside of me", 1),
        Post(3, "2022-12-08 13:45:21", "Smoking so much I cant breathe", 1),
        Post(4, "2023-05-09 05:45:21", "Les oiseaux chantonnaient dans la jungle maudite", 1)
    ]