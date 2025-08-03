# LangGraph Agent

A simple LangGraph-based agent that demonstrates tool usage with weather and stock price queries.

## Features

- **LangGraph Workflow**: Implements a state-based workflow with conditional tool execution
- **Tool Integration**: Includes weather and stock price tools
- **Streaming Output**: Real-time response streaming
- **12-Factor Design**: Follows 12-factor app principles

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Configure environment**:
   ```bash
   cp .example.env .env
   # Add your OpenAI API key to .env
   ```

## Usage

Run the agent:
```bash
python src/langgraph_agent/main.py
```

## Project Structure

- `src/langgraph_agent/main.py` - Entry point and agent execution
- `src/langgraph_agent/graph.py` - LangGraph workflow definition
- `src/langgraph_agent/tools.py` - Tool implementations (weather, stock price)

## Requirements

- Python 3.12+
- OpenAI API key
