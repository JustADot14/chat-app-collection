Simple Chat App
===============
<h2>Default Values</h2>
IP address: 127.0.0.1<br>
Port: 4444<br>
Username: Me<br>

<h2>Running in Default Mode</h2>
<h4>Linux</h4>
Running server: ./chat-app_server.sh<br>
Running client: ./chat-app_client.sh

<h4>Windows</h4>
Running server: double click "chat-app_server.bat"<br>
Running client: double click "chat-app_client.bat"

<h2>Running Using chat-app.py </h2>
<h4>Running in default mode</h4>
Running server: chat-app.py --server<br>
Running client: chat-app.py --client

<h4>Running with optional parameters</h4>
Running server: chat-app.py --server -a [IP Address] -p [Port Number] -u [Username]<br>
Running client: chat-app.py --client -a [IP Address] -p [Port Number] -u [Username]

<h2>Running Using chat-server.py and chat-client</h2>
<h4>Running in default mode</h4>
Running server: chat-server.py<br>
Running client: chat-client.py

<h4>Running with optional parameters</h4>
Running server: chat-server.py -a [IP Address] -p [Port Number] -u [Username]<br>
Running client: chat-client.py -a [IP Address] -p [Port Number] -u [Username]
