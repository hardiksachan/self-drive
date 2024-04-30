import os
import torch
from PIL import Image
import numpy as np
import pandas as pd
from .labels import cityscapesDefaultLabels

class SegmentationDataset(torch.utils.data.Dataset):
    def __init__(self, dataset_csv, data_root, labels=cityscapesDefaultLabels, mode="test", transform=None):
        """
        Initializes the SegmentationDataset class.

        Args:
            dataset_csv (str): The path to the CSV file containing dataset information.
            data_root (str): The root directory of the dataset.
            labels (list, optional): A list of labels. Defaults to cityscapesDefaultLabels.
            mode (str, optional): The mode of the dataset (e.g., "train", "test", "val"). Defaults to "test".
            transform (callable, optional): A function/transform that takes in a sample and returns a transformed version. Defaults to None.
        """
        self.data_root = data_root
        self.df = pd.read_csv(dataset_csv, nrows=None)
        self.mode = mode
        self.transform = transform
        self.labels = labels
        self.color_to_trainId = np.zeros((256, 256, 256), dtype=np.uint8)
        for label in self.labels:
            color = label.color
            self.color_to_trainId[color[0], color[1], color[2]] = label.trainId
        self.n_classes = len(set([label.trainId for label in self.labels]))

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        image_path = os.path.join(self.data_root, self.df["image_path"][idx])
        semantic_path = os.path.join(self.data_root, self.df["label_path"][idx])

        image = Image.open(image_path).convert("RGB")
        semantic = Image.open(semantic_path).convert("RGB")

        # convert RGB nparray to single channel nparray using trainId from self.labels
        semantic = np.array(semantic)

        # THINK LATER!!!
        if self.transform:
            image = self.transform(image)
            # semantic = self.transforms(semantic)  # maybe use a different transform

        image = torch.from_numpy(np.array(image)).float()

        semantic_single_channel = self.color_to_trainId[semantic[:, :, 0], semantic[:, :, 1], semantic[:, :, 2]]
        
        semantic = torch.from_numpy(semantic_single_channel).long()
        # if self.mode == "train":
        #     semantic = torch.nn.functional.one_hot(
        #         semantic, num_classes=self.n_classes
        #     )  # Assuming 20 classes (adjust)
        # else:
        #     # For validation, keep labels as integers for evaluation metrics like mIoU
        #     pass

        return image, semantic
