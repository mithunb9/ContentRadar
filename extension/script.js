// Function to get all text on the page
function getPageText() {
  return document.body.innerText;
}

// Function to send the extracted text to the background script
function sendTextToBackground() {
  const text = getPageText();
  console.log("Extracted text from page:", text);
  chrome.runtime.sendMessage({ action: "saveText", text: text });
}

setInterval(() => {
  // This will run every 10 seconds
  console.log(document.body.innerText);
  // You can send a message to content scripts or perform other actions
}, 1000);
