from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'ahmad@gmail.com', 'mypassword')

# Update fields and then save again
user.first_name = 'ahmad'
user.last_name = 'ali'
user.save()