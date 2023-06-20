// static/js/main.js

// JS code for handling form submission and displaying prediction result
// Function to handle form submission
const form = document.getElementById("prediction-form");
const resultDiv = document.getElementById("prediction-result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const text = formData.get("text");

  if (text) {
    // Send a POST request to the server
    fetch('/predict', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: text,
      }),
    })
      .then(response => response.json())
      .then(data => {
        // Update the prediction value and translated text in the UI
        var predictionElement = document.getElementById("prediction");
        predictionElement.textContent = data.language;
      
        var translatedTextElement = document.getElementById("translated-text");
        translatedTextElement.textContent = data.translated_text;
      })
      .catch(error => console.error('Error:', error));
  }
});

// Function to handle translation button click
function translateTo(language) {
  const translatedTextElement = document.getElementById('translated-text');
  const translatedText = translatedTextElement.textContent;

  // Send a POST request to the server to translate the text
  fetch('/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: translatedText,
      language: language,
    }),
  })
    .then(response => response.json())
    .then(data => {
      // Update the translated text in the UI
      translatedTextElement.textContent = data.translated_text;
    })
    .catch(error => console.error('Error:', error));
}
