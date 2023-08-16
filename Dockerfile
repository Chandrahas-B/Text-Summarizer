FROM python:3.9.17-slim-bullseye

WORKDIR home/
COPY . .

RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install -U summarizer
RUN pip install -U sentence-transformers
RUN pip install -U bert-extractive-summarizer
CMD python app.py
