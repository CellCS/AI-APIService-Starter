FROM python:3.12.0b1-slim-buster
COPY ./api_service /app
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt
CMD ["python","main.py"]