import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_dennis = User(first_name = "Dennis",last_name = "Njeru",username = "thephi",password = "dennje349",email = "testmail@gmail.com")
        self.new_post = Post(post_title = "Cement",post_content = "Types of cement used in construction",user_id = self.user_dennis.id)
        self.new_comment = Comment(comment = "Great piece",post_id = self.new_post.id,user_id = self.user_dennis.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_dennis, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))