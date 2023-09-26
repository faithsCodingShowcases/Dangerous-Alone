import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
	def __init__(self):
		self.frames = {
			# magic
			'flame': import_folder('../graphics/particles/flame/frames'),
			'aura': import_folder('../graphics/particles/aura'),
			'heal': import_folder('../graphics/particles/heal/frames'),
			
			# attacks 
			'bloodblade': import_folder('../graphics/particles/bloodblade'),
			'slash': import_folder('../graphics/particles/slash'),
			'ghostbomb': import_folder('../graphics/particles/ghostbomb'),
			'groundpound': import_folder('../graphics/particles/groundpound'),
			'seismicsmash': import_folder('../graphics/particles/seismicsmash'),

			# monster deaths
			'mage': import_folder('../graphics/particles/smoke_orange'),
			'demon': import_folder('../graphics/particles/demondeath'),
			'ghost': import_folder('../graphics/particles/ghostdeath'),
			'golem': import_folder('../graphics/particles/golemdeath'),
			'spider': import_folder('../graphics/particles/spiderdeath'),			
			}				
	def reflect_images(self,frames):
		new_frames = []

		for frame in frames:
	 		flipped_frame = pygame.transform.flip(frame,True,False)
	 		new_frames.append(flipped_frame)
		return new_frames



	def create_particles(self,animation_type,pos,groups):
		animation_frames = self.frames[animation_type]
		ParticleEffect(pos,animation_frames,groups)


class ParticleEffect(pygame.sprite.Sprite):
	def __init__(self,pos,animation_frames,groups):
		super().__init__(groups)
		self.sprite_type = 'magic'
		self.frame_index = 0
		self.animation_speed = 0.15
		self.frames = animation_frames
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = pos)

	def animate(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.frames):
			self.kill()
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self):
		self.animate()
