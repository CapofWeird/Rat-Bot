# syntax=docker/dockerfile:1
FROM python:slim

WORKDIR /usr/src/ratty

# Set up a virtualenv.
# This suppresses an error from pip about running pip as root.
# This method was pulled from here: https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRT_ENV=/usr/src/ratty/env
RUN python3 -m venv $VIRT_ENV
ENV PATH="$VIRT_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY rat_bot.py .

CMD [ "python3", "rat_bot.py" ]