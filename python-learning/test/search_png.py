import os


def search_and_delete_images(folder_path, delete=False):
    # 遍历文件夹内的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg"):
                file_path = os.path.join(root, file)
                print("找到图片文件:", file_path)
                if delete:
                    try:
                        os.remove(file_path)
                        print("已删除:", file_path)
                    except Exception as e:
                        print("删除文件时出错:", str(e))


if __name__ == "__main__":
    folder_path = input("请输入要搜索的文件夹路径: ")
    search_option = input("是否删除找到的图片文件？ (y/n): ").strip().lower()

    if search_option == "y":
        delete_option = True
    else:
        delete_option = False

    search_and_delete_images(folder_path, delete_option)
