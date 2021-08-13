def create_and_add():
	from app import db,User,Post

	db.create_all()

	admin = User(username='admin', email='admin@example.com')
	guest = User(username='guest', email='guest@example.com')
	john = User(username='john', email='john@gmail.com')
	doe = User(username='doe', email='doe@gmail.com')


	p_1 = Post(title='Hello Geek 1', body = 'Happy learning Geek 1' ,views = 10 )
	p_2 = Post(title='Hello Geek 2', body = 'Happy learning Geek 2' ,views = 20 )
	p_3 = Post(title='Hello Geek 3', body = 'Happy holidays Geek 3' ,views = 40 )
	p_4 = Post(title='Hello Geek 4', body = 'Happy learning Geek 4' ,views = 40 ) 

	users = (admin,guest,john,doe)
	posts = (p_1,p_2,p_3,p_4)

	db.session.add_all(users)
	db.session.add_all(posts)

	db.session.commit()


create_and_add()