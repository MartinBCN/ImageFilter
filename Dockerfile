FROM python:3.7-buster

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

COPY src/image_filter /app

WORKDIR /app

EXPOSE 8501

RUN "streamlit run filter_frontend.py"
