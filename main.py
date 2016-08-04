from EdisonCamera import EdisonCamera
from Flickr import Flickr
import json
import time
import base64
import urllib2

ENV_EDISON_LINK = <EDISON-LINK>
ENV_EDISON_REPLY_LINK = <EDISON-REPLY-LINK>
ENV_ADMIN_ID = <ADMIN-ID>
ENV_ADMIN_PWD = <ADMIN-PWD>
AUTH_STRING = ''
IMG_BED = Flickr()

def upload_image(filepath):
	image_url = IMG_BED.upload_image(filepath)
	return image_url

def reply_lineBot(mid, image_url):
	data = image_url
	data['mid'] = mid
	print data
	req = urllib2.Request(
		ENV_EDISON_REPLY_LINK,
		json.dumps(data),
		{'Content-Type': 'application/json'}
	)
	req.add_header("Authorization", "Basic {0}".format(AUTH_STRING))
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()

def wait_for_update():
	print "waiting for update..."
	req = urllib2.Request(ENV_EDISON_LINK)
	req.add_header("Authorization", "Basic {0}".format(AUTH_STRING))
	res = urllib2.urlopen(req)
	res_data = res.read()
	obj = json.loads(res_data)
	if obj != {}:
		# Start taking snapshot
		edison = EdisonCamera(5)
		filepath = edison.takeSnapshot()
		image_url = upload_image(filepath)
		reply_lineBot(obj['mid'], image_url)
	time.sleep(10)
	wait_for_update()


if __name__ == "__main__":
	AUTH_STRING = base64.encodestring('%s:%s' % (ENV_ADMIN_ID, ENV_ADMIN_PWD)).replace('\n', '')
	wait_for_update()