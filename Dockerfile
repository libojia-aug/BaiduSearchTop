FROM python:3.7.3

RUN mkdir /code 
COPY / /code 
COPY requirements.txt /code

RUN pip3 install --upgrade pip -i https://pypi.douban.com/simple
RUN pip3 install -r /code/requirements.txt -i https://pypi.douban.com/simple

WORKDIR /code

ENTRYPOINT ["python3","main.py"]