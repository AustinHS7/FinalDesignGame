# Import necessary modules
import sys #allows for our game to "quit" itself when asked using sys.exit.
import time #allows for delays between text so text prints at a readable pace.
import random #allows for random number generation to change the outcome of things in our game.

BLINK = "\033[5m"
END = "\033[0m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"
YELLOW = "\033[93m"
#ansi codes to improve the aesthetic of our game.

# Lists for user inputs
yeslist = ["yes", "y", "ye", "yea", "yeah"]
nolist = ["no", "n", "na", "nah"]
consumelist = ["consume", "devour", "ingest", "eat", "drink", "slurp", "sip", "guzzle"]
looklist = ["check", "look", "glance", "gaze"]
northlist = ["north", "n", "go north"]
westlist = ["west", "w", "go west"]
eastlist = ["east", "e", "go east"]
southlist = ["south", "s", "go south"]
printlist = ["list", "print", "recite", "check"]
openlist = ["open", "unlock",]
#Define/initialize variables
inventory = []
health = 100
wall_hit_counter = 0
door_broken = False
#Check if the player's health is zero
if health == 0:
	print("Your strength wanes and your vision darkens. Your journey has come to an end.")
	print("The world fades into oblivion. Your adventure is over, but your legacy lives on.")
	print(BOLD + "Game over." + END)
	time.sleep(10)
	sys.exit()
#Opening dialogue
Unconscious = " " + BLINK + "*shake* *shake* " + END + " Hey... "
Start = "I was just wandering around in this " + RED + "dungeon" + END + " and I found you asleep out here!"
#Get user ready to start the game
user_ready = input("Enter 'ready' to start GridQuest: \n")
if user_ready == 'ready':
    print("" + BOLD + "Starting" + BLINK + "..." + END + "\n")
    time.sleep(3)
    print(Unconscious)
    time.sleep(2)
    print(Start)
    time.sleep(2)
else:
    sys.exit("You weren't ready to begin the game.")
#Ask if the player is okay (Gives two paths for the player, one with extra damage but less health restoration and one with less damage but more safety)
user_input1 = input("Are you okay? \n")

#Checks user response and update inventory and health accordingly
if user_input1 == "quit": #If user wants to quit, exit game
        print("You decided to end your adventure. Goodbye!")
        sys.exit()
elif user_input1.lower() in yeslist:
    print("Okay, great! We need to get out of here, it's not safe. Take this wand!")
    time.sleep(2)
    print("" + DIM + "You got, an " + BLINK + "old dusty wand! " + END + "")
    inventory.append("wand")
    health = 90
    time.sleep(2)
    print(f"You have {health} " + RED + "health " + END + "")

elif user_input1.lower() in nolist:
    print("Here, take some health potions.")
    time.sleep(2)
    print("" + DIM + "You got, two "+BLINK+"health potions"+END+"")
    inventory.append("potion")
    inventory.append("potion")
    health = 30
    time.sleep(2)
    print(f"Be careful, you only have {health} " + RED + "health " + END + "")

else:
    print("I can't even understand what you're saying, take some health potions.")
    time.sleep(2)
    print("" + DIM + "You got, two "+BLINK+"health potions"+END+"")
    inventory.append("potion")
    inventory.append("potion")
    health = 30
    time.sleep(2)
    print(f"Be careful, you only have {health} " + RED + "health " + END + "")

