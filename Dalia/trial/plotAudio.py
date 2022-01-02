
import record


class plotAudio(record.Recording):
    def __init__(self,data,samplingFrequency,duration) :
        super().__init__(data,samplingFrequency,duration)
    def visualize(self,path:str):
	    print("plotting Audio")
	
	# reading the audio file
	    raw = wave.open(path)
	
	# reads all the frames
	# -1 indicates all or max frames
	    signal = raw.readframes(-1)
	    signal = np.frombuffer(signal, dtype ="int16")
	
	# gets the frame rate
	    f_rate = raw.getframerate()

	# to Plot the x-axis in seconds
	# you need get the frame rate
	# and divide by size of your signal
	# to create a Time Vector
	# spaced linearly with the size
	# of the audio file
	    time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	)

	# using matlplotlib to plot
	# creates a new figure
	    plt.figure(1)
	
	# title of the plot
	    plt.title("Sound Wave")
	
	# label of x-axis
	    plt.xlabel("Time")
	
	# actual ploting
	    plt.plot(time, signal)
	
	# shows the plot
	# in new window
	    plt.show()

	# you can also save
	# the plot using
	 # plt.savefig('filename')











# imports
import matplotlib.pyplot as plt
import numpy as np
import wave, sys

# shows the sound waves




        