from lib.post import Post
class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], str(row["time_posted"]), row["content"], row["user_id"])
            posts.append(item)
        return posts
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (time_posted, content, user_id) '\
                                'VALUES(%s, %s, %s)', [post.time_posted, post.content, post.user_id])