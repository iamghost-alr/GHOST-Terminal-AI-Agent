# GHOST Terminal AI Agent

GHOST is a modular AI-powered terminal assistant built with Python. It combines conversational AI, utility tools, memory capabilities, and voice output into a clean terminal-based experience inspired by modern AI assistants.

## Features

- AI Chat using OpenRouter
- Custom Assistant Personality
- Terminal User Interface using Rich
- API optimzation to reduce cost- Calculator Tool
- Notes Memory System
- Weather Information
- Date and Time Utilities
- Web Search Integration
- Conversation History
- Voice Output using Piper TTS
- Database for saving memories.
- Modular Project Architecture

## Project Structure

```text
GHOST-Terminal-AI-Agent/
│
├── app.py
│
├── router/
│   └── tool_router.py
│
├── database/
│   └── db.py
│
├── tools/
│   ├── calculator.py
│   |__ applications.py
│   |__ sites.py
│   ├── notes.py
│   ├── weather.py
│   ├── web_search.py
│   ├── dbtool.py
│   └── time.py
│
├── voice/
│   ├── tts.py
│   ├── stt.py
│   ├── wake_word.py
│   └── audio.py
│
├── ui/
│   └── terminal_ui.py
│
├── .env
├── requirements.txt
└── README.md
```

## Technologies Used

- Python
- OpenRouter API
- DeepSeek Chat
- Rich
- Piper TTS
- MongoDB
- Requests
- dotenv

## Installation

### Clone Repository

```bash
git clone https://github.com/iamghost-alr/GHOST-Terminal-AI-Agent.git
cd GHOST-Terminal-AI-Agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory.

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Run

```bash
python app.py
```

## Current Capabilities

- AI conversations
- Mathematical calculations locally
- Saving notes and reminders
- Weather lookup
- Date and time queries
- Web search
- Saving and fetching memories using database.
- Voice responses

## Future Plans

- Speech-to-Text
- Wake Word Detection
- Local LLM Support
- Agentic Workflows
- Multi-Tool Reasoning

## Author

Naman Roy

Built as a personal AI assistant project to explore conversational AI, voice systems, tool integration, and agentic workflows.
