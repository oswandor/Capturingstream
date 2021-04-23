#!/usr/bin/python3
import subprocess ; 
from distutils.spawn import find_executable

class Capturing_audio:

    def searchlib(self):

        foundffmepg = find_executable('ffmpeg') is not None ;
        foundffplay = find_executable('ffplay')  is not None;
        foundpactl = find_executable('pactl') is not None ;
        
        if foundffmepg and foundffplay and foundpactl :
           print("All good..") 
        else : 
          raise Exception('Error: Some of the required commands were not found ffmpeg, ffplay or pactl.');
          exit(0); 


    def getinput_devices(self): 

        found = find_executable('pactl') is not None 
        if found:
            try:
                p  = subprocess.run(['pactl', 'list' ,'short' ,'sources'] , capture_output=True ); 
                return self.encodeutf(p.stdout).split('\t')[1]; 

            except Exception as e: 
                print('Faild ' + e)

# ffmpeg -f x11grab -video_size 1280x1024  -framerate 30 -i :1.0 -vcodec libx264  -preset ultrafast -qp 0  -pix_fmt yuv420p -aspect 2:3 23escale.mkv 

    def  screencast(self,filenameout , timesec , resolution  , display ,  aspectarg='16:9'):

        try: 
            p = subprocess.run(['ffmpeg','-ss','00:00:00','-t', timesec ,'-f', 'x11grab', '-video_size' , resolution , '-framerate', '30', '-i', display ,'-vcodec', 'libx264'  ,'-preset' ,'ultrafast' ,'-qp' ,'0' , '-pix_fmt', 'yuv420p' ,'-aspect', aspectarg ,filenameout ])
            return p.stdout 
        except Exception as e: 
            return e 





    def recordAudio(self,nameRecoding, timesec):

        try:
            p =  subprocess.run(['ffmpeg', '-ss' ,'00:00:00' , '-t' , timesec ,  '-f' ,'pulse', '-i' , DEVICEPULSARAUDIO , '-ac', '1', nameRecoding]);
            return p ; 
        except Exception as e: 
            print('Faild ' + e)


    def encodeutf(self , bytess):

       encoding = 'utf-8'
       string = str(bytess , encoding); 
       return string ; 



DEVICEPULSARAUDIO = Capturing_audio().getinput_devices();


class Playaudio():

    def play(namefile):

        try:
            process = subprocess.run(['ffplay' , namefile] );

            if  process.returncode == 0 : 
                 raise  Exception("Error file does not exist.") ; 

            return process 
        except Exception as e : 
            return e 