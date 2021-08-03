import random

chance = (0, 1, 2, 3, 4)

def showInstructions():
  #print a main menu and the commands
  print('''

ESCAPE FROM IKEA

========

You, an exhausted and overworked employee at IKEA, are desperate to leave work. 
Get to the elevator in the Food Court without getting caught.
Don't run into any of your fellow employees or even worse, your manager. They will ask you to complete tasks for them which delays your escape! If you do, make sure you have the correct tools ON HAND to solve their tasks.
Avoid kids at all costs. If you happen to run into them you will need to find something to entertain them with. Don't try to pull any sneaky moves on them either because some of their parents check up on their kids often and might condemn you, further delaying your escape.
When faced with anything that will delay your escape (employees, managers, or children), you may use the 'run' command to run past the obstacle (it does not remove the obstacle from the room). However, there is only a 40% chance of success if this command is used.
You will need your "keycard" to clock out, and you will need your car "keys" to drive home.
Good luck!


Commands:
  go [direction]
  get [item]
  run [direction]
  help (use this command to complete tasks given to you by other employees and the manager)
  subdue (use this command to calm the kids down)
  escape (use this command in the final room to escape the building)
  instructions (repeats instructions)
  commands (this will remind you of what other commands you are able to use)


Directions
  right
  left
  up
  down


Notes:
You are weary from a long day at work, so you are a bit disoriented and must find the staircases on your own.
You may also only carry up to 3 items at a time.

''')

def showStatus():
  #print the player's current status
  print('------------------------------------------------------')
  print()
  print('STATUS')
  print()
  print('You are in the ' + currentRoom)
  print()
  #print the current inventory
  print('Inventory : ' + str(inventory))
  print()
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see', rooms[currentRoom]['item'])
  print()
  print('------------------------------------------------------')

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            #Floor One: The Basement
            'Kitchen Ware' : { 
                  'right' : 'Lighting Section',
                  'item' : 'keys',
                },

            'Lighting Section' : {
                  'left' : 'Kitchen Ware',
                  'right' : 'Living Room Section',
                  'item' : 'hammer',
                },
            
            'Living Room Section' : {
                  'left' : 'Lighting Section',
                  'right' : 'Office Supplies Section',
                  'item' : 'employee',
                },
            'Office Supplies Section' : {
                  'left' : 'Living Room Section',
                  'right' : 'Plants Section',
                  'up' : 'Dining Room',
                },
            'Plants Section' : {
                  'left' : 'Office Supplies Section',
                  'item' : 'hammer',
                },
            #Floor Two: The Demos
            'Appliances Section' : {
                  'right' : 'Smaland Section',
                  'item' : 'wrench',
                },
            'Smaland Section' : {
                  'left' : 'Appliances Section',
                  'right' : 'Bathroom Section',
                  'item' : 'kids',
                },
            'Bathroom Section' : {
                  'left' : 'Smaland Section',
                  'right' : 'Dining Room',
                  'up' : 'Check Out Area',
                },
            'Dining Room' : {
                  'left' : 'Bathroom Section',
                  'right' : 'Bedroom Section',
                  'down' : 'Office Supplies Section',
                  'item' : 'hammer',
                },
            'Bedroom Section' : {
                  'left' : 'Dining Room',
                  'item' : 'toy',
                },
            #Floor Three: Check Out
            'Employee Lounge' : {
                  'right' : 'Return Area',
                  'item' : ['keycard', 'toy'],
                },
            'Return Area' : {
                  'left' : 'Employee Lounge',
                  'right' : 'Check Out Area',
                  'item' : 'manager',
                },
            'Check Out Area' : {
                  'left' : 'Return Area',
                  'right' : 'Managers Office',
                  'down' : 'Bathroom Section',
                  'item' : 'employee',
                },
            'Managers Office' : {
                  'left' : 'Check Out Area',
                  'right' : 'Food Court',
                  'item' : 'kids',
                },
            'Food Court' : {
                  'left' : 'Managers Office',
                  'item' : 'elevator',
                },
         }

