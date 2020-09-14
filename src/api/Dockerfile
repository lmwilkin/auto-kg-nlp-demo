FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
ENV PORT 40000
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2
EXPOSE 8501

# Install spacy requirments separately first so that Docker will 
# cache the (somewhat) expensive download of a spacy model
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
RUN python -m spacy download en_core_web_lg

COPY ./app /app/app
