FROM mageai/mageai:llm

ARG USER_CODE_PATH=/home/dmitry/Documents/Programming/Python/dtc-arch-support-bot

# Note: this overwrites the requirements.txt file in your new project on first run.
# You can delete this line for the second run :)

RUN pip3 install -r /home/dmitry/Documents/Programming/Python/dtc-arch-support-bot/requirements.txt