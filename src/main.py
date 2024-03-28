# Micromouse - Comsoc x LTU Robotics club Prototype

from map_nodes import node

def rotate_left(angle = 90):
    # Moves the mouse to the left by 90 degrees
    return

def rotate_right(angle = 90):
    # Moves the mouse to the right by 90 degrees
    return

def move_forward():
    # Moves forward 1 unit
    return

def scan_left():
    # See if we can go to the left
    can_move = False

    # Sensor input


    return can_move

def scan_forward():
    # See if we can go to the forward
    can_move = False

    # Sensor input

    return can_move

def scan_right():
    # See if we can go to the right
    can_move = False

    # Sensor input

    
    return can_move

def main_scan():
    scan_list = []
    scan_list.append(scan_left())
    scan_list.append(scan_forward())
    scan_list.append(scan_right())
    
    # Format: Left, forward, right

    return scan_list

def map_initialisation():
    # Maps the whole play area
    
    # Map size
    map_size = 16
    map_length = map_size ** 2

    x = 3
    y = 4
    i = x + 16 * y
    map_nodes[i]

    x = i % 16
    y = i / 16
    
    # List init
    map_nodes = []
    for y in range(map_size):
        row = []
        for x in range(map_size):
            row.append(None)
        map_nodes.append(row)

    #for i in range(map_length):
    #    x = i % 16
    #    y = i / 16
    #    map_nodes.append(new_node(x, y))
    #    [[1,2],
    #     [3, 4]]
    #   
    #    [1, 2, 3, 4]
    
    # Scanning phase
    # Temporary while true until we figure out the goal exception
    
    # Node location
    node_x = 0
    node_y = 0
    current_angle = 90
    movement_log = []

    for current_node_number in range(pow(map_size,2)):

        scan_results = main_scan()
        map_nodes[node_x][node_y] = node(scan_results, current_node_number)

        # Moving
        if scan_results[0] == True:
            rotate_left()
            move_forward()
            if current_angle == 180:
                node_x -= 1
                movement_log.append("Moved X -1")
            elif current_angle == 90:
                node_y += 1
                movement_log.append("Moved Y +1")
            elif current_angle == 0:
                node_x += 1
                movement_log.append("Moved X +1")
            elif current_angle == 270:
                node_y -= 1
                movement_log.append("Moved Y -1")

        elif scan_results[1] == True:
            move_forward()
            if current_angle == 90:
                node_y += 1
            elif current_angle == 180:
                node_x -= 1
            elif current_angle == 0:
                node_x += 1
            elif current_angle == 270:
                node_y -= 1
        elif scan_results[2] == True:
            rotate_right()
            move_forward()
            if current_angle == 90:
                node_x += 1
            elif current_angle == 180:
                node_y -= 1
            elif current_angle == 0:
                node_y += 1
            elif current_angle == 270:
                node_x -= 1
        else:
            # Move back
            rotate_right(180)
            move_forward()
            if current_angle == 90:
                node_y -= 1
            elif current_angle == 180:
                node_x += 1
            elif current_angle == 0:
                node_x -= 1
            elif current_angle == 270:
                node_y += 1
            # Implement search algorithm to go back to the
                
        


    return map_nodes

# Main code section
first = node(3, None)

# A* search algorithm