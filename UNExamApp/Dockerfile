
FROM centos7
LABEL Author="Mohamad Rahhal"
WORKDIR .
COPY . .

RUN yum install -y python36 python36-virtualenv 

RUN yum clean all && \
    mkdir /log && \
    virtualenv-3.6 env && \
    source /env/bin/activate && \
    /env/bin/pip install -r requirements.txt \
    python3 manage.py runserver 

