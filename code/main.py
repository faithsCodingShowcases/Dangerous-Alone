import pygame, sys
from settings import *
from level import Level


#last stopped at 1hour 12min
class Game:
	def __init__(self):
		  
		# Initialize
		pygame.init() 
		# Display window
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH)) #Sets widow to specific hight/width
		# Window Name
		pygame.display.set_caption('Its Dangerous to go Alone') #title bar
		self.clock = pygame.time.Clock()

		self.level = Level() #instant of level file

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1) #plays sound in  loop
	
	def run(self): #function to run the game
		while True:
			for event in pygame.event.get(): #gets the events
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()
					
			self.screen.fill(BACKGROUND_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__': #makes the game run
	game = Game()
	game.run() 
