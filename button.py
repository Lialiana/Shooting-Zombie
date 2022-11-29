import pygame
import math 

class Button():
	def __init__(self,x, y, image, scale, text=None, xoff=None):
		self.width = int(image.get_width() * scale)
		self.height = int(image.get_height() * scale)
		self.image = pygame.transform.scale(image, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

MENU_DELAY = 200

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = ( 20, 180,  20)

pygame.init()
screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption( "Menuosity" )

font  = pygame.font.Font( None, 32 )  # font used to make menu Items
                

class MenuItem:
    """ Simple sprite-like object representing a Menu Button """
    def __init__( self, label ):
        super().__init__()
        self.image    = pygame.Surface( ( 200, 50 ) )   # long rectangle
        self.rect     = self.image.get_rect()
        self.label    = label.strip().capitalize()
        self.selected = False
        self.fore     = BLACK
        self.back     = WHITE
        self.makeImage( self.fore, self.back )

    def makeImage( self, foreground, background ):
        """ Make the image used for the menu item, in the given colour """
        self.image.fill( background )
        pygame.draw.rect( self.image, foreground, [0, 0, self.image.get_width(), self.image.get_height()], 3 )

        # centred text for Label
        text = font.render( self.label, True, foreground )
        text_centre_rect = text.get_rect( center = self.image.get_rect().center )
        self.image.blit( text, text_centre_rect )

    def moveTo( self, x, y ):
        """ Reposition the menu item """
        self.rect.x = x
        self.rect.y = y

    def makeSelected( self, selected=True ):
        """ If the button is selected, invert it's colours """
        if ( self.selected != selected ):
            # Only re-generate if different
            if ( selected ):
                self.makeImage( self.back, self.fore )  # inverted colours on selection
            else:
                self.makeImage( self.fore, self.back )  # non-selected, normal colours
        self.selected = selected

    def draw( self, surface ):
        """ Paint the item on the given surface """
        surface.blit( self.image, self.rect )



### Create a Menu of Items
menu = []
menu.append( MenuItem( "First Item" ) )
menu.append( MenuItem( "Second Item" ) )
menu.append( MenuItem( "Third Item" ) )
menu.append( MenuItem( "Fourth Item" ) )

### Highlight the first item
current_option = 0
menu[0].makeSelected()

### Lay-out the menu
for i,item in enumerate( menu ):
    item.moveTo( 150, 50 + ( i * 80 ) )   # spread out in a single column

### Used to slow down the UI Changes
clock = pygame.time.Clock()
next_change_time = 0  

	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

    # paint the screen
    screen.fill( GREEN )  # paint background

		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))
		if self.text:
			self.image.blit(self.text, (self.width//2 - self.xoff, self.height//2 - self.yoff))

		return action