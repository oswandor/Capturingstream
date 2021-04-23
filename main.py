#!/usr/bin/python3

import os ; 
import sys ; 
import io ; 
from distutils.spawn import find_executable
from src.Capturing.recording import Capturing_audio , Playaudio; 

try: 
    Capturing =  Capturing_audio()
    Capturing.searchlib() 
    print(Capturing.screencast('nuevoscreen.mkv' ,'00:01:00','1280x1024' ,':1.0',aspectarg='4:3')); 
    
except Exception as e: 
    print(e); 

#method recordAudio 
#Capturing.recordAudio('recording0.m4a', '00:01:00').stdout; 

#play audio class Playaudio 
#print(Playaudio.play('recording0.m4a')); 








