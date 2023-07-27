from flask import abort

class Post():
    POSTS = [
        {'id': 1, 'title': 'First Post', 'content': 'This is my first post' },
        {'id': 2, 'title': 'Second Post', 'content': 'This is my second post' },
        {'id': 3, 'title': 'Third Post', 'content': 'This is my third post' }    
    ]

    @classmethod
    def all(cls):
        """Fetch all posts"""
        return cls.POSTS  #cls est un paramètre spécial utilisé dans les méthodes de classe pour faire référence à la classe elle-même


    @classmethod
    def find(cls, id):
        """Fetch single post a specific blog post based on its ID"""
        try:
            return cls.POSTS[int(id) - 1]

        except IndexError:
            abort(404)