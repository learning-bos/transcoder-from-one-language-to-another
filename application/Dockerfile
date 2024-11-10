
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "-m", "streamlit", "run", "main.py" ]