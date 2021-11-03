import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

joke = pyjokes.get_joke()

data = {'text': joke}
requests.post(url='https://hooks.slack.com/services/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', json = data)