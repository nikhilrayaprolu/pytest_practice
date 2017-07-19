from Board import Board
from scores import Score
board=Board()
class TestBoard():
	def test_initialconditions1(self):
		assert board.FPS == 25
	def test_initialconditions2(self):
		assert board.WINDOWWIDTH == 640
	def test_initialconditions3(self):
		assert board.WINDOWHEIGHT == 480
	def test_initialconditions4(self):
		assert board.BOXSIZE == 20
	def test_initialconditions5(self):
		assert board.BOARDWIDTH == 10
	def test_initialconditions6(self):
		assert board.BOARDHEIGHT == 20
	def test_initialconditions7(self):
		assert board.BLANK == '.'
	def test_initialconditions8(self):
		assert board.XMARGIN == int((board.WINDOWWIDTH -board.BOARDWIDTH *board.BOXSIZE) / 2)
	def test_initialconditions9(self):
		assert board.TOPMARGIN == board.WINDOWHEIGHT - (board.BOARDHEIGHT *board.BOXSIZE) - 5
	def test_initialconditions10(self):
		assert board.TEMPLATEWIDTH == 5
	def test_initialconditions11(self):
		assert board.TEMPLATEHEIGHT == 5

	def test_pygameColors1(self):
		assert board.WHITE       == (255, 255, 255)
	def test_pygameColors2(self):
		assert board.GRAY        ==(185, 185, 185)
	def test_pygameColors3(self):
		assert board.BLACK       == (  0,   0,   0)
	def test_pygameColors4(self):
		assert board.RED         == (155,   0,   0)
	def test_pygameColors5(self):
		assert board.LIGHTRED    == (175,  20,  20)
	def test_pygameColors6(self):
		assert board.GREEN       == (  0, 155,   0)
	def test_pygameColors7(self):
		assert board.LIGHTGREEN  == ( 20, 175,  20)
	def test_pygameColors8(self):
		assert board.BLUE        == (  0,   0, 155)
	def test_pygameColors9(self):
		assert board.LIGHTBLUE   == ( 20,  20, 175)
	def test_pygameColors10(self):
		assert board.YELLOW      == (155, 155,   0)
	def test_pygameColors11(self):
		assert board.LIGHTYELLOW == (175, 175,  20)
	def test_pygameColors12(self):
		assert board.BORDERCOLOR == board.BLUE
	def test_pygameColors13(self):
		assert board.BGCOLOR == board.BLACK
	def test_pygameColors14(self):
		assert board.TEXTCOLOR == board.WHITE
	def test_pygameColors15(self):
		assert board.TEXTSHADOWCOLOR == board.GRAY
	def test_pygameColors16(self):
		assert board.COLORS      == (     board.BLUE,      board.GREEN,      board.RED,      board.YELLOW)
	def test_pygameColors17(self):
		assert board.LIGHTCOLORS == (board.LIGHTBLUE, board.LIGHTGREEN, board.LIGHTRED, board.LIGHTYELLOW)


	def test_initialboard(self):
		board.board = []
		initialboard=board.InitialBoard()
		initialrow=[board.BLANK] * board.BOARDHEIGHT
		for i in range(board.BOARDWIDTH):
			assert initialboard[i]==initialrow

	def test_removeCompleteLines(self):
		board.InitialBoard()
		for i in range(board.BOARDWIDTH):
			board.board[i][2]='O'
		number=board.removeCompleteLines(board.board)
		assert number==1
	def test_isCompleteLine(self):
		board.InitialBoard()
		for i in range(board.BOARDWIDTH):
			board.board[i][2]='O'
		assert board.isCompleteLine(board.board,2)==True
	def test_isOnBoard1(self):
			value=board.isOnBoard(0,0)
			assert value==True
	def test_isOnBoard2(self):
			value=board.isOnBoard(10,20)
			assert value==False
	def test_isOnBoard3(self):
			value=board.isOnBoard(11,20)
			assert value==False
	def test_isOnBoard4(self):
			value=board.isOnBoard(10,19)
			assert value==False




	
