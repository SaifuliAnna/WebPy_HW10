from models import Post, LinkPost, TextPost, User

_id = '632446cf1ca21bdc82bbf999'

post = Post.objects(id=_id)
post.update(email='http://anetka.one@gmail.com/')

print(post)

for p in post:
    # print(p.title, p.email)
    print(p.to_mongo().to_dict())
    