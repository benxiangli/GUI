import os
from datetime import datetime
from tkinter import Tk, Button, Label, Entry, filedialog

from PIL import Image


def choose_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.tiff *.jpg *.jpeg *.png")])
    if file_paths:
        process_files(file_paths)


def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        input_directory.delete(0, 'end')
        input_directory.insert(0, directory)


def process_files(file_paths):
    width = int(input_width.get())
    height = int(input_height.get())
    save_directory = input_directory.get()

    for file_path in file_paths:
        image = Image.open(file_path)

        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = os.path.basename(file_path)
        folder_name = current_datetime + file_name[:file_name.rfind('.')]
        folder_path = os.path.join(save_directory, folder_name)
        os.makedirs(folder_path)

        image_width, image_height = image.size
        num_rows = image_height // height
        num_cols = image_width // width

        for i in range(num_rows):
            for j in range(num_cols):
                left = j * width
                upper = i * height
                right = left + width
                lower = upper + height
                box = (left, upper, right, lower)
                image_part = image.crop(box)
                part_name = f"{file_name}_{i}_{j}.jpg"
                part_path = os.path.join(folder_path, part_name)
                image_part.save(part_path)

    label_status.config(text="影像切割完成")


# 建立Tkinter視窗
root = Tk()
root.title("影像切割程式V1.0")

# 檔案選擇按鈕
button_choose_files = Button(root, text="選擇檔案", command=choose_files)
button_choose_files.pack()

# 影像切割寬度輸入
label_width = Label(root, text="影像切割寬度(px):")
label_width.pack()
input_width = Entry(root)
input_width.pack()

# 影像切割高度輸入
label_height = Label(root, text="影像切割高度(px):")
label_height.pack()
input_height = Entry(root)
input_height.pack()

# 存檔路徑輸入
label_directory = Label(root, text="存檔路徑:")
label_directory.pack()
input_directory = Entry(root)
input_directory.pack()

# 選擇儲存資料夾按鈕
button_choose_directory = Button(root, text="選擇資料夾", command=choose_directory)
button_choose_directory.pack()

# 狀態標籤
label_status = Label(root, text="")
label_status.pack()

# 執行視窗
root.mainloop()
