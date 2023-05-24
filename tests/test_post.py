from lib.post import Post
"""
Create an instance of User with the properties id, time_posted, content, user_id
"""

def test_construct_post():
    post = Post(2, "2008-11-09 15:45:21", "hello my name is", 1)
    assert post.id == 2
    assert post.time_posted == "2008-11-09 15:45:21"
    assert post.content == "hello my name is"
    assert post.user_id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "2022-02-08 18:45:21", "Test Content", 3)
    assert str(post) == "Post: 1, 2022-02-08 18:45:21, Test Content, 3"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    post1 = Post(1, "2022-02-08 18:45:21", "Test Content", 2)
    post2 = Post(1, "2022-02-08 18:45:21", "Test Content", 2)
    assert post1 == post2