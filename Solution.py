

collect_coin()
    
while not goal_reached():
	if goal_reached():
		# Stop moving once the goal is reached
		break
	
	if can_move_forward():
		move()
		collect_coin()  # Collect coin at the new position
	else:
		rotate_left()  # Rotate left if forward movement is blocked

while not check_goal():

	collect_coin()
	
	rotate_right()


	while not can_move_forward():
		rotate_left()
        
	move()



while not goal_reached():
	if can_move_forward():
		move()
	else: 
		rotate_left()


while True: 
	if can_move_forward(): 
		move() 
	else: 
		rotate_right() 
		
		if can_move_forward(): 
			move() 
		else: 
			rotate_left() 
			rotate_left() 
			if can_move_forward(): move() else: rotate_right()