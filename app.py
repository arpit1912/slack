import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = []
channels = {}
channel_names =[]
@app.route('/')
def index():
	return render_template('login.html')

@app.route('/channel',methods = ["POST"])
def channel():
	username = request.form.get('username')
	if username not in users:
		users.append(username)
	print(users)
	return render_template('channel.html',channels = channel_names,user = username)


@app.route('/channel/<string:username>',methods =["POST","GET"])
def chatroom(username):
	channel_name = request.form.get('channel_name')

	if channel_name not in channels:
			channels[channel_name] = []
			channel_names.append(channel_name)
	chat_users = channels[channel_name]

	if request.method =="POST":
		channel_name = request.form.get('channel_name')
		print(channel_name)
		chat_users.append(username)
		channels[channel_name] = chat_users
		return render_template('chatroom.html',chatter = chat_users, channel_name = channel_name,username = username)

	else:
		return render_template('chatroom.html',chatter = chat_users, channel_name = channel_name,username = "hello artpiy")

@socketio.on('submit message')
def mess(data):
	print(data['message'],"inside the socketio")
	message = data['message']
	emit('transmit message',{'message':message},broadcast=True)

app.run(debug = True)