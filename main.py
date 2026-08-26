"""
Game design project - Grade 1 game
Shirley Li, Hannah Shi
ICS3U
This is a program that allows the user to play the game we made 
History:
Program Creation: Febuary 27, 2024
"""

#Template 

# ============== Image Sources ==============
"""
purple banana image source: https://joke-battles.fandom.com/wiki/Urple_Banana?file=Urplebanana.jpg
spike image source: https://twitter.com/MindCap/status/1700649650376634715
background source: https://www.facebook.com/111428700717475/photos/a.150077210185957/150081773518834/?type=3
heart image source: https://en.wikipedia.org/wiki/Heart_symbol#/media/File:Heart_coraz%C3%B3n.svg
"""

# ======================== IMPORTS & SETUP ========================
import sys
import time  # for the end win/lose screen and levels
import random

# allows access to the pygame library
import pygame

# These allow you to just write QUIT instead of having to write pygame.QUIT. Not necessary, but handy as shortforms
from pygame.locals import (
    RLEACCEL,
    KEYDOWN,
    QUIT,
    K_ESCAPE,
    K_RETURN
)

# Initialize pygame - this is required.
pygame.init()

# ================== CONSTANTS =============

#  Define constants for the screen width and height
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# ======================== FUNCTIONS ========================


def createPlayer(player):
  """
  Initializes Player surface and rectangle.
  player.image (Surface): geometry image
  player.rect (Rectangle): rectangle placed at bottom centre of screen

  Args:
      player (Sprite)

  Note that nothing is returned. The player is mutable and passed by reference
  When we change the surface / rectangle of the player in the function, it changes that object's attributes in the global scope
  """
  # load the image, which returns a surface. Convert makes it faster to blit
  player.image = pygame.image.load("geometry.png").convert()
  #Make a specific colour on the image transparent (white, here).
  player.image.set_colorkey((255, 255, 255), RLEACCEL)
  # the rectangle is used for the location of an object (where to place it), but also for collisions, etc..
  # this creates with the size of the surf. Without parameters, the rect is located wherever the surf was created
  player.rect = player.image.get_rect()

  # Move player to bottom centre of the screen
  # Constants are in the global scope. Note that changing the name of these constants would cause an issue.
  player.rect.x = SCREEN_WIDTH / 2
  player.rect.bottom = SCREEN_HEIGHT

def playerUpdate(player, mousePos):
  """
  Move the Player sprites based on mouse position
  Args:
  player (Sprite)
  mousePos (tuple(float)): Mouse position
  """

  # Move the Player's rectangle based on the mouse position
  player.rect.center = (mousePos[0], mousePos[1])

  #  Keep player on the screen
  if player.rect.left < 0:
      player.rect.left = 0
  elif player.rect.right > SCREEN_WIDTH:
      player.rect.right = SCREEN_WIDTH
  if player.rect.top <= 0:
      player.rect.top = 0
  elif player.rect.bottom >= SCREEN_HEIGHT:
      player.rect.bottom = SCREEN_HEIGHT

def createSpike_1(spike):
  """
  Adds an image, rectangle, and speed to a spike object
  spike.image (Surface): spike image
  spike.rect (Rectangle): initial position is randomly placed just above the screen
  spike.speed (int): Random integer between 5 and 20

  Args:
      spike (Sprite)
  Note that nothing is returned. The spike is mutable and passed by reference
  When we change the surface / rectangle of the spike in the function, it changes that object's attributes in the global scope
  """
  spike.image = pygame.image.load("spike.png").convert(
  )  # load the image, which returns a surface. Convert makes it faster to blit
  spike.image.set_colorkey(
      (255, 255, 255), RLEACCEL
  )  # This can be used to make a specific colour on your image transparent (white, here).

  # Place the spike randomly on the screen, starting between 20-100 pixels beyond the right hand side of the screen
  spike.rect = spike.image.get_rect(center=(
    random.randint(20, SCREEN_WIDTH - 20),
    random.randint(-50, 0),
))
  # Select a random speed
  spike.speed = random.randint(5, 20)

