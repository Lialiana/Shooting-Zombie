# buttons

import pygame

WIDTH = 500
HEIGHT= 500
FPS   = 60

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

###
### MAIN
###
while True:
    time_now = pygame.time.get_ticks()   # milliseconds elapsed time 

    # Handle events
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # if the user pressed [space]
    if ( keys[pygame.K_SPACE] ):
        # When space is pushed move to the next item, but not more than every 300ms
        # So, has enough time elapsed since the last keypress?
        if ( time_now > next_change_time ):
            # enough time elapsed, un-select the current, and select the next menu-item
            menu[current_option].makeSelected( False )    
            current_option += 1
            if ( current_option >= len( menu ) ):
                current_option = 0
            menu[current_option].makeSelected( True )
            next_change_time = time_now + MENU_DELAY  # remember the time of the change

    # paint the screen
    screen.fill( GREEN )  # paint background

    # Paint the menu
    for item in menu:
        item.draw( screen );

    pygame.display.flip()
    clock.tick( FPS )       # keep a sane frame-rate