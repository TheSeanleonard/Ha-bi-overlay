# MQTToverlay
Home assistant blue iris overlay
(Assuming Blue Iris is running on windows)

# Install
1) Run an [MQTT](https://www.home-assistant.io/integrations/mqtt/) server. I would recommend the [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) built into home assistant.
2) I use node red in Home Assistant to set the values of the MQTT topics. (I have included an [example flow](/example flow.json))
3) Download and extract this repository anywhere on your blue iris pc.
4) Edit the config area in the ```overlay_v2.py``` python file with the text editor of your choice.
5) Run ```overlay_v2.py``` which will create a "values" folder. (Assuming you have [python](https://www.python.org/downloads/) installed)
6) Set the [macros](/images/page134.pdf) source in blue iris to the text files in the values folder. This will set the macros to the value of the MQTT topic.
7) place macros over cameras.


# Tips
Once you have the overlay completely configured the way you want it, close the python file then change the name of ```overlay_v2.py``` to ```overlay_v2.pyw``` then start the file again. This will make it run in the background.

On the blue iris pc create a shortcut of the python file and move the shortcut to the startup folder on windows to start it on boot.
