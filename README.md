#Our solution for NTIRE Real Super-Resolution Challenge(Encode-Decode residual network)

Our implementation is built on [EDSR (PyTorch)](https://github.com/thstkdgus35/EDSR-PyTorch) and tested on Ubuntu 16.04 environment (Python3.5, PyTorch_0.4.1, CUDA9.0, cuDNN7.1) with a NVIDIA GTX 1080Ti GPU.

#prepare data

download the dataset from https://competitions.codalab.org/competitions/21439#participate, and then put the downloaded dataset into ntire file. 

#How to train

python main.py --save EDRN --save_results --save_models --model edrn --patch_size 128 --lr_decay 50 --n_GPUs 1 --chop

#How to reproduce our result

python main.py --save_results --model edrn --n_GPUs 1 --chop --pre_train ../experiment/model/EDRN.pt --self_ensemble --test_only

