class authenthication(object):
	def __init__(self, name, email, member):
		self.name = name
		self.email = email
		self.__member = "member_private"

	def authenthicate(self):
		print("authenthicating...")
		print(self.__member)

class login(authenthication):
	def __init__(self, name, email, age):
		self.log_name = name
		self.log_email = email
		self.log_age = age
		super().__init__("auth_name", "auth_email", "this this")

	def displayinfo(self):
		print('name: ', self.name)

		


if __name__ == "__main__":
	usr = login('man', 'man@gmail.com', 12)
	usr.displayinfo()
	usr.authenthicate()
	print("var usr.name ==> ", usr.name, "usr.log_name --> ", usr.log_name)
	print("var usr.email ==> ", usr.email, "usr.log_email --> ", usr.log_email)

	Auth = authenthication('mostafa_auth', 'mostafa99@gmail.com_auth', "mostafa_private_auth")



