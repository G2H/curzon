import urllib
from bs4 import BeautifulSoup

def JSONfromURL(url):
	url_to_open = urllib.urlopen(url)
	html = url_to_open.read()
	soup = BeautifulSoup(html,'html.parser')
	data = []
	theatres = soup.find_all("div", { "class" : "theater" })
	for theatre in theatres: ## get theatre info
		new_entry= {}
		new_entry["cinema"] = theatre.find_all("h2", { "class" : "name" })[0].a.string
		new_entry["address"] = theatre.find_all("div", { "class" : "info" })[0].text
		listings = theatre.find_all("div", { "class" : "movie" })
		movies = []
		for listing in listings: ## get movies info
			new_movie = {}
			new_movie["title"] = listing.find_all("div", { "class" : "name" })[0].a.string
			new_movie["info"] = listing.find_all("span", { "class" : "info" })[0].text
			#new_movie["imdb_link"] = listing.find_all("span", { "class" : "info" })[0].a['href'] ## there is no link sometimes, need to do something about it
			new_movie["times"] = listing.find_all("div", { "class" : "times" })[0].get_text()
			movies.append(new_movie)
		new_entry["movies"] = movies
		data.append(new_entry)
	return data

today = 'http://www.google.com/movies?near=london&date=0&tid&q=curzon'
tomorrow = 'http://www.google.com/movies?near=london&date=1&tid&q=curzon'

#data = [{'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '15:15 \xa017:45 \xa020:15', 'title': 'Hail, Caesar!'}, {'info': '1hr 58min - Rated 15 - Action/Adventure/Drama/Scifi/Fantasy - English - IMDb', 'times': '13:00 \xa015:30 \xa018:00 \xa020:30', 'title': 'High-Rise'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '13:15 \xa015:45 \xa018:15 \xa020:45', 'title': 'Anomalisa'}, {'info': '2hr 4min - Rated 15 - Drama/Suspense/Thriller - English - Trailer - IMDb', 'times': '12:30', 'title': 'A Bigger Splash'}], 'address': '99 Shaftesbury Avenue, London, United Kingdom - 0871 703 3988', 'cinema': 'Curzon Soho'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '12:30', 'title': 'Hail, Caesar!'}, {'info': '1hr 58min - Rated 15 - Action/Adventure/Drama/Scifi/Fantasy - English - IMDb', 'times': '12:40 \xa015:15 \xa017:50 \xa020:30', 'title': 'High-Rise'}, {'info': '1hr 30min - Rated 15 - Horror - English - Trailer - IMDb', 'times': '20:40', 'title': 'The Witch'}, {'info': '2hr 7min - Rated 15 - Suspense/Thriller - English - Trailer - IMDb', 'times': '17:30', 'title': 'Spotlight'}, {'info': '2hr 36min - Rated 15 - Action/Adventure - English - Trailer - IMDb', 'times': '14:20', 'title': 'The Revenant'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '12:00 \xa014:00 \xa016:10 \xa018:15 \xa020:20', 'title': 'Anomalisa'}, {'info': '2hr 7min - Rated 15 - Drama - French - Trailer - IMDb', 'times': '15:00 \xa018:00', 'title': 'Marguerite'}, {'info': '2hr 10min - Rated 15 - Drama - English - Trailer - IMDb', 'times': '12:20 \xa020:15', 'title': 'The Big Short'}], 'address': '58 Victoria Street, London, United Kingdom - 0330 500 1331', 'cinema': 'Curzon Victoria'}, {'movies': [{'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '13:45 \xa016:00 \xa018:15 \xa020:30', 'title': 'Anomalisa'}], 'address': 'At Sea Containers - 20 Upper Ground, London, United Kingdom - 0330 500 1331', 'cinema': 'Curzon Mondrian London'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '15:30 \xa018:00 \xa020:30', 'title': 'Hail, Caesar!'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '13:15 \xa015:50 \xa018:15', 'title': 'Anomalisa'}, {'info': '2hr 7min - Rated 15 - Drama - French - Trailer - IMDb', 'times': '13:00 \xa020:20', 'title': 'Marguerite'}], 'address': 'Mayfair, 38 Curzon Street, London, United Kingdom - 0871 703 3989', 'cinema': 'Curzon Mayfair'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '11:15 \xa013:40 \xa016:00 \xa018:20 \xa020:40', 'title': 'Hail, Caesar!'}, {'info': '1hr 58min - Rated 15 - Action/Adventure/Drama/Scifi/Fantasy - English - IMDb', 'times': '12:30 \xa015:00 \xa017:30 \xa020:00', 'title': 'High-Rise'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '12:10', 'title': 'Anomalisa'}, {'info': '1hr 22min - Rated UC - Documentary - Spanish', 'times': '14:10 \xa016:10 \xa018:00 \xa020:20', 'title': 'Pearl Button'}, {'info': '2hr 4min - Rated 15 - Drama/Suspense/Thriller - English - Trailer - IMDb', 'times': '17:50', 'title': 'A Bigger Splash'}, {'info': '1hr 58min - Rated 15 - Drama - Italian - Trailer - IMDb', 'times': '15:10', 'title': 'Youth'}, {'info': '1hr 20min - Rated 12A - Documentary - English - Trailer - IMDb', 'times': '16:30', 'title': 'Hitchcock/Truffaut'}, {'info': '1hr 33min - Rated 15 - Drama - Ic - IMDb', 'times': '13:00 \xa020:50', 'title': 'Rams'}, {'info': '1hr 40min - Rated UC - Documentary - Hebrew - IMDb', 'times': '14:00 \xa018:10', 'title': 'Mr. Gaga'}, {'info': '1hr 15min - Rated 15 - Documentary - English - IMDb', 'times': '20:10', 'title': 'The Propaganda Game'}, {'info': '1hr 24min - Rated UC - Documentary - English - IMDb', 'times': '12:00', 'title': 'Among The Believers'}, {'info': '3hr 30min - Rated UC - Program - English - Trailer - IMDb', 'times': '11:00', 'title': 'National Theatre Live: Les Liaisons Dangereuses'}], 'address': 'The Brunswick, London, United Kingdom - 0330 500 1331', 'cinema': 'Curzon Bloomsbury'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '18:00', 'title': 'Hail, Caesar!'}, {'info': '1hr 58min - Rated 15 - Action/Adventure/Drama/Scifi/Fantasy - English - IMDb', 'times': '15:15 \xa020:30', 'title': 'High-Rise'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '13:00', 'title': 'Anomalisa'}], 'address': "206 King's Road, London, United Kingdom - 0871 703 3990", 'cinema': 'Curzon Chelsea'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '20:30', 'title': 'Hail, Caesar!'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '14:00 \xa018:15', 'title': 'Anomalisa'}, {'info': '1hr 20min - Rated 12A - Documentary - English - Trailer - IMDb', 'times': '16:15', 'title': 'Hitchcock/Truffaut'}], 'address': 'Lewisham Way, Goldsmiths University of London, Richard Hoggart Building, New Cross, United Kingdom - 0330 500 1331', 'cinema': 'Curzon Goldsmiths'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '17:15', 'title': 'Hail, Caesar!'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '15:00 \xa019:50', 'title': 'Anomalisa'}, {'info': '3hr 30min - Rated UC - Program - English - Trailer - IMDb', 'times': '11:00', 'title': 'National Theatre Live: Les Liaisons Dangereuses'}], 'address': '3 Water Lane, Richmond, United Kingdom - 0871 703 3992', 'cinema': 'Curzon Richmond'}, {'movies': [{'info': '1hr 35min - Rated PG - Animation - English - Trailer - IMDb', 'times': '14:00 \xa016:00', 'title': 'Kung Fu Panda 3'}, {'info': '2hr 1min - Rated 12A - Action/Adventure/Romance/Scifi/Fantasy - English - Trailer - IMDb', 'times': '14:10 \xa017:00 \xa020:00', 'title': 'The Divergent Series: Allegiant'}, {'info': '1hr 37min - Rated 15 - Horror - English - Trailer - IMDb', 'times': '18:00 \xa020:10', 'title': 'The Boy'}, {'info': '1hr 48min - Rated PG - Animation/Action/Adventure - English - Trailer - IMDb', 'times': '14:05', 'title': 'Zootropolis'}, {'info': '2hr 1min - Rated 15 - Drama - English - Trailer - IMDb', 'times': '17:05 \xa020:05', 'title': 'Truth'}], 'address': 'Langney Road, Eastbourne, United Kingdom - 01323 731441', 'cinema': 'Curzon Cinema - Eastbourne'}, {'movies': [{'info': '1hr 46min - Rated 12A - Comedy - English - Trailer - IMDb', 'times': '13:40 \xa016:00 \xa018:20 \xa020:15', 'title': 'Hail, Caesar!'}, {'info': '1hr 58min - Rated 15 - Action/Adventure/Drama/Scifi/Fantasy - English - IMDb', 'times': '11:45 \xa014:30 \xa017:45 \xa020:30', 'title': 'High-Rise'}, {'info': '1hr 30min - Rated 15 - Animation/Comedy - English - Trailer - IMDb', 'times': '11:30 \xa014:45 \xa020:45', 'title': 'Anomalisa'}, {'info': '2hr 7min - Rated 15 - Drama - French - Trailer - IMDb', 'times': '12:00 \xa017:30', 'title': 'Marguerite'}], 'address': 'Westgate Hall Road, Canterbury, United Kingdom - 0330 500 1331', 'cinema': 'Curzon Canterbury'}]

