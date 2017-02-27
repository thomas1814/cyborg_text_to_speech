#!/usr/bin/env python
"""Created by Thomas Rostrup Andersen on 11/11/2016.
Copyright (C) 2016 Thomas Rostrup Andersen. All rights reserved."""

import rospy
import sys
import pyttsx
from std_msgs.msg import String

__author__ = "Thomas Rostrup Andersen"
__copyright__ = "Copyright (C) 2016 Thomas Rostrup Andersen"
#__license__ = ""
__version__ = "0.0.2"
__all__ = []

"""Cyborg Text To Speech (TTS) Module"""

engine = None

def text_callback(data):
	global engine
	engine.say(data.data)
	engine.iterate()
	
def main():
	rospy.init_node("cyborg_text_to_speech")
	text_subscriber = rospy.Subscriber( rospy.get_name() + "/text_to_speech", String, text_callback, queue_size=100)
	global engine
	engine = pyttsx.init()
	engine.startLoop(False)
	rospy.loginfo("Cyborg TTS: Activated...")
	rospy.spin()
	engine.endLoop()
	rospy.loginfo("Cyborg TTS: Deactivated...")
	
if __name__ == "__main__":
	print("Cyborg TTS: Starting Program...")

	if sys.version_info < (2,5):
		print("Cyborg TTS: Running Python version " + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro) + " (Python version 2.5 or grater is required)...")
		exit()

	main()

	print("Cyborg TTS: End of Program...")