#ICS201 CULMINATING PROJECT by Josef Gavronskiy
# goal is to win by either killing the opposing teams players, or destroying the vault
# each player on your team has 1 move and 1 attack per turn. Complete your turn by clicking end turn on the top left.
# you can move by dragging and dropping your player
# attack by hovering over your player and pressing "a", and then selecting a target
# hover over a player and hold "i" to view the players health and other stats.


# visual indicator - is displayed when a player is selected to attack or to move

#list of different player names 
# when you click the arrow keys the player displayed shifts one index
players = ["rifleman","assasin","warrior","grenadelauncher","machinegunner"]

#stores information about each player in the format 
#Name:[health,attackRadius,movementRadius,splashRadius,damage,imageAdress,if the player can attack while moving, image url that shows stats]
# the 7th index that represents whether the player can attack while moving was not implemented. I kept it in the information list in case
# i add it in a later version. Same goes with the 4th index that represents splash damage. 
playerInfoList = { 
    "rifleman" : [200,5,4,0,50,"https://drive.google.com/file/d/1pzpHb2ayH1f1QfqVWx3b2N-NJ7I5qDSM/view?usp=sharing",False,"https://drive.google.com/file/d/1-meT5Wvxk-i_XKp00CNSRlzZnt5n105-/view?usp=share_link","line"],
    "assasin" : [150,1,10,0,80,"https://liquipedia.net/commons/images/5/5c/Omen_Artwork.png",True,"https://drive.google.com/file/d/1G9q7sL5UaWFKaC0eVEBIhQnPT1zB-sk1/view?usp=share_link","line"], 
    "warrior" : [250,1,4,0,65,"https://static.wikia.nocookie.net/boombeach/images/b/b2/WarriorD.png/revision/latest?cb=20150803213842",False,"https://drive.google.com/file/d/1l4utpzpwuow3KtQBBBTUDc1xbkO1n8qx/view?usp=share_link","line"],
    "grenadelauncher" : [250,3,4,1,40,"https://static.wikia.nocookie.net/boombeach/images/c/c5/GrenadierB.png/revision/latest?cb=20150803213922",False,"https://drive.google.com/file/d/1UjfgHtZfoyAMudMej7pceQUBSKzcZWk3/view?usp=sharing","parabola"],
    "machinegunner" : [320,3,3,0,85,"https://static.wikia.nocookie.net/boombeach/images/1/1e/HeavyD.png/revision/latest?cb=20150803213729",False,"https://drive.google.com/file/d/1VFWQi7Y14fQx3SyWeHaEufdTdf1ztr-E/view?usp=sharing","line"]
    
}

# sets background
app.background = rgb(252,168,112)

# placeholder for image that shows the stats of a player. stats.img (holds the information image any selected player), set to None
stats = Rect(1,1,2,2,visible = False)
stats.img = None

# variable stores the coordinates of your mouse [x,y]
coordinates = [0,0]

# list that stores the keys that can be pressed to select your players
# the first sublist changes the first character when clicked, same with the second and 3rd. The 0th index of each sublist
# represents the left key while the 1st index represents the right key 
keysToSwitchCharacter = [
    [RegularPolygon(175,75,10,3,rotateAngle=90),
    RegularPolygon(25,75,10,3,rotateAngle=270)],
    
    [RegularPolygon(175,200,10,3,rotateAngle=90),
    RegularPolygon(25,200,10,3,rotateAngle=270)],
    
    [RegularPolygon(175,325,10,3,rotateAngle=90),
    RegularPolygon(25,325,10,3,rotateAngle=270)]
]

# stores the the same keys but in a group so they can be hittested
keysGroup = Group(keysToSwitchCharacter[0][0],keysToSwitchCharacter[0][1],keysToSwitchCharacter[1][0],keysToSwitchCharacter[1][1],keysToSwitchCharacter[2][0],keysToSwitchCharacter[2][1])

# the first rectangle that is placed underneath the first selected player 
p1bg = Rect(50,35,100,80, fill=rgb(236,157,111),rotateAngle=90)
p1bg.index = 0 # the index of the players [] list that represents the selected player
p1bg.img = None # displays the selected player
p1bg.name = None # the name of the selected player

p2bg = Rect(50,160,100,80, fill=rgb(236,157,111),rotateAngle=90)
p2bg.index = 0
p2bg.img = None
p2bg.name = None

p3bg = Rect(50,285,100,80, fill=rgb(236,157,111),rotateAngle=90)
p3bg.index = 0
p3bg.img = None
p3bg.name = None

# stores the 3 rectangles that are on the background of the selected players 
bg = [p1bg,p2bg,p3bg]
# same except in a group
bgGroup = Group(p1bg,p2bg,p3bg)

#title
title = Label("Wild West",290,50,size=30,font="cinzel",bold= True)

# starts the game when pressed
playButton = Image("https://drive.google.com/file/d/1W0lDOK_k49cCFfmLzAY5pEqdboY8W7qR/view?usp=sharing",0,0)
playButton.width =120
playButton.height = 60
playButton.centerX = 290
playButton.centerY = 140
playLabel = Label("PLAY",290,140,font="cinzel",bold = True,size=15)

#starts the tutorial 
tutorialButton = Image("https://drive.google.com/file/d/1W0lDOK_k49cCFfmLzAY5pEqdboY8W7qR/view?usp=sharing",0,0)
tutorialButton.width =120
tutorialButton.height = 60
tutorialButton.centerX = 290
tutorialButton.centerY = 220
tutorialLabel = Label("TUTORIAL",290,220,font="cinzel",bold = True,size=15)

# press to modify settings. Doesnt do anything yet. Can be implemented in a later version. 
settingsButton = Image("https://drive.google.com/file/d/1W0lDOK_k49cCFfmLzAY5pEqdboY8W7qR/view?usp=sharing",0,0)
settingsButton.width =120
settingsButton.height = 60
settingsButton.centerX = 290
settingsButton.centerY = 300
settingsLabel = Label("SETTINGS",290,300,font="cinzel",bold = True,size=15)

# group with all the buttons for play, tutorial and settings 
buttonLabels = Group(playLabel,tutorialLabel,settingsLabel)

# intructions for tutorial
instructions = Label("",290,365,fill="red",size=15)

# a placeholder for the game class. game.g stores the game class. 
game = Rect(1,1,2,2,visible = False)
game.g = None

