# ImageNet classifier on Banana.dev

## Cloning
Clone the repo and run:
```bash
git clone --recurse-submodules https://github.
com/egslava/test_banana_image_classifier.git 
```

## Testing
After cloning, run:
```bash
bash run_n_test_all.bash
```

It will:
1) Create the model from the PyTorch model and the 
   weights
2) Convert it to onnx-format and the resulting 
   high-level interface
3) Test the high-level interface against provided 
   examples
4) Run the API (Banana) server
5) Test the server against the provided examples
6) Build the Docker image
7) Test the Docker image with the provided examples.


## Example api call:

```bash
curl --location --request POST 'https://api.banana.dev/start/v4/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "apiKey": "d3a8262d-25e2-4393-ac03-b8e888cf8d8e",
    "modelKey": "5f5051db-1249-4530-be36-a2dc95b0746b",
    "modelInputs" : {
        "image": "UklGRiwAAABXRUJQVlA4ICAAAABQAQCdASoBAAEAAkA4JQBOgCgAAP76eV8CStWlVemeAA=="
    }
}'
```

Where image is base64-encoded image file.

Example output:

```json
{
    "id": "a46d75e8-e9c9-474b-a939-3fd8e849ceec",
    "message": "",
    "created": 1679143667,
    "apiVersion": "January 11, 2023",
    "callID": "",
    "finished": true,
    "modelOutputs": [
        {
            "class": "111"
        }
    ]
}
```

The API is fully working, you can check it manually,
via Postman.