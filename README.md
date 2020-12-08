# Text-to-Sketch

Drawing a face for a suspect just based on the descriptions of the eyewitnesses is a difficult task. There are some state-of-the-art methods in generating face images from text, but there is still a lot of room for improvement in similarity between input text and generated images. Here, we want to go even further and generate sketches rather than a RGB image.

Since there are not many datasets to work off of, we used CycleGAN to create an artificial dataset of sketes. We then used AttnGAN to perform text-to-Sketch generation.

The original repos we used can be found here:\
[AttnGAN](https://github.com/taoxugit/AttnGAN)\
[CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/jeanmichaeldiei/11785-Text-to-Sketch
```
- The DCGAN and CycleGAN implementations **require** two separate environments because the dependencies clash.
- Install DCGAN dependencies:
  - For pip users, please type the command `pip install -r AttnGAN/requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f AttnGAN/environment.yml`.
- Install CycleGAN dependencies (e.g., torchvision, [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate)):
  - For pip users, please type the command `pip install -r pytorch-CycleGAN-and-pix2pix/requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f pytorch-CycleGAN-and-pix2pix/environment.yml`.

### AttnGAN-CelebA train/test
1. Put images of sketches in `AttnGAN/data/CelebA/images`
2. Put corresponding text of sketches in `AttnGAN/data/CelebA/text` as folders
3. Put rest of necessary files in `AttnGAN/data/CelebA/`. Files from: https://cmu.app.box.com/folder/127508082472
4. Fill out `code/cfg/CelebA_attn2.yml` as necessary with proper directory paths and model sizes
5. Change to correct directory:
    ```bash
    cd AttnGAN/code/
    ```
6. Pre-train DAMSM (encoder) models:
    ```bash
     python pretrain_DAMSM.py --cfg cfg/DAMSM/CelebA.yml --gpu 0
    ```
7. Train a model:
    ```bash
    python main.py --cfg cfg/CelebA_attn2.yml --gpu 0
    ```
- To see more intermediate results (generated testimages and models), check out `AttnGAN/output/CelebA_attn2_<datatime>/`.
    
8. Perform inference on a model with proper `cfg/eval_CelebA.yml` (put in correct paths to NET_G and NET_E):
    ```bash
    python main.py --cfg cfg/eval_CelebA.yml --gpu 0
    ```
- The test results will be saved to a folder in the same path as NET_G.

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
For more detailed descriptions of AttnGAN and Image-to-Image translation (CycleGAN), please refer to their READMEs:\
[AttnGAN](AttnGAN/README.md)\
[Image-to-Image Translation](pytorch-CycleGAN-and-pix2pix/README.md)
