FROM python:3.8.7

WORKDIR /app/

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && \
    pipenv install --system --ignore-pipfile

EXPOSE 5000

ENTRYPOINT ["python"]

COPY . /app/

CMD ["src/app.py"]



