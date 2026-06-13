const form = document.querySelector(".cht-form");
const input = document.querySelector(".message-input");
const chatBody = document.querySelector(".chtbody");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const msg = input.value.trim();
    if (!msg) return;

    addMessage("user", msg);
    input.value = "";

    const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: msg})
    });

    const data = await response.json();
    addMessage(data.reply);
});

function addMessage(sender, text) {
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}-message`;
    msgDiv.innerHTML = `<div class="text-message">${text}</div>`;
    chatBody.appendChild(msgDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}
