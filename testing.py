from maps import *


gen_hw =9
obstacles = 40
d_map = Map(obstacles, gen_hw,gen_hw)

d_map.map[0][0]= "O"
d_map.map[gen_hw-1][gen_hw - 1]= "O"
d_map.map[4][1] = "O"

d_map.find_shortest_path((1,4), (gen_hw - 1, gen_hw - 1))
d_map.print_map()