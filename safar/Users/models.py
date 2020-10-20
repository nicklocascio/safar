from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Friend(models.Model):
	username = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.username



class user_lib():
	def add_user(username, first_name, last_name, password, email):
		temp_u = User(
			username=username, 
			first_name=first_name, 
			last_name=last_name, 
			password=password,
			email=email
			)
		temp_u.save()
		return temp_u

	def add_friend(user=None, f_un=""):
		if user != None and f_un != "":
			try:
				friend_user = User.objects.get(username=f_un)
			except:
				print('Finding Friend Failed')
				friend_user = None

			if friend_user != None:
				friend = Friend(username=friend_user.username, user=user)
				friend.save()
				user.save()
		
		return
			