def onMousePress(x,y):
    
    # checks if the game hasnt started yet
    if game.g == None:
        # checks if you press the play button. It also makes sure that you have selected 3 players.
        if playButton.hits(x,y) and p1bg.name != None and p2bg.name != None and p3bg.name != None:
            #creates the game from the Game() class. Passes the 3 player names as parameters.
            game.g = Game(p1bg.name,p2bg.name,p3bg.name)
        
        # i represents which player the key changes
        # k represents which key is pressed L/R
        for i in range(len(keysToSwitchCharacter)):
            for k in range(len(keysToSwitchCharacter[i])):
                if keysToSwitchCharacter[i][k].hits(x,y):
                    
                    # visual queue that the key is pressed
                    keysToSwitchCharacter[i][k].opacity = 0
                    sleep(0.01)
                    keysToSwitchCharacter[i][k].opacity = 100
                    
                    # if the left key is clicked
                    if k == 0:
                        # shifts the displayed player 1 right 
                        # ex: index = 1, machine gunner is displayed, index 2 riflemen would be displayed
                        # [assasin,machinegunner,riflemen]
                        bg[i].index += 1
                        
                    # if the right key is pressed
                    else:
                        bg[i].index -= 1
                    
                    # if the index is greater than four (the maximum index of the players[] list). set it to one.
                    if bg[i].index > 4:
                        bg[i].index = 0
                    # if the index is less than 0 (the minimum index of the players[] list). set it to four.
                    if bg[i].index < 0:
                        bg[i].index = 4
                        
                    # try and except ensures that the program wont break in the case that bg[i].img = None
                    try:    
                        # sets the image of the player to visible
                        bg[i].img.visible = False
                    except:
                        pass
                    
                    # sets the name of the rectangle to the name of the character that will be displayed ontop of it
                    bg[i].name = players[bg[i].index]
                    
                    # sets the image ontop of the rectangle to the image of the character
                    bg[i].img = Image(playerInfoList[bg[i].name][5],0,0)
                    
                    # sets the height and width and centers the image
                    bg[i].img.width = 60
                    bg[i].img.height = 80
                    bg[i].img.centerX = bg[i].centerX
                    bg[i].img.centerY = bg[i].centerY
                    
        # if you click on the tutorial button it tells you to check the project 
        if tutorialButton.hits(x,y):
            instructions.value = "Check project assignment for tutorial"
    
    # else makes sure that the game has already started
    else: 
        #makes sure you have selected one of your players to attack
        if game.g.playerSelectedToAttack != None: 
            #goes through the list of enemies and checks if you clicked on any of them
            for enemy in game.g.enemies:
                if enemy.shape.hits(x,y):
                    # checks if there is an unobstructed projectile path between you and your targeted enemy and then attacks the enemy
                    if game.g.playerSelectedToAttack.validProjectilePath == True:
                        game.g.playerSelectedToAttack.attack(enemy)
                        
                        # breaks in case you select 2 enemies at the same time. This is rare but would otherwise cause an error.
                        break
                    
                    # attacking an enemey when you have an obstructed path causes you to void your turn
                    else:
                        game.g.playerSelectedToAttack.clearProjectilePath()
                        game.g.playerSelectedToAttack.clearVisualIndicators()
                        game.g.playerSelectedToAttack.attackCompleted = True
                        game.g.playerSelectedToAttack = None
                            
            # checks if the entity that you are attacking is the vault and not an enemy
            if game.g.vault.shape.hits(x,y):
                game.g.playerSelectedToAttack.attack(game.g.vault)
                
        # clicking on the complete turn button will end your turn
        if game.g.completeTurnButton.hits(x,y):
            game.g.completeTurn()
    
def onMouseMove(x,y):
    # sets the coordinates variable to your current [x,y] position
    coordinates[0] = x
    coordinates[1] = y
    
    # checks which button you are hovering over (play,tutorial,settings)
    buttonHover = buttonLabels.hitTest(x,y)
    
    # checks which arrow key you are hovering over
    keyHover = keysGroup.hitTest(x,y)
    
    # if there is a button being hovered over. If so increase its size. 
    if buttonHover != None:
        buttonHover.size = 16.5
    
    # otherwise all buttons return to normal size
    else:
        for c in buttonLabels.children:
            c.size = 15
    
    # hovering over a key causes its radius to increase temporarily, and then go back to normal
    if keyHover != None:
        keyHover.radius = 12
    else:
        for c in keysGroup.children:
            c.radius = 10
    
    # easter egg makes the title turn rainbow when hovered over
    if title.hits(x,y):
        title.fill = rgb(randrange(255),randrange(255),randrange(255))
    else:
        title.fill = "black"
    
    # checks if the game has started
    if game.g != None:
        # goes through the players list. If you hover over your player its size increases. 
        for player in game.g.players:
            if player.shape.hits(x,y):
                player.shape.width = 34
                player.shape.height = 34
            else:
                player.shape.width = 30
                player.shape.height = 30
        
        # goes through each tile in the grid
        for row in game.g.grid.grid:
            for tile in row:
                # checks if you are hovering over the tile, if it is visible, and if you have selected a player to attack
                if tile.shape.hits(x,y) and tile.visitable == True and game.g.playerSelectedToAttack != None:
                    # checks if the tile is within the attacking range
                    isWithinRange = tile.x >= game.g.playerSelectedToAttack.tile.x - game.g.playerSelectedToAttack.rAttack and tile.y >= game.g.playerSelectedToAttack.tile.y - game.g.playerSelectedToAttack.rAttack and tile.x <= game.g.playerSelectedToAttack.tile.x + game.g.playerSelectedToAttack.rAttack and tile.y <= game.g.playerSelectedToAttack.tile.y + game.g.playerSelectedToAttack.rAttack
                    if isWithinRange == True:
                        # shows the path that the projectile would take if you confirmed your attack
                        game.g.playerSelectedToAttack.selectedTileIndicator.left = tile.shape.left
                        game.g.playerSelectedToAttack.selectedTileIndicator.top = tile.shape.top
                        game.g.playerSelectedToAttack.showProjectilePath(tile) 
                    else:
                        # if its out of range the selected player clears its visual indicators 
                        game.g.playerSelectedToAttack.clearVisualIndicators()
                        game.g.playerSelectedToAttack.clearProjectilePath() 
                        
                        # the selected player de-selects itself
                        game.g.playerSelectedToAttack = None
            

