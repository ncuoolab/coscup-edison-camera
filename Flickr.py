import flickr_api

class Flickr:
	def __init__(self, API_KEY, API_SECRET, album_name=''):
		flickr_api.set_keys(
			api_key = API_KEY,
			api_secret = API_SECRET
		)
		flickr_api.set_auth_handler('flickr.auth')
		self.user = flickr_api.test.login()
		# self.album = get_album(album_name)

	def upload_image(self, filepath):
		photo_title_base = "Coscup Edison Camera - "
		photo_title = photo_title_base + filepath.split('/')[-1].split('.')[0]
		photo = flickr_api.upload(photo_file=filepath, title=photo_title)
		return self.get_image_url(photo)

	def get_image_url(self, photo):
		base_url_prefix = 'https://farm' + str(photo.farm) + '.staticflickr.com/' +  photo.server + '/' + photo.id + "_" + photo.secret
		base_url_postfix = '.jpg'
		return {
			'originalUrl': base_url_prefix + '_z' + base_url_postfix,
			'previewUrl': base_url_prefix + '_m' + base_url_postfix,
		}

	def check_album_title(self, e):
		return e.title == self.album_name

	def get_album(self, album_name):
		Photosets = self.user.getPhotosets()
		album = filter(check_album_title, Photosets)
		if len(album == 0):
			raise Exception('Album "{0}" not found!'.format(album_name))
		elif len(album > 1):
			raise Exception('More than one albums "{0}" found!'.format(album_name))
		return album[0]
