FROM zauberzeug/nicegui:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "main.py"]