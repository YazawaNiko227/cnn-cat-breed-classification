#### Đoạn mã Python lọc theo quy ước tên file:

import os
import shutil
import pandas as pd

# Đường dẫn thư mục
dataset_dir = "data/raw/dataset-iiit-pet-master"
images_dir = os.path.join(dataset_dir, "images")
list_file = os.path.join(dataset_dir, "annotations/list.txt")
output_dir = "data/processed/cats"

# 1. Đọc file list.txt (bỏ qua các dòng comment bắt đầu bằng '#')
df = pd.read_csv(
    list_file,
    sep=" ",
    comment="#",
    header=None,
    names=["Image", "Class_ID", "Species", "Breed_ID"],
)

# 2. Lọc danh sách chỉ lấy các dòng có Species == 1 (Mèo)
cat_df = df[df["Species"] == 1]

# 3. Tạo thư mục đầu ra
os.makedirs(output_dir, exist_ok=True)

# 4. Copy các file ảnh mèo sang thư mục mới
copied_count = 0
for image_name in cat_df["Image"]:
    filename = f"{image_name}.jpg"
    src_path = os.path.join(images_dir, filename)
    dst_path = os.path.join(output_dir, filename)

    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
        copied_count += 1

print(f"Đã lọc và lưu thành công {copied_count} ảnh mèo vào '{output_dir}'.")

