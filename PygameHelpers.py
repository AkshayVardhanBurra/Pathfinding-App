import pygame

#Number of nodes
NODE_SCALER = 9

width = 500
height = 500

alloted_width = (0.80) * width
alloted_height = (0.80) * height

class Node(pygame.sprite.Sprite):
    def __init__(self, color, pos, x,y, w, h):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
    
    def change_color(self, color):
        self.image.fill(color)
    
node_groups = []


def update_nodes(p_map, nodes):
    y_pos = 0

    #deleting nodes
    nodes.clear()

    
    for i in range(len(p_map.map)):
        node_group = pygame.sprite.Group()
        
        for a in range(len(p_map.map[i])):
            if p_map.map[i][a] == "O" or p_map.map[i][a] == "#":
                node_group.add(Node((0,0,200),(a, i) ,a * (alloted_width/NODE_SCALER), y_pos, alloted_width/NODE_SCALER - 3, alloted_height/NODE_SCALER - 3))
            elif p_map.map[i][a] == "S":
                node_group.add(Node((0,255,0),(a, i) ,a * (alloted_width/NODE_SCALER), y_pos, alloted_width/NODE_SCALER - 3, alloted_height/NODE_SCALER - 3))
            else:
                node_group.add(Node((0,0,0),(a, i) ,a * (alloted_width/NODE_SCALER), y_pos, alloted_width/NODE_SCALER - 3, alloted_height/NODE_SCALER - 3))
        nodes.append(node_group)
        y_pos += alloted_height/NODE_SCALER

def findClickedNode(x, y):
    
    
    # for i in range(0, len(node_groups)):
    #     # for node in group:
    #     #     print(f"({node.pos}): {node.rect.left}, {node.rect.top}")
    #     #     if node.rect.collidepoint(x,y):
    #     #         return node
        
    #     print(node_groups[i])
    #     return None

    for group in node_groups:

        for node in group:
            if node.rect.collidepoint(x,y):
                return node
            
    return None


def get_node(pos):
    return node_groups[pos[1]].sprites()[pos[0]]




