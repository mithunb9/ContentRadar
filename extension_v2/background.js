chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("Message received in background script:", message);
  if (message.type === "pageContent") {
    fetch("http://127.0.0.1:5000/text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: message.url, text: message.content, timestamp: new Date() }),
    })
      .then((response) => {
        console.log("Response from server:", response);
        return response.json();
      })
      .then((data) => console.log("Success:", data))
      .catch((error) => console.error("Error:", error));
  }
});
