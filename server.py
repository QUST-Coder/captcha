import falcon
from captcha.image import ImageCaptcha
import base64

class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles POST requests"""
        resp.status = falcon.HTTP_200
        char = req.query_string[0:4]
        captcha = ImageCaptcha()
        data = captcha.generate(char)
        img_str = base64.b64encode(data.getvalue())
        resp.body = (img_str)


# falcon.API instances are callable WSGI apps
app = falcon.API()

# resources are represented by long-live class instances
things = ThingsResource()

#things will handle all requests to the '/cpc,' URL path
app.add_route('/cpc', things)
