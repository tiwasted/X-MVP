import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):

            # Декодируем token если он имеет тип bytes.
            data['token'] = token.decode('utf-8')

        return json.dump({
            'user': data
        })
