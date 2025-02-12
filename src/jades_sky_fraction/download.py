from pathlib import Path

import httpx
from loguru import logger


# Currently unused as we're going with Pearls first
def get_goods_segmentation_images() -> dict[str, Path]:
    """Get the segmenetation images from https://archive.stsci.edu/hlsp/jades"""
    here = Path(__file__).parent
    goods_s_file = here / "data" / "hlsp_jades_jwst_nircam_goods-s-deep_segmentation_v2.0_drz.fits"
    goods_n_file = here / "data" / "hlsp_jades_jwst_nircam_goods-n_segmentation_v1.0_drz.fits"

    if not goods_s_file.exists():
        logger.info(f"Downloading GOODS-S segmentation image to {goods_s_file}")
        url = "https://archive.stsci.edu/hlsps/jades/dr2/goods-s/images/hlsp_jades_jwst_nircam_goods-s-deep_segmentation_v2.0_drz.fits"

        response = httpx.get(url, timeout=300)
        with goods_s_file.open("wb") as f:
            f.write(response.content)

    if not goods_n_file.exists():
        logger.info(f"Downloading GOODS-N segmentation image to {goods_n_file}")
        url = "https://archive.stsci.edu/hlsps/jades/dr3/goods-n/images/hlsp_jades_jwst_nircam_goods-n_segmentation_v1.0_drz.fits"

        response = httpx.get(url, timeout=300)
        with goods_n_file.open("wb") as f:
            f.write(response.content)

    return {"goods_s": goods_s_file, "goods_n": goods_n_file}


def get_pearls_image() -> Path:
    """Get the PEARLS segmentation image from https://archive.stsci.edu/hlsp/pearls"""
    here = Path(__file__).parent
    pearls_file = here / "data" / "mosaic_nep_nircam_f277w_30mas_20221014_drz.fits"

    if not pearls_file.exists():
        logger.error(
            f"You are missing {pearls_file}. Please go to "
            "https://arizonastateuniversity10.app.box.com/s/79lwrd22s7hou6byjhautqct2a0gmrnm/folder/186306612937 "
            "and download the mosaic_nep_nircam_f277w_30mas_20221014_drz.fits file to the data directory here"
        )
        raise FileNotFoundError(f"Missing {pearls_file}")  # noqa: TRY003

    return pearls_file
