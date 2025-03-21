#Added To github!

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
  



# CONSTANTS ------------------------------------


#------------------------------------------------

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

slider_rect = pygame.Rect((200, height - 100), (200, 50))
size_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect, value_range=(3,15), start_value=9)
size_slider.set_current_value(9)
size_ui_rect = pygame.Rect((50, height - 100), (150,50))
size_ui = pygame_gui.elements.UILabel(size_ui_rect, text = "Size: 9 x 9")
obstacle_rect = pygame.Rect((200, height - 50), (200, 50))
obstacle_ui_rect = pygame.Rect((50, height - 50), (150,50))
obstacle_ui = pygame_gui.elements.UILabel(obstacle_ui_rect, text = "Obstacles: 40")



obstacle_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=obstacle_rect, value_range=(0,81 - 20), start_value = 0)
obstacle_slider.set_current_value(40)
previous_range = obstacle_slider.value_range
previous_value = obstacle_slider.get_current_value()

gen_hw =9
obstacles = 40
previous_start = (-1,-1)
start_pos = (-1,-1)
previous_end = (-1, -1)
end_pos = (-1, -1)

setStart = True
has_cleared = False

#-------------------------------------------------

#Methods------------------------------------------

def reset_clicked_areas():
    global previous_start
    global previous_end
    global start_pos
    global end_pos

    previous_start = (-1,-1)
    previous_end = (-1, -1)
    start_pos = (-1,-1)
    end_pos = (-1,-1)

def compare_coords(t1, t2):
    return t1[0] == t2[0] and t1[1] == t2[1]
       

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
                print(clicked_node.color)
                
                
                if pygame.mouse.get_pressed()[0] and not compare_coords(clicked_node.pos,start_pos) and not compare_coords(clicked_node.pos, end_pos):
                    d_map.update_coord(clicked_node.pos[0], clicked_node.pos[1], "O")
                    previous_start = start_pos
                    start_pos = clicked_node.pos
                    
                    
                    
                    clicked_node.change_color(PygameHelpers.START_COLOR)
                    if previous_start[0] != -1:
                        get_node(previous_start).change_color((0,0,200))
                    has_updated=True
                    PygameHelpers.reset_colors((0,255,0))
                    
                    
                elif pygame.mouse.get_pressed()[2] and not compare_coords(clicked_node.pos,start_pos) and not compare_coords(clicked_node.pos, end_pos) :
                    print("right clicked!")
                    d_map.update_coord(clicked_node.pos[0], clicked_node.pos[1], "O")
                    previous_end = end_pos
                    end_pos = clicked_node.pos
                    d_map.__reset__()
                    
                    
                    clicked_node.change_color(PygameHelpers.END_COLOR)
                    if previous_end[0] != -1:
                        get_node(previous_end).change_color((0,0,200))
                    has_updated=True
                    PygameHelpers.reset_colors((0,255,0))
                    

                print("found node!")

                
            
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                # generate based on gen_hw
                PygameHelpers.NODE_SCALER = gen_hw
                d_map = generate_new_random_map(gen_hw, obstacles)
                update_nodes(d_map, PygameHelpers.node_groups)
                print("-----" + str(PygameHelpers.node_groups))
                reset_clicked_areas()
                
                has_updated = True
                trapped=False
        
            if event.ui_element == shortest_path and start_pos[0] != -1 and end_pos[0] != -1:
                
                trapped = d_map.find_shortest_path(start_pos, end_pos)
                
                
                if trapped:
                    d_map.__reset__()
                    print("trapped!")
                
                update_nodes(d_map, PygameHelpers.node_groups)
                reset_clicked_areas()
                has_updated = True

            
            if event.ui_element == clear_path:
                d_map.__reset__()
                reset_clicked_areas()
                print(start_pos)
                print(end_pos)
                update_nodes(d_map, PygameHelpers.node_groups)
                has_updated = True
        
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == size_slider:
                gen_hw = size_slider.get_current_value()
                PygameHelpers.NODE_SCALER = gen_hw
                print(size_slider.get_current_value())

                
                obstacle_slider.value_range = (0, round(0.8 * (gen_hw * gen_hw)))
                obstacles = round((previous_value/previous_range[1]) * obstacle_slider.value_range[1])
                print(previous_value/previous_range[1])

                print(f" obstacles new range: {obstacle_slider.value_range}, obstacle curr value {obstacles}")

            if event.ui_element == obstacle_slider:
                previous_range = obstacle_slider.value_range
                previous_value = obstacle_slider.get_current_value()
                obstacles = obstacle_slider.get_current_value()
                print(f"obstacle curre value: {obstacles}")

                

        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(screen)
    
    
    pygame.display.flip()
    pygame.display.update()
    
















                













