import numpy as np


def dice_score(prediction, ground_truth):

    prediction = prediction > 0
    ground_truth = ground_truth > 0

    intersection = np.logical_and(
        prediction,
        ground_truth
    ).sum()

    prediction_volume = prediction.sum()
    ground_truth_volume = ground_truth.sum()

    denominator = prediction_volume + ground_truth_volume

    if denominator == 0:
        return 1.0

    return (2.0 * intersection) / denominator