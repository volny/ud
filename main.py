import webbrowser
import os
import re
import sys

import data

# Templates
main_page_head = open('templates/head.html').read()
main_page_content = open('templates/main.html').read()
movie_tile_content = open('templates/tile.html').read()

def create_movie_tiles_content(movies):
	output = ''
	for movie in movies:
		# Extract the youtube ID from the url
		youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
		youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_url)
		trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

		# Append the title for the movie with its content filled in
		output += movie_tile_content.format(
			movie_title=movie.title,
			poster_image_url=movie.poster_url,
			trailer_youtube_id=trailer_youtube_id,
			production_date=movie.date,
			imdb_rating=movie.imdb_rating
		)
	return output

def open_movies_page(movies):
	# If an output file is already present we want to ask the user before overwriting it.
	if os.path.isfile('fresh_tomatoes.html'):
		sys.stdout.write("I appears you've run this before, an output file is already present. Overwrite it? [yes/no] ")
		choice = raw_input().lower()
		if choice != "yes":
			exit()

	# Create or overwrite the output file
	output_file = open('fresh_tomatoes.html', 'w')

	# Replace the placeholder for the movie tiles with the actual dynamically generated html
	rendered_html = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

	# Output the file
	output_file.write(main_page_head + rendered_html)
	output_file.close()
	
	# open the output file in the browser
	url = os.path.abspath(output_file.name)
	webbrowser.open('file://' + url, new=2) # open in a new tab, if possible

open_movies_page(data.movies)
