FROM python:3
RUN apt-get update
RUN yes | apt-get install python3-pip
RUN pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN yes | pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["api.py"]
