# Simple Car Park

#implementing the class Queue


class Queue:
    def __init__(self):
        self.items = []
        
    def clear(self):
        self.items = []

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#creating two queues
cars=Queue()
back=Queue()
bakc=Queue()

#printing the welcome message and directions to input commands
print("\nWelcome to the Laughs Parking Garage!\n   --Enter-- \n'a license_plate_number' for arrival  \n'd license_plate_number' for departure \n'exit' to exit the program\n'n' to see the current number of vehicles in the garage\n              ***** Sizi Creations *****\n")

#creating a loop for continuous inputs 
while True:
	inp=raw_input(">>>")
	
	#exit command	
	if (inp=="exit"):
		exit()	
	
	#arriving of vehicles to the garage and printing whether the garage is full or not & arriving message
	elif (inp.lower()[:2]=="a "):		
		if (cars.size()>=10):
			print("\nThe Parking Garage is Full! Please wait..\n")
			z=inp[2:len(inp)]
		else:
			print("\nWelcome to the Parking Garage!")
			cars.enqueue(inp[2:len(inp)]+"0")
			print("Vehicle with License plate no."+inp[2:len(inp)]+" has been arrived to the Parking Garage..\n")

	#departing of vehicles from the garage and printing departing message
	elif (inp.lower()[:2]=="d "):
		l=cars.size()
		while (not cars.isEmpty()):
			x=cars.dequeue()
			if (inp[2:len(inp)]!=x[:len(x)-1]):
				back.enqueue(x[:len(x)-1]+str(int(x[len(x)-1:])+1))
				bakc.enqueue(x)
			else:
				print("\nVehicle with License plate no."+x[:len(x)-1]+" has been daparted from the Parking Garage..")
				print("Vehicle has moved "+x[len(x)-1:]+" times while in the queue!\n")

		#checking whether a vehicle with given license plate number is present in the garage
		if (back.size()==l):
			print("\nNO vehicle for License plate number "+inp[2:len(inp)]+" present in the Parking Garage.Please check your License plate number again!\n ")
			while (not bakc.isEmpty()):
			    cars.enqueue(bakc.dequeue())
			back.clear()
			continue

		#moving back vehicles after giving space to a vehicle in the queue
		while (not back.isEmpty()):
			cars.enqueue(back.dequeue())
		bakc.clear()
		
		#room available message
		if (cars.size()==9):
			print("\nVehicle with License plate no."+z+"\nThanks for waiting!\nNow you can enter the Parking Garage..\n")

	#checking the number of vehicles in the queue 
	elif (inp.lower()=="n"):
		print ("\nAt the moment, there are "+str(cars.size())+" vehicle(s) in the garage!\n")

	#view the northernmost vehicle
	elif (inp.lower()=="north"):
		print ("The northernmost vehicle's License plate number is "+cars.peek())
	
	#checking for wrong input commands	
	elif (inp==""):
		continue
	else:
		print("\nPlease enter the data/command in the correct format.\neg-: a WI0684\n")
		
		
	

