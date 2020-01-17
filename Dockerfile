FROM python:3.8-slim

ENV CHROME_DRIVER_VERSION 79.0.3945.36
ENV CHROME_DRIVER_TARBALL http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
ENV PATH /usr/lib/chromium/:$PATH

WORKDIR /behave
COPY ./ /behave

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gnupg \
    && curl https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \    
    && curl $CHROME_DRIVER_TARBALL | zcat > /usr/local/bin/chromedriver \
    && chown root:root /usr/local/bin/chromedriver \
    && chmod 0755 /usr/local/bin/chromedriver \
    && pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "behave" ]
