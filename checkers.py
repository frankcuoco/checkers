
#PIECES - basic setup
"""
1,x = player 1's pieces
2,o = player 2's pieces
3,X = player 1 king piece
4,o = player 2 king piece

player 1 moves up and player 2 moves down
position typed as row,col
"""
pieces = [
[0, 2, 0, 2, 0, 2, 0, 2], 
[2, 0, 2, 0, 2, 0, 2, 0], 
[0, 2, 0, 2, 0, 2, 0, 2], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 1, 0, 1, 0, 1, 0], 
[0, 1, 0, 1, 0, 1, 0, 1], 
[1, 0, 1, 0, 1, 0, 1, 0]]

def pieceinsquare(player, pos): #checks if player's piece is in a square
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	if (pieces[row][col] == player) or (pieces[row][col] == player + 2):
		return True
	else:
		return False

def square_empty(pos): #checks if position of square is empty
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	return (pieces[row][col] == 0)		

def whatpiece(player, pos): #reports whether piece is normal or king
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	if pieces[row][col] == player:
		return "normal"
	elif pieces[row][col] == player + 2:
		return "king"

def valid_reg_move(player, pos, new): #only for regular pieces, not king pieces
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	if player == 1:
		if ((newrow,newcol) == (row-1,col-1)) or ((newrow,newcol) == (row-1,col+1)):
			return True
		else:
			return False
	if player == 2:
		if ((newrow,newcol) == (row+1,col-1)) or ((newrow,newcol) == (row+1,col+1)):
			return True
		else:
			return False		

def valid_king_move(pos, new): #checks if move is valid for king pieces
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	if ((newrow,newcol) == (row-1,col-1)) or ((newrow,newcol) == (row-1,col+1)) or ((newrow,newcol) == (row+1,col-1)) or ((newrow,newcol) == (row+1,col+1)):
		return True
	else:
		return False				

def reg_move(player, pos, new): #basis for regular piece moves
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	if (pieceinsquare(player, pos) == True) and (square_exists(new) == True):
		if player == 1:
			pieces[row][col] = 0
			pieces[newrow][newcol] = 1
		if player == 2:
			pieces[row][col] = 0
			pieces[newrow][newcol] = 2

def king_move(player, pos, new): #basis for king moves
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	if (pieceinsquare(player, pos) == True) and (square_exists(new) == True):
		if player == 1:
			pieces[row][col] = 0
			pieces[newrow][newcol] = 3
		if player == 2:
			pieces[row][col] = 0
			pieces[newrow][newcol] = 4
	
def square_exists(pos): #determines if square exists within board
    if (int(pos[0]) > 8) or (int(pos[0]) < 1) or (int(pos[2]) > 8) or (int(pos[2]) < 1):
        return False
    else:
        return True							

def pieceindiagonal(player, pos): #reports if opponents piece exists in diagonal square
    if player == 1:												
        possible_spaces = []
        possible_spaces.append(str(int(pos[0]) - 1) + "," + str(int(pos[2]) + 1))
        possible_spaces.append(str(int(pos[0]) - 1) + "," + str(int(pos[2]) - 1))
        available = [x for x in possible_spaces if square_exists(x)]
        for item in available:
            if whose_piece(item) == 2 or whose_piece(item) == 4:
                return True
        return False
    if player == 2:
        possible_spaces = []
        possible_spaces.append(str(int(pos[0]) + 1) + "," + str(int(pos[2]) + 1))
        possible_spaces.append(str(int(pos[0]) + 1) + "," + str(int(pos[2]) - 1))
        available = [x for x in possible_spaces if square_exists(x)]
        for item in available:
            if whose_piece(item) == 1 or whose_piece(item) == 3:									
                return True
        return False
    if player == 3 or player == 4:
        possible_spaces = []
        possible_spaces.append(str(int(pos[0]) - 1) + "," + str(int(pos[2]) + 1))
        possible_spaces.append(str(int(pos[0]) - 1) + "," + str(int(pos[2]) - 1))
        possible_spaces.append(str(int(pos[0]) + 1) + "," + str(int(pos[2]) + 1))
        possible_spaces.append(str(int(pos[0]) + 1) + "," + str(int(pos[2]) - 1))
        available = [x for x in possible_spaces if square_exists(x)]
        for item in available:
            if whose_piece(item) == 2 or whose_piece(item) == 4:
                return True
        return False

