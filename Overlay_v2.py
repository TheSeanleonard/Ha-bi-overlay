import os
import time
import logging
import paho.mqtt.client as mqtt

###################################################
##             Edit this stuff (config)
###################################################

# MQTT broker information
broker_address = "HA ip"
broker_port = 1883
mqtt_username = "MQTT USERNAME"
mqtt_password = "MQTT PASSWORD"

# Array of topics to subscribe to (add any topic and a text document will be created)
topics = ["temperature", "garagedoor", "mandoor", "frontdoor"]


###################################################
##       probably dont edit past here
###################################################



# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Dictionary to store file handles for each topic
topic_to_file_handle = {}

def get_file_name(topic):
    return f"values/{topic}.txt"

def create_values_folder():
    if not os.path.exists("values"):
        os.makedirs("values")
        logger.info("Created 'values' folder.")

def ensure_file_handle_open(topic):
    file_name = get_file_name(topic)
    if topic not in topic_to_file_handle or topic_to_file_handle[topic].closed:
        create_values_folder()
        topic_to_file_handle[topic] = open(file_name, "r+")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logger.info("Connected to MQTT broker")
        # Subscribe to all topics in the array
        for topic in topics:
            client.subscribe(topic)
    else:
        logger.error("Failed to connect to MQTT broker with result code " + str(rc))

def on_message(client, userdata, msg):
    try:
        topic = msg.topic
        new_data = msg.payload.decode("utf-8")

        ensure_file_handle_open(topic)

        with topic_to_file_handle[topic] as file:
            current_data = file.read().strip()

            if new_data != current_data:
                file.seek(0)  # Move the cursor to the beginning of the file
                file.truncate()  # Clear the file contents
                file.write(new_data)  # Write the new data
                logger.info(f"Received new data for {topic}: {new_data}")
            else:
                logger.info(f"Received duplicate data for {topic}: {new_data}")

    except Exception as e:
        logger.error(f"Error processing MQTT message for {topic}: {str(e)}")

def main():
    # Create an MQTT client
    client = mqtt.Client()

    # Set up the callback functions
    client.on_connect = on_connect
    client.on_message = on_message

    # Set authentication credentials
    client.username_pw_set(mqtt_username, mqtt_password)

    # Connect to the MQTT broker
    client.connect(broker_address, broker_port, 60)

    # Start the MQTT loop
    client.loop_start()

    try:
        while True:
            # Wait for 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        # Stop the MQTT loop
        client.loop_stop()
        client.disconnect()
        logger.info("Script stopped by user")

        # Close all file handles
        for file_handle in topic_to_file_handle.values():
            file_handle.close()

if __name__ == "__main__":
    main()