def onKeyHold(keys):
    if  "i" in keys:
        # makes sure that the game hasnt started
        if game.g == None:
            # represents which player preview is selected
            selected = bgGroup.hitTest(coordinates[0],coordinates[1])
            
            # checks if you selected a player preview, if that player preview was assigned a name. Makes sure there is no stats image.
            if selected != None and stats.img == None and selected.name != None:
                # loads an image with the stats/info about the player
                stats.img = Image(playerInfoList[selected.name][7],0,0)
                
                #sets the height and width and aligns the image.
                stats.img.width *= 0.5
                stats.img.height *= 0.5
                
                stats.img.top = selected.top
                stats.img.left = selected.right
                
                # creates a background for the image, to make the text visible
                stats.background = Rect(stats.img.left, stats.img.top ,stats.img.width - 10 ,stats.img.height -20 ,fill="white",opacity = 60, border = "black")
                
                # moves the stats image to the front
                stats.img.toFront()
        
        # checks if the game has started
        else:
            selectedPlayer = None
            
            # goes through all the players on the board
            for player in game.g.players:
                # if you are hovering over the player select it by setting it to selectedPlayer
                if player.shape.hits(coordinates[0],coordinates[1]):
                    selectedPlayer = player
            
            # checks if a player has been selected. Makes sure there is no stats image. 
            if selectedPlayer != None and stats.img == None:
                # sets the stats image to the image of the selected player
                stats.img = Image(playerInfoList[selectedPlayer.name][7],0,0)
                
                #sets the height and width and aligns the image.
                stats.img.width *= 0.25
                stats.img.height *= 0.25
                
                stats.img.top = selectedPlayer.shape.bottom
                stats.img.left = selectedPlayer.shape.right
                
                # creates a background for the image, to make the text visible
                stats.background = Rect(stats.img.left, stats.img.top ,stats.img.width - 5 ,stats.img.height - 10 ,fill="white",opacity = 60, border = "black",borderWidth = 0.5)
                
                # moves the stats image to the front
                stats.img.toFront()
                
                # displays the health percentage of the player on the healthbar on the sidebar
                game.g.healthBar.width = 60 * selectedPlayer.health / selectedPlayer.originalHealth
                
                # displays an image of the selected player on the sidebar
                game.g.preview = Image(playerInfoList[selectedPlayer.name][5],370,370)
                game.g.preview.width=80
                game.g.preview.height=80
                game.g.preview.centerX = 360
                game.g.preview.centerY=350
            
            
           
            
def onKeyRelease(keys):
    # if the key i was pressed and a stats image is being displayed
    if "i" in keys and stats.img != None:
        
        # sets the stats image and background to be invisible 
        stats.img.visible = False
        stats.img = None   
        stats.background.visible = False
        
        # checks if the game has started
        if game.g != None:
            # checks if there is a preview being displayed
            if game.g.preview != None:
                # sets the preview to invisible  
                game.g.preview.visible = False
            

def onKeyPress(key):
    # checks if the game has already started
    if game.g != None:
        # checks if you pressed the "a" key
        if key == "a":
            # goes through the list of players
            for player in game.g.players:
                # if you hit the shape with your cursor and the player hasnt already attacked this turn
                if player.shape.hits(coordinates[0],coordinates[1]) and player.attackCompleted == False:
                    # selects the player to attack
                    game.g.playerSelectedToAttack = player
                else:
                    # if the player is not selected clear all its visual indicators 
                    player.clearVisualIndicators()
            
            # if we have selected a player to move
            if game.g.playerSelectedToMove != None:
                # deselect the player selected to move and clear its visual indicators
                game.g.playerSelectedToMove.clearVisualIndicators()
                game.g.playerSelectedToMove = None
            
            # if we have succesfully selected a player to attack
            if  game.g.playerSelectedToAttack != None:
                # set the selected players indicators to visible
                game.g.playerSelectedToAttack.attackRadiusVisualIndicator.visible = True
                game.g.playerSelectedToAttack.selectedTileIndicator.visible = True
            
def onMouseDrag(x,y):
    # checks if the game has started 
    if game.g != None: 
        # goes through the players list
        for player in game.g.players:
            # checks that you hit the shape with your cursor and that the player hasnt already moved on this turn
            if player.shape.hits(x,y) and player.moveCompleted == False:
                # selects the player to move 
                game.g.playerSelectedToMove = player

            else:
                # if the player is not selected to move clear its visual indicators
                player.clearVisualIndicators()
        
        # if a player is still selected to attack
        if  game.g.playerSelectedToAttack != None:
            # de-selects the player selected to attack and clears its visual indicators
            game.g.playerSelectedToAttack.clearVisualIndicators()
            game.g.playerSelectedToAttack = None
        
        # if a player has been selected to move set the visual indicators to visible
        if  game.g.playerSelectedToMove != None:
            game.g.playerSelectedToMove.movementRadiusVisualIndicator.visible = True
            game.g.playerSelectedToMove.selectedTileIndicator.visible = True
        
        # goes through the tiles in the grid
        for row in game.g.grid.grid:
            for tile in row:
                # checks if our cursor is being dragged on top of the tile, if the tile is visible, and if we have selected a player to move
                if tile.shape.hits(x,y) and tile.visitable == True and game.g.playerSelectedToMove != None:
                    # checks if the tile is within range
                    isWithinRange = tile.x >= game.g.playerSelectedToMove.tile.x - game.g.playerSelectedToMove.rMove and tile.y >= game.g.playerSelectedToMove.tile.y - game.g.playerSelectedToMove.rMove and tile.x <= game.g.playerSelectedToMove.tile.x + game.g.playerSelectedToMove.rMove and tile.y <= game.g.playerSelectedToMove.tile.y + game.g.playerSelectedToMove.rMove
                    if isWithinRange == True:
                        # aligns the selected tile indicator with the selected tile 
                        game.g.playerSelectedToMove.selectedTileIndicator.left = tile.shape.left
                        game.g.playerSelectedToMove.selectedTileIndicator.top = tile.shape.top
                        
                        return # returns so that we dont have to go through the entire grid
                        
                    # if it is out of range
                    else:
                        # clear the selected players visual indicators and de-select it. 
                        game.g.playerSelectedToMove.clearVisualIndicators()
                        
                        game.g.playerSelectedToMove = None
        
