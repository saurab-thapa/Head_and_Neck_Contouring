import os

import streamlit as st

from src.data_loader import (
    load_ct,
    find_oars,
    load_segmentation
)

from src.viewer import create_overlay


# ============================================================
# CONFIGURATION
# ============================================================

CASE_PATH = r"C:\Users\Saurab\Desktop\Head_and_Neck_Contouring\tcia-ct-scan-dataset\nrrds\test\oncologist\0522c0017"

CT_PATH = os.path.join(
    CASE_PATH,
    "CT_IMAGE.nrrd"
)

SEGMENTATION_PATH = os.path.join(
    CASE_PATH,
    "segmentations"
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="TARGET-AI",
    layout="wide"
)

st.title("TARGET-AI")
st.subheader("Head & Neck OAR Contouring Tool")


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def get_ct():
    return load_ct(CT_PATH)


@st.cache_data
def get_oars():
    return find_oars(SEGMENTATION_PATH)


ct, ct_image = get_ct()

oars = get_oars()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("OAR Selection")

organ_names = sorted(oars.keys())

selected_organ = st.sidebar.selectbox(
    "Select Organ at Risk",
    organ_names
)

slice_index = st.sidebar.slider(
    "CT Slice",
    0,
    ct.shape[0] - 1,
    ct.shape[0] // 2
)

opacity = st.sidebar.slider(
    "Contour Opacity",
    0.0,
    1.0,
    0.5,
    0.05
)


# ============================================================
# LOAD OAR
# ============================================================

@st.cache_data
def get_segmentation(path):
    return load_segmentation(path)


mask, mask_image = get_segmentation(
    oars[selected_organ]
)


# ============================================================
# VIEW
# ============================================================

ct_slice = ct[slice_index]

mask_slice = mask[slice_index]

fig = create_overlay(
    ct_slice,
    mask_slice,
    selected_organ,
    slice_index,
    opacity
)

st.pyplot(
    fig,
    use_container_width=True
)


# ============================================================
# INFORMATION
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "CT Slices",
        ct.shape[0]
    )

with col2:
    st.metric(
        "OARs",
        len(oars)
    )

with col3:
    st.metric(
        "Current Slice",
        slice_index
    )