FROM nikolaik/python-nodejs:python3.9-nodejs18
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN git clone -b master https://github.com/TeamYukki/YukkiMusicBot/
COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install --ignore-installed PyYAML 
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
CMD [ "bash", "start" ]
