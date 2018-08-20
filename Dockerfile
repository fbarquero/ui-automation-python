# Docker image for flask service

FROM python:2.7-alpine

RUN mkdir /tmp/results
COPY . /app
RUN pip install -r /app/requirements.txt
# CMD ["nosetests", "-v", "--with-xunit", "--xunit-file=/tmp/results/test_result.xml"]
# CMD ["cat", "/app/tests/test_python_selenium.py"]
CMD ["nosetests", "-vvv"]