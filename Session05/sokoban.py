map = {
    "size_x": 5,
    "size_y": 5,
}

player = {"x": 3, "y": 4}

boxes = [
    {"x": 1, "y":1},
    {"x": 2, "y":2},
    {"x": 3, "y":3}
]

destinations = [
    {"x": 2, "y":1},
    {"x": 3, "y":2},
    {"x": 4, "y":3}
]

playing=True
while playing: 
########print map
    for y in range(map['size_y']):
        for x in range(map['size_x']):
            player_is_here=False
            if y == player['y'] and x == player['x']:
                player_is_here=True
            
            box_is_here = False
            for box in boxes:
                if y == box['y'] and x == box['x']:
                    box_is_here=True
            
            destination_is_here=False
            for destination in destinations: 
                if y == destination['y'] and x == destination['x']:
                    destination_is_here=True

            if player_is_here:
                print("P ", end=' ')
            elif box_is_here:
                print("B ", end=' ')
            elif destination_is_here:
                print("D ", end=' ')
            else: 
                print("- ", end=' ')

        print()
#################################end of print map
   ########## check win 
    win=True
    for box in boxes:
        if box not in destinations:
            win=False 
        
    if win:
        print("You win.")
        break
####### end of check win

#############move up and down    
    move = input("Your move: ").upper()
    dx=0
    dy=0
    if move =="W":
        dy =-1
        #print("Up")
    elif move =="S":
        dy =1
        #print("Down")
    elif move =="A":
        dx =-1
        #print("left")
    elif move == "D":
        dx =1
        #print("right")
    else: 
        playing=False

    if 0<=player['x']+dx <= map['size_x'] and \
    0<=player['y']+dy <= map ['size_y']:
        player['x'] +=dx
        player['y'] +=dy
########end of move up and down
    for box in boxes:
        if box['x'] == player['x'] and \
        box ['y'] == player ['y']:
            box['x'] += dx
            box['y'] += dy

    #copy/clone/deep clone