def createSite(data):
	## create the base site object
	site = {}
	site['title'] = 'Curzon cinemas'
	site['footer'] = ''
	pages = []
	## create cinema menu
	menu = {}
	menu['id'] = 1
	menu['type'] = 'menu'
	menu_elements = []
	cinema2id = {}
	# i will be the id of every page
	i = 2
	## create the first menu with the cinemas
	for cinema in data:
		cinema2id[cinema['cinema']] = i
		new_cinema = {}
		new_cinema['title'] = cinema['cinema']
		new_cinema['subtitle'] = cinema['address']
		new_cinema['link_id'] = i
		menu_elements.append(new_cinema)
		i = i + 1
	menu['elements'] = menu_elements
	pages.append(menu)
	## create a menu per cinema and page per movie
	for cinema in data:
		cinema_menu = {}
		cinema_menu['id'] = cinema2id[cinema['cinema']]
		cinema_menu['type'] = 'menu'
		cinema_menu_elements = []
		for movie in cinema['movies']:
			## create the movie page
			new_movie = {}
			new_movie['id'] = i
			new_movie['type'] = 'page'
			new_movie['elements'] = "<h1>"+movie['title']+"</h1><br><h2>"+movie['times']+"</h2><br><h3>"+movie['info']+"</h3>"
			pages.append(new_movie)
			## add the movie to the menu
			movie_in_menu = {}
			movie_in_menu['link_id'] = i
			movie_in_menu['title'] = movie['title']
			movie_in_menu['subtitle'] = movie['times']
			cinema_menu_elements.append(movie_in_menu)
			i = i + 1
		cinema_menu['elements'] = cinema_menu_elements
		pages.append(cinema_menu)
	site['pages'] = pages
	return site
#createSite(data)