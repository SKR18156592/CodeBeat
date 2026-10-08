FROM python
WORKDIR /app
COPY . /app
CMD [ "python","example.py" ]