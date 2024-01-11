const socket = io.connect('http://' + document.domain + ':' + location.port);

const buzzerBtn = document.getElementById('buzzerBtn');
const resetBtn = document.getElementById('resetBtn');
const buzzerEventsContainer = document.getElementById('buzzerEvents');

socket.on('buzzerEvent', (data) => {
    const playerName = data.playerName;
    buzzerEventsContainer.innerHTML += `<p>${playerName} buzzed!</p>`;
});

socket.on('resetBuzzerEvent', () => {
    buzzerBtn.disabled = false;
});

function buzz() {
    const playerName = document.getElementById('playerName').value;
    socket.emit('buzz', { playerName });
    buzzerBtn.disabled = true;
}

function resetBuzzer() {
    socket.emit('resetBuzzer');
}
