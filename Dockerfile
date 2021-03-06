# pull the official base image
FROM python:3.9-slim

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /code
RUN pip install -r requirements.txt

# copy project
COPY . /code
# CMD ["python", "manage.py", "collectstatic"]
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]