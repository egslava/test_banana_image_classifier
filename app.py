import torch
from transformers import T5Tokenizer, \
    T5ForConditionalGeneration


# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    global tokenizer

    device = 0 if torch.cuda.is_available() else -1

    from _2_convert_to_onnx.model import Model
    model = Model(
        '_2_convert_to_onnx/model/model.onnx')


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs: dict) -> dict:
    import base64, io
    global model

    # Parse out your arguments
    image = model_inputs.get('image', None)
    if image is None:
        return {'error': "No image provided"}

    # try:
    with open('out.jpg', 'wb') as f:
        f.write(base64.b64decode(image))

    return {'class': str(model.predict('out.jpg'))}
    # except Exception as e:
    #     return {'error': str(e)}
