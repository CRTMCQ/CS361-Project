import pika
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_soundtrack(title):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    query = title.decode()
    print(f" [x] Received: " + query)
    query += " (Original Motion Picture Soundtrack)"

    searchResults = spotify.search(query, 1, 0, "album")
    albums_dict = searchResults['albums']
    albums_items = albums_dict['items']
    soundtrack = albums_items[0]['external_urls']['spotify']
    return soundtrack


# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='request-queue')


def callback(ch, method, properties, body):
    response = get_soundtrack(body)

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     body=response)


channel.basic_consume(queue='request-queue',auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for requests')
channel.start_consuming()
