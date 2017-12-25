from enum import Enum 
import Math
import time

class Bullet(Entity):
	def __init__(self, senderEntityID, damage, pos, vel):
		Entity.__init__(self, senderEntityID, SpriteID.BULLET)
		self.damage = damage
		self.pos   = pos
		self.vel   = vel
		self.angle = Math.atan(vel(1)/vel(0))

class Weapon():
	def __init__(self, ownerEntityID):
		self.damage 	= 1.0
		self.rateoffire	= 1.0
		self.lastTimeShot = -1000.0


class SpriteID(Enum):
	BULLET = auto()
	PLAYER_AGENT = auto()

class GameState(Enum):
	PAUSED 		= 0
	INGAME 		= 1
	MAINMENU 	= 2
	INGAMEMENU	= 3

class Entity():
	def __init__(self, spriteID):
		self.spriteID = spriteID

		self.visible	= False
		self.collidable = False
		self.pos 		= (0.0,0.0)
		self.angle 		= 0.0
		self.vel		= (0.0,0.0)

class Agent(Entity):
	def __init__(self, agentID, spriteID):
		Entity.__init__(self, spriteID)
		
		self.agentID = agentID
		self.angle 	= (0.0,0.0)
		self.force 	= (0.0,0.0)
		self.mass 	= 1
		self.weapon = Weapon()

	def fireWeapon(self, gO):
		if
		bullet = self.weapon.shoot()
		gO.scene.addBullet(bullet)



class World():
	def __init__(self):
		self.gameState 			= GameState.MAINMENU
		self.UPDATE_FREQUENCY 	= 100

class Renderer():
	def __init__(self):
		self.RENDER_FREQUENCY	= 30
		self.spriteList 		= list()

class Scene():
	def __init__(self):
		self.agentsAI 			= list()
		self.playerAgent 		= PlayerAgent()

class GameObject():

	def __init__(self):
		self.world = World()
	# WORLD
			GameState gameState
			float 	UPDATE_FREQUENCY


	# RENDERER
			float 	RENDER_FREQUENCY
	list	Sprite 	SpriteList
			Menu 	menu

	# SCENE
	list 	Agent 	agentsAI
		 	Agent 	playerAgent

	# SOUND

	# PHYSICS
			float gravityConstant
			float gameSpeed

	# AI

	# UI












