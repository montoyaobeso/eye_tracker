"""
Start of a simple wrapper to expose the EyeX C/C++ api using the code of
https://github.com/wolfmanstout/simple-eye-tracker
I've included the dll files needed in the repo just so it's easier to copy over, 
obviously they need to be stored in the appropriate file in the SDK 

S Kailasa

"""



from ctypes import *
import time

DLL_DIRECTORY =  "C:\Users\wjjw53\TobiiEyeXSdk\lib\practice"
eyex_dll = CDLL(DLL_DIRECTORY + "/Tobii.EyeX.Client.dll")
tracker_dll = CDLL(DLL_DIRECTORY + "/Tracker.dll")

def connect():
    result = tracker_dll.connect()
    print "connect: %d" % result

def disconnect():
    result = tracker_dll.disconnect()
    print "disconnect: %d" % result

def get_position():
    x = c_double()
    y = c_double()
    tracker_dll.last_position(byref(x), byref(y))
    return (x.value, y.value)

def print_position():
    print "(%f, %f)" % get_position()

def move_to_position():
    position = get_position()
    Mouse("[%d, %d]" % (max(0, int(position[0])), max(0, int(position[1])))).execute()

def activate_position():
    tracker_dll.activate()



def track(exp_time):
    """
    function to call the EyeX API and record gaze for a specified experimental time

    inputs:
    -------
    exp_time    :    experiment time in seconds (float)

    outputs:
    --------
    gaze

    """
    g_data = []
    start = time.time()   
    elapsed = 0
    connect()
    while elapsed < exp_time:
        elapsed = time.time() - start
        time.sleep(1)
        g_data.append(print_position())
    disconnect()
    return g_data

print len(track(10))
