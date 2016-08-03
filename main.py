from EdisonCamera import EdisonCamera
import json
import time
import base64
import urllib2

ENV_EDISON_LINK = 'http://localhost:5000/edison'

def make_resp(mid, img):
	return {
		'mid': mid,
		'file': mid + '_' + str(time.time()).split('.')[0] + '.png',
		'data': base64.b64encode(img)
	}

def send_image(mid, image):
	print make_resp(mid, image)

def wait_for_update():
	print "waiting for update..."
	res = urllib2.urlopen(ENV_EDISON_LINK)
	obj = json.loads(res.read())
	if obj != {}:
		# Start taking snapshot
		edison = EdisonCamera(5)
		img = edison.takeSnapshot()
		send_image(obj['mid'], img)
	time.sleep(10)
	wait_for_update()


if __name__ == "__main__":
	wait_for_update()