def createSpike_2(spike):
  """
  Adds an image, rectangle, and speed to a spike object
  spike.image (Surface): spike image
  spike.rect (Rectangle): initial position is randomly placed just above the screen
  spike.speed (int): Random integer between 5 and 20

  Args:
      spike (Sprite)
  Note that nothing is returned. The spike is mutable and passed by reference
  When we change the surface / rectangle of the spike in the function, it changes that object's attributes in the global scope
  """
  spike.image = pygame.image.load("spike.png").convert(
  )  # load the image, which returns a surface. Convert makes it faster to blit
  spike.image.set_colorkey(
      (255, 255, 255), RLEACCEL
  )  # This can be used to make a specific colour on your image transparent (white, here).

  # Place the spike randomly on the screen, starting between 20-100 pixels beyond the right hand side of the screen
  spike.rect = spike.image.get_rect(center=(
    random.randint(20, SCREEN_WIDTH - 20),
    random.randint(-50, 0),
))
  # Select a random faster speed
  spike.speed = random.randint(20, 35)

def spikeUpdate(spike):
  """
  Updates the position of the spike sprite, destorying it if it off screen
  Args:
      spike (Sprite)
  """
  # position is shifted in y-direction only, based on the sprite's speed
  spike.rect.move_ip(0, spike.speed)

  # if off screen, kill/destroy the object
  if spike.rect.top > SCREEN_HEIGHT:
      spike.kill()

def createKing_Spike(king_Spike):
  """
  Adds an image, rectangle, and speed to the king spike object
  king_spike.image (Surface): spike image
  king_spike.rect (Rectangle): initial position is randomly placed just above the screen
  king_spike.speed (int): 35

  Args:
      king_Spike (Sprite)
  Note that nothing is returned. The spike is mutable and passed by reference
  When we change the surface / rectangle of the spike in the function, it changes that object's attributes in the global scope
  """
  king_Spike.image = pygame.image.load("king_spike.png").convert(
  )  # load the image, which returns a surface. Convert makes it faster to blit
  king_Spike.image.set_colorkey(
      (255, 255, 255), RLEACCEL
  )  # This can be used to make a specific colour on your image transparent (white, here).

  # Place the king spike on the screen, center on top
  king_Spike.rect = king_Spike.image.get_rect(center=(SCREEN_WIDTH/2,250))
  # Set speed to 35
  king_Spike.speed = 35

def king_spikeUpdate(king_Spike):
  """
  Updates the position of the king_spike sprite, making it move left and right
  Args:
      king_Spike (Sprite)
  """
  #if it reaches the end, go other way
  if king_Spike.rect.right > (SCREEN_WIDTH-1):
      king_Spike.speed *= -1
  elif king_Spike.rect.left < 1:
      king_Spike.speed *= -1

  king_Spike.rect.move_ip(king_Spike.speed,0)

def createBanana(banana,mousePos):
  """
  Adds an image, rectangle, and speed to a banana object
  banana.image (Surface): banana image
  banana.rect (Rectangle): initial position is where the mouse is
  banana.speed (int): 25

  Args:
      banana (Sprite)
  Note that nothing is returned. The banana is mutable and passed by reference
  When we change the surface / rectangle of the spike in the function, it changes that object's attributes in the global scope
  """
  banana.image = pygame.image.load("purple_bananas.png").convert(
  )  # load the image, which returns a surface. Convert makes it faster to blit
  banana.image.set_colorkey(
      (255, 255, 255), RLEACCEL
  )  # This can be used to make a specific colour on your image transparent (white, here).

  # Place the banana where the mouse is
  banana.rect = banana.image.get_rect(center=(mousePos[0], mousePos[1]))
  # Set speed to -25
  banana.speed = -25

