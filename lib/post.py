class Post:
    def __init__(self, id, time_posted, content, user_id):
        self.id = id
        self.time_posted = time_posted
        self.content = content
        self.user_id = user_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Post
    def __repr__(self):
        return f"Post: {self.id}, {self.time_posted}, {self.content}, {self.user_id}"