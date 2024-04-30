# Self Drive

Autonomous driving using Carla.

## Sensors Used

### For prod

- Front facing rgb camera.

### For data collection

- Front facing camera with semantic segmentation.

## Project checklist

Currently we have two major goals/pipeline:

- [ ] Semantic Segmentation from dashcam stream.
  - [ ] Collect labelled data from carla

- [ ] RL model to control race and steering based on traffic and GPS.
  - [ ] Control steering based on GPS (Carla waypoints) at constant race and no traffic.

## Environment

- Carla 0.9.13
- Python 3.8
- CUDA 11.8
- Pytorch
  
  ```ps
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
   ```

- OpenCV

  ```ps
  pip install opencv-python
  ```

- Pandas

## Authors

- Hardik Sachan - [@hardiksachan](https://github.com/hardiksachan)
- Ishita Kohli - [@ishita-kohli](https://github.com/ishita-kohli)
- Ishita Gattani - [@ishitagattani](https://github.com/ishitagattani)
