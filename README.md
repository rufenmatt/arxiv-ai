# Flask app for reading arXiv ML papers and generating answers using OpenAI

This Flask app is a simple implementation for fetching the latest [arXiv](https://arxiv.org/) papers on machine learning and generating answers to questions using the OpenAI API.

## Prerequisites

Before running the Flask app, make sure you have the following installed:

- Python 3.6 or higher
- Flask
- Requests
- Feedparser
- OpenAI API key

## Installation

1. Clone the repository to your local machine:


2. Install the required packages:


3. Create a free account on [OpenAI](https://beta.openai.com/signup/) and get your API key.

4. Set your OpenAI API key in the user input after spinning of the app.


## Usage

To run the Flask app, execute the following command:


The app will be available on `http://localhost:81/`.

## API Endpoints

- `/`: Displays a list of papers related to machine learning fetched from arXiv API.

- `/set-openai-key`: Sets the OpenAI API key in the session.

- `/paper/<int:paper_id>`: Displays the details of a paper with the specified ID.

- `/generate-answer`: Generates an answer to a prompt using the OpenAI API.

## License

This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 License. See the `LICENSE` file for details.
