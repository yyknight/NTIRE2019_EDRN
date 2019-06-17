# Encoder-Decoder Residual Network (IVIP-Lab)
This repository is our solution for NTIRE2019 Real Super-Resolution Challenge.  

We, team IVIP-LAB, won the 9th PSNR and Top5 SSIM in the final phase of NTIRE2019 Real Super-resolution challenge.  
Our paper will be published in CVPR 2019 Workshop. </i> [[pdf](http://openaccess.thecvf.com/content_CVPRW_2019/papers/NTIRE/Cheng_Encoder-Decoder_Residual_Network_for_Real_Super-Resolution_CVPRW_2019_paper.pdf)] [[poster](http://github.com/yyknight/NTIRE2019_EDRN/blob/master/ntire/cvpr19_poster_edrn.pdf)]

### Table of contents
  * [Network Architecture](#network)
  * [Experimental Results](#result)
  * [Dependencies](#Dependencies)
  * [Dataset](#Dataset)
  * [Training](#Training)
  * [Test](#Test)
  * [Citation](#Citation)
  
<a id="network"></a>
## Network Architecture
**Encoder-Decoder Residual Network (EDRN)**  
![Overview of EDRN](/figs/edrn.png)

<a id="result"></a>
## NTIRE2019 Real Super-resolution Challenge Results  
**Quantitative Results**  

 Method | PSNR (dB) | SSIM | Runtime (s)
 :---------------:|:----------:|:---------:|:---------: 
 Baseline | 26.89 | 0.78 | --
 EDRN (ours) | 28.79 | 0.84 | 47.08


**Qualitative Results**  

![Qualitative_results](/figs/visualization.png)

## Classic single image super-resolution benchmark results  
![SISR_results](/figs/sisr_results.png)

# About Our Source Code & Trained Model
## Dependencies
  * Python (tested on release 3.5)
  * PyTorch (tested on release 0.4.1)
  * CUDA9.0
  * cuDNN7.1
  
Our code is tested on Ubuntu 16.04 environment with an NVIDIA GTX 1080Ti GPU.

## Dataset
Please download the dataset from [here](https://competitions.codalab.org/competitions/21439#participate), and then put the downloaded dataset into ntire file. 

## Training
`$ python main.py --save EDRN --save_results --save_models --model edrn --patch_size 128 --lr_decay 50 --n_GPUs 1 --chop`

## Test
Quick start (Demo) to reproduce our results. Please download our pretrained model from [here](https://drive.google.com/open?id=1CxVtrxlgB-iWEFsYuUicqksjTvpBDtxD).

`$ python main.py --save EDRN --save_results --model edrn --n_GPUs 1 --chop --pre_train ../experiment/model/EDRN.pt --self_ensemble --test_only`

# Citation
If you find this work useful in your reseach, please cite our paper. 
```
@InProceedings{Cheng_2019_CVPR_Workshops,
author = {Cheng, Guoan and Matsune, Ai and Li, Qiuyu and Zhu, Leilei and Zang, Huaijuan and Zhan, Shu},
title = {Encoder-Decoder Residual Network for Real Super-Resolution},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
month = {June},
year = {2019}
} 
```

# Acknowledgements
This code is built on [EDSR (PyTorch)](https://github.com/thstkdgus35/EDSR-PyTorch). We are grateful to the authors for sharing their codes of EDSR.
