# Encode-Decode Residual Network (Ivip-Lab)
Our solution for NTIRE2019 Real Super-Resolution Challenge.

## Dependencies
  * Python (tested on release 3.5)
  * PyTorch (tested on release 0.4.1)
  * CUDA9.0
  * cuDNN7.1
  
Our code is tested on Ubuntu 16.04 environment with a NVIDIA GTX 1080Ti GPU.

## Dataset
Please download the dataset from [here](https://competitions.codalab.org/competitions/21439#participate), and then put the downloaded dataset into ntire file. 

## Training
`$ python main.py --save EDRN --save_results --save_models --model edrn --patch_size 128 --lr_decay 50 --n_GPUs 1 --chop`

## Test
`$ python main.py --save_results --model edrn --n_GPUs 1 --chop --pre_train ../experiment/model/EDRN.pt --self_ensemble --test_only`

## Acknowledgements
This code is built on [EDSR (PyTorch)](https://github.com/thstkdgus35/EDSR-PyTorch). We are grateful to the authors for sharing their codes of EDSR.