# Main game loop + first user input oppurtunity 
while True:
    print("The mysterious person goes North.")
    input2 = input("What do you do?\n")

    #Converts the user input to lowercase for case-insensitivity
    user_input2 = input2.lower()

    if user_input2 == "quit": #Line 54
        print("You decided to end your adventure. Goodbye!")
        sys.exit()

    elif user_input2 in looklist: #checks if user input has key words in the looklist to check the action needed to do
        print("You look around the room, a large hole looms far overhead. Wow! Did you really fall "+ BOLD +"that"+ END +" far? Luckily, this bed of "+YELLOW+"flowers"+END+" must have broken your fall.")
        time.sleep(1)

    elif user_input2 in consumelist: #checks if user input has key words in the consume to check the action needed to do
        print("You try to consume the mysterious person, but they slip farther north.")
        time.sleep(1)

    elif any(action in user_input2 for action in consumelist) and "potion" in inventory and "potion" in user_input2: # Check if the user input contains any action word related to consumption, and if the potion is in the player's inventory and mentioned in the input
        print("You drank the bright " + RED + "red " + END + "potion. You feel yourself getting stronger.") # Display a message indicating the player drank a red potion and gained strength
        inventory.remove("potion") #removes the potion after drinking it
        health += 60 #Grants the health from the potion
        print(f"You now have {health} " + RED + "health " + END + ".") #displays the new amount of health of the user
        time.sleep(1) 

    elif any(action in user_input2 for action in consumelist) and "wand" in inventory and "wand" in user_input2: # Check if the user input contains any action word related to consumption, and if the wand is in the player's inventory and mentioned in the input
        print("You try shoving your newly gained wand into your throat. Sadly, You swallow it whole. Maybe get checked out for that. ") # Display a funny message about attempting to consume the wand
        inventory.remove("wand") #Remove the eaten wand

    elif any(action in user_input2 for action in printlist) and "inventory" in user_input2: #Checks if the user input has an action word related to printing and if the word inventory is in the input as well.
        print("You check your inventory:") #prints what's in the inventory
    
        if not inventory: #If nothing is inside of the player's inventory
            print("You have nothing in your bag") 

        else:
            print(inventory) #prints all items in the inventory

    elif any(action in user_input2 for action in printlist) and "health" in user_input2:  #Checks if the user input has an action word related to printing and if the word health is in the input as well.
        print(f"Your current health is: {health}") #prints how much health the user has.

    elif user_input2 in northlist: #if the user input has words involved in going north
        time.sleep(1)
        print("You go follow the mysterious man; he leads you to a room. In front of you stands a giant door, 10 times the size of you.") #continues the game to the next "screen"
        time.sleep(1)
        break # Continues the game

   # Check if the user input corresponds to movement commands in the west, east, or south direction
    elif user_input2 in westlist or user_input2 in eastlist or user_input2 in southlist: 
    # Display a message indicating the player hit a wall
        print("You hit a wall hard.")
    # Increment the wall_hit_counter to keep track of the number of times the player hits a wall
        wall_hit_counter += 1
    # Check if the player has hit the wall three times
        if wall_hit_counter == 3:
        # If so, deduct 5 health points from the player
            health -= 5
            print("Ouch! You lost 5 health for hitting the wall too hard.")
            print(f"You now have {health} " + RED + "health " + END + ".")
        else: #if the user input is not any of the above approved inputs.
            print("You stand there, unsure of what to do.") #prints and restarts the loop


print ("He points to you. ") #Transition dialogue
time.sleep(1)
print ("Seems like he's waiting for you to do something") #implies the user has to do something to continue