def onMouseRelease(x,y):
    # checks if the game has started
    if game.g != None:
        # goes through the grid
        for row in game.g.grid.grid:
            for tile in row:
                # checks if the cursor hits the tile, if the tile is visitable, and if a player has been selected to move
                if tile.shape.hits(x,y) and tile.visitable == True and game.g.playerSelectedToMove != None:
                    #checks if the tile is within range
                    isWithinRange = tile.x >= game.g.playerSelectedToMove.tile.x - game.g.playerSelectedToMove.rMove and tile.y >= game.g.playerSelectedToMove.tile.y - game.g.playerSelectedToMove.rMove and tile.x <= game.g.playerSelectedToMove.tile.x + game.g.playerSelectedToMove.rMove and tile.y <= game.g.playerSelectedToMove.tile.y + game.g.playerSelectedToMove.rMove
                    if isWithinRange == True:
                        
                        # moves the player from its own tile "game.g.playerselectedtomove.tile" to the clicked on tile
                        game.g.playerSelectedToMove.move(game.g.playerSelectedToMove.tile,tile)
                        
                        # resets certain properties of the grid tiles that are used in the .move() method
                        game.g.grid.resetGrid() 
                        
                        # clears the visual indicators of the player selected to move and de selects the player that just moved. 
                        game.g.playerSelectedToMove.clearVisualIndicators()
                        
                        game.g.playerSelectedToMove = None
                        
                        return # returns so that we dont have to go through the entire grid
                    
                        
        
      

# each object created from the Tile() class represents a tile on the grid
class Tile():
    def __init__(self,x,y,shape,coverPercent):
        # coordinates of the tile
        self.x = x
        self.y = y
        
        self.adjacent = [] # contains the tiles adjacent to it
        self.shape = shape # the Rect() object that appears on the screen
        self.coverPercent = coverPercent#0,.5,1, (determines if it can be shot through or visited)
        self.visitable = True # determines if the tile is visitable or not
        self.grass = None #holds the image for the grass block if it is a grass tile
        self.vault = False #represents whether or not the tile holds part of the vault
        self.visited = False # used to assist the pathfinding process 
        self.occupied = False # determines if the tile is occupied 
        
        # if the coverpercent is 1 projectiles cannot travel through the tile. sets visitable to false and loads the cover image
        if self.coverPercent == 1:
            self.visitable = False
            self.shape = Image("https://drive.google.com/file/d/1HT0BbKYR3VWOWdSuT1zHUOGOAAmrGB_W/view?usp=sharing",0,0)
            self.shape.width = 20
            self.shape.height = 20
            self.shape.centerX = self.x * 20 +10
            self.shape.centerY = self.y * 20 + 10
        
        # if the coverpercent is 0.5 projectiles have a 50/50 chance of passing through the tile. sets visitable to false and loads the cover image
        elif self.coverPercent ==0.5:
            self.visitable = False
            self.shape = Image("https://drive.google.com/file/d/16GWpXx5VoODT21lfLwoVhVJVel2OjJ1y/view?usp=sharing",0,0)
            self.shape.width = 20
            self.shape.height = 20
            self.shape.centerX = self.x * 20 +10
            self.shape.centerY = self.y * 20 + 10

    def addToCoverGroup(self):
        # adds the tile to a group that stores all the cover tiles in the grid
        if self.coverPercent == 1:
            game.g.grid.fullCoverTilesGroup.add(self.grid[y][x].shape)
        elif self.coverPercent == 0.5:
            game.g.grid.partialCoverTilesGroup.add(self.grid[y][x].shape)
    
            
class Grid():
    def __init__(self):
        # 2d array that will store all the tiles in the grid
        self.grid = []
        
        # stores all the full cover tiles (tiles that provide 100% cover)
        self.fullCoverTiles = []
        # stores all the partial cover tiles (tiles that provide 50% cover)
        self.partialCoverTiles = []
        
        #generates the grid
        for y in range(20):
            row = []
            for x in range(16):
                random = randrange(0,35)
                
                # randomly generates a tile with grass, a barrier block, or generate an empty tile
                # doesnt generate anything on tiles that have 10>=x>=3 and 6>=y>=2 
                # doesnt generate any tiles above y 13
                # adds that tile to the row, which is then added to the grid
                if random == 0 and y < 13 and (x>=3 and x <= 10 and y >= 2 and y <= 6) == False:
                    row.append(Tile(x,y,Rect(x*20,y*20,20,20,fill=rgb(252,168,112),border="black",borderWidth = 0.2),1))
                elif random == 1 and y < 13 and (x>=3 and x <= 10 and y >= 2 and y <= 6) == False:
                    row.append(Tile(x,y,Rect(x*20,y*20,20,20,fill=rgb(252,168,112),border="black",borderWidth = 0.2),0.5))
                elif random == 2 and y < 13 and (x>=3 and x <= 10 and y >= 2 and y <= 6) == False:
                    row.append(Tile(x,y,Rect(x*20,y*20,20,20,fill=rgb(252,168,112),border="black",borderWidth = 0.2),0))
                    row[x].grass = Image('https://drive.google.com/file/d/1MVGbCXEcuhyleUR2IKsRqeaMG1PTIyqm/view?usp=sharing',0,0)
                    row[x].grass.width = 20
                    row[x].grass.height = 26
                    row[x].grass.bottom = y * 20 + 20
                    row[x].grass.left = x * 20
                else:
                    row.append(Tile(x,y,Rect(x*20,y*20,20,20,fill=rgb(252,168,112),border="black",borderWidth = 0.2),0))
                    
            self.grid.append(row)
         
         
        # designates the squares for the vault
        self.grid[4][7].vault = True
        self.grid[4][7].visitable = False
        self.grid[4][7].coverPercent = 1
        self.grid[5][7].vault = True
        self.grid[5][7].visitable = False
        self.grid[5][7].coverPercent = 1
        self.grid[4][8].vault = True
        self.grid[4][8].visitable = False
        self.grid[4][8].coverPercent = 1
        self.grid[5][8].vault = True
        self.grid[5][8].visitable = False
        self.grid[5][8].coverPercent = 1 
        
        
        # goes through the grid and surrounds cover tiles with grass
        for y in range(20):
            for x in range(16):
                # if the tile has a cover percent of 1 or is a vault tile add it to the full cover tiles list
                if self.grid[y][x].coverPercent == 1 or self.grid[y][x].vault == True:
                    self.fullCoverTiles.append(self.grid[y][x])
                # if the tile has a cover percent of 0.5 add it to the partial cover tiles list
                elif self.grid[y][x].coverPercent == 0.5:
                    self.partialCoverTiles.append(self.grid[y][x])
                    
                # checks if the adjacent tile has a cover square. If that is true, add grass to the tile
                try:
                    if self.grid[y+1][x].visitable == False and self.grid[y][x].visitable == True and self.grid[y][x].grass == None:
                        self.addGrass(x,y)
                except:
                    pass
                try:
                    if self.grid[y-1][x].visitable == False and self.grid[y][x].visitable == True and self.grid[y][x].grass == None:
                        self.addGrass(x,y)
                except:
                    pass
                try:
                    if self.grid[y][x+1].visitable == False and self.grid[y][x].visitable == True and self.grid[y][x].grass == None:
                        self.addGrass(x,y)
                except:
                    pass
                try:
                    if self.grid[y][x-1].visitable == False and self.grid[y][x].visitable == True and self.grid[y][x].grass == None:
                        self.addGrass(x,y)
                except:
                    pass
                
        #goes through the grid to add extra grass
        for y in range(20):
            for x in range(16):
        
                # checks if a tile is surrounded on 3 adjacent sides by grass. If that is true then it adds grass to that square.
                # example: 3 grass tiles (G) surround the empty tile (E) on 3 sides. 
                #   G
                # G E
                #   G
                # first checks if the tile is visitable and it doesnt already have grass
                # checks each individual senario for arrangements of adjacent grass blocks
                if self.grid[y][x].visitable == True and self.grid[y][x].grass == None:
                    # uses try and except in case the grid tile that is being looked at is out of range
                    # preventing that from causing an error
                    
                    try:
                        if self.grid[y+1][x].grass != None and self.grid[y-1][x].grass != None and self.grid[y][x+1].grass != None:
                            self.addGrass(x,y)
                    except:
                        pass
                    try:
                        if self.grid[y-1][x].grass != None and self.grid[y][x+1].grass != None and self.grid[y][x-1].grass != None:
                            self.addGrass(x,y)
                    except:
                        pass
                    try:
                        if self.grid[y][x+1].grass != None and self.grid[y][x-1].grass != None and self.grid[y+1][x].grass != None:
                            self.addGrass(x,y)
                    except:
                        pass
                    try:
                        if self.grid[y][x-1].grass != None and self.grid[y+1][x].grass != None and self.grid[y-1][x].grass != None:
                            self.addGrass(x,y)
                    except:
                        pass
                    
                    
            
               
        
        
        # fills each tiles tile.adjacent list with the tiles adjacent to it
        self.populateAdjacency()
        
        
        
    # helper function adds grass to a tile, given its x and y coordinates. 
    def addGrass(self,x,y):
        # adds an image and then centers it on the tile
        self.grid[y][x].grass = Image('https://drive.google.com/file/d/1MVGbCXEcuhyleUR2IKsRqeaMG1PTIyqm/view?usp=sharing',0,0)
        self.grid[y][x].grass.width = 20
        self.grid[y][x].grass.height = 26
        self.grid[y][x].grass.bottom = y * 20 + 20
        self.grid[y][x].grass.left = x * 20 
        
    # goes through each tile and adds any tiles adjacent to it to the adjacency list
    def populateAdjacency(self):
        for row in self.grid:
            for node in row:
                # uses try and except incase the grid index that we are looking at is out of range
                try:
                    if node.x < len(self.grid) and self.grid[node.y][node.x+1].visitable == True:
                        node.adjacent.append(self.grid[node.y][node.x+1] )
                except:
                    pass
                try:
                    if node.x > 0 and self.grid[node.y][node.x-1].visitable == True:
                        node.adjacent.append(self.grid[node.y][node.x-1] )
                except:
                    pass
                try:
                    if node.y < len(self.grid) and self.grid[node.y+1][node.x].visitable == True:
                        node.adjacent.append(self.grid[node.y+1][node.x] )
                except:
                    pass
                try:
                    if node.y > 0 and self.grid[node.y-1][node.x].visitable == True:
                        node.adjacent.append(self.grid[node.y-1][node.x] )
                except:
                    pass  
    
    # sets each tiles visited property to false
    def resetGrid(self):
        for  row in self.grid:
            for tile in row:
                tile.visited = False



