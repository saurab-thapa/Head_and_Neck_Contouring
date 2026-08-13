import os
import SimpleITK as sitk
import numpy as np


def load_ct(path):
    image = sitk.ReadImage(path)
    array = sitk.GetArrayFromImage(image)

    return array, image


def find_oars(folder):
    oars = {}

    for filename in os.listdir(folder):
        if filename.lower().endswith(".nrrd"):
            organ_name = os.path.splitext(filename)[0]
            oars[organ_name] = os.path.join(folder, filename)

    return oars


def load_segmentation(path):
    image = sitk.ReadImage(path)
    array = sitk.GetArrayFromImage(image)

    return array, image