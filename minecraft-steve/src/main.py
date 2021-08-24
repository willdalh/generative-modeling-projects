import torch
import numpy as np
from torchvision import transforms
from gankit import GanKit

height = 150
cut_upper = 15
images = GanKit.load_images("../datasets/test_dataset", [transforms.Resize((height, height)), transforms.CenterCrop((int(50*(ratio)), int(25*(ratio))))], with_alpha=False, to_grayscale=True)
images = images[:, :, cut_upper:, :]
gan = GanKit(images=images, hidden_size=int(256*2), latent_size=12, log_path="../logs/log_attempt2_2")
gan.train(5000000, visualize_every=500, save_nets_every=1000)