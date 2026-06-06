from si_image_processing_lab.pipelines.image_processing.nodes import process_image

def test_process_image():
    result = process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/marte_processed.jpg"
    )

    assert result is not None