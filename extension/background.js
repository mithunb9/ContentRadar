chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "runCommand") {
    // Your command to execute on the page
    console.log("Command executed on the page.");
    // Example: Refresh a translator or any other functionality
  }
});
