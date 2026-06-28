# Five AI Agents Collection

## Overview

This repository contains five independent AI agents developed using Python, the Groq API, and the Llama-3.3-70B-Versatile large language model. Each agent is designed to solve a specific real-world problem through prompt engineering and natural language processing. The agents are independent and focus on their individual tasks without interacting with one another.

## AI Agents

### Resume Review Agent

Analyzes resumes and provides constructive feedback on content, skills, formatting, and areas for improvement.

### Email Classification Agent

Classifies emails into categories such as Work, Personal, Promotions, and Spam based on their content.

### Study Planner Agent

Generates personalized study plans according to the user's goals, available study time, and learning priorities.

### Contract Risk Analyzer Agent

Reviews contract text and identifies potential risks, important clauses, and areas that may require attention.

### Bug Report Analyzer Agent

Analyzes software bug reports and summarizes the issue, estimates severity, and highlights possible causes.

## Technologies Used

* Python 3
* Groq API
* Llama-3.3-70B-Versatile
* python-dotenv

## Project Structure

```text
five-ai-agents/
│
├── bug-report-analyzer-agent/
├── contract-risk-analyzer-agent/
├── email-classification-agent/
├── resume-review-agent/
├── study-planner-agent/
│
├── run.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/five-ai-agents.git
```

Navigate to the project directory:

```bash
cd five-ai-agents
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Groq API key.

```env
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

## Running the Project

Run the following command:

```bash
python run.py
```

A menu will be displayed where you can choose any of the five AI agents. The selected agent will process the input and generate a response based on its specific purpose.

## Future Enhancements

Possible improvements for this project include:

* Adding a web interface using FastAPI or Streamlit
* Maintaining conversation history
* Supporting additional AI agents
* Writing automated tests
* Containerizing the project with Docker

## License

This project is licensed under the MIT License.