def whose_piece(pos): #reports which piece is in the given position
    return pieces[int(pos[0]) - 1][int(pos[2]) - 1]

def squareoverempty(pos): #reports if square over opponent's piece is empty, boolean
	row = int(pos[0])-1
	col = int(pos[2])-1
	piece = pieces[row][col]
	data = []
	diaglup = str(row-1)+","+str(col-1)
	diagrup = str(row-1)+","+str(col+1)
	diagldown = str(row+1)+","+str(col-1)
	diagrdown = str(row+1)+","+str(col+1)
	p2_diagonalleft = (pieceinsquare(2, diaglup) == True) or (pieceinsquare(4, diaglup) == True)
	p2_diagonalright = (pieceinsquare(2, diagrup) == True) or (pieceinsquare(4, diagrup) == True)
	p1_diagonalleft = (pieceinsquare(1, diagldown) == True) or (pieceinsquare(3, diagldown) == True)
	p1_diagonalright = (pieceinsquare(1, diagrdown) == True) or (pieceinsquare(3, diagrdown) == True)
	if piece == 1:
		if p2_diagonalleft:
			data.append((square_exists((row-2,col-2)) == True) and (square_empty((row-2,col-2)) == True))
		elif p2_diagonalright:
			data.append((square_exists((row-2,col+2)) == True) and (square_empty((row-2,col+2)) == True))
	elif piece == 2:
		if p1_diagonalleft:
			data.append((square_exists((row+2,col-2)) == True) and (square_empty((row+2,col-2)) == True))
		elif p1_diagonalright:
			data.append((square_exists((row+2,col+2)) == True) and (square_empty((row+2,col+2)) == True))
	elif (piece == 3) or (piece == 4):
		if p2_diagonalleft:
			data.append((square_exists((row-2,col-2)) == True) and (square_empty((row-2,col-2)) == True))
		if p2_diagonalright:
			data.append((square_exists((row-2,col+2)) == True) and (square_empty((row-2,col+2)) == True))
		if p1_diagonalleft:
			data.append((square_exists((row+2,col-2)) == True) and (square_empty((row+2,col-2)) == True))
		if p1_diagonalright:
			data.append((square_exists((row+2,col+2)) == True) and (square_empty((row+2,col+2)) == True))
	return (True in data)		
	
def valid_jump(player, pos, new): #basis for jump validity
	return ((pieceindiagonal(player, pos) == True))

def jump(player, pos, new): #single jump
	row = int(pos[0]) - 1
	col = int(pos[2]) - 1
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	midrow = int((row+newrow)/2)
	midcol = int((col+newcol)/2)
	pieces[midrow][midcol] = 0
	pieces[newrow][newcol] = pieces[row][col]
	pieces[row][col] = 0


def switchpiece(player, new): #switches regular piece to king when it reaches the other side of the board
	newrow = int(new[0]) - 1
	newcol = int(new[2]) - 1
	if player == 1:
		if newrow == 0:
			pieces[newrow][newcol] = 3
	if player == 2:
		if newrow == 7:
			pieces[newrow][newcol] = 4					

def valid_move(player, selected, move): #conditional validity
	if whatpiece(player, selected) == "normal":
		if valid_reg_move(player, selected, move):
			return True
		elif valid_jump(player, selected, move):
			return True
		elif (int(move[0])-1) == 0:        			
			return True
	if whatpiece(player, selected) == "king":
			if valid_king_move(selected, move):
				return True
	else:
		return False

#BOARD
def update_board(pieces):
	newboard = []
	for list in pieces:
		for i in list:
			if i == 0:
				newboard.append(".")
			if i == 1:
				newboard.append("x")
			if i == 2:
				newboard.append("o")
			if i == 3:
				newboard.append("X")
			if i == 4:
				newboard.append("O")
	newboard = " ".join(newboard)
	print("  1 2 3 4 5 6 7 8")
	print("1 " + newboard[:16])
	print("2 " + newboard[16:32])
	print("3 " + newboard[32:48])
	print("4 " + newboard[48:64])
	print("5 " + newboard[64:80])
	print("6 " + newboard[80:96])
	print("7 " + newboard[96:112])
	print("8 " + newboard[112:128])

