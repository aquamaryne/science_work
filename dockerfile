FROM python:3.11-slim
WORKDIR /flask
COPY requirements.txt . /flask/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["flask", "run"]