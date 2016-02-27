class Photo(object):
	width = 800
	height = 600
	def get_dimension(self):
		width = 600
		return self.width*self.height
	dimension = width*height

class NewPhoto(Photo):
	def get_dimension(self):
		if self.height>1024:
			self.height=1024

class RestrictPhoto(Photo):
	def get_dimension(self, do_restrict):
		if do_restrict:
			print( super().get_dimension() )
		else:
			return self.width*2*self.height*2;