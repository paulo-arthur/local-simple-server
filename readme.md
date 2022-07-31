# Simple Local Server
## This project allows text transfer between multiple external devices.

The *server.py* uses **Ngrok** to create a public HTTP URL for your *Localhost* and creates a Flask server that receives and stores the client's messages.

The *client.py* connects to the **server** and provides 3 types of interaction:
* Write - (Send a message)
* Read - (See all sent messages)
* Delete - (Clear all sent messages)

#### Dependecies:
* Flask
* pyngrok
