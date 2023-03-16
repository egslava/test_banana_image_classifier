# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests, os
from base64 import b64encode


def api(path):
    from pathlib import Path
    img = Path(path).read_bytes()
    image = b64encode(img).decode('utf-8')
    res = requests.post(
        'http://localhost:8000/',
        json={'image': image}
    )
    return int(res.json()['class'])


def test_image(image: str):
    return os.path.join(
        '_2_convert_to_onnx',
        'tests',
        image
    )

# banana_config.json doc example
response = requests.post(
    'http://localhost:8000/',
    json={'image': "UklGRiwAAABXRUJQVlA4ICAAAABQAQCdASoBAAEAAkA4JQBOgCgAAP76eV8CStWlVemeAA=="}
)
assert 111 == int(response.json()['class'])
assert 0 == api(test_image('n01440764_tench.jpeg'))
assert 35 == api(
    test_image('n01667114_mud_turtle.JPEG')
)
