# Text-to-Sketch

Drawing a face for a suspect just based on the descriptions of the eyewitnesses is a difficult task. There are some state-of-the-art methods in generating face images from text, but there is still a lot of room for improvement in similarity between input text and generated images. Here, we want to go even further and generate sketches rather than a RGB image.

We want to leverage two different models in order to produce sketches from text. To obtain an image of a face from a description, we are using Text-To-Image Synthesis with DCGAN. Then, we can use CycleGAN to produce a sketch given an image of a face.

The original repos we used can be found here:\
[Text-To-Image](https://github.com/zsdonghao/text-to-image)\
[CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/jeanmichaeldiei/11785-Text-to-Sketch
cd 11785-Text-to-Sketch/text-to-image
```
- The DCGAN and CycleGAN implementations **require** two separate environments because the dependencies clash.
- Install DCGAN dependencies:
  - For pip users, please type the command `pip install -r text-to-image/requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f text-to-image/environment.yml`.
- Install CycleGAN dependencies (e.g., torchvision, [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate)):
  - For pip users, please type the command `pip install -r pytorch-CycleGAN-and-pix2pix/requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f pytorch-CycleGAN-and-pix2pix/environment.yml`.

### Text-To-Image DCGAN train/test
1. Change to correct directory:
    ```bash
    cd text-to-image
    ```
2. Download all necessary files for text to Flowers
    ```bash
    python downloads.py
    ``` 
3. Process the data:
    ```bash
    python data_loader.py
    ``` 
4. Train the model
    ```bash
    python train_txt2im.py
    ``` 
### CycleGAN train/test
1. Put images of faces in pytorch-CycleGAN-and-pix2pix/datasets/face2sketch/trainA
2. Put images of sketches in pytorch-CycleGAN-and-pix2pix/datasets/face2sketch/trainB
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.
3. Change to correct directory:
    ```bash
    cd pytorch-CycleGAN-and-pix2pix
    ```
4. Train a model:
    ```bash
    python train.py --dataroot ./datasets/face2sketch --name face2sketch --model cycle_gan --preprocess 'resize_and_crop' --batch_size 2 --num_threads 0 --netG unet_256
    ```
- To see more intermediate results, check out `./checkpoints/maps_cyclegan/web/index.html`.
    
5. Test the model:
    ```bash
    python test.py --dataroot ./datasets/face2sketch/testA --name face2sketch --model test --no_dropout --netG unet_256 --num_test 50
    ```
- The test results will be saved to a html file here: `./results/face2sketch/latest_test/index.html`.

# NOTE:
For more detailed descriptions of Text-to-Image(DCGAN) and Image-to-Image translation (CycleGAN), please refer to their READMEs:\
[Text-to-Image](text-to-image/README.md)\
[Image-to-Image Translation](pytorch-CycleGAN-and-pix2pix/README.md)
