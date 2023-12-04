import time




class starter:
	def __init__(self):
		pass

	def introduce_player(self):
		return """
		get up in bed..
		weather is cold...
		you can't see anything due to the dark room you woke up in...
		(you are at the buttom of your room)
		"""

	
	def commnads_str(self):
		return """
			command you can use :
				commands 	your_decition 								explenation

				go 			N(North), E(East), W(west), S(South)		type go + e.g. (N) to go to the North at where you are
				get 		[things]									type get + whatever you find as stuff to have it
				talk 		[people]									type talk + eneyone you see to get his/her opition or help
				use  		[things]									get use + that stuff to use it
				look 		[]											just type look to search in that specific place
				read 		[papers]									read pappers
				unlock 		[the password you got]						unlock locks


		"""


	def get_command(self, command): # analyz_command
		pass

	def decide(): # decides to what answer it has to take 

	def send_to() # sends the player to a room base on the command
	  	pass 



class Map:

	def __init__(self):
		pass

	def black_room(self):
		# black room directions
		black_room_direc = {
			'starter':"dark empty room with a cold bed you chained on!",
			'N':"black NORTH",
			'S':"black SOUTH",
			'E':"black EAST",
			'W':"black WEST"
		}
		return black_room_direc

	def room2(self, pa):
		room2_direc = {
			'starter':"there are 10 doors in front of you",
			'N':"",
			'S':"",
			'E':"",
			'W':""
		}
		return room2_direc

	def cafe(self):
		cafe_direc= {
		 	'starter':"cafe is full of strainge people who doesnt look like a normal human except one who is the owner of the cafe",
		    'N':"",
			'S':"",
			'E':"",
			'W':""
		}
		return cafe_direc

	def clock_room(self):
		clock_room_direc = {
		 	'starter':"there is clock on every where you look. each of them are showing you a different time!!",
		    'N':"clock NORTH",
			'S':"clock SOUTH",
			'E':"clock EAST",
			'W':"clock WEST"
		}
		return clock_room_direc

	def laboratory(self):
		laboratry_direc = {
		 	'starter':"there are two dead people on the ground. everywhere is foggy. you smell sth like a wierd strainge gass. its making you sick.",
		    'N':"",
			'S':"",
			'E':"",
			'W':""
		}
		return laboratry_direc

	def crime_scene_room(self):
		crime_scene_room_direc = {
		 	'starter':" its like you are entering to a wooden house.. you can see any kind of killing equipment such gun, kinfe, (tab here to see all)... you notice that there is a bloody eye looking at you every where you going on the wall, also three hanged girls and a little boy bleeding on the ground.",
			'N':"",
			'S':"",
			'E':"",
			'W':""
		}
		return crime_scene_room_direc


 
def function():
	pass

class player(underground_building):
	
	def __init__(self, bag, score, current_room):
		self.bag = bag # list containing abjects in it
		self.score = score
		self.current_room = current_room
		
		self.handle_story = {
			'starter':self.black_room,
			'room2':self.cafe,
			'clock_room':self.clock_room,
			'laboratory':self.laboratory,
			'crime_scene_room':self.crime_scene_room
		}
		


	def go(self, place, direc='starter'):
		ddestin_func = self.handle_story[place] # find the related function
		story_dic = destin_func() # execute the related room story function and store whole story in 'story dic'
		self.current_room= place # change the place you are 
		return story_dic[direc] # return the specific part of room's story

	def get(self, stuff):
		pass

	def drop(self, stuff):
		pass

	def use(self, stuff):
		pass

	def read(self, paper):
		pass

	def explain_situation(self, place):
		pass

	def talk(self, character):
		pass

	def unlock(self, obj):
		pass

	def get_help(self, place):
		pass

	def commands(self):
		commands_explained = """
		command  |  followed_by  |  color				 

		go 			place			GREEN	
		get 		stuff			RED
		drop 		stuff			RED
		use 		stuff			RED
		read		paper			YELLOW
		explain 	  _ 			  _ 
		talk 		character		BLUE
		unlock 		obj				PURPLE
		get_help      _ 			  _

		"""
		print(commands_explained)





def write_story(self, story):
	for ch in story:
		print(ch)
		sleep(0.1)





if __name__ == "__main__":
	mmd = player([], 0, 'black_room')
	print(mmd.go('clock_room', 'starter'))

	# if __name__ == "__main__":
ddf





















