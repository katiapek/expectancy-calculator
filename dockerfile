FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "expectancy_calculator.py", "--server.port=8080", "--server.address=0.0.0.0"]