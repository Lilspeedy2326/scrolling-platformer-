import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('side-scrolling Game')
clock = pygame.time.Clock()

img = pygame.image.load("forest2.jpg").convert()

#globals
player = [100, 450, 0, 0] #xpos, ypos, xvel, yvel
platforms = [(500, 400), (700, 300), (900, 200), (1100, 300), (1300, 200), (1500, 100)]
isOnGround = False
offset = 0

def move_player():
      global isOnGround #needed to modify a global variable from within a function
      global offset
      isOnGround = False
      
      if player[1] > 520-50:
          player[1] = 520-50
          isOnGround = True
      #platform collision
      for i in range(len(platforms)):
          if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50< platforms[i][1]+50:
              isOnGround = True #stop gravity
              player[1]=platforms[i][1]-50 #rest player's feet
              player[3] = 0 #stop downward velocity
              #print("on platform") #for testing
                  
      if keys[pygame.K_LEFT]:
          if offset > 260 and player[0]>0: #check if you've reached the left edge of the map
              player[2] = -5 #update velocity
          
          elif player[0]>400 and offset < -1500: #check if we're on the far right edge of the map
              player[2] = -5 #let player get back to the center of the game screen
              
          elif player[0]>0: #if player is recentered, move the *offset*, not the player
              offset += 5
              player[2] = 0
              
          else:
              player[2]=0 #make sure motion is off (stop from going off edge)
              
      elif keys[pygame.K_RIGHT]:
          if offset < -1500 and player[0]<750: #check if you've reached the right edge of the map
              player[2] = 5 #update velocity
              
          elif offset >260 and player[0]<400:#check if we're on the far left edge of the map
              player[2] = 5 #let player get back to the center of the game screen
              
          elif player[0]<750:#if player is recentered, move the *offset*, not the player
              offset -= 5
              player[2] = 0
       
          else:
              player[2] = 0
      # Jump mechanics
      if isOnGround == True and keys[pygame.K_UP]:
          player[3] = -20 #player jumps
          isOnGround = False
          
      if isOnGround == False:
          player[3] += 1 #gravity
           
      player[0]+=player[2] #add x velocity to y position
      player[1]+=player[3] #add y velocity to y position
      
def draw_clouds():
    # Draw clouds in the backgound
    for x in range(100, 800, 300): # this loop controls WHERE and HOW MANY clouds are drawn
        for i in range(3): #draw 3 circles
            pygame.draw.circle(screen, (255, 255, 255), (x + offset/2, 100), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x - 50 + offset/2, 125), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x + 50 + offset/2, 125), 40)
        pygame.draw.rect(screen, (255, 255, 255), (x - 50 + offset/2, 100, 100, 65)) #flatten bottom
def draw_Tree():        
    for x in range(100, 800, 300,): # this loop controls WHERE and HOW MANY Trees are drawn
        for i in range(4): #draw 3 circles
            pygame.draw.circle(screen, (0, 180, 0), (x + offset, 290), 45)
            pygame.draw.circle(screen, (0, 180, 0), (x-50 + offset, 335), 45)
            pygame.draw.circle(screen, (0, 180, 0), (x+50 + offset, 335), 45)
        pygame.draw.rect(screen, (92, 64, 51), (x-5 + offset, 335, 15, 600)) #flatten bottom edge
        
def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))
        
running = True
while running: # Main game loop
    #input section
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    #physics section
    move_player()
    # Render section
    screen.fill((135, 206, 235)) # Sky blue background
    screen.blit(img,(0 + offset/4,0))
    draw_clouds() #function call
    draw_Tree()
    draw_platforms()
    pygame.draw.rect(screen, (0, 128, 0), (0, 525, 800, 80)) #flatten bottom edge
    pygame.draw.rect(screen, (255, 0, 255), (player[0], player[1], 50, 50)) #player
    pygame.draw.circle(screen, (255, 255, 0), (700, 85), 80)
    pygame.display.flip()
    
pygame.quit()
