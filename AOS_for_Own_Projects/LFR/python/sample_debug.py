import json
import numpy as np
import os
import cv2
import time
from LFR_utils import read_poses_and_images, pose_to_virtualcamera, init_aos, init_window
import glm
import matplotlib.pyplot as plt
from pathlib import Path
import sys

if __name__ == '__main__':
    
    if 'window' not in locals() or window == None: 
        window = init_window()
    fov = 50.815436217896945
    
    print("Initializing AOS...")
    aos = init_aos(fov=fov)
    
    basedatapath = Path(__file__).resolve().parent
    dem_path = os.path.join(basedatapath, '..', 'data', 'F0', 'DEM', 'dem.obj')
    print(f"Loading DEM from: {dem_path}")
    aos.loadDEM(dem_path)
    print("DEM loaded successfully")

    pose_file = os.path.join(basedatapath, '..', 'data', 'F0', 'poses', 'poses_first30.json')
    images_dir = os.path.join(basedatapath, '..', 'data', 'F0', 'images_ldr')
    print(f"Loading poses from: {pose_file}")
    print(f"Loading images from: {images_dir}")
    
    single_images, site_poses = read_poses_and_images(aos, pose_file, images_dir, adjust_mean=False, replace_ext='.png')
    print(f"Loaded {len(single_images)} images")
    
    center_index = int(round(len(single_images) / 2))
    print(f"Center index: {center_index}")

    print("Rendering...")
    integral = aos.render(pose_to_virtualcamera(aos.getPose(center_index)), fov)
    print(f"Integral shape: {integral.shape}")
    print(f"Integral last channel stats: min={integral[:,:,-1].min()}, max={integral[:,:,-1].max()}")

    tmp = integral[:,:,0] / integral[:,:,-1]
    
    imshow_img = cv2.cvtColor(tmp.astype(np.float32), cv2.COLOR_GRAY2RGB) if len(tmp.shape) == 2 else tmp
    plt.imshow(tmp)
    plt.axis('off')
    plt.title('integral image (N={})'.format(aos.getViews()))
    plt.show()

    del aos
    del window
