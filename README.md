# Google Search Agent

This project is an intelligent assistant built using Streamlit and the Groq language model, which performs Google searches and summarizes the content of the top results. The application leverages the `langchain-groq`, `googlesearch-python`, `beautifulsoup4`, `requests`, and `python-dotenv` libraries to provide accurate and concise answers to user queries.

## Features

- Perform Google searches based on user queries.
- Summarize the content of the top search results.
- Display the summarized information in a user-friendly Streamlit app.

## Installation

### Prerequisites

- Python 3.7 or higher

### Step-by-Step Guide

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/Google_Search_Agent.git
    cd Google_Search_Agent
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:

    Create a file named `.env` in the root directory of the project and add your Groq API key:

    ```plaintext
    GROQ_API_KEY=your_api_key_here
    ```

## Usage

1. **Run the Streamlit app**:

    ```sh
    streamlit run app.py
    ```

2. **Interact with the app**:

    - Open your web browser and go to `http://localhost:8501`.
    - Enter your query in the text input field.
    - Click the "Get Answer" button to receive a summarized answer.

## Project Structure
Google_Search_Agent/
│
├── .env
├── app.py
├── requirements.txt
└── README.md
- **`.env`**: Contains environment variables, including the Groq API key.
- **`app.py`**: The main application script that sets up the Streamlit app and integrates the Google search and summarization functionalities.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`README.md`**: Provides an overview and instructions for the project.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Groq](https://www.groq.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [tqdm](https://github.com/tqdm/tqdm)
- [googlesearch-python](https://github.com/MarioVilas/googlesearch-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
