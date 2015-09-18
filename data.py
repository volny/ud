import models

pulp_fiction = models.Video("Pulp Fiction",
													8.9,
													"https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
													"https://www.youtube.com/watch?v=ewlwcEBTvcg",
													"1994"
											)

fight_club = models.Video("Fight Club",
													8.9,
													"http://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
													"https://www.youtube.com/watch?v=SUXWAEX2jlg",
													"1999"
											)

inception = models.Video("Inception",
													8.8,
													"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
													"https://www.youtube.com/watch?v=8hP9D6kZseM",
													"2010"
											)

city_of_god = models.Video("City of God",
													8.7,
													"https://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg",
													"https://www.youtube.com/watch?v=_mDvXaRJcTM",
													"2002"
											)

true_detective = models.Video("True Detective",
														9.3,
														"http://ecx.images-amazon.com/images/I/A1E8BYXdWML._SL1500_.jpg",
														"https://www.youtube.com/watch?v=TXwCoNwBSkQ",
														"2014 - "
											)

house_of_cards = models.Video("House of Cards",
														9.1,
														"http://img4.wikia.nocookie.net/__cb20140217231358/house-of-cards/images/a/a8/House_of_Cards_Season_1_Poster.jpg",
														"https://www.youtube.com/watch?v=ULwUzF1q5w4",
														"2013 - "
											)

cowboy_bebop = models.Video("Cowboy Bebop",
														9.0,
														"http://upload.wikimedia.org/wikipedia/en/3/37/CowboyBebopDVDBoxSet.jpg",
														"https://www.youtube.com/watch?v=LnbKF_uosrA",
														"1997 - 1998"
											)

better_call_saul = models.Video("Better Call Saul",
														9.4,
														"http://proto.mtv.ca/wp-content/uploads/2015/02/tumblr_n1xyxwgXYE1qzpxx1o1_r1_1280.jpg",
														"https://www.youtube.com/watch?v=9q4qzYrHVmI",
														"2015 - "
											)

# Sorry, please repeat yourself. List of movies goes here.
movies = [pulp_fiction, fight_club, inception, city_of_god, true_detective, house_of_cards, cowboy_bebop, better_call_saul]
