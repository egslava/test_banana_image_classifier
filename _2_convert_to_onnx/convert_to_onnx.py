import sys, os, torch

sys.path.append(os.path.join('..'))

from _1_pull_model.pytorch_model import (
    Classifier, BasicBlock
)


def load_weights_n_save_as_onnx(
        filename='model/model.onnx'
):
    mtailor = Classifier(BasicBlock, [2, 2, 2, 2])
    mtailor.load_state_dict(
        torch.load("./model/resnet18-f37072fd.pth")
    )

    torch.onnx.export(
        mtailor,
        torch.zeros((1, 3, 224, 224)),
        filename
    )


if __name__ == '__main__':
    load_weights_n_save_as_onnx()
