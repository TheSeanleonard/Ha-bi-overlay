# MQTToverlay
Home assistant Blue Iris overlay
(Assuming Blue Iris is running on windows)

# Install
1) Run an [MQTT](https://www.home-assistant.io/integrations/mqtt/) server. I would recommend the [Mosquitto broker](https://github.com/home-assistant/addons/tree/master/mosquitto) built into home assistant.
2) I use node red in Home Assistant to set the values of the MQTT topics. (I have included ```example flow.json```)
3) Download and extract this repository anywhere on your Blue Iris pc.
4) Edit the config area in the ```overlay_v2.py``` python file with the text editor of your choice.
5) In a terminal on the Blue Iris pc run ```pip install paho-mqtt```. This will install required MQTT library. (Assuming you have [python](https://www.python.org/downloads/) installed)
6) Run ```overlay_v2.py``` which will create a "values" folder.
7) Set the [macros](/images/page134.pdf) source in blue iris to the text files in the values folder. This will set the macros to the value of the MQTT topic.
8) place macros over cameras.


# Tips

**Run in background**

Once you have the overlay completely configured the way you want it, close the python file then change the name of ```overlay_v2.py``` to ```overlay_v2.pyw``` then start the file again. This will make it run in the background.



**Start on boot**

On the Blue Iris pc create a shortcut of the python file and move the shortcut to the startup folder on windows.
1. Press Windows +R on the keyboard.
2. A dialog box will appear, type ```shell:startup``` and click on OK.
3. The Windows 10 startup folder will open.
4. Move a shortcut of the python file to that folder.

# Screenshots

![MQTTsendflow](https://github.com/TheSeanleonard/MQTToverlay/assets/88116814/1c95afab-9862-4f57-a9f2-79ffbbd53943)
