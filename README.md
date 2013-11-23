This is a collection of useful python scripts and stuff that i've written
over the years

script: make_csv.py
usage: 
	called with path to a facedb that has images organised into 
	directories it will build a csv containing the absolute paths to all
	those files with a number on the end denoting the image category

script: zipcracker.py
usage: 
	called with the filename of a zip file and a dictionary to execute
	a dictionary attack against the zip.

script: pynmap.py
usage:
	python pynamp.py -H <host> -p <port>
	
	it will tell you whats listening on that port <port> can be a
	csv list of ports
