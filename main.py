
# Fetching data
# Setting Up the tutorial environment.
# Before you proceed make sure to set a test environment for the tutorial if you wish to
# test each of the queries as you proceed.
# Check out set up instructions here ...

# Now that we have our database set up with some dummy data,it's time to kick off the queries.
# Typing python on Linux/MacOS terminal opens a python shell where we'll be testing our queries
# For Windows OS users,during python installation a python Command Line Interphase / Shell
# sure enough was installed along. You can access this by typing python on the search bar

# Fetching all users and post objects using get()
# Assumingly,you have prior knowlwdge on SQLAlchemy or flask_sqlalchemy.

# Querying the User and Post models using the all() method returns a list of user objects,
# the list of object is arranged by default in an ascending order based on the id's.

>>> User.query.all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>, <User 'doe'>]

>>> Post.query.all()
# Output
[<Post 'Hello Geek 1'>, <Post 'Hello Geek 2'>, <Post 'Hello Geek 3'>, <Post 'Hello Geek 4'>]

# Getting user by primary key
# Apart from using the query() method, records can also be accessed using the get() method.
# The get method accepts a parameter,the id and 
# Returns an instance based on the given primary key identifier, or None if not found.

>>> User.query.get(1)
# Output
<User 'admin'>

# Getting a post by primary key

>>> Post.query.get(1)
# Output
<Post 'Hello Geek 1'>

# Handling None
# This will raise 404 errors instead of returning None
# first and first_or_404() are methods that fetch the first record that meets a condition whereas
# the all() method returns all the records found in the table / model.

# Often when handling queries in your views,you will at some point run into issues of
# missing or None entries
# Flask-SQLAlchemy has a helper for this. Instead of get(), use get_or_404(),
# and instead of first(), use first_or_404() and Instead of getting no results,
# this will generate 404 errors.

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
# When handling complex expressions you'll always need to customise your queries
# to make your whole process comfy. Using the endswith() method,you can run a query
# on a Model column that ends with an expression or anything of your choice.
# For example ,here we query the User model to fetch all the users whose email host
# is gmail. You notice that out of the four records,only two that meets the criteria
# are fetched.

>>> User.query.filter(User.email.endswith('@gmail.com')).all()
# Output
[<User 'john'>, <User 'doe'>]

# Limiting users / records

# Flask-SQLAlchemy also provides a method limit() that can be used to restrict
# the number of records fetched
# As shown below passing 2 and 3 as parameters in the queries limit() returns
# 2 records and 3 records respectively.

>>> User.query.limit(2).all()
# Output
[<User 'admin'>, <User 'guest'>]

>>> User.query.limit(3).all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>]

# Query a table and get results of specific column(s)
# Another method with_entities() proves more useful. For example when you're sending newsletter updates
# to your registered users,you'll only need their emails and perhaps their names(not covered),
# this can be easliy done as shown below.

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
# When working with records of any type order is always important. Flask-SQLAlchemy makes this
# easy using the order_by() method that accepts a paramater to be used in the ordering and the 
# type of order i.e ascending or descending.

>>> User.query.order_by(User.id.desc()).all()
# Output
[<User 'doe'>, <User 'john'>, <User 'guest'>, <User 'admin'>]

>>> User.query.order_by(User.id.asc()).all()
# Output
[<User 'admin'>, <User 'guest'>, <User 'john'>, <User 'doe'>]

# Filter by
# To filter records,we use the filter_by() method. 
# To demonstrate this,let's query the Post model and filter only those posts with 
# views equal to 40. This returns the two posts that has 40 views.

>>> Post.query.filter_by(views=40).order_by(Post.id.desc()).all()
# Output
[<Post 'Hello Geek 4'>, <Post 'Hello Geek 3'>]

# We can also chain the filter_by() and order_by() method with the count() to
# determine the number of occurences returned by the query.

>>> Post.query.filter_by(views=40).order_by(Post.id.desc()).count()
# Output
2

# The difference between the two filter methods is that filter_by
# uses keyword arguments, whereas filter allows pythonic filtering arguments 
# like filter(User.name=="john")

Post.query.filter(Post.views > 10).order_by(Post.date_posted.desc())
# Output
[<Post 'Hello Geek 4'>, <Post 'Hello Geek 3'>, <Post 'Hello Geek 2'>]

# Text search
# Searching through reecords in a database is ultimately the fastest way to access a specific
# or close;y related record in terms of label,term or title
# In this section of this article,we'll perform a full database text search based on a keyword.

# Import or_ from sqlalchemy,to enable us use alternative columns for the search
from sqlalchemy import or_

# If you're getting input from a form filed,you may prefer to use:
# keyword = request.form.get('search-query')

# Set a keyword variable with a value for our search
>>> keyword = 'holiday'
# Assign the list of results to a variable result
>>> results = Post.query.filter(or_(Post.title.ilike(f'%{keyword}%'), Post.body.ilike(f'%{keyword}%'))).all()
# Loop through each item in the list of posts and print for each the title and body
>>> [print(result.title,result.body) for result in results]
# Output
Hello Geek 3 Happy holidays Geek 3
[None]
