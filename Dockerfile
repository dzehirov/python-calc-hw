FROM python:3

ADD . .

RUN pip install coverage

CMD [ "python", "-m", "unittest", "discover", "-s", "Tests" ]