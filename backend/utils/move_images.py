import os
import shutil
import imghdr

def is_image(file_path):
    return imghdr.what(file_path) is not None

def flatten_images_copy(src_dir, dest_dir, log_file="image_copy_log.txt"):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    log_entries = []
    image_count = 0

    for root, _, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if is_image(file_path):
                filename = os.path.basename(file)
                dest_path = os.path.join(dest_dir, filename)

                # Handle duplicate names
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(dest_dir, f"{base}_{counter}{ext}")
                    counter += 1

                shutil.copy2(file_path, dest_path)
                log_entries.append(f"{file_path} -> {dest_path}")
                image_count += 1

    # Write log to file
    with open(log_file, "w") as f:
        f.write("\n".join(log_entries))

    print(f"Copied {image_count} image(s) to '{dest_dir}'. Log written to '{log_file}'.")

# Example usage:
src_directory = "/path/to/source"
dest_directory = "/path/to/flat_images"

flatten_images_copy(src_directory, dest_directory)
