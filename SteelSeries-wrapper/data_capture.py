"""
Module to capture and store data in appropriate format from SteelSeries Sentry eye tracker

requirements:
=============
psychopy
numpy
wrapper
matplotlib

S Kailasa (2016)
"""
import wrapper as wp
import numpy as np
import matplotlib.pyplot as plt
import psychopy
import time

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
	while elapsed < exp_time:
		elapsed = time.time() - start
		time.sleep(1)  


print track(10)


def pickled(exp_time):
	"""
	function to return a nice pickled list of the gaze coordinates with time in a useable format

	inputs:
	------- 
	exp_time    :    length of experiment in seconds (float)

	outputs:
	--------

	"""

	x = [] # empty lists to append gaze data to
	y = []
	tlist = []




