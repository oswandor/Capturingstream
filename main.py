#!/usr/bin/python3

import os ; 
import sys ; 
import io ; 

from src.Proxy.proxy import *;  

Capturing =  Capturing_audio();

targetout  = Capturing_audio().getinput_devices().stdout


print(Capturing.encodeutf(targetout).split('\t')) 