import time, pyautogui, datetime
try:
    for i in range(100, 10000): 
        print('Start Time: '+ str(datetime.datetime.now()))
        pyautogui.moveTo(i, i, duration=1)
        time.sleep(i/10)
except KeyboardInterrupt:
    print('End Time: ' + str(datetime.datetime.now()))


