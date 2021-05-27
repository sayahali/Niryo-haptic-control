# Niryo-haptic-control
This is a python script to control a niryo robotic arm with haptic geomagic touch (phantom omni)
Tested system: ubuntun 16.04 & ROS kinetic

1)You need at first to install phantom omni package in your workspace following the stpes described in this link: 

https://github.com/fsuarez6/phantom_omni

2)Copy this project into your workspace

3) catkin_make
    
4)roslaunch geomagic_control geomagic.launch

5) rosrun niryo_haptic_control niryo_haptic_control.py
    
Video link: https://www.youtube.com/watch?v=w8cuW6sPWIE
