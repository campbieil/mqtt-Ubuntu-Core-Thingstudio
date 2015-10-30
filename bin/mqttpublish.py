#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

topic_counter ="testubuntucore/counter"
topic_command = "testubuntucore/command"
topic_result = "testubuntucore/result"

payload = "None"
qos = "0"
retain = "False"

#Use this for MQTT servers needing authentication
username = "guest"
password = "guest"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to ThingStudio sandbox with result code "+str(rc))
 # use this to subscribe to the counter feed for debug purposes to listen to your counter feed
 #   client.subscribe(topic_counter)
 # use this to subscribe to the command feed to receive commands
    client.subscribe(topic_command)
 # use this to subscribe to the result feed for debug purposes to listen to your result feed
#    client.subscribe(topic_result)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received the message : "+str(msg.payload)+" on topic : "+str(msg.topic))
#strip the incoming command from its json - TODO
    command=str(msg.payload)
 # Write code to test what command we have received and respond accordingly right now testing on non stripped json
    if command == 'b\'"ls"\'':
      message = "{\"Message\":\"I received the ls command\"}"
      client.publish(topic_result, message)
      print("Sent ls")
    elif command == 'b\'"cd"\'':
      message = "{\"Message\":\"I received the cd command\"}"
      client.publish(topic_result, message)
      print("Sent cd")
    else:
      message = "{\"Message\":\"I received an unkown command\"}"
      client.publish(topic_result, message)
      print("Sent unknown")


def on_publish(mosq, obj, mid):

	print("Publishing successful")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.will_set(topic_command, payload=None, qos=0, retain=False)
client.username_pw_set(username,password)
client.connect("mqtt.thingstud.io",1883,60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
i=1
while client.loop() == 0:
	message = "\""+str(i)+"\""
	print("Sending on topic: "+str(topic_counter)+" the message :"+str(message))	
	client.publish(topic_counter, message)
	i =i +1
	time.sleep(1)# sleep for 1 seconds before next call

