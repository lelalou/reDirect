from flask import Flask, render_template
import cv2
import mediapipe as mp
import numpy as np
from pywinauto.application import Application


app = Flask(__name__)


@app.route('/')
def page():
   
    
    return render_template('page.html')
@app.route('/start')

def start():
  
  cap = cv2.VideoCapture(1)
  mpHands = mp.solutions.hands
  hands = mpHands.Hands()
  mpDraw = mp.solutions.drawing_utils
  finger = ([8,6],[12,10], [16,14], [20,18])


  while True:
          success, img = cap.read();
          imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          results = hands.process(imgRGB)
          
    
          if results.multi_hand_landmarks:
             fingerList = []
             for handlandmark in results.multi_hand_landmarks:
                  mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)
                  for id, lm in enumerate(handlandmark.landmark):
                   h,w,c = img.shape
                   cx, cy = int(lm.x * w), int(lm.y * h)
                   fingerList.append([cx,cy])
             for fingers in fingerList:
                 cv2.circle(img, fingers, 8, (255, 255, 0), cv2.FILLED)

             count = 0
             for choice in finger:
                   if fingerList[choice[0]][1] < fingerList[choice[1]][1]:
                       count+=1

        

             if count == 1:
                 Application(backend = 'uia').start('C:\Program Files\Google\Chrome\Application\chrome.exe')
                 count == 0
             if count == 2:
                 Application(backend = 'uia').start('C:\Program Files\Internet Explorer\iexplore.exe')
                 count == 0
             if count == 3:
                 Application(backend = 'uia').start('C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2209.0.0_x64__8wekyb3d8bbwe\CalculatorApp.exe')
                 count == 0
             if count == 4:
                 Application(backend = 'uia').start('C:\Program Files\WindowsApps\Disney.37853FC22B2CE_1.42.5.0_x64__6rarf9sa4v8jt\DisneyPlus.exe')
                 count == 0
             else:
                pass

           
 
if __name__ == '__main__':
    # Run the app server on localhost:4449
  app.run('localhost', 4449)          
        
              
                        


       





   

       













