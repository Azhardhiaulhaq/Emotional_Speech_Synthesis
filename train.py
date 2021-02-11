import argparse
import os
from hparams import hparams

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # TODO : Add Needed argument for training
    parser.add_argument('-o','--directory_output',type=str,help='directory to save checkpoints')
    parser.add_argument('-l','--directory_log',tpye=str,help='directory to save tensorboard logs')
    parser.add_argument('-c','--checkpoint_path',type=str,defaulte=None,required=False,help='checkpoint path')

    
