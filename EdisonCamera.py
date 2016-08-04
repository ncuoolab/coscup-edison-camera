import cv2
import time

class EdisonCamera:
	def __init__(self, count=5):
		self.count = count
		self.frame = None

	def __str__(self):
		self.cap.release()

	def getCap(self):
		self.cap = cv2.VideoCapture(0)
		if not self.cap.isOpened:
			raise Exception('No camera detected!')
		else:
			print("Camera ready")

	def releaseCap(self):
		self.cap.release()

	def countDown(self):
		# Count Down
		for i in range(self.count):
			print("{0}...".format(self.count - i))
			time.sleep(1)

	def takeSnapshot(self):
		self.getCap()
		self.countDown()
		ret, frame = self.cap.read() #Take snapshot
		self.releaseCap()
		filename = str(int(time.time())) + '.jpeg'
		filepath = './img/' + filename
		cv2.imwrite(filepath, frame)
		return filepath

	def saveImage(self):
		#Save snapshot using timestamp as file name
		return self.frame
		self.frame = None

if __name__ == '__main__':
	ed = EdisonCamera(5)
	frame = ed.takeSnapshot()