FROM python:3.6 
LABEL maintainer "Taketoshi Kazusa <taketoshi.kazusa@gmail.com>"
ENV REFRESHED_AT 2018/09/07

RUN apt-get -qq update; \
    apt-get -qq -y upgrade; \
    apt-get -qq -y install \
        curl vim \ 
    pip install --upgrade setuptools; \
    pip install --upgrade gcloud; \
    pip install scikit-learn pandas scipy flask requests

ADD src /src
EXPOSE 8081
RUN ["chmod", "+x", "/src/backend.py"]
CMD ["python3", "/src/backend.py"]