# each object created from the Player() class represents a character in the game
class Player():
    
    
    def __init__(self,health,name,rAttack,rMove,rSplash,damage,tile,shape,movingAttack,stats,projectileTrajectory):
        self.name = name # player name
        self.rAttack = rAttack # players attack range
        self.rMove = rMove  # players movement radius
        self.rSplash = rSplash # players splash radius (not implemented)
        self.damage = damage # players attack damage 
        self.validProjectilePath = False # whether or not the player has an unobstructed path to its targeted enemy
        
        # represents whether the players turn is completed or not
        self.attackCompleted = False
        self.moveCompleted = False
        
        # represents if the unit is dead or not
        self.dead = False
        
        # health/totalHealth will be used to create the healthbar
        self.health = health 
        self.originalHealth = health 
        
        # tile represents the tile that the player is standing on. this tile is set to occupied.
        self.tile = tile
        self.tile.occupied = True 
        
        # the image of the player that appears on the screen
        self.shape = Image(shape,0,0)
        self.shape.width = 30
        self.shape.height = 30
        
        # aligns the player with the tile 
        self.shape.centerX = self.tile.shape.centerX
        self.shape.centerY = self.tile.shape.centerY
        
        # url for the stats image of the player
        self.stats = stats
        
        #can be "parabola" or "line". parabola avoids obstacles while line doesnt
        self.projectileTrajectory = projectileTrajectory
        
        # indicates how far you can move
        self.movementRadiusVisualIndicator = Rect(0,0,20+self.rMove*2*20,20+self.rMove*2*20,fill="orange",opacity=30,visible = False)
        self.movementRadiusVisualIndicator.centerX = self.shape.centerX
        self.movementRadiusVisualIndicator.centerY = self.shape.centerY
        
        #indicates how far you can attack
        self.attackRadiusVisualIndicator = Rect(0,0,20+self.rAttack*2*20,20+self.rAttack*2*20,fill="blue",opacity=30,visible = False)
        self.attackRadiusVisualIndicator.centerX = self.shape.centerX
        self.attackRadiusVisualIndicator.centerY = self.shape.centerY
        
        # shows which tile you are targeting when preparing to attack
        self.selectedTileIndicator = Rect(0,0,20,20,fill="red",visible = False,opacity = 50)
        
        # creates a projectile trajectory indicator based on which type of attack the player utilizes 
        if self.projectileTrajectory == "line":
            self.projectileTrajectoryIndicator = Line(self.tile.shape.centerX,self.tile.shape.centerY,self.tile.shape.centerX,self.tile.shape.centerY)
            
        else:
            self.projectileTrajectoryIndicator = None
        
    def move(self,tileStart,tileEnd):
        # ensures that the tile you are trying to move to isnt occupied and isnt your starting tile
        if tileEnd == tileStart or tileEnd.occupied == True:
            return
        
        # stores the shortest path to tileend
        shortestPath = []
        
        # queue stores the tiles that are yet to be visited 
        queue = [[tileStart,0,None]]
        
        
        while len(queue) > 0:
            node = queue[0][0] # node aka tile currently being explored
            dist = queue[0][1]
            
            arr = queue[0] # format: [tile,distance from start, arr of the previous tile]
            queue.remove(arr)
            
            # checks if you have reached your end tile 
            if node == tileEnd:
                # retraces the path back to the starting tile 
                while arr[0] != tileStart:
                    shortestPath.insert(0,arr)
                    arr = arr[2]
                shortestPath.insert(0,arr)
               
                # line group displays the path of the player
                for i in range(len(shortestPath)):
                    try:
                        game.g.lineGroup.add(Line(shortestPath[i][0].shape.centerX,shortestPath[i][0].shape.centerY,shortestPath[i+1][0].shape.centerX,shortestPath[i+1][0].shape.centerY,fill="black"))
                    except:
                        pass
                    
                # the player moves to the end tile
                for i in range(len(shortestPath)):
                    if i < len(shortestPath) - 1:
                        self.goDirectlyTo(game.g.grid.grid[shortestPath[i+1][0].y][shortestPath[i+1][0].x])  
                
                # sets the end tile to occupied. sets the tile we were previously on to not occupied. Sets our tile to our desired end tile, 
                tileEnd.occupied = True
                self.tile.occupied = False
                self.tile = tileEnd
                
                # gets rid of the line group
                game.g.lineGroup.clear()
                
                # centers the visual indicators to the new position of the player
                self.movementRadiusVisualIndicator.centerX = self.tile.shape.centerX
                self.movementRadiusVisualIndicator.centerY = self.tile.shape.centerY
                self.attackRadiusVisualIndicator.centerX = self.tile.shape.centerX
                self.attackRadiusVisualIndicator.centerY = self.tile.shape.centerY
                
                # centers the shape with the tile it is located on
                self.shape.centerX = self.tile.shape.centerX
                self.shape.centerY = self.tile.shape.centerY
                
                
                # ends the loop
                break
            
            # goes through the current tiles adjacent tiles and checks if they have been explored. If they havent been explored then add them to the queue to be visited later.
            for adj in node.adjacent:
                if adj.visited == False:
                    adj.visited = True
                    queue.append([adj,dist+1,arr])
                    
        # set move completed to true. Player wont be able to attack until next turn
        self.moveCompleted = True
    
    # gets rid of the visual indicators connected to the player
    def clearVisualIndicators(self):
        self.selectedTileIndicator.visible = False
        self.movementRadiusVisualIndicator.visible = False
        self.attackRadiusVisualIndicator.visible = False
        
    # goes from its current position to the position of the desired tile
    def goDirectlyTo(self,tile):
        distanceX = tile.shape.centerX - self.shape.centerX
        distanceY = tile.shape.centerY - self.shape.centerY
        
        
        # closes the gap in 5 pixel increments 
        for i in range (0,abs(distanceY),5):
            sleep(0.00001)
            if distanceY < 0:
                self.shape.centerY -= 5
            else:
                self.shape.centerY += 5
                
        for i in range (0,abs(distanceX),5):
            sleep(0.00001)
            if distanceX < 0:
                self.shape.centerX -= 5
            else:
                self.shape.centerX += 5
    
    # attacks the eneny passed as an argument
    def attack(self,enemy):
        # clears visual indicators
        self.clearProjectilePath()
        self.clearVisualIndicators()
        
        # sets attack completed to true. Player wont be able to attack this turn. Sets the player selected to attack to none
        game.g.playerSelectedToAttack = None
        self.attackCompleted = True
        
        # if the hit will make reduce the enemies health at or below zero. Remove the enemy from the game with .selfDestruct()
        if enemy.health - self.damage <= 0:
            enemy.health = 0
            enemy.selfDestruct()
            return 
        
        # reduce the enemies health and re adjust the enemies health bar.
        enemy.health -= self.damage
        enemy.healthBar[0].width = 20*enemy.health/enemy.originalHealth
        
        # vaults healthbar is double the length of a regular healthbar. Width is multiplied by 40 instead of 20.
        if enemy.type == "vault":
            enemy.healthBar[0].width = 40*enemy.health/enemy.originalHealth
        
        # changes the color of the healthbar based on how much health the enemy has
        if enemy.health / enemy.originalHealth >= 2/3:
            enemy.healthBar[0].fill = "green"
        elif enemy.health / enemy.originalHealth < 2/3 and enemy.health / enemy.originalHealth >= 1/3:
            enemy.healthBar[0].fill = "yellow"
        else:
             enemy.healthBar[0].fill = "red"
             
    
    # shows the projectile path trajectory
    def showProjectilePath(self,tile):
        # if the unit is melee, set validprojectilepath to true
        if self.rAttack == 1:
            self.validProjectilePath = True
        # if the unit is ranged and attacks in a line
        elif self.rAttack > 1 and self.projectileTrajectory == "line":
            # positions the projectileTrajectoryIndicator.
            self.projectileTrajectoryIndicator.x1 = self.tile.shape.centerX
            self.projectileTrajectoryIndicator.y1 = self.tile.shape.centerY
            self.projectileTrajectoryIndicator.x2 = tile.shape.centerX
            self.projectileTrajectoryIndicator.y2 = tile.shape.centerY
            self.projectileTrajectoryIndicator.fill = "black"
            self.projectileTrajectoryIndicator.visible = True
            self.projectileTrajectoryIndicator.toFront()
            
            # default value
            self.validProjectilePath = True
            
            for cover in game.g.grid.partialCoverTiles:
                    # if the trajectory hits a partial cover tile make the TrajectoryIndicator yellow.
                    if self.projectileTrajectoryIndicator.hitsShape(cover.shape):
                        self.projectileTrajectoryIndicator.fill = "yellow"
                        
                        # validProjectilePath can be false given a 50/50 chance
                        r = random()
                        if r > 0.5:
                            self.validProjectilePath = False
                            
            for cover in game.g.grid.fullCoverTiles:
                # if the trajectory hits a partial cover tile make the TrajectoryIndicator red and set validProjectilePath to false.
                if self.projectileTrajectoryIndicator.hitsShape(cover.shape):
                    self.projectileTrajectoryIndicator.fill = "red"
                    self.validProjectilePath = False
                    
        # a unit with a "parabola" trajectory automatically gets validProjectilePath set to true.
        elif self.rAttack > 1 and self.projectileTrajectory == "parabola":
            self.validProjectilePath = True
    
    # clears the projectile path
    def clearProjectilePath(self):
        if self.rAttack > 1 and self.projectileTrajectory == "line":
            self.projectileTrajectoryIndicator.visible = False 
    
    # removes the player from the game
    def selfDestruct(self):
        self.shape.visible = False
        self.dead = True
        self.tile.occupied = False
        
        game.g.players.remove(self)

