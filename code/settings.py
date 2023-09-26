# game setup
WIDTH    = 1300	
HEIGTH   = 650
FPS      = 60
TILESIZE = 32
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'invisible': 0}

# When finding coordinates of player designated by 'p'.
# Multiply the X-axis by tilesize
# Multiply the Y-axis by tilesize
# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
BACKGROUND_COLOR = '#FF4500'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'



weapon_data = {
	'powersword': {'cooldown': 100, 'damage': 25,'graphic':'../graphics/weapons/powersword/full.png'},
	'flamberge': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/flamberge/full.png'},
	'claymore': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/claymore/full.png'},
	'thorn':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/thorn/full.png'},
	'flash':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/flash/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
	'mage': {'health': 25,'exp':100,'cooldown': 250,'damage':5,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 2, 'resistance': 1, 'attack_radius': 35, 'notice_radius': 125},
        'demon': {'health': 100,'exp':250,'cooldown': 400,'damage':20,'attack_type': 'bloodblade', 'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 150},
        'ghost': {'health': 35,'exp':110,'cooldown': 300,'damage':8,'attack_type': 'ghostbomb', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 30, 'notice_radius': 120},
        'golem': {'health': 75,'exp':120,'cooldown': 350,'damage':14,'attack_type': 'seismicsmash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 2, 'resistance': 2, 'attack_radius': 40, 'notice_radius': 175},
        'spider': {'health': 50, 'exp':100,'cooldown': 275,'damage':11,'attack_type': 'groundpound', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 2, 'resistance': 2, 'attack_radius': 25, 'notice_radius': 100}}



