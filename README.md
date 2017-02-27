# README
This is the repository for the source code to the text to speech (TTS) ROS node for the NTNU Cyborg.

Node name: cyborg_text_to_speech  
Language: Python  

## Requirements:  
* ROS  
* PyTTSX  

PyTTSX can be installed:  
//This is pip2 for Python 2.7 (used by ROS)  
$ sudo apt-get install python-pip  
$ pip2 install PyTTSX  

## Features:
* This node subscribes to cyborg_text_to_speech/text_to_speech (String message type). All text are spoken out as speech.

## Usage:
$ rosrun cyborg_text_to_speech text_to_speech.py
