function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        document.getElementById('user-input').value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}