def bananaUpdate(banana):
  """
  Updates the position of the banana sprite, destorying it if it off screen
  Args:
      banana (Sprite)
  """
  # position is shifted in y-direction only, based on the sprite's speed
  banana.rect.move_ip(0, banana.speed)

  # if off screen, kill/destroy the object
  if banana.rect.bottom <= 0:
      banana.kill()

def createHeart(heart,space):
  """
  Adds an image, rectangle, and speed to a heart object
  heart.image (Surface): heart image
  heart.rect (Rectangle): initial position is randomly placed just above the screen
  banana.speed (int): 25

  Args:
      banana (Sprite)
  Note that nothing is returned. The banana is mutable and passed by reference
  When we change the surface / rectangle of the spike in the function, it changes that object's attributes in the global scope
  """
  heart.image = pygame.image.load("Heart.png").convert(
  )  # load the image, which returns a surface. Convert makes it faster to blit
  heart.image.set_colorkey(
      (255, 255, 255), RLEACCEL
  )  # This can be used to make a specific colour on your image transparent (white, here).

  # Place the banana at the top right corner of the screen
  heart.rect = heart.image.get_rect(center=(1200+space, 100))

def start(screen):
  """
  Instruction screen shown at the start of the game
  Args:
      screen (Surface)
  """
  # Set screen as black with white text. 
  screen.fill((0,0,0))
  font = pygame.font.Font('freesansbold.ttf', 32)

  # Create text object, with associated rectangle in centre of screen
  text1 = font.render('Help save the world!', True, (255,255,255))
  textRect1 = text1.get_rect()
  textRect1.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 45

  # Create text object, with associated rectangle below the other text
  text2 = font.render('Geometry must destory his enemy the spike!', True, (255,255,255))
  textRect2 = text2.get_rect()
  textRect2.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2 
  text3 = font.render('Move your mouse to help him avoid the spikes and left click to fire purple bananas at them!', True, (255,255,255))
  textRect3 = text3.get_rect()
  textRect3.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 45
  text4 = font.render('Be careful - they will get faster and stronger before you reach the KING SPIKE!!!', True, (255,255,255))
  textRect4 = text4.get_rect()
  textRect4.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 90
  text5 = font.render('Press Enter to Begin.', True, (255,255,255))
  textRect5 = text5.get_rect()
  textRect5.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 135

  # blit needed for it to be placed on the surface, then display updated for it to show up.
  screen.blit(text1, textRect1)
  screen.blit(text2, textRect2)
  screen.blit(text3, textRect3)
  screen.blit(text4, textRect4)
  screen.blit(text5, textRect5)

def end(status, screen):
  """
  Win screen shown at the end of the game
  Args:
      status (str)
      screen (Surface)
  """
  # Set screen as black with white text.
  screen.fill((0, 0, 0))
  font = pygame.font.Font('freesansbold.ttf', 32)

  # Create text object, with associated rectangle in centre of screen
  text = font.render('YOU ' + status.upper(), True, (255, 255, 255))
  textRect = text.get_rect()
  textRect.center = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2

  # blit needed for it to be placed on the surface, then display updated for it to show up.
  screen.blit(text, textRect)
  pygame.display.update()


# ======================== MAIN ========================

#  Set up the drawing window
screen = pygame.display.set_mode(
    [SCREEN_WIDTH, SCREEN_HEIGHT]
)  # Returns a Surface, which represents the inside dimensions of your drawing window --> the OS controls the borders & title bar, etc.
bg = pygame.image.load("Background.png").convert()

#  Create a custom event for adding a new spike
ADDSPIKE = pygame.USEREVENT + 1  # USEREVENT is the last kind of event that pygame reserves, so by adding 1 to this number, ADDSPIKE becomes a new event with its own individual #
pygame.time.set_timer(
      ADDSPIKE, 1000
  )  # this makes the ADDSPIKE event happen every 1000ms (1/s). We call this once, but it fires throughout the game.