#start the player in the Lighting Section
currentRoom = 'Lighting Section'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      if move[0] == 'go' and 'item' in rooms[currentRoom] and 'employee' in rooms[currentRoom]['item']:
        print('They called the manager on you, and now you\'re stuck at work ... RESTART THE GAME')
        break
      if move[0] == 'go' and 'item' in rooms[currentRoom] and 'kids' in rooms[currentRoom]['item']:
        print('The parents called the manager on you, and now you\'re stuck at work ... RESTART THE GAME')
        break
      if move[0] == 'go' and 'item' in rooms[currentRoom] and 'manager' in rooms[currentRoom]['item']:
        print('They threaten to fire you if you leave, and now you\'re stuck at work ... RESTART THE GAME')
        break
      if move[1] == 'go' and 'item' in rooms[currentRoom] and 'elevator' in rooms[currentRoom]['item']:
        print('Your manager sees you trying to leave and calls you over to do more work. You\'re stuck at work ... RESTART')
        break 
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #when user uses the 'run' command to avoid enemies
  if move[0] == 'run' and 'item' in rooms[currentRoom] and 'employee' in rooms[currentRoom]['item']:
    skip = random.choice(chance)
    if skip <= 1:
      print('You ran past the employee without them identifying who you were.')  
    if skip > 1:
      print('The employee called the manager on you! ... RESTART THE GAME')
      break
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]

  if move[0] == 'run' and 'item' in rooms[currentRoom] and 'kids' in rooms[currentRoom]['item']:
    skip = random.choice(chance)
    if skip <= 1:
      print('You ran past the kids without the parents seeing you.')  
    if skip > 1:
      print('One of the parents saw you ditch the scene and called the manager on you! ... RESTART THE GAME')
      break
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]

  if move[0] == 'run' and 'item' in rooms[currentRoom] and 'manager' in rooms[currentRoom]['item']:
    skip = random.choice(chance)
    if skip <= 1:
      print('You ran out of the room before your manager identified who you were.')     
    if skip > 1:
      print('Your manager catches up to you and threatens to fire you! You have to stay back to talk to your manager ... RESTART THE GAME')
      break
    if move[1] in rooms[currentRoom]:
      currentRoom = rooms[currentRoom][move[1]]



      
  #if they type 'get' first
  if move[0] == 'get' :

    #blocks user from holding more than 3 items
    if len(inventory) == 3:
      print('You can\'t hold more than 3 items at once')
      
    #if the room contains an item, and the item is the one they want to get
    elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and type(rooms[currentRoom]['item']) == str:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
      
    #otherwise, if the item isn't there to get
    elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and type(rooms[currentRoom]['item']) == list :
      inventory += [move[1]]
      print(move[1] + ' got!')
      rooms[currentRoom]['item'].remove(move[1])
    
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')


  #gives user a list of commands they can use
  if move[0] == 'commands':
    print('''
Commands:
  go [direction]
  get [item]
  run [direction]
  help (use this command to complete tasks given to you by other employees and the manager)
  subdue (use this command to calm the kids down)
  escape (use this command in the final room to escape the building)
  instructions (repeats instructions)
  commands (this will remind you of what other commands you are able to use)
    ''')

  #repeats instructions
  if move[0] == 'instructions':
    print('''
You, an exhausted overworked employee at IKEA, are desperate to leave work. 
Get to the elevator in the Food Court without getting caught.
Don't run into any of your fellow employees or even worse, your manager. They will ask you to complete tasks for them which delays your escape! If you do, make sure you have the correct tools ON HAND to solve their tasks.
Avoid kids at all costs, they will need you to entertain them. Don't try to pull any sneaky moves on them either because some of their parents check up on their kids often and might condemn you, further delaying your escape.
You will need your "keycard" to clock out, and you will need your car "keys" to drive home.
Good luck!
    ''')


  
  #Rooms with new employees
  if 'item' in rooms[currentRoom] and 'employee' in rooms[currentRoom]['item']:
    if move[0] == 'go':
      print('One of the newly hired staff members has spotted you and is now progressing towards you (probably to ask for your assistance).')

    elif move[0] == 'help' and 'hammer' in inventory :
      print('You fixed their problem!')
      #remove the item from their inventory
      inventory.remove ('hammer')
      #delete the item from the room
      del rooms[currentRoom]['item']
    elif move[0] == 'help' and 'hammer' not in inventory :
      print('You don\'t have the tool to fix their problem... You\'re stuck at work :( ... RESTART THE GAME')
      break
    

  #Rooms with  kids
  if 'item' in rooms[currentRoom] and 'kids' in rooms[currentRoom]['item']:
    if move[0] == 'go' :
      print('Screeching kids are running rampant throughout the room. You will need to "subdue" them with something that will entertain them. Do this quickly before their parents notice!')
    
    if move[0] == 'subdue' and 'toy' in inventory :
      print('You were able to calm the kids down.')
      #remove the item from their inventory
      inventory.remove ('toy')
      #delete the item from the room
      del rooms[currentRoom]['item']
    elif move[0] == 'subdue' and 'toy' not in inventory :
      print('You don\'t have anything to subdue them with ... You must act as a form of entertainment so you must stay at work :( ... RESTART THE GAME')
      break


  #Return Area
  if 'item' in rooms[currentRoom] and 'manager' in rooms[currentRoom]['item']:
    if move[0] == 'go' :
      print('You see one of your managers with a badly half-built shelving unit. You make eye contact and immediately regret walking into the room. She angrily marches towards you (probably to ask if you can build it for her). To do this you will need a wrench and a hammer')
    
    if move[0] == 'help' and 'hammer' in inventory and 'wrench' in inventory :
      print('You were able to rebuild the unit.')
      #remove the item from their inventory
      inventory.remove ('hammer')
      inventory.remove ('wrench')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #player loses if
    elif move[0] == 'help' and 'hammer' not in inventory and 'wrench' not in inventory :
      print('You don\'t have enough tools to fix the unit... You\'re stuck at work :( ... RESTART THE GAME')
      break
    elif move[0] == 'help' and 'hammer' not in inventory and 'wrench' in inventory :
      print('You don\'t have enough tools to fix the unit... You\'re stuck at work :( ... RESTART THE GAME')
      break
    elif move[0] == 'help' and 'hammer' in inventory and 'wrench' not in inventory :
      print('You don\'t have enough tools to fix the unit... You\'re stuck at work :( ... RESTART THE GAME')
      break

  #Food Court
  if 'item' in rooms[currentRoom] and 'elevator' in rooms[currentRoom]['item']:
    if move[0] == 'go' :
      print('You see the elevator. This is your chance to escape the building. All you need is your "keys" to the car and your "keycard" to clock out of the building. However, you can hear your manager coming down the hall, so you must act quickly! ')
    #player wins if
    if move[0] == 'escape' and 'keycard' in inventory and 'keys' in inventory :
      print('You were able to leave the building and drive home safely. YOU ESCAPED, CONGRATS!!')
      break
      #remove the item from their inventory
      inventory.remove ('keycard')
      inventory.remove ('keys')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #player loses if
    elif move[0] == 'escape' and 'keycard' not in inventory and 'keys' not in inventory :
      print('You don\'t have the necessary items to leave the premises... You\'re stuck at work :( ... RESTART THE GAME')
      break
    elif move[0] == 'escape' and 'keycard' not in inventory and 'keys' in inventory :
      print('You don\'t have the necessary items to leave the building... You\'re stuck at work :( ... RESTART THE GAME')
      break
    elif move[0] == 'escape' and 'keycard' in inventory and 'keys' not in inventory :
      print('You don\'t have the necessary items to leave the premises... You\'re stuck at work :( ... RESTART THE GAME')
      break

  
