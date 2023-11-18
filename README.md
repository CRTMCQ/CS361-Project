# Microservice - Set Up
My microservice can be found in the file: <b>soundtrackMicro.py</b>

<b>Requirements</b>

With the current authentication method, accessing the Spotify Web API requires the creation of a Spotify app, through the dashboard here: https://developer.spotify.com/dashboard

Will likely need to install the Spotipy library https://spotipy.readthedocs.io/en/2.22.1/ .
Be sure to follow the setup instructions provided there to set up the proper environment variables.


# Microservice Communication
This microservice utilises a "Request-Reply" pattern within RabbitMQ.

# Requesting Data
To request data from <b>soundtrackMicro.py</b>, you first need to establish a connection to the RabbitMQ server and declare the proper queue:
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/3f0bea14-a5f6-4d33-b540-a432ca30fd0e)
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/3a3dfaa2-56e9-49ed-b731-91a9d25f02e0)

To send a request message to this queue (Note: soundtrackMicro.py is expecting to receive a string_type movie title):
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/5a9486d4-0d77-4493-b9c9-d020d30c6c7d)


# Receiving Data
<b>soundtrackMicro.py</b> will return a URL based on the message it was sent. To receive this data, define the consume attributes of the RabbitMQ server, set up a callback function, and start "consuming" data like so: 
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/7efff2dc-1d4b-49fb-adbc-0e1e6078583f)
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/946297c4-e949-41b8-9a27-1f069fa6526a)
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/02ec5913-eb27-4b21-bb72-dd3e47bb7a36)


# Communication Example
Here is an example of the full communication loop in action. Also included (it is commented out) is one way to utilize the data sent from <b>soundtrackMicro.py</b> by opening it within the user's web browser:
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/708e51d5-1871-4a51-ab6e-23e612037e67)


# UML Sequence Diagram
![image](https://github.com/CRTMCQ/CS361---Project/assets/146783107/89739e8e-acdb-4b42-835b-490bec877721)

