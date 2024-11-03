if (document.readyState === "loading") {
  // The DOM is still loading, wait for it
  document.addEventListener("DOMContentLoaded", initializeObserver);
} else {
  // The DOM is already loaded
  initializeObserver();
}

function initializeObserver() {
  console.log("DOM fully loaded and parsed");

  // Function to handle sending content
  let timeout;
  function sendContent() {
    if (timeout) clearTimeout(timeout); // Clear previous timeout

    timeout = setTimeout(() => {
      const content = document.body.innerText;
      console.log("Sending content:", content);

      chrome.runtime.sendMessage({ type: "pageContent", content, url: window.location.href }, (response) => {
        if (chrome.runtime.lastError) {
          console.error("Runtime error:", chrome.runtime.lastError);
        } else {
          console.log("Message sent successfully:", response);
        }
      });
    }, 300); // Debounce interval of 300ms
  }

  // Observe mutations with debounce
  let observer = new MutationObserver(sendContent);

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });

  // Initial call to send content right after loading
  sendContent();
}
