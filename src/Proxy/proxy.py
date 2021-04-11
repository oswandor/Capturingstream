#!/usr/bin/python3
import subprocess; 


class Capturing_audio(): 


    def __init__(self):
        """Get information `pactl list short sources`"""
        pass 

    def getinput_devices(self): 

        try:
         
         return subprocess.Popen(['pactl', 'list' ,'short' ,'sources']).wait(); 

        except: 
            pass 

  

