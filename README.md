# behave-tests

## Run tests locally

It requires locally installed Chrome/Chromium and chromedriver/chromiumdriver.

```bash
$ pip install -r requirements.txt
$ behave
```

By default it runs in headless mode. To see actual browser use `fixtures.selenium_browser_chrome` in [features/environment.py](features/environment.py)

## Run tests in docker

```bash
$ docker build . -t behave
$ docker run behave
```
