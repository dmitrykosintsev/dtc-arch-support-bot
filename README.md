# dtc-arch-support-bot
DataTalks.Club project as part of llm-zoomcamp

## Problem statement
New Linux users often find it difficult to solve problems with software. There are many forums and wiki-websites. However, they contain a lot of information, which can be confusing. By using LLMs, we can provide a user-friendly and customisable response that will directly tackle the issues the user is facing. Arch-support-bot provides information based on the pages of Arch wiki, which is one of the biggest resources available for Linux users.

## Tech stack
**Search:** Elasticsearch

**UI**: NiceGUI

**LLM:** gemma2b, qwen2, phi3, chatGPT-4o-mini

**Database:** SQLite

**Container**: docker-compose

## How to run
1. Clone the repository or download the code
2. Add .env file to the root directory with the following content:
~~~
export OPENAI_API_KEY='your-key'
export HF_TOKEN="your-token"

# Elastic search setup
export ELASTIC_URL = http://elasticsearch:9200
export ELASTIC_PORT=9200

# Ollama setup
export OLLAMA_URL = http://ollama:11434/v1/
export OLLAMA_PORT=11434
export OLLAMA_MODELS=/path/to/your/ollama/models
~~~
3. Run:
~~~
docker-compose up
~~~
from the project directory
