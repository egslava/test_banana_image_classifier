from PIL import Image
import sys

try:
    from rescale import preprocess_numpy
except:
    import sys
    sys.path.append('..')
    from rescale import preprocess_numpy

import onnxruntime as ort


class Model:
    def __init__(self, filename='model/model.onnx'):
        self.sess = ort.InferenceSession(filename)

    def predict(self, filename: str):
        img = Image.open(filename)
        inp = preprocess_numpy(img).unsqueeze(0)

        output = self.sess.run(
            None,
            {'input.1': inp.numpy()}
        )

        # [0] because first batch
        # argmax() because it returns ndarray of
        # probabilities and we need the class
        # with the max probability
        return output[0].argmax()
