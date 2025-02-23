# Intelligent Hotel Chatbot

This project is an intelligent chatbot that interacts based on hotel information. The chatbot is designed to process and retrieve relevant hotel data efficiently using natural language processing (NLP) and embedding techniques.

## Features
- Load and process hotel data
- Perform text embedding for semantic search
- Search for relevant hotel information
- Provide conversational responses based on hotel data
- Convert raw text data into structured CSV format

## Project Structure
```
chatbot/
│── app.py                  # Main application file
│── data.txt                # Raw hotel data file
│── embeddings.csv          # Preprocessed text embeddings
│── scraped.csv             # Scraped hotel data
│── search.py               # Search functionality implementation
│── text_embedding.py       # Text embedding logic
│── text_to_csv_converter.py # Data conversion utility
```

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/chatbot.git
cd chatbot
```

### 2. Install Dependencies
Ensure you have Python installed (Python 3.8+ recommended). Install required dependencies using:
```sh
pip install -r requirements.txt
```

## How to Run
### 1. Prepare Data
Ensure `data.txt` contains the necessary hotel information. If the data is in an unstructured format, use the `text_to_csv_converter.py` to convert it into a structured CSV format.
```sh
python text_to_csv_converter.py
```
This will generate `scraped.csv`, which will be used for further processing.

### 2. Generate Embeddings
Run the following command to generate text embeddings for hotel information:
```sh
python text_embedding.py
```
This will create an `embeddings.csv` file, which stores vector representations of hotel data.

### 3. Start the Chatbot Application
```sh
python app.py
```
This will launch the chatbot, allowing users to query hotel-related information interactively.

### 4. Search for Hotel Information
To search for specific hotel details, run:
```sh
python search.py "query text here"
```
Replace `"query text here"` with your actual query.

## Usage Example
1. Start the chatbot using `python app.py`
2. Enter queries like:
   - "Find me a 5-star hotel in Paris."
   - "What are the amenities of Hotel XYZ?"
   - "Which hotels are available near the airport?"
3. The chatbot will provide relevant responses based on processed data.

## Future Enhancements
- Improve NLP capabilities with advanced AI models
- Integrate with external hotel APIs for real-time availability
- Develop a web interface for a more interactive user experience

## License
This project is licensed under the MIT License.