while True:
    
    input3 = input("What do you want to do?\n")
    
    user_input3 = input3.lower()  # Convert the user input to lowercase for case-insensitivity

    if user_input3 == "quit": #line 54
        print("You decided to end your adventure. Goodbye!")
        sys.exit()

    elif user_input3 in looklist: # Check if the user wants to look around the room
        print("You look around the room, the large door looms close. You hear noises through the door." )
        time.sleep(1)
   
    elif any(action in user_input3 for action in printlist) and "inventory" in user_input3:  # Check if the user wants to print/check their inventory
        print("You check your inventory:")
    
        if not inventory: #Display the contents of the inventory or notify the player if it's empty
            print("You have nothing in your bag")

        else:
            print(inventory)

    elif any(action in user_input3 for action in printlist) and "health" in user_input3: #Checks if the user input has an action word related to printing and if the word health is in the input as well.
        print(f"Your current health is: {health}") #prints user health
    
    elif any(action in user_input3 for action in consumelist) and "door" in user_input3: # Check if the user is attempting to consume and has a door it in their input
        print("You eat through the wood and steel door.")
        time.sleep(1)
        print("It worked?")
        time.sleep(1)
        print("Don't eat things that aren't supposed to be eaten.")

        door_broken = True # Set the door_broken flag to True, indicating that the door has been successfully broken
        break # Exit the while loop, as the door has been "opened"

    elif any(action in user_input3 for action in consumelist): # Check if the user is attempting an action related to consuming
        print("The man dodges your attempt.")
        time.sleep(1)
        print("\"Open the door.\" the figure says.")

    elif any(action in user_input3 for action in openlist) and "door" in user_input3: # Check if the user is attempting to open a "door" and has it in their open list
        print("The door moves easily at your touch.")
        break # Exit the while loop, as the user has successfully opened the door

    elif any(action in user_input2 for action in consumelist) and "potion" in inventory and "potion" in user_input2: # Check if the user input contains any action word related to consumption, and if the potion is in the player's inventory and mentioned in the input
        print("You drank the bright " + RED + "red " + END + "potion. You feel yourself getting stronger.") # Display a message indicating the player drank a red potion and gained strength
        inventory.remove("potion") #removes the potion after drinking it
        health += 60 #Grants the health from the potion
        print(f"You now have {health} " + RED + "health " + END + ".") #displays the new amount of health of the user
        time.sleep(1) 

    elif any(action in user_input2 for action in consumelist) and "wand" in inventory and "wand" in user_input2: # Check if the user input contains any action word related to consumption, and if the wand is in the player's inventory and mentioned in the input
        print("You try shoving your newly gained wand into your throat. Sadly, You swallow it whole. Maybe get checked out for that. ") # Display a funny message about attempting to consume the wand
        inventory.remove("wand") #Remove the eaten wand
    
    elif user_input3 in westlist or user_input3 in eastlist or user_input3 in southlist or user_input3 in northlist: #If user attempts to leave the area, game forces them to stay
        print("You have to open this door somehow...")
    
    else:
        print("The mysterious figure sighs and taps his wrist.") #restarts the list

if door_broken == True: #If the door was broken, change the dialogue to reflect that.
    print ("You push through the remains of the door.")
else:
    print ("You walk in between the two doors.")
time.sleep(1)
print ("As you step in through the room, you see a circular platform.")
time.sleep(1)
print ("In the middle of it, a giant slime monster stands.")
time.sleep(1)
print ("\"I've been looking for someone to help me with this.\" Your new companion says.")
time.sleep(1)

while True: #starts another loop to ask whether the user needs a tutorial
    input4 = input("\"Do you want me to teach you how to battle this creature?\"\n") #Asks about the tutorial
        
    user_input4 = input4.lower() # Convert the user input to lowercase for case-insensitivity

    if any(action in user_input4 for action in yeslist): # Check if any word in user_input4 is in the yeslist
        # Positive response from the user
        print("\"Okay!\"")
        time.sleep(1)
        print("\"If you didn't know, magic in this world comes from a special source, Knowledge!\"")
        time.sleep(1)
        print("\"If someone like you answers a question from an esteemed wizard like me, you can channel your energy into power!")
        time.sleep(1)
        if "wand" in inventory:  # Check if the user has a wand in their inventory
            print("\"I see you still have the wand I gave you!\"")
            time.sleep(1)
            print("\"Tools like that can help focus your energy even more!\"")
            time.sleep(1)
            print("\"Now let's get started\"")
            # Exit the loop, as the wizard is ready to start
            break
        else:
            print("\"Now let's get started!\"")
            # Exit the loop, as the wizard is ready to start
            break

            
    
    elif any(action in user_input4 for action in nolist): # Check if any word in user_input4 is in the nolist
        # Negative response from the user
        time.sleep(1)
        print ("\"Okay! Lets start this!\"")
        break # Exit the loop, as the wizard is ready to start



