FROM python:3.12.0

WORKDIR /navigator

COPY  navigator.py requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY . /navigator/

CMD streamlit run --server.port 8501 --server.enableCORS false navigator.py


