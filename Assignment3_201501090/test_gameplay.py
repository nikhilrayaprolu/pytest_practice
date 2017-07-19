from gameplay import GamePlay
from scores import Score
score=Score()
gameplay=GamePlay()

class TestGamePlay():
	def test_initialcheck(self):
		pass
	def test_calculateLevelAndFall(self):
		level,fallFreq=score.calculateLevelAndFallFreq(0)
		assert level==1
		
	def test_calcu2lateLevelAndFall(self):
		level,fallFreq=score.calculateLevelAndFallFreq(0)
		
		assert fallFreq==0.25


	def test_convertToPixel(self):
		xcoordinate,ycoordinate=gameplay.convertToPixelCoords(2,3)
		assert xcoordinate<10000000
		
	def test_convertToPixel2(self):
		xcoordinate,ycoordinate=gameplay.convertToPixelCoords(2,3)
		
		assert ycoordinate<10000000
