chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("Message received from content script:", message);

  if (message.type === "sendText") {
    console.log(message);
    fetch("http://127.0.0.1:5000/text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: message.payload }),
    }).then((response) => {
      if (response.ok) {
        sendResponse({ response: "Sent request" });
        return true;
      }
      throw new Error("Network response was not ok.");
    });
  }
  return true; // Keep the message channel open for async sendResponse
});
