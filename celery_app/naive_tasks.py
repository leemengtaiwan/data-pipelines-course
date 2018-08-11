''' Here are a few options for chp3 homework '''
from celeryapp import app
from datetime import datetime, timedelta

@app.task
def test():
    return {"result": "successed"}

