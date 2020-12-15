FROM python:3.8

WORKDIR /api
COPY api api
COPY migrations migrations
COPY requirements.txt requirements.txt
COPY run.py run.py
COPY config.py config.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python run.py