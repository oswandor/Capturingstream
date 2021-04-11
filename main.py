#!/usr/bin/python3

import os ; 
import sys ; 
import io ; 

from src.Capturing.recording import *;  

Capturing =  Capturing_audio(); 

print(Capturing_audio().getinput_devices()) ; 

print(DEVICEPULSARAUDIO) 