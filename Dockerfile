FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    x11vnc \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN echo '#!/bin/bash\n\
XVFB_RUN="xvfb-run -a"\n\
$XVFB_RUN python main.py\n' > /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]
