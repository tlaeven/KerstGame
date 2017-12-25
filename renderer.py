# class Entity():
# 	def __init__(self, entityID, spriteID):
# 		self.entityID 	= entityID
# 		self.spriteID = spriteID

# 		self.visible	= False
# 		self.collidable = False
# 		self.pos 		= (0.0,0.0)
# 		self.vel		= (0.0,0.0)
# 		self.angle 		= (0.0,0.0)
# 
# class SpriteID(Enum):
# 	BULLET = auto()
# 	PLAYER_AGENT = auto()

def renderer(gO):
	if timeToRender(gO)
		if gO.world.gameState == GameState.MAINMENU:
			drawMainMenu(gO)
		if gO.world.gameState == GameState.INGAME:
			drawGame(gO)
		if gO.world.gameState == GameState.PAUSED:
			drawPaused(gO)
		if gO.world.gameState == GameState.INGAMEMENU:
			drawInGameMenu(gO)

def drawGame(gO):
	for entity in gO.scene.entityList:
		if(entity.isVisible):
			draw(entity)

def drawMainMenu(gO):
	pass

def drawPaused(gO):
	pass

def drawInGameMenu(gO):
	pass

def timeToRender(gO):
	return True
