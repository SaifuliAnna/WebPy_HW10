from models import Post, LinkPost, TextPost, User

_id = '632446c91ca21bdc82bbf996'

# post = Post.objects() так можна знищити все

post = User.objects(id=_id)
print(post.delete())