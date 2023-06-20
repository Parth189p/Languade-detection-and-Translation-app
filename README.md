# Languade-detection-and-Translation-app

This data science project focuses on developing a language detection model that can predict the language of a given text. The model is trained using a dataset collected from various websites, consisting of approximately 20,000 rows and covering around 20 different languages. After performing data cleaning and analysis, different classification models were evaluated, and the CountVectorizer combined with Multinomial Naive Bayes was selected as the best-performing model.

This project implements a language detection model and translation functionality using a web application built with FASTAPI. The application allows users to input text, detect the language, and translate it into different languages including English, Hindi, and Gujarati.

## Table of Contents

- [Dataset](#dataset)
- [Models](#models)
- [Features](#features)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Progress](#progress)
- [Next Steps](#next-steps)

## Dataset

The dataset used in this project is sourced from various websites and contains a wide range of texts in different languages. The dataset comprises approximately 20,000 rows, and each row consists of a text sample and its corresponding language label. The data was cleaned and preprocessed to remove symbols, numbers, and special characters, ensuring the accuracy and reliability of the model.

## Models

Several classification models were evaluated to identify the most suitable model for language detection. After rigorous testing and evaluation, the combination of CountVectorizer and Multinomial Naive Bayes proved to be the most effective in accurately predicting the language of a given text. The CountVectorizer technique converts text into numerical features, and Multinomial Naive Bayes is a probabilistic classifier commonly used for text classification tasks.

## Features

- Language detection: The system employs a trained language detection model to identify the language of the provided text accurately. It supports a wide range of languages, including Arabic, Danish, Dutch, English, French, German, Greek, Gujarati, Hebrew, Hindi, Hinglish, Italian, Kannada, Malayalam, Portuguese, Russian, Spanish, Swedish, Tamil, and Turkish.
- Translation: The application integrates translation functionality, allowing users to convert text into various languages. Currently, it supports translation into English, Hindi, and Gujarati, but it can be easily expanded to include more languages.
- User-friendly interface: The web-based user interface provides a simple and intuitive experience. Users can input text, receive language predictions, view translations, and choose different target languages with just a few clicks.

## Usage

1. Start the FASTAPI server: `uvicorn main:app --reload`
2. Open your web browser and go to http://localhost:8000.
3. Enter the text you want to analyze in the input field.
4. Click the "Predict" button to detect the language and view the translation.
5. To translate the text into a different language, click on one of the available language buttons (English, Hindi, Gujarati).

## API Endpoints

- `POST /predict`: Accepts a JSON payload with a text field and returns the detected language and translated text in English.
- `POST /translate`: Accepts a JSON payload with a text field and a language field specifying the target language for translation. It returns the translated text in the specified language.

## Project Structure

- `main.py`: Contains the main FastAPI application code, including the API endpoints and their corresponding logic.
- `static/`: Directory containing static files for the web application, such as CSS stylesheets and JavaScript files.
- `templates/`: Directory containing HTML templates for the web application.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Progress

The project has made significant progress in implementing the language detection and translation functionalities. Here are the key accomplishments so far:

- Developed a language detection model using machine learning techniques.
- Created a web application using FASTAPI to provide an interactive user interface.
- Integrated the trained language detection model into the application for predicting the language of input text.
- Implemented translation functionality to convert text into English, Hindi, and Gujarati.
- Designed a user-friendly interface that allows users to easily input text, view language predictions, and access translations.
- Ensured scalability by using modular code structure and adhering to best practices.

## Next Steps

- Expand the language translation options to include additional languages based on user demand.
- Optimize the language detection model for improved accuracy and efficiency.
- Implement user authentication and authorization to manage access to the application.
- Enhance the user interface with additional features and customization options.
- Perform rigorous testing and debugging to ensure the application's stability and reliability.

