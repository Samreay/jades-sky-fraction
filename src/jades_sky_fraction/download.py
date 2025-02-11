from pathlib import Path

import httpx
from loguru import logger


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
