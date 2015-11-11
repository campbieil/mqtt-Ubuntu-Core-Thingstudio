# mqtt-Ubuntu-Core-Thingstudio
This repository contains an example MQTT client ready to be built for Ubuntu Core interacting with the ThingStudio BaaS<br>
To build this project clone this repository on your Ubuntu Classic machine using <code>git clone git@github.com:campbieil/mqtt-for-ubuntu-core.git</code><br>
Then enter the directory <code>cd mqtt-for-ubuntu-core</code>and enter <code>snapcraft</code><br>
This will be a snap that you can then install into your Ubuntu Core target<br>
You can either do a <code>snappy -remote</code>  or scp the snap to your Ubuntu Core machine and install it from there using <code>sudo snappy install --allow-unauthenticated mqtt_testclient_1_amd64.snap</code><br>
To run it on your Ubuntu Core machine use <code>mqtttestclient.mqttpublish</code></br>
Note that you need ot have snapcraft installed on your Ubuntu Classic machine.<br>
When running on your Ubuntu Core target you will see your snap send and receive messages on the topic <em>ubuntucore</em>
