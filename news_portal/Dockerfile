FROM python:3.7

WORKDIR /news_portal

COPY .requirements.txt /news_portal/requirements.txt
RUN pip install -r /news_portal/requirements.txt

COPY . /news_portal/


EXPOSE 8000

CMD ["python", "manage.py", "parser_news"]
CMD ["pytnon", "manage.py", "runserver", "0.0.0.0:8000"]