# Used to determine whether the user quit (default setting), lost, or won
status = 'instructions' 

# Timer
ADDTIME = pygame.USEREVENT + 2  # Needs to be one bigger than ADDSPIKE
pygame.time.set_timer(
    ADDTIME, 1000
)  # this makes the timer event happen once per second. We call this once, but it fires throughout the game.
timer = 0

#distance is the initial distance between the heart being drawn and the fist heart
distance = 25
    
# ====PLAYER SPRITE
# Create a player sprite. This allows adding a surface, rectangle, etc.. durectly to the player so all the data is kept with that sprite. It also allows adding the player to a sprite group, which will come in handy later
player = pygame.sprite.Sprite()
# Add a surface (image) and rectangle (what is moved and where the image is drawn) to the player using the function we defined above
createPlayer(player)

# =====SPRITE GROUPS
#  Create groups to hold spike sprites and all sprites
#  - spikeGrp is used for collision detection and position updates
#  - bananaGrp is used for banana collisions
#  - kingspikeGrp for king spike
#  - heartGrp for the hearts (king spike's health)
#  - all_sprites is used for rendering
spikeGrp = pygame.sprite.Group()
bananaGrp = pygame.sprite.Group()
kingspikeGrp = pygame.sprite.Group()
heartGrp = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#This sees how many times banana cllided with king spike
king_colcounter=0

#  Adjust the timing so the framerate isn't so high (adjusted in the game loop)
clock = pygame.time.Clock()

#  Run until the user asks to quit or game ends
running = True

