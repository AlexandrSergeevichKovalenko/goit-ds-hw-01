#using the oficial python basic image
FROM python:3.11

#poetry installation
RUN pip install poetry

#creating a directory for the project
WORKDIR /app

#creating a file copy
COPY . /app

#installation of dependencies
RUN poetry install

#the command to run the CLI app
ENTRYPOINT [ "poetry", "run", "python", "/app/my_project/main.py" ]




