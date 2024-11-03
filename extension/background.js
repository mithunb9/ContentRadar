// Listener for incoming messages from the content script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("Received message from content script:", message);

  if (message.type === "sendText") {
    const text = message.payload;
    const endpoint = "http://127.0.0.1:5000/text"; // Your Flask endpoint

    console.log("SENDING");

    // Send the text to the Flask server
    fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text }),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Text sent successfully!");
          sendResponse({ response: "Text sent successfully!" });
        } else {
          console.error("Failed to send text.");
          sendResponse({ response: "Failed to send text." });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        sendResponse({ response: "Error occurred while sending text." });
      });

    // Required for asynchronous `sendResponse`
    return true;
  }
});
