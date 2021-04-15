#!/usr/bin/python3
import subprocess; 


class Capturing_audio():
   
    def __init__(self):
        """Get information `pactl list short sources`"""
           
    def getinput_devices(self): 

        try:
         p  = subprocess.run(['pactl', 'list' ,'short' ,'sources'] , capture_output=True ); 
         return self.encodeutf(p.stdout).split('\t')[1]; 

        except: 
            pass 
    def recoringaudio(self,timesecoss):

        try:
            p =  subprocess.run(['ffmpeg', '-f' ,'pulse', '-i' , DEVICEPULSARAUDIO , '-ac', '1','recording.m4a']);
            return p ; 
        except:
            pass




    def encodeutf(self , bytess):

       encoding = 'utf-8'
       string = str(bytess , encoding); 
       return string ; 



DEVICEPULSARAUDIO = Capturing_audio().getinput_devices();

