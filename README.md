# dtc-arch-support-bot
DataTalks.Club project as part of llm-zoomcamp

## Problem statement
New Linux users often find it difficult to solve problems with software. There are many forums and wiki-websites. However, they contain a lot of information, which can be confusing. By using LLMs, we can provide a user-friendly and customisable response that will directly tackle the issues the user is facing. Arch-support-bot provides information based on the pages of Arch wiki, which is one of the biggest resources available for Linux users.

## UI showcase from an early build
[Screencast_20240810_001001.webm](https://github.com/user-attachments/assets/75078295-44bf-4470-a36a-fb7a606d1a29)

## Example response
![Screenshot_20240917_103632](https://github.com/user-attachments/assets/b28dd6a7-19c0-4ac7-bfc1-71e9009e8a0a)

## Tech stack
**Search:** Elasticsearch 8.4.3

**Code**: Python 3.12

**UI**: NiceGUI latest

**LLMs:** llama3.1:8b, qwen2:7b, zephyr:7b, chatGPT-4o-mini

**Database:** SQLite (./data/feedback.db)

**Container**: docker-compose

**Visualisation**: Metabase latest (in progress)

## What it can do:
- provides a choice of 4 models. GPT-4o-mini usually shows the best results, but if you do not have API, you can use Qwen2 as the second-best;
- checks that you choose a model;
- informs you if the query is empty;
- stores all queries, corresponding answers, and feedback in feedback.db (SQlite);
- stores the knowledge base as Elasticsearch indices;
- can re-index files using the indexer.py.

## How to run
1. Clone the repository or download the code

2. Add .env file to the root directory with the following content:
~~~
export OPENAI_API_KEY='your-key' # CHANGE THIS!
export HF_TOKEN="your-token" # CHANGE THIS!

# Elastic search setup
export ELASTIC_URL = http://elasticsearch:9200
export ELASTIC_PORT=9200
export ELASTIC_PATH=/path/to/your/elasticsearch/data/ # CHANGE THIS!

# Ollama setup
export OLLAMA_URL = http://ollama:11434/v1/
export OLLAMA_PORT=11434
export OLLAMA_MODELS=/path/to/your/ollama/models # CHANGE THIS!
~~~
3. (Optional) The indices are located in ./data/indices/UDix6qDkTaWQGO9uziKGHg/. To check that Elasticsearch found the indices, use the following command:
~~~
curl -X GET "localhost:9200/_cat/indices?v"
~~~
You should see something like this:
~~~
health status index         uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   archwiki      UDix6qDkTaWQGO9uziKGHg   3   1      25708            0     16.3mb         16.3mb
~~~

If you have a problem with indices in Elasticsearch, you can delete the existing files in ./data/indices and extract the attached tar.gz. It contains a copy of the index of Archwiki.

4. Comment the following lines in docker-compose.yaml if you do not have a dedicated GPU or want to run on CPU:
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
from the project directory.

6. NiceGUI takes some time to start. Look for the output that says NiceGUI is ready. It will mention the address you need to access. It is usually localhost:8080 and an alternative address using a random IP. The localhost does not work all the time, so you need to look for the IP address.

7. (Optional) You can create the index from scratch if you want. In this case, run the following command to index the Archwiki after you start the docker-compose:
~~~
python3 indexer.py
~~~
## Known problems
- sometimes UI shows the 'Connection lost' error when the Send button is pressed. The connection goes away, but the result is not shown. The docker-compose output will have the following lines:
~~~
ollama         | [GIN] 2024/09/17 - 02:33:00 | 200 | 18.576690483s |      172.21.0.2 | POST     "/v1/chat/completions"
~~~
In this case, simply refresh the page, and you will see the output.
