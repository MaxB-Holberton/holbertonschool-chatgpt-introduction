def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def game_is_tied(board):
	for col in range(len(board[0])):
		for row in range(len(board[0])):
			if board[row][col] == " ":
				return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	while True:
		print_board(board)
		try:
			row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
			if row not in range(3):
				print("invalid input, please enter (0, 1 or 2)")
				continue
			col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
			if col not in range(3):
				print("invalid input, please enter (0, 1 or 2)")
				continue
		except ValueError:
			print("invalid input, please enter a integer")
			continue

		if board[row][col] != " ":
			print("That spot is already taken! Try again.")
			continue

		board[row][col] = player
		if check_winner(board):
			print_board(board)
			print("Player " + player + " wins!")
			break
		if game_is_tied(board):
			print_board(board)
			print("The game is tied!")
			break

		if player == "X":
			player = "O"
		else:
			player = "X"

tic_tac_toe()
