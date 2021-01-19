FROM python:3.6

ARG project_dir=/project/

ADD ./requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

RUN export FLASK_ENV=development

RUN export FLASK_APP='run.py'