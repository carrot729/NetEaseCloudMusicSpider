FROM python
LABEL authors="hnf72"
RUN pip install virtualenv
RUN pip install pip install -r requirements.txt
RUN virtualenv venv
CMD source venv/bin/activate

ENTRYPOINT ["top", "-b"]