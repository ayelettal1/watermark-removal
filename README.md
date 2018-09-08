# watermark-removal
Firs you need to download the dataset or create your own dataset with watermarks.
Than, in order to run the code you need to follow pix-2pix instructions as we can see bellow - 
Train a model: python train.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --which_direction BtoA
Test the model: python test.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --which_direction BtoA
The test results will be saved to a html file here: ./results/facades_pix2pix/test_latest/index.html.

Citation

@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}


@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}
