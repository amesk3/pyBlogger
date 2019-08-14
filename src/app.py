import pymongo
from models.post import Post

Database.initialize()

post = Post('a', 'b', 'c')
post2 = Post('1', '2', '3')

print(post.title)
print(post2.title)
