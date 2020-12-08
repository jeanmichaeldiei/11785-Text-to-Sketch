# AttnGAN Text-to-Sketch

The original repo of AttnGAN can be found here:
[AttnGAN](https://github.com/taoxugit/AttnGAN)

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

# NOTE:
For more detailed descriptions of AttnGAN-CelebA, please refer to this repo:
[AttnGAN-CelebA](https://github.com/2KangHo/AttnGAN-CelebA)
