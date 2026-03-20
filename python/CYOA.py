#CYOALonniePryor
# -- No Modules --

#Instructions
#Initialize Variables
count = 0
returns = True

#Output
def run():
    start_story()

# Fifth Functions
def winoregon():
    print("You have made it to Oregon! From here you know where you are and you are able to arrive home.\n\nYOU WIN")

def failure5minnesota():
    print("You have made it to Minnesota, which is the wrong direction from Oregon! From here you book a flight to arrive home.\n\nGAME OVER")

def jail():
    print("You arrive at a border crossing in Canada. You unknowingly cross the border and are arrested for illegal border crossing.\n\nGAME OVER")

def raise_cap():
    if count >= 5:
        print("You are so tired from driving so much that you get on a plane and go home. You fail.\n\nGAME OVER")
        returns = False
    count += 1

# Fourth Functions
def fargo4():
    raise_cap()
    if returns == False: 
        return
    print("You have made it to Fargo, North Dakota. You have another choice to make." \
    "\n\n1. Head West on I-94\n2. Head East on I-94")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        montana3()
    elif choice == 2:
        failure5minnesota()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        fargo4()
    
def sacramento4():
    raise_cap()
    if returns == False: 
        return
    print("You have made it to Sacramento, California. You have another choice to make." \
    "\n\n1. Head North on I-5\n2. Head East on I-80")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        winoregon()
    elif choice == 2:
        saltlake3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sacramento4()

def idaho4():
    raise_cap()
    if returns == False: 
        return
    print("You have made it to Idaho. You have another choice to make." \
    "\n\n1. Head West on I-84\n2. Head North on I-15")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        winoregon()
    elif choice == 2:
        montana3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        idaho4()
        
def seattle4():
    raise_cap()
    if returns == False: 
        return
    print("You have made it to Sacramento, California. You have another choice to make." \
    "\n\n1. Head South on I-5\n2. Head North on I-5")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        winoregon()
    elif choice == 2:
        jail()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        seattle4()

# Third Functions
def la3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Los Angeles, California. You have another choice to make." \
    "\n\n1. Head North on I-5\n2. Head North on I-15")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        sacramento4()
    elif choice == 2:
        saltlake3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        la3()

def saltlake3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Salt Lake City, Utah. You have another choice to make." \
    "\n\n1. Head North on I-15\n2. Head West on I-80")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        idaho4()
    elif choice == 2:
        sacramento4()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        saltlake3()

def montana3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Billings, Montana. You have another choice to make." \
    "\n\n1. Head West on I-90\n2. Head East on I-94")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        seattle4()
    elif choice == 2:
        fargo4()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        montana3()

def siouxfalls3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Sioux Falls, South Dakota. You have another choice to make." \
    "\n\n1. Head West on I-90\n2. Head North on I-29")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        montana3()
    elif choice == 2:
        fargo4()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        siouxfalls3()

def dallas3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Dallas, Texas. You have another choice to make." \
    "\n\n1. Head South on I-45\n2. Head West on I-20")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        houston3()
    elif choice == 2:
        texas3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        dallas3()

def houston3():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Houston, Texas. You have another choice to make." \
    "\n\n1. Head West on I-10\n2. Head East on I-10")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        texas3()
    elif choice == 2:
        failure3louisiana()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        houston3()

def texas3():
    raise_cap()
    if returns == False: 
        return
    print("You come across an interchange in the middle of nowhere. What do you do?" \
    "\n\n1. Head West on I-10\n2. Head East on I-20\n3. Head East on I-10")
    choice = int(input("Enter 1, 2 or 3: "))

    if choice == 1:
        la3()
    elif choice == 2:
        dallas3()
    elif choice == 3:
        houston3()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        texas3()

def failure3louisiana():
    print("You have made it to Louisiana, and you know at this point you are very far from Oregon. You find the nearest airport and fly home.\n\nGAME OVER")

# Second Functions
def cheyenne2():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Cheyenne, Wyoming. You have another choice to make." \
    "\n\n1. Head North on I-25\n2. Head West on I-80")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        saltlake3()
    elif choice == 2:
        montana3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        cheyenne2()

def albuquerque2():
    raise_cap()
    if returns == False: 
        return
    print("You are headed toward Albequerque, New Mexico. You have another choice to make." \
    "\n\n1. Head South on I-25\n2. Head West on I-40")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        texas3()
    elif choice == 2:
        la3()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        albuquerque2()

def omaha2():
    raise_cap()
    if returns == False: 
        return
    print("You are headed north toward Omaha, Nebraska. You have another choice to make." \
    "\n\n1. Continue on I-29 North\n2. Take the I-80 West ramp")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        siouxfalls3()
    elif choice == 2:
        cheyenne2()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        omaha2()

def oklahomacity2():
    raise_cap()
    if returns == False: 
        return
    print("You are headed south toward Oklahoma City, Oklahoma. You have another choice to make." \
    "\n\n1. Continue on I-35 South\n2. Take the I-40 West ramp")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        dallas3()
    elif choice == 2:
        albuquerque2()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        oklahomacity2()

# First Functions
def denver1():
    raise_cap()
    if returns == False: 
        return
    print("You are headed west toward Denver, Colorado. After a grueling 5 hour drive of nothing but plains, you have a choice to make." \
    "\n\n1. Take the I-25 North ramp\n2. Continue on I-70 West")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        cheyenne2()
    elif choice == 2:
        albuquerque2()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        denver1()

def kansascity1():
    raise_cap()
    if returns == False: 
        return
    print("You are headed east toward Kansas City. After 4 hours of driving through the plains, you come across many new highways, however you know that you are currently headed away from oregon." \
    "\n\n1. Take the I-29 North ramp\n2. Take the I-35 South ramp")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        omaha2()
    elif choice == 2:
        oklahomacity2()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        kansascity1()

#Loop
def start_story():
    print("\nYou find yourself on a highway in the middle of Kansas. You need to make it back to your home in Oregon, but you are unsure of how to get there. You have no GPS. Which direction do you go?" \
    "\n\n1. Continue staight\n2. Turn around")
    choice = int(input("Enter 1 or 2: "))
    
    if choice == 1:
        denver1()
    elif choice == 2:
        kansascity1()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        start_story()

#Output 2.0
run()