while running:
    #  Did the user click the window close button?
    for event in pygame.event.get(
    ):  # every user input --> an event. This gets each of the events in a list.
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Create banana
        new_Banana = pygame.sprite.Sprite()
        # Call createBanana to add image, rectangle, speed
        createBanana(new_Banana,pygame.mouse.get_pos())
        all_sprites.add(new_Banana)
        #  Add the new banana to the group
        bananaGrp.add(new_Banana)
        # Updates banana position
        bananaUpdate(new_Banana)
      if event.type == KEYDOWN:
            # Check if the user clicked the escape key
            if event.key == K_ESCAPE:
                running = False
            if event.key==K_RETURN and status=='instructions':
                status='game'
                timer=0
      elif event.type == QUIT:  # The user clicked the x button
          running = False
      if event.type == ADDTIME:
          timer += 1
        #  Add a new spike?
      if event.type == ADDSPIKE and timer<10 and status=='game':
            #  Create the new spike
            new_spike = pygame.sprite.Sprite()
            # Call createSpike to add image, rectangle, and speed
            #This is level 1 so it will be at a slower speed
            createSpike_1(new_spike)
            # Add new spike to the spike group and to the all sprites group
            spikeGrp.add(new_spike)
            all_sprites.add(new_spike)
      #Add faster spikes in level 2 and 3
      if event.type == ADDSPIKE and timer >= 10 and status=='game':
        #  Create the new spike
        new_spike = pygame.sprite.Sprite()
        # Call createSpike to add image, rectangle, and speed
        createSpike_2(new_spike)
        # Add new spike to the spike group and to the all sprites group
        spikeGrp.add(new_spike)
        all_sprites.add(new_spike)

    #Add king spike in level 3
    if timer == 20 and len(kingspikeGrp) < 1:
      #  Create the king spike
      king_spike = pygame.sprite.Sprite()
      # Call createSpike to add image, rectangle, and speed
      createKing_Spike(king_spike)
      # Add king spike to the all sprites group
      kingspikeGrp.add(king_spike)
      all_sprites.add(king_spike)

    #Creates 5 hearts  
    if timer==20 and len(heartGrp)<5:
      # Create heart
      new_Heart = pygame.sprite.Sprite()
      # Call createBanana to add image, rectangle, speed
      createHeart(new_Heart,distance)
      #Add heart to all sprites 
      all_sprites.add(new_Heart)
      #  Add the new banana to the group
      heartGrp.add(new_Heart)
      #make the distance go up 
      distance+=50 
  
    # update player position based on mouse
    playerUpdate(player, pygame.mouse.get_pos())

    #show instructions
    if status == 'instructions':
      start(screen)

    elif status=='game':

      # Update position of each spike object
      for spike in spikeGrp:
          spikeUpdate(spike)

      #Updates position of each banana
      for banana in bananaGrp:
          bananaUpdate(banana)

      #Updates position of king_spike
      for king_spike in kingspikeGrp:
        king_spikeUpdate(king_spike)

      #  Check if any of the bananaGrp have collided with any of the spikeGrp
      col_banana_spike=pygame.sprite.groupcollide(bananaGrp, spikeGrp, True, True)

      #  Check if any of the spikeGrp have collided with the player
      col = pygame.sprite.spritecollideany(player, spikeGrp)
      if col is not None:
          col.kill()  # kill the spike it ate
          running = False
          status = 'lose'

      #  Check if the player has collided with the king spike
      col_ = pygame.sprite.spritecollideany(player, kingspikeGrp)
      if col_ is not None:
          col_.kill()  # kill the spike it ate
          running = False
          status = 'lose' 

      #  Check if any of the bananaGrp have collided with the king spike
      king_col=pygame.sprite.groupcollide(kingspikeGrp, bananaGrp, False, True)

      #The King spike has five lives, this will make sure it ies after five hits from the banana
      for king in king_col.keys():
        for banana in king_col[king]:
          king_colcounter+=1
          pygame.sprite.Group.sprites(heartGrp)[-1].kill()
      if king_colcounter==5:
        status='win'
        running=False

      #User starts in level 1
      if timer < 10:
          font = pygame.font.Font('freesansbold.ttf', 50)
          text = font.render('Level 1!', True, (255, 255, 255))
          textRect = text.get_rect()
          textRect.center = SCREEN_WIDTH / 2, 50

      # if timer reaches 10, user goes to level 2
      elif timer >= 10 and timer<20:
          font = pygame.font.Font('freesansbold.ttf', 50)
          text = font.render('Level 2!', True, (255, 255, 255))
          textRect = text.get_rect()
          textRect.center = SCREEN_WIDTH / 2, 50

      # if timer reaches 20, user goes to level 3
      elif timer >= 20:
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('Level 3!', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = SCREEN_WIDTH / 2, 50


      #  Draw the background
      # screen.fill((0,0,0)) # solid colour option
      screen.blit(bg, (0, 0))  # bg image displayed with top left corner at 0,0
      screen.blit(text, textRect)
      
      # if timer reaches 20, we display the health of King Spike
      if timer >= 20:
        font = pygame.font.Font('freesansbold.ttf', 25)
        health = font.render('King Spike Health:', True, (255, 255, 255))
        healthtextRect = health.get_rect()
        healthtextRect.center = 1075, 100
        screen.blit(health, healthtextRect)


      # Draw all sprites
      # draw is a built in method. We pass the display screen, and it will draw the sprites within the group
      # In order to draw the sprites, they must have an image attribute (.image -- this is a Surface) and a rect attribute (.rect)
      all_sprites.draw(screen)

      # Display the timer level
      font = pygame.font.Font('freesansbold.ttf', 25)
      text = font.render('Time: ' + str(timer), True, (255, 255, 255))
      textRect = text.get_rect()
      textRect.center = SCREEN_WIDTH / 2, 100
      screen.blit(text, textRect)

    #  Update the display
    pygame.display.update()

    #  Set framerate to 30 frames per second
    clock.tick(30)

# At end of game, display a win or lose screen
if status in ['win', 'lose']:
    end(status, screen)
    # User won't be able to close the game here.
    # This is annoying for the user, but done here just to show drawing a screen outside of the loop
    time.sleep(3)

# Quit
pygame.quit()