# https://hub.docker.com/_/python
FROM python:3.10.6

WORKDIR /usr/src/app

COPY requirements.txt ./
# pip업글 하라고 에러떠서...
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN uvicorn app:app --port 5556 --reload
# RUN uvicorn app:app --reload
# CMD ["python3","app.py"]
# CMD ["uvicorn","app:app","--port 5556","--reload"]
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","5556","--reload"]
