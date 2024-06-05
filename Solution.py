while not check_goal():
	rotate_right()


	while not can_move_forward():
		rotate_left()
        
	move()