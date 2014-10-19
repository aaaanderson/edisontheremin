#!/usr/bin/python

import mraa
import math
import time

gmajor = False
scale = []
scale2 = []
scale_length = 0

def toggle_scale():
        global gmajor
        global scale
        global scale2
        global scale_length
        if(gmajor == False):
                scale = [1703, 2024, 2272, 2551, 3030, 3401]
                scale2 =  [851, 1012, 1136, 1275, 1515, 1700]
                scale_length = 6
                gmajor = True
        else:   
                scale = [1912, 2024, 2272, 2865, 3030, 3816, 4048]
                scale2 = [956, 1012, 1136, 1432, 1515, 1908, 2024]              
                scale_length = 7                                                
                gmajor = False                                                  
                                                                                
toggle_scale()                                                                  
                                                                                
red = mraa.Gpio(7)                                                              
green = mraa.Gpio(8)                                                            
blue = mraa.Gpio(4)                                                             
red.dir(mraa.DIR_OUT)                                                           
green.dir(mraa.DIR_OUT)                                                         
blue.dir(mraa.DIR_OUT)                                                          
red.write(0)                                                                    
blue.write(0)                                                                   
green.write(0)                                                                  
                                                                                
toggle_button = mraa.Gpio(6)                                                    
toggle_button.dir(mraa.DIR_IN)                                                  
                                                                                
                                                                                                                                                               
freq = mraa.Aio(0)                                                              
output = mraa.Pwm(3)                                                            
output.enable(True)                                                             
output.write(255)                                                               
output2 = mraa.Pwm(5)                                                           
output2.enable(True)                                                            
output2.write(255)                                                              
                                                                                
articulator = mraa.Aio(1)                                                       
note = int(freq.read() * scale_length / 1024)                                   
                                                                                
while True:                                                                     
        if toggle_button.read() == 1:                                           
                toggle_scale()                                                  
        note = int(freq.read() * scale_length / 1024)                           
        if(articulator.read() > 500) :                                          
                note = int(freq.read() * scale_length / 1024)                   
                output.enable(False)                                            
                output2.enable(False)                                           
                time.sleep(0.05)                                                
                output.enable(True)                                             
                output2.enable(True)                                            
                output.period_us(scale[note])                                   
                output2.period_us(scale2[note])                                 
        if note % 3 == 0 :                                                      
                red.write(1)                                                    
                green.write(0)                                                  
                blue.write(0)                                                   
        elif note % 3 == 1 :                                                    
                red.write(0)                                                    
                green.write(1)                                                  
                blue.write(0)                                                   
        else :                                                                  
                red.write(0)                                                    
                green.write(0)                                                  
                blue.write(1)                                    