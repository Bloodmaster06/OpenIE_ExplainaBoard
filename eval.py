import argparse
import os
import sys
# sys.path.append('../')

import torch.nn as nn
import logging
import torch
from utils.antu.io.configurators import IniConfigurator
from eval.evaluation import eval
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Usage for OPENIE evaluation.")
    parser.add_argument('--CFG', type=str, help="Path to config file.")
    parser.add_argument('--DEBUG', action='store_true', help="DEBUG mode.")
    args, extra_args = parser.parse_known_args()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    cfg = IniConfigurator(args.CFG, extra_args)
    args = parser.parse_args()
    auc, precision, recall, f1 = eval(cfg, 'test')