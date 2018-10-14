FROM python:3.6
LABEL maintainer "Taketoshi Kazusa <taketoshi.kazusa@gmail.com>"
ENV REFRESHED_AT 2018/09/07

RUN apt-get -qq update; \
    apt-get -qq -y upgrade; \
    apt-get -qq -y install \
        curl vim \
    pip install --upgrade setuptools; \
    pip install --upgrade gcloud; \
    pip install FLask Flask-SQLAlchemy Flask-WTF Flask-Bootstrap Flask-Migrate pytest pytest-mock requests

ADD src /src
EXPOSE 8080
RUN ["chmod", "+x", "/src/frontend.py"]
CMD ["python3", "/src/frontend.py"]

