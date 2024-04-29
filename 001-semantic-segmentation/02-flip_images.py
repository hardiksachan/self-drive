import os
import cv2

workspace_root = os.environ["SELF_DRIVE_CARLA_WORKSPACE"]
project_workspace = os.path.join(workspace_root, "01-semantic-segmentation")

rgb_dir = os.path.join(project_workspace, "out_sem", "rgb")
sem_dir = os.path.join(project_workspace, "out_sem", "sem")

images = [f for f in os.listdir(rgb_dir) if f.endswith(".png") and not f.endswith("_flip.png")]

print(f"[INFO] Found {len(images)} images.")

# Flip images in rgb
imgCounter = 0
for f in images:
    print(f"flipping rgb image {imgCounter}...")
    imgCounter += 1
    in_pth = os.path.join(rgb_dir,f)
    out_pth = os.path.join(rgb_dir,f.split('.')[0]+'_flip.png')
    frame = cv2.imread(in_pth)
    flipped_frame = cv2.flip(frame,1)
    cv2.imwrite(out_pth, flipped_frame)

# Flip images in sem
imgCounter = 0
for f in images:
    print(f"flipping sem image {imgCounter}...")
    imgCounter += 1
    in_pth = os.path.join(sem_dir,f)
    out_pth = os.path.join(sem_dir,f.split('.')[0]+'_flip.png')
    frame = cv2.imread(in_pth)
    flipped_frame = cv2.flip(frame,1)
    cv2.imwrite(out_pth, flipped_frame)