#TODO Use the Map classes personal (x,y) coordinates that matches array's to help locate node in double array.
# As node is clicked, update in array too.

from maps import *

#Create a window

# import the pygame module 
import pygame 
import pygame_gui
import PygameHelpers
from PygameHelpers import *

pygame.init()
# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 

screen = pygame.display.set_mode((width, height))



  
# Set the caption of the screen 
pygame.display.set_caption('Shortest Path') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True







# Map Initialization code ----------------------------
d_map = Map(30, 10,10)
PygameHelpers.NODE_SCALER=10
update_nodes(d_map, PygameHelpers.node_groups)     




has_updated = True
trapped = False

#------------------------------------------------------


#UI ELEMENTS
#-------------------------------------------------
manager = pygame_gui.UIManager((width, height))

clock = pygame.time.Clock()

# button_layout_rect = pygame.Rect(0,0,100,50)
# button_layout_rect.bottomleft = (30, -50)
# generate_random = pygame_gui.elements.UIButton(text="generate", relative_rect=button_layout_rect, manager=manager)
hello_rect = pygame.Rect((400,height-100), (100,50))

hello_button = pygame_gui.elements.UIButton(relative_rect=hello_rect, text="generate", manager=manager)
hello_rect = pygame.Rect((400,height-50), (100,50))
shortest_path = pygame_gui.elements.UIButton(relative_rect=hello_rect, text="shortest path", manager=manager)
hello_rect = pygame.Rect((400,height-150), (100,50))
clear_path = pygame_gui.elements.UIButton(relative_rect=hello_rect, text="clear path", manager=manager)

gen_hw =9
obstacles = 40

previous_start = (0,0)
start_pos = (0,0)
end_pos = (gen_hw - 1, gen_hw - 1)

setStart = True

#-------------------------------------------------

# game loop 
while running: 
 
    
    if has_updated:
        screen.fill(color=(255, 209, 233))
        for group in PygameHelpers.node_groups:
            
            group.draw(screen)
        
        
        has_updated = False
    

    

    
# for loop through the event queue   
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            #Find which square
            clicked_node = PygameHelpers.findClickedNode(x,y)

            if clicked_node != None:
                print("pos: " + str(clicked_node.pos))
                d_map.update_coord(clicked_node.pos[0], clicked_node.pos[1], "O")
                previous_start = start_pos
                start_pos = clicked_node.pos
                d_map.__reset__()
                
                
                clicked_node.change_color((255, 0, 0))
                get_node(previous_start).change_color((0,0,255))
                has_updated=True
                
                print("found node!")
            
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                # generate based on gen_hw
                PygameHelpers.NODE_SCALER = gen_hw
                d_map = generate_new_random_map(gen_hw, obstacles)
                update_nodes(d_map, PygameHelpers.node_groups)
                print("-----" + str(PygameHelpers.node_groups))
                has_updated = True
                trapped=False
        
            if event.ui_element == shortest_path:
                
                trapped = d_map.find_shortest_path(start_pos, end_pos)
                
                
                if trapped:
                    d_map.__reset__()
                    print("trapped!")
                
                update_nodes(d_map, PygameHelpers.node_groups)
                
                has_updated = True

            
            if event.ui_element == clear_path:
                d_map.__reset__()
                update_nodes(d_map, PygameHelpers.node_groups)
                has_updated = True
                

                

        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(screen)
    
    
    pygame.display.flip()
    pygame.display.update()
    
















                













