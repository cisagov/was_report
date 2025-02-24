FROM python:latest
ENV WAS_GENERATE_REPORT_SRC="/usr/src/was-generate-report"

RUN apt-get update && apt-get -y install python3 texlive-xetex

RUN mkdir /WAS_REPORT_GENERATION
RUN mkdir /WAS_REPORT_GENERATION/docs
RUN mkdir /WAS_REPORT_GENERATION/assets
RUN mkdir /WAS_REPORT_GENERATION/assets/fonts
WORKDIR /WAS_REPORT_GENERATION
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