# objects creates from the enemy class represent enemies. Enemies inherit many properties of the player() class
class Enemy(Player):
    def __init__(self,health,name,rAttack,rMove,rSplash,damage,tile,shape,movingAttack,stats,projectileTrajectory):
        # uses super().__init__() to run the Player() class's constructor.
        super().__init__(health,name,rAttack,rMove,rSplash,damage,tile,shape,movingAttack,stats,projectileTrajectory)
        
        # sets enemy type to standardenemy
        self.type = "standardenemy"
        
        # halfs the damage of the regular player
        self.damage *= 0.5
        
        # healthbar[0], will be used to show the health of the player. healthbar[1] is the border of the healthbar
        self.healthBar = [Rect(self.tile.shape.left,self.tile.shape.top-3,20,3,fill="green"),Rect(self.tile.shape.left,self.tile.shape.top-3,20,3,border="black",borderWidth= 0.3,fill=None)]
    
    
    def AIPlayMove(self):
        # checks if there are no players left, if so, plays losing animation
        if len(game.g.players) == 0:
            game.g.playLosingAnimation()
            return
            
        #checks if any player can be attacked, if so attack that player and return.
        for player in game.g.players:
            if self.canAttack(player):
                self.attack(player)
                return
        
        # determines the closest player
        closestPlayer = None
        closestPlayerDistance = 565 #max possible distance between squares
        for player in game.g.players:
            dist = distance(player.shape.centerX,player.shape.centerY, self.shape.centerX,self.shape.centerY)
            if dist < closestPlayerDistance:
                closestPlayerDistance = dist
                closestPlayer = player
           
        # moves towards the closest player
        self.move(self.tile,closestPlayer.tile)
        
        # checks if any player can be attacked, if som attack that player and return.
        for player in game.g.players:
            if self.canAttack(player):
                self.attack(player)
                return
                    
    
    def move(self,tileStart,tileEnd):
        # set start tile to un occupied
        tileStart.occupied = False
        
        #checks if your starting tile is next to your end tile 
        if tileStart in tileEnd.adjacent:
            return
        
        # list stores the shortest path to the tilend
        shortestPath = []
        
        # queue of tiles that must be visited
        queue = [[tileStart,0,None]]
        
        #following uses an algorithm to find the tile closest to the end tile that is within the enemies movement radius (optimalTile), (similar algorithm to that used in line 740)
        optimalTile = None
        distanceFromEndTile = 565
        
        while len(queue) > 0:
            node = queue[0][0]
            dist = queue[0][1]
            arr = queue[0]
            queue.remove(arr)

            dist = distance(tileEnd.shape.centerX,tileEnd.shape.centerY,node.shape.centerX,node.shape.centerY) 
            
            if dist < distanceFromEndTile and node.occupied == False:
                distanceFromEndTile = dist
                optimalTile = node
 
            
            
            for adj in node.adjacent:
                if adj.visited == False and adj.x >= self.tile.x - self.rMove and  adj.x <= self.tile.x + self.rMove and adj.y >= self.tile.y - self.rMove and adj.y <= self.tile.y + self.rMove:
                    adj.visited = True
                    queue.append([adj,dist+1,arr])
    
        
        # resets the grid 
        game.g.grid.resetGrid()
        
        
        # finds the shortest path to the optimal tile and moves to it (same algorithm as used in line 740)
        shortestPath = []
        visited = []
        
        queue = [[tileStart,0,None]]
        
        
        while len(queue) > 0:
            node = queue[0][0]
            dist = queue[0][1]
            arr = queue[0]
            queue.remove(arr)
            

            if node == optimalTile:
                while arr[0] != tileStart:
                    shortestPath.insert(0,arr)
                    arr = arr[2]
                shortestPath.insert(0,arr)
                
                self.healthBar[0].visible = False
                self.healthBar[1].visible = False

                for i in range(len(shortestPath)):
                    if i < len(shortestPath) - 1:
                        self.goDirectlyTo(game.g.grid.grid[shortestPath[i+1][0].y][shortestPath[i+1][0].x])  
                
                optimalTile.occupied = True
                self.tile.occupied = False
                self.tile = optimalTile
                
                self.healthBar[0].bottom = self.tile.shape.top
                self.healthBar[0].left = self.tile.shape.left
                
                self.healthBar[1].bottom = self.tile.shape.top
                self.healthBar[1].left = self.tile.shape.left
                
                self.healthBar[0].visible = True
                self.healthBar[1].visible = True
                
                
                
                break
            
            for adj in node.adjacent:
                if adj.visited == False:
                    adj.visited = True
                    queue.append([adj,dist+1,arr])
        
        # resets the grid  
        game.g.grid.resetGrid()
    
    # removes enemy from the game
    def selfDestruct(self):
        self.shape.visible = False
        self.dead = True
        
        self.healthBar[0].visible = False
        self.healthBar[1].visible = False
        
        self.tile.occupied = False
        
        
        game.g.enemies.remove(self)
    
    # checks if you can attack (similar to the algorithm used in Player.showprojectilepath)
    def canAttack(self,player):
        # checks if it is within range of the player, if so returns true
        if self.rAttack == 1 and self.isInRange(player):
            return True
        
        # if the projectiletrajectory is in the form of a line and the player is within range
        elif self.rAttack > 1 and self.projectileTrajectory == "line" and self.isInRange(player):
            projectileTrajectoryIndicator = Line(self.tile.shape.centerX, self.tile.shape.centerY,player.tile.shape.centerX,player.tile.shape.centerY)
            projectileTrajectoryIndicator.visible = False

            # checks if cover tiles are in the way
            for cover in game.g.grid.fullCoverTiles:
                if projectileTrajectoryIndicator.hitsShape(cover.shape):
                    return False
            
            for cover in game.g.grid.partialCoverTiles:
                if projectileTrajectoryIndicator.hitsShape(cover.shape):
                    return False
                    
            return True
        
        # checks if it is within range of the player, if so returns true
        elif self.rAttack > 1 and self.projectileTrajectory == "parabola" and self.isInRange(player):
            return True
    
    def attack(self,player):
        # if this attack will reduce the players health at or below zero remove the player from the game.
        if player.health - self.damage <= 0:
            player.health = 0
            player.selfDestruct()
            return 
        
        # reduce the players damage
        player.health -= self.damage
        
        # visual indicator that the player is being attacked
        player.tile.shape.fill = "darkRed"
        sleep(0.5)
        player.tile.shape.fill = rgb(252,168,112)
    
    # checks if the player is within range to be attacked
    def isInRange(self,player):
        inRange = player.tile.x >= self.tile.x - self.rAttack and player.tile.x <= self.tile.x + self.rAttack and player.tile.y >= self.tile.y - self.rAttack and player.tile.y <= self.tile.y + self.rAttack
        return inRange

