import json

# 读取第二种格式的 JSON 文件
with open('raw.json', 'r') as file:
    data = json.load(file)

# 创建第一种格式的 JSON 数据结构
output_data = {
    "image_path": {
        "file_paths": {}
    },
    "bbox": {
        "transform": data["frames"][0]["transform_matrix"]
    },
    "camera_track_map": {
        "images": {}
    }
}

# 填充第一种格式的 JSON 数据结构
for i, frame in enumerate(data["frames"]):
    output_data["image_path"]["file_paths"][str(i)] = frame["file_path"]
    output_data["camera_track_map"]["images"][str(i)] = {
        "flg": 2,
        "size": [1236, 800],
        "camera": {
            "intrinsic": {
                "ppt": [823.205, 619.071],
                "focal": [2892.33, 2883.18]
            },
            "extrinsic": frame["transform_matrix"]
        }
    }

# 将转换后的数据写入第一种格式的 JSON 文件
with open('new.json', 'w') as file:
    json.dump(output_data, file, indent=4)