FROM python:3.8

RUN pip install streamlit

COPY ./main.py /streamlit/

CMD ["streamlit", "run", "streamlit/main.py", "--server.port", "80"]