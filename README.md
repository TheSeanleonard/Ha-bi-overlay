# MQTToverlay
Home assistant blue iris overlay

# Install
1) Run an MQTT server. I would recommend the Mosquitto broker built into home assistant.
2) I use node red in Home Assistant to set the values of the MQTT topics.
3) Download and extract this repository anywhere on your blue iris pc.
4) Edit the config area in the ```overlay_v2.py``` python file with the text editor of your choice.
5) Run ```overlay_v2.py``` which will create a "values" folder. (Assuming you have python installed)
6) Set the macros source in blue iris to the text files in the values folder. This will set the macros to the value of the MQTT topic.
7) place macros over cameras.


# Tips
Once you have the overlay completely configured the way you want it, change the name of ```overlay_v2.py``` to ```overlay_v2.pyw```. This will make it run in the background.

On the blue iris pc create a shortcut of the python file and move the shortcut to the startup folder on windows to start it on boot.
