
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


## Banana API
API should (but not) available, since my connection 
often drops, but the base docker image is about 3GB.
Thus, every time the connection drops, it just 
starts downloading it over and over again. I was 
dumb enough to try starting downloading Docker 
image only ~3h after I started and, thus, 2h was 
not enough to download it. Optimistically, soon API 
would be available and it would be possible to call 
it by calling:

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

Since I don't have downloaded docker image, it's 
hard for me to debug effectively. I tried debug on 
banana.dev itself, but it takes ~20-25 minutes to 
compile the model, so it's also quite 
time-consuming and breaks the 5h limit for this task.