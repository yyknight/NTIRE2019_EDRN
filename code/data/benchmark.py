import os

from data import common
from data import srdata

import numpy as np

import torch
import torch.utils.data as data

class Benchmark(srdata.SRData):
    def __init__(self, args, name='ntire', train=True, benchmark=True):
        super(Benchmark, self).__init__(
            args, name=name, train=train, benchmark=True
        )

    def _set_filesystem(self, dir_data):
        self.apath = dir_data
        self.dir_hr = os.path.join(self.apath, 'ntire/Test_LR')
        #self.dir_lr = os.path.join(self.apath, 'ntire/ValidationLR')
        #self.dir_hr = os.path.join(self.apath, 'ntire/ValidationGT')
        self.dir_lr = os.path.join(self.apath, 'ntire/Test_LR')
        #self.dir_hr = os.path.join(self.apath, 'Set5/HR')
        #self.dir_lr = os.path.join(self.apath, 'Set5/LR_bicubic_ntire')
        self.ext = ('.png', '.png')
