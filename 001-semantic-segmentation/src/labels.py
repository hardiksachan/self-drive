# Sourced from: https://github.com/mcordts/cityscapesScripts/blob/master/cityscapesscripts/helpers/labels.py
from collections import namedtuple

# a label and all meta information
SemanticLabel = namedtuple(
    "Label",
    [
        "name",  # The identifier of this label, e.g. 'car', 'person', ... .
        # We use them to uniquely name a class
        "id",  # An integer ID that is associated with this label.
        # The IDs are used to represent the label in ground truth images
        # An ID of -1 means that this label does not have an ID and thus
        # is ignored when creating ground truth images (e.g. license plate).
        # Do not modify these IDs, since exactly these IDs are expected by the
        # evaluation server.
        "trainId",  # Feel free to modify these IDs as suitable for your method. Then create
        # ground truth images with train IDs, using the tools provided in the
        # 'preparation' folder. However, make sure to validate or submit results
        # to our evaluation server using the regular IDs above!
        # For trainIds, multiple labels might have the same ID. Then, these labels
        # are mapped to the same class in the ground truth images. For the inverse
        # mapping, we use the label that is defined first in the list below.
        # For example, mapping all void-type classes to the same ID in training,
        # might make sense for some approaches.
        # Max value is 255!
        "category",  # The name of the category that this label belongs to
        "categoryId",  # The ID of this category. Used to create ground truth images
        # on category level.
        "hasInstances",  # Whether this label distinguishes between single instances or not
        "ignoreInEval",  # Whether pixels having this class as ground truth label are ignored
        # during evaluations or not
        "color",  # The color of this label
    ],
)


# --------------------------------------------------------------------------------
# A list of all labels
# --------------------------------------------------------------------------------

# Please adapt the train IDs as appropriate for your approach.
# Note that you might want to ignore labels with ID 255 during training.
# Further note that the current train IDs are only a suggestion. You can use whatever you like.
# Make sure to provide your results using the original IDs and not the training IDs.
# Note that many IDs are ignored in evaluation and thus you never need to predict these!

# fmt: off
cityscapesDefaultLabels = [
    #               name                     id    trainId   category            catId     hasInstances   ignoreInEval   color
    SemanticLabel(  'unlabeled'            ,  0 ,        0 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    # cityscape
    SemanticLabel(  'road'                 ,  1 ,        1 , 'flat'            , 1       , False        , False        , (128, 64, 128) ),
    SemanticLabel(  'sidewalk'             ,  2 ,        2 , 'flat'            , 1       , False        , False        , (244, 35, 232) ),
    SemanticLabel(  'building'             ,  3 ,        3 , 'construction'    , 2       , False        , False        , ( 70, 70, 70) ),
    SemanticLabel(  'wall'                 ,  4 ,        4 , 'construction'    , 2       , False        , False        , (102, 102, 156) ),
    SemanticLabel(  'fence'                ,  5 ,        4 , 'construction'    , 2       , False        , False        , (190, 153, 153) ),
    SemanticLabel(  'pole'                 ,  6 ,        5 , 'object'          , 3       , False        , False        , (153, 153, 153) ),
    SemanticLabel(  'traffic light'        ,  7 ,        5 , 'object'          , 3       , False        , False        , (250, 170, 30) ),
    SemanticLabel(  'traffic sign'         ,  8 ,        5 , 'object'          , 3       , False        , False        , (220, 220, 0) ),
    SemanticLabel(  'vegetation'           ,  9 ,        6 , 'nature'          , 4       , False        , False        , (107, 142, 35) ),
    SemanticLabel(  'terrain'              , 10 ,        7 , 'nature'          , 4       , False        , False        , (152, 251, 152) ),
    SemanticLabel(  'sky'                  , 11 ,        8 , 'sky'             , 5       , False        , False        , (70, 130, 180) ),
    SemanticLabel(  'pedestrian'           , 12 ,        9 , 'human'           , 6       , True         , False        , (220, 20, 60) ),
    SemanticLabel(  'rider'                , 13 ,       10 , 'human'           , 6       , True         , False        , (255, 0, 0) ),
    SemanticLabel(  'car'                  , 14 ,       11 , 'vehicle'         , 7       , True         , False        , (0, 0, 142) ),
    SemanticLabel(  'truck'                , 15 ,       11 , 'vehicle'         , 7       , True         , False        , (0, 0, 70) ),
    SemanticLabel(  'bus'                  , 16 ,       11 , 'vehicle'         , 7       , True         , False        , (0, 60, 100) ),
    SemanticLabel(  'train'                , 17 ,       12 , 'vehicle'         , 7       , True         , False        , (0, 80, 100) ),
    SemanticLabel(  'motorcycle'           , 18 ,       13 , 'vehicle'         , 7       , True         , False        , (0, 0, 230) ),
    SemanticLabel(  'bicycle'              , 19 ,       13 , 'vehicle'         , 7       , True         , False        , (119, 11, 32) ),
    # custom
    SemanticLabel(  'static'               , 20 ,        0 , 'void'            , 0       , False        , True         , (110, 190, 160) ),
    SemanticLabel(  'dynamic'              , 21 ,        0 , 'void'            , 0       , False        , True         , (170, 120, 50) ),
    SemanticLabel(  'other'                , 22 ,        0 , 'void'            , 0       , False        , True         , (55, 90, 80) ),
    SemanticLabel(  'water'                , 23 ,        0 , 'void'            , 0       , False        , True         , (45, 60, 150) ),
    SemanticLabel(  'road line'            , 24 ,       14 , 'void'            , 0       , False        , True         , (157, 234, 50) ),
    SemanticLabel(  'ground'               , 25 ,        0 , 'void'            , 0       , False        , True         , (81, 0, 81) ),
    SemanticLabel(  'bridge'               , 26 ,        0 , 'void'            , 0       , False        , True         , (150, 100, 100) ),
    SemanticLabel(  'rail track'           , 27 ,        0 , 'void'            , 0       , False        , True         , (230, 150, 140) ),
    SemanticLabel(  'guard rail'           , 28 ,        4 , 'void'            , 0       , False        , True         , (180, 165, 180) )
]
# fmt: on


# --------------------------------------------------------------------------------
# Create dictionaries for a fast lookup
# --------------------------------------------------------------------------------

# name to label object
name2label = {label.name: label for label in cityscapesDefaultLabels}
# id to label object
id2label = {label.id: label for label in cityscapesDefaultLabels}
# trainId to label object
trainId2label = {label.trainId: label for label in cityscapesDefaultLabels}
# category to list of label objects
category2labels = {}
for label in cityscapesDefaultLabels:
    category = label.category
    if category in category2labels:
        category2labels[category].append(label)
    else:
        category2labels[category] = [label]
