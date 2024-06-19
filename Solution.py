while not check_goal():
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