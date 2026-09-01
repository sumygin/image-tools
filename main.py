import time

from pathlib import Path
from PIL import Image


root_path = Path.cwd()

test_dir = root_path / "test-dir"
output_dir = root_path / "output"

print(test_dir, output_dir)

test_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)


def get_timestamp() -> str:
    """Get filename-friendly timestamp (accurate to minutes)."""

    return time.strftime("%Y-%m-%d_%H-%M")



def get_file_names_in_dir(dir: Path) -> list[str]:
    return [item.name for item in dir.iterdir() if item.is_file()]



def rotate_images(directory) -> None:
    '''Takes a directory path and rotates all images 90º'''

    img_file_names = get_file_names_in_dir(directory)

    new_out_dir = output_dir / get_timestamp()
    new_out_dir.mkdir(parents=True, exist_ok=True)

    print("Start processing...")

    for name in img_file_names:
        with Image.open(str(directory / name)) as img:
            rotated_image = img.transpose(Image.Transpose.ROTATE_270)

            rotated_image.save(str(new_out_dir / name))

            print(f"Processed {name}")

    print(f"Finished processing, saved to {str(new_out_dir)}")

if __name__ == "__main__":
    rotate_images(test_dir)
