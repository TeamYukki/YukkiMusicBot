FROM nikolaik/python-nodejs:python3.9-nodejs17
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
WORKDIR /app/
RUN chmod 777 /app/
RUN pip3 install --no-warn-script-location --force-reinstall --ignore-installed --no-cache-dir --user -r requirements.txt
CMD bash start
