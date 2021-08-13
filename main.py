# Fetching data
>>> User.query.all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>, <User 'doe'>]

>>> Post.query.all()
# Output
[<Post 'Hello Geek 1'>, <Post 'Hello Geek 2'>, <Post 'Hello Geek 3'>, <Post 'Hello Geek 4'>]

>>> User.query.get(1)
# Output
<User 'admin'>

# Getting a post by primary key

>>> Post.query.get(1)
# Output
<Post 'Hello Geek 1'>

# Handling None

>>> User.query.get_or_404(1)
# Output
<User 'admin'>

>>> User.query.order_by(User.id.desc()).first_or_404()
# Output
<User 'doe'>

# Adding a description to a 404 response

>>> User.query.filter_by(username='admin').first_or_404(description='No data!')
# Output
<User 'admin'>
# You can also pass a description as an arguement with some message as shown
>>> User.query.filter_by(username='mike').first_or_404(description='No data!')
# Output
werkzeug.exceptions.NotFound: 404 Not Found: No data


# Selecting a bunch of users/record by a more complex expression

>>> User.query.filter(User.email.endswith('@gmail.com')).all()
# Output
[<User 'john'>, <User 'doe'>]

# Limiting users / records

>>> User.query.limit(2).all()
# Output
[<User 'admin'>, <User 'guest'>]

>>> User.query.limit(3).all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>]

# Query a table and get results of specific column(s)

>>> User.query.with_entities(User.email).first()
# Output
('admin@example.com',) 

>>> User.query.with_entities(User.email).all()
# Output
[('admin@example.com',), ('doe@gmail.com',), ('guest@example.com',), ('john@gmail.com',)]

# The with_entities() method can be too used with multiple values
>>> User.query.with_entities(User.username,User.email).first()
# Output
('admin', 'admin@example.com')

# Ordering users by something

>>> User.query.order_by(User.id.desc()).all()
# Output
[<User 'doe'>, <User 'john'>, <User 'guest'>, <User 'admin'>]

>>> User.query.order_by(User.id.asc()).all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>, <User 'doe'>]

# Filter by

>>> Post.query.filter_by(views=40).order_by(Post.id.desc()).all()
# Output
[<Post 'Hello Geek 4'>, <Post 'Hello Geek 3'>]

# We can also chain the filter_by() and order_by() method with the count() to
# determine the number of occurrences returned by the query.

>>> Post.query.filter_by(views=40).order_by(Post.id.desc()).count()
# Output
2


Post.query.filter(Post.views > 10).order_by(Post.date_posted.desc())
# Output
[<Post 'Hello Geek 4'>, <Post 'Hello Geek 3'>, <Post 'Hello Geek 2'>]

# Text search

# Import or_ from sqlalchemy,to enable us use alternative columns for the search
from sqlalchemy import or_

# If you're collecting data from a form field, you might prefer to use:
# keyword = request.form.get('search-query')

# Set a keyword variable with a value for our search
>>> keyword = 'holiday'
# Assign the list of results to a variable result
>>> results = Post.query.filter(or_(Post.title.ilike(f'%{keyword}%'), Post.body.ilike(f'%{keyword}%'))).all()
# Loop through the list of posts, printing the title and body for each.
>>> [print(result.title,result.body) for result in results]
# Output
Hello Geek 3 Happy holidays Geek 3
[None]
