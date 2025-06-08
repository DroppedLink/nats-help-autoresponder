FROM python:3.11-slim
WORKDIR /app
COPY responder.py .
RUN pip install nats-py
CMD ["python", "responder.py"]
