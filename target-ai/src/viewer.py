import numpy as np
import matplotlib.pyplot as plt


def create_overlay(ct_slice, mask_slice, organ_name, slice_index, opacity=0.5):

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.imshow(
        ct_slice,
        cmap="gray"
    )

    masked = np.ma.masked_where(
        mask_slice == 0,
        mask_slice
    )

    ax.imshow(
        masked,
        cmap="autumn",
        alpha=opacity
    )

    ax.set_title(
        f"{organ_name} | Slice {slice_index}"
    )

    ax.axis("off")

    return fig