from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gamemaster')
def gamemaster():
    return render_template('gamemaster.html')

@socketio.on('buzz')
def handle_buzz(data):
    player_name = data['playerName']
    print(f'{player_name} buzzed!')

    # Broadcast the buzzer event to gamemaster
    socketio.emit('buzzerEvent', {'playerName': player_name})

@socketio.on('resetBuzzer')
def handle_reset_buzzer():
    print('Buzzer reset by Gamemaster!')

    # Broadcast the reset event to all players
    socketio.emit('resetBuzzerEvent')

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
