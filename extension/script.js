// Function to send a message to the background service worker
function sendMessageToBackground() {
  console.log("sending");
  chrome.runtime.sendMessage({ type: "sendText", payload: document.body.innerText }, (response) => {
    if (chrome.runtime.lastError) {
      console.error("Error:", chrome.runtime.lastError);
    } else {
      console.log("Response from background script:", response.response);
    }
  });
}

// Call the function every 10 seconds
setInterval(sendMessageToBackground, 10000);
