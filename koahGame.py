#koah video game
#import/initialize libraries
import pygame
pygame.init()
import random
import time

#define colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

#score text
score = 0

#This class represents the sprites
class Sprite(pygame.sprite.Sprite):

    #---Attributes---
    #this is radius for group koah circle detection
    radius = 50

    #constructor. Pass in image/color,x and y
    def __init__(self,fill,width,height): 

        #call pygame's sprite constructor
        pygame.sprite.Sprite.__init__(self)

        #create/fill graphic of block
        self.image = pygame.Surface([width,height])
        if fill == koahPic:
            print ("pooop")
            screen.blit(fill,(30,30))
        else:
            print ("noon")
            self.image.fill(fill)

        #fetch rect w/ dims of graphic
        #Update with positions
        self.rect = self.image.get_rect()


#dims of screen + koah
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])
koahPic = pygame.image.load("koahSprite.png").convert()

#list of toys
toy_list = pygame.sprite.RenderPlain()

#list of toys and koah
all_sprites_list = pygame.sprite.RenderPlain()

#Toy distro behaivor
for i in range(50):
    #this is a toy
    toy = Sprite(red,20,15)

    #place toys randomly
    toy.rect.x = random.randrange(screen_width)
    toy.rect.y = random.randrange(screen_height)

    toy_list.add(toy)
    all_sprites_list.add(toy)

#Create Koah

koah = Sprite(koahPic,30,30)
all_sprites_list.add(koah)
koah.xspeed = 0
koah.yspeed = 0

#speed at which sprites move
speed = 2
mod=1

#Loop until close button clicked
done = False

#Clock to update screen
clock = pygame.time.Clock()

#Print Intro Text : Not In Final
def intro():
    print("This is Koah's Big Adventure!")
    pygame.time.wait(3000)
    print("Koah's toys have come to life")
    pygame.time.wait(2000)
    print("Now they're running away!")
    pygame.time.wait(2000)
    print("Help Koah catch his toys--move him with the arrow keys!")
    pygame.time.wait(3000)
    print("Catch as many as you can in 20 seconds")
    pygame.time.wait(3000)
    print("Three")
    pygame.time.wait(1000)
    print("Two")
    pygame.time.wait(1000)
    print("One")
    pygame.time.wait(1000)
    print("Go!")
    pygame.time.wait(1000)

intro()

#intro text function
def txt(text,time):
    initText = initFont.render(text, False, red)
    screen.blit(initText,[40,40])
    pygame.display.flip()
    pygame.time.wait(time)

intro = True
while intro == True:
    initFont = pygame.font.SysFont("Times New Roman",60)
    txt("Hello!",2000)
    
    intro = False
    

#Time at beginning
time1 = time.time()

#--------- Main Program Loop -------------
while done == False:
    for event in pygame.event.get(): #Used did something
        if event.type == pygame.QUIT: #User clicked close
            done = True # Exit while loop!

        #----Control Koah with keyboard----
  
        #When user presses down X key
        #koah moves Y direction with velocity
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                koah.yspeed = -(speed + mod)
            if event.key == pygame.K_DOWN:
                koah.yspeed = speed + mod
            if event.key == pygame.K_LEFT:
                koah.xspeed = -(speed + mod)
            if event.key == pygame.K_RIGHT:
                koah.xspeed = speed + mod

        #When user releases  X key, Y speed = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                koah.yspeed = 0
            if event.key == pygame.K_DOWN:
                koah.yspeed = 0
            if event.key == pygame.K_LEFT:
                koah.xspeed = 0
            if event.key == pygame.K_RIGHT:
                koah.xspeed = 0


    #Clear the screen
    screen.fill(white)

    #update koah
    koah.rect.x += koah.xspeed
    koah.rect.y += koah.yspeed

    #screen wrap around for koah
    if koah.rect.y > screen_height:
        koah.rect.y = screen_height - koah.rect.y
    if koah.rect.x > screen_width:
        koah.rect.x = screen_width - koah.rect.x
    if koah.rect.y < -3:
        koah.rect.y = koah.rect.y + screen_height - 5
    if koah.rect.x < -3:
        koah.rect.x = koah.rect.x + screen_width - 5

    #Get the current mouse position as 2 nums in list : Not in Final
    #pos=pygame.mouse.get_pos()

    #Fetch the x any y out of the list -- set playerpos to it :Not in Final
    #koah.rect.x=pos[0]
    #koah.rect.y=pos[1]

    #see if player block has collided with anything
    toy_hit_list = pygame.sprite.spritecollide(koah,toy_list, True)
    
    #toy control loop
    for toy in toy_list:

        #give toys random velocity and direction
        toy.rect.x += random.randrange(3)*random.randrange(-3,3)
        toy.rect.y += random.randrange(3)*random.randrange(-3,3)
        
        #see if koah is nearby, and adjust pos accordingly
        toy_detect_koah = pygame.sprite.collide_circle(koah,toy)

        #Move Toys away from koah
        if toy_detect_koah == True:
            if toy.rect.y < koah.rect.y:
                toy.rect.y -= speed
            if toy.rect.y > koah.rect.y:
                toy.rect.y += speed
            if toy.rect.x < koah.rect.x:
                toy.rect.x -= speed
            if toy.rect.x > koah.rect.x:
                toy.rect.x += speed

        #screen wrap around for toys
        if toy.rect.y > screen_height:
            toy.rect.y = screen_height - toy.rect.y
        if toy.rect.x > screen_width:
            toy.rect.x = screen_width - toy.rect.x
        if toy.rect.y < -3:
            toy.rect.y = toy.rect.y + screen_height - 5
        if toy.rect.x < -3:
            toy.rect.x = toy.rect.x + screen_width - 5

    #draw all the sprites
    all_sprites_list.draw(screen)

    #Create Scorekeeping
    if len(toy_hit_list) > 0:
        score += len(toy_hit_list)
        print "toy number", score

    #Check Time and end game, replay option -- implement later
    time2 = time.time()
    if time2 - time1 > 20:
        print("Done!!!")
        print "You caught", score, "toys"
        done = True
        pygame.time.wait(1000)
        print "This Game By Max Caldwell"
        pygame.time.wait(1000)
        print "Dedicated to Keith Caldwell"
        pygame.time.wait(1000)
        print
        print "Happy Father's Day!"
        print "I love you"
        
    
    #limit to 20 fps
    clock.tick(20)

    #update the screen
    pygame.display.flip()

pygame.quit()
