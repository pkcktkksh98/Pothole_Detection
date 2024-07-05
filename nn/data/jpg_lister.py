import os

def list_jpg_files(folder_path, output_file):
  """
  Lists all JPG files in a folder and writes them to a text file.

  Args:
    folder_path: Path to the folder containing the JPG files.
    output_file: Path to the output text file.
  """
  jpg_files = []
  for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
      jpg_files.append(filename)

  with open(output_file, "w") as f:
    f.write("\ndata/obj/valid".join(jpg_files))

# Example usage
folder_path = "obj/valid/"
output_file = "obj/valid.txt"

list_jpg_files(folder_path, output_file)

print(f"Listed JPG files written to: {output_file}")