# the game class has important properties and methods related to the game
class Game():
    def __init__(self,p1,p2,p3):
        # creates the grid
        self.grid = Grid()
        
        # creates the 3 players
        self.p1 = Player(playerInfoList[p1][0],p1,playerInfoList[p1][1],playerInfoList[p1][2],playerInfoList[p1][3],playerInfoList[p1][4],self.grid.grid[17][3],playerInfoList[p1][5],playerInfoList[p1][6],playerInfoList[p1][7],playerInfoList[p1][8])
        self.p2 = Player(playerInfoList[p2][0],p2,playerInfoList[p2][1],playerInfoList[p2][2],playerInfoList[p2][3],playerInfoList[p2][4],self.grid.grid[17][8],playerInfoList[p2][5],playerInfoList[p2][6],playerInfoList[p2][7],playerInfoList[p2][8])
        self.p3 = Player(playerInfoList[p3][0],p3,playerInfoList[p3][1],playerInfoList[p3][2],playerInfoList[p3][3],playerInfoList[p3][4],self.grid.grid[17][12],playerInfoList[p3][5],playerInfoList[p3][6],playerInfoList[p3][7],playerInfoList[p3][8])
        
        # list with all the players
        self.players = [self.p1,self.p2,self.p3]
        
        # represents players selelected to attack and move
        self.playerSelectedToMove = None
        self.playerSelectedToAttack = None
        
        # shows the movement path for players
        self.lineGroup = Group()
        
        # creates enemies
        self.e1 = Enemy(playerInfoList["rifleman"][0],"gaurd",playerInfoList["rifleman"][1],playerInfoList["rifleman"][2],playerInfoList["rifleman"][3],playerInfoList["rifleman"][4],self.grid.grid[2][4],playerInfoList["rifleman"][5],playerInfoList["rifleman"][6],playerInfoList["rifleman"][7],playerInfoList["rifleman"][8])
        self.e2 = Enemy(playerInfoList["rifleman"][0],"gaurd",playerInfoList["rifleman"][1],playerInfoList["rifleman"][2],playerInfoList["rifleman"][3],playerInfoList["rifleman"][4],self.grid.grid[2][8],playerInfoList["rifleman"][5],playerInfoList["rifleman"][6],playerInfoList["rifleman"][7],playerInfoList["rifleman"][8])
        self.e3 = Enemy(playerInfoList["rifleman"][0],"gaurd",playerInfoList["rifleman"][1],playerInfoList["rifleman"][2],playerInfoList["rifleman"][3],playerInfoList["rifleman"][4],self.grid.grid[2][11],playerInfoList["rifleman"][5],playerInfoList["rifleman"][6],playerInfoList["rifleman"][7],playerInfoList["rifleman"][8])
        self.e4 = Enemy(playerInfoList["rifleman"][0],"gaurd",playerInfoList["rifleman"][1],playerInfoList["rifleman"][2],playerInfoList["rifleman"][3],playerInfoList["rifleman"][4],self.grid.grid[4][5],playerInfoList["rifleman"][5],playerInfoList["rifleman"][6],playerInfoList["rifleman"][7],playerInfoList["rifleman"][8])
        self.e5 = Enemy(playerInfoList["rifleman"][0],"gaurd",playerInfoList["rifleman"][1],playerInfoList["rifleman"][2],playerInfoList["rifleman"][3],playerInfoList["rifleman"][4],self.grid.grid[4][10],playerInfoList["rifleman"][5],playerInfoList["rifleman"][6],playerInfoList["rifleman"][7],playerInfoList["rifleman"][8])
        
        # list with all the enemies
        self.enemies = [self.e1,self.e2,self.e3,self.e4,self.e5]
        
        # sidebar
        Rect(320,0,80,400,fill=rgb(236,157,111),borderWidth = 2,border="black")
        Rect(320,0,80,400,fill="black",border=None,opacity=10)
        
        # healthbar shows the health % of players
        self.healthBar = Rect(330,390,60,5,fill="green")
        
        # healthbar border
        Rect(330,390,60,5,fill=None,border="black",borderWidth = 0.5)
        
        # shows the image of the player whos stats you are looking at
        self.preview = None
        
        # creates the vault
        self.vault = Vault()
        
        # indicates whos turn it is
        self.teamTurnIndicator = Label("YOUR TURN",360,80,size=8)
        
        # finishes your turn when pressed
        self.completeTurnButton = Label("COMPLETE TURN",360,40,size=8)
        
    # indicates win/lose
    def playWinningAnimation(self):
        Label("YOU WIN",200,200,size=40)
    def playLosingAnimation(self):
        Label("YOU LOSE",200,200,size=40)
    
    def playEnemiesTurn(self):
        for enemy in self.enemies:
            enemy.AIPlayMove()
    
    # finishes your turn
    def completeTurn(self):
        # sets move/attack completed to false for every player
        for player in self.players:
            player.moveCompleted = False
            player.attackCompleted = False
        
        # indicates that it is the enemies turn
        self.teamTurnIndicator.value = "ENEMIES TURN"
        
        # if there are no more enemies play winning animation
        if len(self.enemies) == 0:
            self.playWinningAnimation()
        
        # enemies move and attack
        self.playEnemiesTurn()
        
        # your turn again
        self.teamTurnIndicator.value = "YOUR TURN"
    
class Vault():
    def __init__(self):
        # sets health and original health
        self.health = 2000
        self.originalHealth = 2000
        
        # healthbar shows what % the vault is at in terms of health
        self.healthBar = [Rect(140,117,40,5,fill="green"),Rect(140,117,40,5,fill=None,border = "black",borderWidth = 0.5)]
        
        # image of the vault
        self.shape = Image("https://play-lh.googleusercontent.com/UN3Hq98zm81wPCYCT8yWh2xOPlZm4k-c_KXjLqp3Fsy2tTujy2eH3w-Hb4ZnhxsQmIY",0,0)
        self.shape.height = 40
        self.shape.width = 40
        self.shape.bottom = 120
        self.shape.centerX = 160
        
        # sets the type of the entity to vault
        self.type = "vault"
        
    def selfDestruct(self):
        game.g.playWinningAnimation()
