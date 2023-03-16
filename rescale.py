def preprocess_numpy(img):
    """
    The function from the original model. I believe
    it had to be a static function, so to use this
    function the model shouldn't be a dependency.

    Anyways, I have to copy-paste it here or to
    modify the original repo
    """
    from torchvision import transforms
    resize = transforms.Resize((224, 224))  # must same as here
    crop = transforms.CenterCrop((224, 224))
    to_tensor = transforms.ToTensor()
    normalize = transforms.Normalize(
        [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    img = resize(img)
    img = crop(img)
    img = to_tensor(img)
    img = normalize(img)
    return img