board_setup = ("""
  1 2 3 4 5 6 7 8
1 . o . o . o . o 
2 o . o . o . o . 
3 . o . o . o . o 
4 . . . . . . . . 
5 . . . . . . . . 
6 x . x . x . x . 
7 . x . x . x . x 
8 x . x . x . x .
""")

#TEXT
intro = """
THIS IS A TWO PLAYER GAME OF CHECKERS
PLAYER 1 IS x AND PLAYER 2 IS o
TYPE IN POSITION OF PIECE AS ROW,COLUMN (ex. 3,2)
FOR IN DEPTH INSTRUCTIONS, TYPE HELP
"""
instructions = """
EACH PLAYER WILL TAKE TURNS MAKING A MOVE AND CAN MOVE A PIECE DIAGONALLY OR 
JUMP OVER THE OPPONENT'S PIECE. IF A PIECE CAN JUMP, IT MUST JUMP UNTIL IT RUNS
OUT OF JUMPS. JUMPING OVER THE OPPONENT'S PIECE WILL CAUSE THAT PIECE TO 
DISAPPEAR. WHEN A PIECE REACHES THE OPPOSITE SIDE OF THE BOARD IT BECOMES 
A KING PIECE THAT CAN MOVE FORWARD OR BACKWARD DIAGONALLY WITH THE SAME 
RULES OF A REGULAR PIECE. THE PLAYER WITH NO PIECES LEFT LOSES.

TYPE 'START' TO START: """
p1_prompt = "PLAYER 1, WHICH PIECE WOULD YOU LIKE TO MOVE? ENTER IN ROW,COLUMN FORMAT: "
p2_prompt = "PLAYER 2, WHICH PIECE WOULD YOU LIKE TO MOVE? ENTER IN ROW,COLUMN FORMAT: "
prompt2 = "WHERE WOULD YOU LIKE TO MOVE THAT PIECE TO? ENTER IN ROW,COLUMN FORMAT: "

#GAME
print("WELCOME TO CHECKERS")
game = True
print(intro)
command = input("""WOULD YOU LIKE TO START THE GAME OR READ THE INSTRUCTIONS? 
(PLEASE TYPE START OR HELP): """)
if command == "HELP":
	command = input(instructions)
if command == "START": #FOREVER LOOP HERE
	print(board_setup)
	while game == True:
		#END GAME
		data1 = []
		data2 = []
		for i in range(0, 8):
			data1.append((1 in pieces[i]) or (3 in pieces[i]))
			data2.append((2 in pieces[i]) or (4 in pieces[i]))
		if (True in data1) and (True in data2):
			game = True
		elif (True in data1) and not(True in data2):
			game = False
			print("PLAYER 1 WINS")
		elif not(True in data1) and (True in data2):
			game = False
			print("PLAYER 2 WINS")

		#PLAYER 1
		selected = input(p1_prompt)
		move = input(prompt2)
		while not(valid_move(1, selected, move)):
			print("THAT IS NOT A VALID MOVE, TRY AGAIN.")
			selected = input(p1_prompt)
			move = input(prompt2)
		if whatpiece(1, selected) == "normal":
			if valid_reg_move(1, selected, move):
				reg_move(1, selected, move)	
			if valid_jump(1, selected, move):
				jump(1, selected, move)
			if (int(move[0])-1) == 0:        
				switchpiece(1, move)
		if whatpiece(1, selected) == "king":
			if valid_king_move(selected, move):
				king_move(1, selected, move)
		update_board(pieces)		

		#PLAYER 2
		selected2 = input(p2_prompt)
		move2 = input(prompt2)
		while not(valid_move(2, selected2, move2)):
			print("THAT IS NOT A VALID MOVE, TRY AGAIN.")
			selected2 = input(p2_prompt)
			move2 = input(prompt2)
		if whatpiece(2, selected2) == "normal":
			if valid_reg_move(2, selected2, move2):
				reg_move(2, selected2, move2)
			if valid_jump(2, selected2, move2):
				jump(2, selected2, move2)
			if (int(move2[0])-1) == 7:
				switchpiece(2, move2)
		if whatpiece(2, selected2) == "king":
			if valid_king_move(selected2, move2):
				king_move(2, selected2, move2)
		update_board(pieces)





