"""
Training option module
these training options assume to use on aws s3 p2.xlarge instance.
learning rate and batch size was decide by reference to paper of 
Fully Convolutional Networks for Semantic Segmentation.
# note: Larger batch size might speed up training, 
        but it can degrade the quality of the model at the same time.
"""

training_options = {
    "num_class": 2,
    "image_shape": (160, 576),
    "epochs": 15,
    "batch_size": 4,
    "keep_prob": 0.5,
    "learning_rate": 0.0001,
    "is_restore": False,
    "restore_model_path": "./runs/2017-10-18-07:55:49.851706"
}

data_paths = {
    "data_dir": "./data",
    "runs_dir": "./runs",
    "model_dir": "./model"
}