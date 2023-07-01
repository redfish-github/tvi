#import
import cv2
import os
import time

#def
#print data
def cout(message):
    print(' [Data] '+message)

#clean out
def dell(p):
    l = os.listdir(p)
    for i in l:
        f = os.path.join(p,i)
        if os.path.isdir(f):
            del(f)
        else:
            os.remove(f)

#input
inp=input()
if inp == '':
    cout('open mp4 --- failed')
    input('Press the enter to exit the program')
    quit()
cout('input --- success')


#creat and del 'out' pack
if os.path.exists('./out') == False:
    cout('their is not have out file')
    cout('create a new out file')
    os.mkdir('out')
    cout('create out file --- success')

cout('find a out file')
cout('start clean out file')

dell('./out')

cout('cleaning.....')

cout('clean out file --- success')
cout('chance workspace')
os.chdir('./out')  
cout('chance workspace --- success')

#read
cout('start read video')
cout('  start open video')
video=cv2.VideoCapture(inp)
if video.isOpened():
    open,f=video.read()
    cout('  open video --- success')
else:
    open=False
    cout('  open mp4 --- failed')
    input('Press the enter to exit the program\n')
    quit()
jj=1
png='png'
cout('      reading is starting')
while open:
    ret,f=video.read()
    if f is None:
        break
    if ret == True:
        cv2.imwrite(str(str(jj)+'.png'),f)
        cout('          save '+str(jj)+'.png --- success')
        jj+=1

cout('read video --- sucess')
#free
video.release()
cout('free the resource')
cout('the program is success')
input('Press the enter to exit the program\n')
quit()