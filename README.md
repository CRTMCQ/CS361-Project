# Main Project - Getting Started
This is a simple project that utilizes the Spotipy python library to search the Spotify Web API. Current features include seeing a list of an artist's albums, and an artist's top 10 songs.
The main project runs from the files: <b>main.py</b>, and <b>myFunctions.py</b>

With the current authentication method, accessing the Spotify Web API requires the creation of a Spotify app, through the dashboard here: https://developer.spotify.com/dashboard

Will likely need to install the Spotipy library https://spotipy.readthedocs.io/en/2.22.1/ .
Be sure to follow the setup instructions provided there to set up the proper environment variables.

# Microservice - Set Up
My microservice can be found in the file: <b>soundtrackMicro.py</b>

This microservice is designed to take in a movie title (string value) through a RabbitMQ server, and will return a URL to that movie's soundtrack album on Spotify (when possible).

<b>Requirements</b>

With the current authentication method, accessing the Spotify Web API requires the creation of a Spotify app, through the dashboard here: https://developer.spotify.com/dashboard

Will likely need to install the Spotipy library https://spotipy.readthedocs.io/en/2.22.1/ .
Be sure to follow the setup instructions provided there to set up the proper environment variables.


# Microservice Communication
This microservice utilises a "Request-Reply" pattern within RabbitMQ.

# Requesting Data
To request data from <b>soundtrackMicro.py</b>, you first need to establish a connection to the RabbitMQ server and declare the proper queue:
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/request1.png)
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/request3.png)

To send a request message to this queue (Note: soundtrackMicro.py is expecting to receive a string_type movie title):
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/request2.png)


# Receiving Data
<b>soundtrackMicro.py</b> will return a URL based on the message it was sent. To receive this data, define the consume attributes of the RabbitMQ server, set up a callback function, and start "consuming" data like so: 
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/receive1.png)
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/receive2.png)
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/receive3.png)


# Communication Example
Here is an example of the full communication loop in action. Also included (it is commented out) is one way to utilize the data sent from <b>soundtrackMicro.py</b> by opening it within the user's web browser:
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/fullExample.png)


# UML Sequence Diagram
![image](https://github.com/CRTMCQ/CS361-Project/blob/main/README_images/UML.png)

