from Block import Block

blocks=Block()
class TestBlocks():
	def test_initial_S_SHAPE_TEMPLATE(self):
		assert blocks.S_SHAPE_TEMPLATE == [['.....',
	                     '.....',
	                     '..OO.',
	                     '.OO..',
	                     '.....'],
	                    ['.....',
	                     '..O..',
	                     '..OO.',
	                     '...O.',
	                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.Z_SHAPE_TEMPLATE == [['.....',
		                     '.....',
		                     '.OO..',
		                     '..OO.',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '.OO..',
		                     '.O...',
		                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.I_SHAPE_TEMPLATE == [['..O..',
		                     '..O..',
		                     '..O..',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     'OOOO.',
		                     '.....',
		                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.O_SHAPE_TEMPLATE == [['.....',
		                     '.....',
		                     '.OO..',
		                     '.OO..',
		                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.J_SHAPE_TEMPLATE == [['.....',
		                     '.O...',
		                     '.OOO.',
		                     '.....',
		                     '.....'],
		                    ['.....',
		                     '..OO.',
		                     '..O..',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     '.OOO.',
		                     '...O.',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '..O..',
		                     '.OO..',
		                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.L_SHAPE_TEMPLATE == [['.....',
		                     '...O.',
		                     '.OOO.',
		                     '.....',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '..O..',
		                     '..OO.',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     '.OOO.',
		                     '.O...',
		                     '.....'],
		                    ['.....',
		                     '.OO..',
		                     '..O..',
		                     '..O..',
		                     '.....']]
 	def test_initial_Z_SHAPE_TEMPLATE(self):
		assert blocks.T_SHAPE_TEMPLATE == [['.....',
		                     '..O..',
		                     '.OOO.',
		                     '.....',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '..OO.',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '.....',
		                     '.OOO.',
		                     '..O..',
		                     '.....'],
		                    ['.....',
		                     '..O..',
		                     '.OO..',
		                     '..O..',
		                     '.....']]
	def test_PIECES(self):
		blocks.PIECES = {'S': blocks.S_SHAPE_TEMPLATE,
      'Z': blocks.Z_SHAPE_TEMPLATE,
      'J': blocks.J_SHAPE_TEMPLATE,
      'L': blocks.L_SHAPE_TEMPLATE,
      'I': blocks.I_SHAPE_TEMPLATE,
      'O': blocks.O_SHAPE_TEMPLATE,
      'T': blocks.T_SHAPE_TEMPLATE}	
	def test_getnewpieceshape(self):
		newpiece=blocks.getNewPiece()
		print newpiece
		assert newpiece['shape'] in blocks.PIECES
	
	def test_getnewrotation(self):
		newpiece=blocks.getNewPiece()
		print newpiece
		assert newpiece['rotation'] in [0,1,2,3]
	def test_getnewy(self):
		newpiece=blocks.getNewPiece()
		print newpiece
		assert newpiece['y']==-2


	def test_moveLeft(self):
		initialx=blocks.fallingPiece['x']
		blocks.moveLeft()
		finalx=blocks.fallingPiece['x']
		assert finalx==initialx-1
	def test_moveRight(self):
		initialx=blocks.fallingPiece['x']
		blocks.moveRight()
		finalx=blocks.fallingPiece['x']
		assert finalx==initialx+1
	def test_Rotate(self):
		initialrotation=blocks.fallingPiece['rotation']
		blocks.Rotate(2);
		finalrotation=blocks.fallingPiece['rotation']
		assert finalrotation==(initialrotation+2)%2
	def test_Rotateafter20times(self):
		initialrotation=blocks.fallingPiece['rotation']
		t=20
		while t:
			blocks.Rotate(1)
			t=t-1
		finalrotation=blocks.fallingPiece['rotation']
		assert finalrotation==(initialrotation+2)%2




			
	                     
	


