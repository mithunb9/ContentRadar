// Function to send a message to the background service worker
function sendMessageToBackground() {
  console.log("sending");
  if (chrome && chrome.runtime && chrome.runtime.sendMessage) {
    console.log("Sending message to background...");
    chrome.runtime.sendMessage({ type: "sendText", payload: document.body.innerText }, (response) => {
      if (chrome.runtime.lastError) {
        console.error("Error:", chrome.runtime.lastError.message);
      } else if (response) {
        console.log("Response from background script:", response.response);
      } else {
        console.log("No response from background script.");
      }
    });
  } else {
    console.error("chrome.runtime.sendMessage is not available.");
  }
}

setInterval(sendMessageToBackground, 1000);
