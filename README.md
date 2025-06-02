# Research-Paper-Summarizer

An autonomous AI research assistant that performs multi-step research tasks by planning, collecting, verifying, summarizing, and generating research reports from multiple data sources like Wikipedia, NewsAPI, and scholarly articles.

---

## Features

- Plans research tasks based on user query
- Collects data from Wikipedia summaries, NewsAPI headlines, and more
- Verifies collected information credibility
- Summarizes verified data into concise reports
- Generates comprehensive research reports in a readable format
- Built with Flask for a simple web interface

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Research-Paper-Summarizer.git
cd Research-Paper-Summarizer
```
2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install required dependencies:
```bash
pip install -r requirements.txt
```
4. (Optional) Add your NewsAPI API key in graph/agent_graph.py:
NEWS_API_KEY = "your_newsapi_key_here"

## Usage

Run the Flask app:
```bash
python app.py
```
Open your browser and go to http://127.0.0.1:5000
Enter a research query and get an AI-generated research report.

Project Structure
```bash
project/
├── app.py                  # Flask app entry point
├── templates/
│   └── index.html          # HTML template for web UI
├── graph/
│   └── agent_graph.py      # Workflow graph connecting AI agents
├── agents/
│   ├── planner.py          # Task planning agent
│   ├── collector.py        # Data collection agent
│   ├── verifier.py         # Data verification agent
│   ├── summarizer.py       # Summarization agent
│   └── reporter.py         # Report generation agent
└── requirements.txt        # Python dependencies
```
## Dependencies
- Flask
- requests
- beautifulsoup4
- langgraph (custom or installed package)

## License
This project is licensed under the MIT License.

Acknowledgments
Inspired by modular AI agent architectures and autonomous workflows.
