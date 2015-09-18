class Video():
	"""Movie information data structure is outlined here. """ 
	def __init__(self, title, imdb_rating, poster, trailer, date):
		self.title = title
		self.imdb_rating = imdb_rating
		self.poster_url = poster
		self.trailer_url = trailer
		self.date = date
