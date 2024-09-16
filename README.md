# dtc-arch-support-bot
DataTalks.Club project as part of llm-zoomcamp

## Problem statement
New Linux users often find it difficult to solve problems with software. There are many forums and wiki-websites. However, they contain a lot of information, which can be confusing. By using LLMs, we can provide a user-friendly and customisable response that will directly tackle the issues the user is facing. Arch-support-bot provides information based on the pages of Arch wiki, which is one of the biggest resources available for Linux users.

## Tech stack
**Search:** Elasticsearch

**UI**: NiceGUI

**LLM:** llama3.1:latest, qwen2:latest, zephyr:latest, chatGPT-4o-mini

**Database:** SQLite

**Container**: docker-compose

**Visualisation**: Metabase

## How to run
1. Clone the repository or download the code
2. Add .env file to the root directory with the following content:
~~~
export OPENAI_API_KEY='your-key'
export HF_TOKEN="your-token"

# Elastic search setup
export ELASTIC_URL = http://elasticsearch:9200
export ELASTIC_PORT=9200
export ELASTIC_PATH=/path/to/your/elasticsearch/data/

# Ollama setup
export OLLAMA_URL = http://ollama:11434/v1/
export OLLAMA_PORT=11434
export OLLAMA_MODELS=/path/to/your/ollama/models
~~~
3.1. Extract the file UDix6qDkTaWQGO9uziKGHg.tar.gz from 'data' directory in ELASTIC_PATH/indices. After, run the following command to make sure the indices are available:
~~~
curl -X GET "localhost:9200/_cat/indices?v"
~~~
You should see something like this:
~~~
health status index         uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   archwiki      UDix6qDkTaWQGO9uziKGHg   3   1      25708            0     16.3mb         16.3mb
~~~
3.2. (Optional) Run the following command to index the Archwiki
~~~
python3 indexer.py
~~~
4. Comment the following lines in docker-compose.yaml if you do not have dedicated GPU or want to run on CPU:
~~~
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [ gpu ]
~~~
5. Run:
~~~
docker-compose up
~~~
from the project directory
