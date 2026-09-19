from pathlib import Path


def test_dvc_file_exists():
    dvc_file = Path("products.csv.dvc")
    assert dvc_file.exists(), "products.csv.dvc is missing"


def test_dvc_file_contains_dataset_reference():
    content = Path("products.csv.dvc").read_text(encoding="utf-8")
    assert "path: products.csv" in content
    assert "md5:" in content
    assert "size:" in content