def trivia_question(): # Function to ask a trivia question during the boss battle
    global energy  # Declare energy as a global variable to modify its value

    questions = [ #provides a huge list of trivia questions for the user to answer
        {
            'question': 'Which big cat is the largest?',
            'options': ['a) Lion', 'b) Tiger', 'c) Jaguar', 'd) Leopard'],
            'correct_answer': 'b'
        },
        {
            'question': 'Which is the largest planet in the solar system?',
            'options': ['a) Earth', 'b) Mars', 'c) Jupiter', 'd) Saturn'],
            'correct_answer': 'c'
        },
        {
            'question': 'In which city did the Olympic games originate?',
            'options': ['a) Rome, Italy', 'b) Athens, Greece', 'c) London, UK', 'd) Beijing, China'],
            'correct_answer': 'b'
        },
        {
            'question': 'How many Olympic rings are there?',
            'options': ['a) Four', 'b) Five', 'c) Six', 'd) Seven'],
            'correct_answer': 'b'
        },
        {
            'question': 'What is the fastest aquatic animal?',
            'options': ['a) Dolphin', 'b) Shark', 'c) The Sailfish', 'd) Swordfish'],
            'correct_answer': 'c'
        },
        {
            'question': 'Are worker bees male or female?',
            'options': ['a) Male', 'b) Female'],
            'correct_answer': 'b'
        },
        {
            'question': 'How many Earths can fit inside the sun?',
            'options': ['a) 100,000', 'b) 500,000', 'c) 1 Million', 'd) 1.3 Million'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which color is an emerald?',
            'options': ['a) Red', 'b) Blue', 'c) Green', 'd) Yellow'],
            'correct_answer': 'c'
        },
        {
            'question': 'Whose nose grew longer every time he lied?',
            'options': ['a) Mickey Mouse', 'b) Pinocchio', 'c) Cinderella', 'd) Donald Duck'],
            'correct_answer': 'b'
        },
        {
            'question': 'Which US state is famous for Hollywood?',
            'options': ['a) New York', 'b) Florida', 'c) Texas', 'd) California'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which type of fish is Nemo?',
            'options': ['a) Goldfish', 'b) Clownfish', 'c) Salmon', 'd) Trout'],
            'correct_answer': 'b'
        },
        {
            'question': 'Where is the Great Pyramid of Giza located?',
            'options': ['a) Iraq', 'b) India', 'c) Egypt', 'd) Mexico'],
            'correct_answer': 'c'
        },
        {
            'question': 'What do bees consume to make honey?',
            'options': ['a) Water', 'b) Nectar', 'c) Pollen', 'd) Tree Sap'],
            'correct_answer': 'b'
        },
        {
            'question': 'Which dinosaur had 15 horns?',
            'options': ['a) Triceratops', 'b) Tyrannosaurus Rex', 'c) Stegosaurus', 'd) Kosmoceratops'],
            'correct_answer': 'd'
        },
        {
            'question': 'How many legs does a lobster have?',
            'options': ['a) Eight', 'b) Ten', 'c) Twelve', 'd) Sixteen'],
            'correct_answer': 'b'
        },
        {
            'question': 'What colors are the spots on a common ladybug?',
            'options': ['a) Red', 'b) Black', 'c) Yellow', 'd) Green'],
            'correct_answer': 'b'
        },
        {
            'question': 'How many teeth does an adult human have?',
            'options': ['a) 28', 'b) 30', 'c) 32', 'd) 36'],
            'correct_answer': 'c'
        },
        {
            'question': 'How many animals are there in the periodic table?',
            'options': ['a) 92', 'b) 108', 'c) 118', 'd) 128'],
            'correct_answer': 'c'
        },
        {
            'question': 'Which is the world’s largest ocean?',
            'options': ['a) Atlantic Ocean', 'b) Indian Ocean', 'c) Southern Ocean', 'd) Pacific Ocean'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which is the largest internal organ in the human body?',
            'options': ['a) Heart', 'b) Lungs', 'c) Liver', 'd) Kidneys'],
            'correct_answer': 'c'
        },
        {
            'question': 'What is the group of stars called that forms an imaginary picture?',
            'options': ['a) Galaxy', 'b) Nebula', 'c) Constellation', 'd) Comet'],
            'correct_answer': 'c'
        },
        {
            'question': 'How much is the diameter of a basketball hoop?',
            'options': ['a) 12 inches', 'b) 15 inches', 'c) 18 inches', 'd) 20 inches'],
            'correct_answer': 'c'
        },
        {
            'question': 'What serves as the base for guacamole?',
            'options': ['a) Tomato', 'b) Avocado', 'c) Onion', 'd) Pepper'],
            'correct_answer': 'b'
        },
        {
            'question': 'Which company is the largest chocolate manufacturer in the United States?',
            'options': ['a) Nestle', 'b) Cadbury', 'c) Lindt', 'd) Hershey’s'],
            'correct_answer': 'd'
        },
        {
            'question': 'What do bees produce?',
            'options': ['a) Jam', 'b) Jelly', 'c) Honey', 'd) Syrup'],
            'correct_answer': 'c'
        },
        {
            'question': 'Who wrote Romeo and Juliet?',
            'options': ['a) Charles Dickens', 'b) Jane Austen', 'c) William Shakespeare', 'd) Mark Twain'],
            'correct_answer': 'c'
        },
        {
            'question': 'What is the name of Harry Potter’s pet owl?',
            'options': ['a) Hedwig', 'b) Errol', 'c) Crookshanks', 'd) Fawkes'],
            'correct_answer': 'a'
        },
        {
            'question': 'How many colors are there in a rainbow?',
            'options': ['a) Five', 'b) Six', 'c) Seven', 'd) Eight'],
            'correct_answer': 'c'
        },
        {
            'question': 'Name the largest state in America.',
            'options': ['a) Texas', 'b) California', 'c) Alaska', 'd) New York'],
            'correct_answer': 'c'
        },
        {
            'question': 'Which planet is known to have the most gravity?',
            'options': ['a) Earth', 'b) Mars', 'c) Saturn', 'd) Jupiter'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which is the chemical name for common salt?',
            'options': ['a) Sodium Nitrate', 'b) Sodium Sulfate', 'c) Sodium Chloride (NaCl)', 'd) Sodium Carbonate'],
            'correct_answer': 'c'
        },
        {
            'question': 'Which was the first country to use paper money?',
            'options': ['a) England', 'b) China', 'c) India', 'd) USA'],
            'correct_answer': 'b'
        },
        {
            'question': 'Which is the fastest flying bird in the world?',
            'options': ['a) Eagle', 'b) Peregrine Falcon', 'c) Albatross', 'd) Hummingbird'],
            'correct_answer': 'b'
        },
        {
            'question': 'What is the princess’s name in Princess and the Frog?',
            'options': ['a) Ariel', 'b) Cinderella', 'c) Tiana', 'd) Elsa'],
            'correct_answer': 'c'
        },
        {
            'question': 'Who was the first Disney princess?',
            'options': ['a) Snow White', 'b) Cinderella', 'c) Aurora', 'd) Belle'],
            'correct_answer': 'a'
        },
        {
            'question': 'Which is the closest star to Earth?',
            'options': ['a) Proxima Centauri', 'b) Betelgeuse', 'c) The Sun', 'd) Alpha Centauri'],
            'correct_answer': 'c'
        },
        {
            'question': 'Who invented the telephone?',
            'options': ['a) Thomas Edison', 'b) Nikola Tesla', 'c) Alexander Graham Bell', 'd) Guglielmo Marconi'],
            'correct_answer': 'c'
        },
        {
            'question': 'From which country did the Statue of Liberty come from?',
            'options': ['a) England', 'b) Spain', 'c) Italy', 'd) France'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which is the largest continent?',
            'options': ['a) North America', 'b) Europe', 'c) Africa', 'd) Asia'],
            'correct_answer': 'd'
        },
        {
            'question': 'How many Great Lakes are there?',
            'options': ['a) Four', 'b) Six', 'c) Seven', 'd) Five'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which school did Harry Potter attend?',
            'options': ['a) Ilvermorny', 'b) Durmstrang', 'c) Beauxbatons', 'd) Hogwarts'],
            'correct_answer': 'd'
        },
        {
            'question': 'Which animal is Baloo in the Jungle Book?',
            'options': ['a) Tiger', 'b) Panther', 'c) Bear', 'd) Monkey'],
            'correct_answer': 'c'
        },
        {
            'question': 'Which is the highest-grossing holiday movie of all time?',
            'options': ['a) Elf', 'b) The Polar Express', 'c) A Christmas Carol', 'd) Home Alone'],
            'correct_answer': 'd'
        },
        {
            'question': 'What is the name of the longest river in the world?',
            'options': ['a) Amazon', 'b) Nile', 'c) Yangtze', 'd) Mississippi'],
            'correct_answer': 'b'
        },
        {
            'question': 'What is a thermometer used for?',
            'options': ['a) Measuring Time', 'b) Measuring Temperature', 'c) Measuring Distance', 'd) Measuring Weight'],
            'correct_answer': 'b'
        },
        {
            'question': 'Where do you get sugar from?',
            'options': ['a) Sugar Beet', 'b) Sugar Maple', 'c) Sugarcane', 'd) Sugar Plum'],
            'correct_answer': 'c'
        },
        {
            'question': 'What is the fastest animal?',
            'options': ['a) Gazelle', 'b) Cheetah', 'c) Antelope', 'd) Kangaroo'],
            'correct_answer': 'b'
        },
        {
            'question': 'What will you get if you freeze water?',
            'options': ['a) Steam', 'b) Ice Cream', 'c) Ice', 'd) Water Vapor'],
            'correct_answer': 'c'
        },
        {
            'question': 'Where does the President of the United States reside?',
            'options': ['a) Capitol Hill', 'b) The Pentagon', 'c) The White House', 'd) Lincoln Memorial'],
            'correct_answer': 'c'
        },
        {
            'question': 'What is the color of the school bus?',
            'options': ['a) Red', 'b) Blue', 'c) Green', 'd) Yellow'],
            'correct_answer': 'd'
        },
    ]

    question = random.choice(questions) # Select a random question from the list
    print(question['question']) # Print the question and answer options
    for option in question['options']:
        print(option)
    
    battle_input1 = input("Choose the correct option (a, b, c, or d): ").lower()  # Get the player's input for the answer

    if battle_input1 == question['correct_answer']:     # Check if the answer is correct
        print("Correct! You gain 10 ability points.")
         # Increase the player's energy by 10
        energy + 10

    elif battle_input1 == "quit": #line 54
        print("You decided to end your adventure. Goodbye!")
        sys.exit()
    
    # If the answer is incorrect, the boss retaliates
    else:
        print("Incorrect! The boss retaliates.")
        print("The slime monster attacks with a gooey hug!")
        # Calculate the damage dealt by the boss
        damage = random.randint(1, 7)
        health -= damage
        # Print the damage taken by the player
        print(f"You take {damage} damage.")
        print(f"Your Health: {health}")
        return 0
# Function for the player's magic attack
def player_attack():
    global energy
    global boss_health

    print("You cast a charm on the slime monster!")
     # Check if the "wand" is in the player's inventory
    if "wand" in inventory:
        # If the wand is present, add an additional 2 damage
        wand_bonus_damage = 2
        print("Your enchanted wand adds extra magic power!")
    else:
        wand_bonus_damage = 0
    # Calculate the damage dealt by the player
    damage = random.randint(5, 15) + energy + wand_bonus_damage
    boss_health -= damage
    # Print the damage dealt to the boss
    print(f"The slime monster takes {damage} damage.")
    print(f"Slime Monster's Health: {boss_health}")

# Function for the boss's attack
def boss_attack():
    global health

    print("The slime monster attacks with a gooey hug!")
    # Calculate the damage dealt by the boss
    damage = random.randint(1, 7)
    health -= damage
    # Print the damage taken by the player
    print(f"You take {damage} damage.")
    print(f"Your Health: {health}")

# Boss Battle Loop
print("The giant slime monster challenges you to a battle!")
# Initialize boss health and player energy
boss_health = 100
energy = 0
# Main game loop for the boss battle
while boss_health > 0 and health > 0:
    print("1. Answer Trivia Question")
    print("2. Attack with Magic")

    choice = input("What do you want to do? (1 or 2): ")# Get the player's choice
    # Process the player's choice
    if choice == "1":
        trivia_question()
    elif choice == "2":
        # Check if the player has enough energy to cast a spell
        if energy >= 20:
            player_attack()
            boss_attack()
        else:
            print("You don't have enough ability points to cast a spell. Answer trivia questions to gain more!")
    else:
        print("Invalid choice. Choose again.")


# Game outcome
if boss_health <= 0:
    print("Congratulations! You defeated the giant slime monster and saved the day!")
    print("Congratulations on beating the game!")
    sys.exit()



