import argparse
import time
import picamera
import os
import pkgutil
parser = argparse.ArgumentParser()
parser.add_argument("-v",dest="vname",type=str, help="input the file name you want the video to be outputted as")
parser.add_argument("-p",dest="pname",type=str, help="Input filename for the wanted outputted image")
args = parser.parse_args()
vVar = str(args.vname)
pVar = str(args.pname)
cwd = os.getcwd()
def takeVid():
	if pkgutil.find_loader("keyboard"):
		print("Installed Everything properly")
	else:
    	os.system("sudo pip3 install keyboard")
	import keyboard
	with picamera.PiCamera() as camera:
		camera.start_preview()
		camera.start_recording(cwd +"/"+ vVar +".h264")
		keyboard.wait('esc')
		camera.stop_recording()
		camera.stop_preview()
	userIn = str(input("Do you want to watch the video? Y/N: "))
	if userIn == "y" or userIn == "Y":
		os.system("omxplayer "+ vVar+".h264")
	else:
		print("Use command omxplayer <fileName>.h264 to view video")
	os.system("ffmpeg -framerate 24 -i "+vVar+".h264 -c copy "+vVar+".mp4")
	os.remove(vVar+".h264")
def takePic():
	os.system("raspistill -o "+pVar+".jpeg")
if args.vname != None:
	takeVid()
elif args.pname != None:
	takePic()
