FROM proycon/lamachine

WORKDIR /src
ADD src .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "--config=gunicorn.py", "app:app"]
