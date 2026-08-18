from llava.train.train import train
import numpy as np
import os
import random
import torch
from transformers import set_seed


# def seed_everything(seed):
#     random.seed(seed)
#     os.environ['PYTHONHASHSEED'] = str(seed)
#     np.random.seed(seed)
#     torch.manual_seed(seed)
#     torch.cuda.manual_seed(seed)
#     torch.cuda.manual_seed_all(seed)
#     torch.backends.cudnn.benchmark = False
#     torch.backends.cudnn.deterministic = True
#     set_seed(seed)

if __name__ == "__main__":
    os.environ["WANDB_PROJECT"] = "oculex"
    os.environ['TRITON_CACHE_DIR'] = '/nfs/bigdisk/sounakm/oculex/.triton'
    # seed_everything(42)
    # os.environ["WANDB_LOG_MODEL"] = "true"
    train(attn_implementation="flash_attention_2")
