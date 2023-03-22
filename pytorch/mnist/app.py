import os
import argparse
from PIL import Image
import torch
from torchvision import transforms


from model import Net


dir_path = os.path.dirname(os.path.realpath(__file__))
default_img_path = os.path.join(dir_path, 'images/6.png')


def main():

    parser = argparse.ArgumentParser(description='PyTorch MNIST Predictor')
    parser.add_argument('--image', type=str, default=default_img_path, metavar='IMG',
                        help='image for prediction (default: {})'.format(default_img_path))
    args = parser.parse_args()

    model_path = os.path.join(dir_path, 'mnist_cnn.pt')
    model = Net()
    model.load_state_dict(torch.load(model_path))

    im = Image.open(args.image)
    # print(args.image, im.format, f"{im.size}x{im.mode}")
    # im.show()
    grayscale_img = im.convert('L')

    transform = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    img = torch.autograd.Variable(transform(grayscale_img).unsqueeze(0))
    im.close()

    model.eval()
    output = model(img)
    pred = output.data.max(1, keepdim=True)[1][0][0]
    print('Prediction: {}'.format(pred))


if __name__ == '__main__':
    main()
