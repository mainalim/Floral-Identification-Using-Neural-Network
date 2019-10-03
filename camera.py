import paramiko
from threading import Thread
import numpy as np
import subprocess as sp
import cv2
import os
import time

PI_USER = "pi"
PI_PASS = "raspberry"
PI_HOST = "192.168.43.106"
MY_IP   = "192.168.43.25"
PI_PORT = 8888

def setupCamera():
    sshClient = paramiko.SSHClient()
    sshClient.load_system_host_keys()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(PI_HOST, username=PI_USER, password=PI_PASS)
    channel = sshClient.get_transport().open_session()
    if channel is not None:
        command = "raspivid -vf -n -w 1280 -h 720 -o - -t 0 -b 2000000 | nc "+ MY_IP + " " + str(PI_PORT)
        channel.exec_command(command)
        print(" Connected to camera.")
    else:
        print(" Could not connect to PI. Quitting...")
    
    print("Camera setup completed. Returning.")
    return
class Cam:
    def __init__(self , port , size):
        self.port = port
        self.w , self.h = size
        self.img = np.array((self.w, self.h, 3), np.uint8)
        print(" IN :: Camera Module. Started Threading for updateFrame")

        print("Inside updateFrame")
        NETCAT_BIN = "nc"
        ncCommand = [NETCAT_BIN,
                '-lp',str(self.port)] 
        nPipe = sp.Popen(ncCommand, stdout = sp.PIPE , bufsize = 10**8)
        print("Created sp pipe")
        FFMPEG_BIN = "ffmpeg"
        fCommand = [ FFMPEG_BIN,
                '-i', 'pipe:0',             # fifo is the named pipe
                '-loglevel' , 'quiet',
                '-pix_fmt', 'bgr24',      # opencv requires bgr24 pixel format.
                '-vcodec', 'rawvideo',
                '-an','-sn',              # we want to disable audio processing (there is no audio)
                '-f', 'image2pipe', '-']
        self.fPipe = sp.Popen(fCommand, stdin = nPipe.stdout , stdout = sp.PIPE, stderr=None, bufsize=11**8)
        time.sleep(2)
        setupCamera()
        print("Threading for image extraction begun...")
        Thread(target=self.updateFrame).start()

    def getFrame(self):
        return self.img

    def updateFrame(self):
        print("Inside updateframe")
        while True:
            raw_image = self.fPipe.stdout.read(self.h * self.w * 3)
            image = np.fromstring(raw_image,dtype = 'uint8')
            image = image.reshape((self.h,self.w,3))
            self.fPipe.stdout.flush()
            if image is not None:
                self.img = image

if __name__ == "__main__":
    print("this works?")
    camera = Cam(8888, (1280,720))
    while True:
        image = camera.getFrame()
        cv2.imshow('frame',image)
        key = cv2.waitKey(1)
        if key & 0xff == ord('s') or key & 0xff == ord('S'):
            filePath = os.path.join("~", "srijana.jpg")
            retVal = cv2.imwrite("/home/srijana/Downloads/latest/flower_photos/predict/leaf/processedleaf.jpg", image)
            newimage = cv2.resize(image, (250, 250))
            retVal = cv2.imwrite("/home/srijana/Downloads/latest/flower_photos/image/resizedleaf.jpg", newimage)
            #grayimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
            #retVal = cv2.imwrite("/home/srijana/Downloads/latest/flower_photos/predict/leaf/processedleaf.jpg", grayimage)
            if(retVal == 0):
                print("Could not saveimage")
            else:
                print("Saved image")
        if key & 0xff == ord('q'):
            exit(0)

  
