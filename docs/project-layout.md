# Project Idea
The end goal of this project is to be able to go to the website it is hosted on, and upload an image of a surface, like a table, and select where the robot will spawn, and optionally mark obstacles. 

Then, that image will be sent to the Python backend which will use machine vision to detect obstacles in the image.

Once obstacles are found, this is generated into a map, and the robot's task is to figure out how to go over all of the non obstacle area. Python backend will eval robot movement, and this movement will be displayed on the website. 

# Project Layout
## Web:
### Backend
Python Backend done using Flask apis, which React can grab. 
### Frontend
Javascript Frontend done using React

## Python Idea:
* Step 1: Detect obstacles in the image
* Step 2: Generate a map of the area the 'robot' can navigate on
* Step 3: Generate movement information for the robot

## JS Idea:
* Have the website just ask you to upload an image, or use a preexisting blank image you can add obstacles to 
* Add further obstacles to the image if the user wants to
* Select a robot start point
* Hit run, and a robot icon will start moving around the image, going around obstacles it detects with machine vision. 


# Future Plans
Feed movement data to a real robot, use live video instead of a photo + machine vision to detect where physical robot is. 