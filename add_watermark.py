from PIL import Image, ImageDraw, ImageFont
import os
import configparser

# 讀取 ini 檔
config = configparser.ConfigParser()
config.read(r"D:\Python39\add_watermark.ini", encoding="utf-8")

folder = config["Settings"]["Input"]
output = config["Settings"]["Output"]
x = int(config["Settings"]["X"])
y = int(config["Settings"]["Y"])
prefix = config["Settings"]["Prefix"]
color = config["Settings"]["Color"]
digits = int(config["Settings"]["Digits"])
fontsize = int(config["Settings"]["FontSize"])
fontpath = config["Settings"]["FontPath"]
start_number = int(config["Settings"]["StartNumber"])

# 使用 ini 設定的字型檔路徑與大小
font = ImageFont.truetype(fontpath, fontsize)

os.makedirs(output, exist_ok=True)

for i, filename in enumerate(os.listdir(folder), start=start_number):
    if filename.lower().endswith((".jpg", ".png")):
        img = Image.open(os.path.join(folder, filename))
        draw = ImageDraw.Draw(img)

        # 流水號位數由 ini 控制，起始數字也由 ini 控制
        text = f"{prefix}{i:0{digits}d}"
        draw.text((x, y), text, font=font, fill=color)

        # 保持原始副檔名
        img.save(os.path.join(output, filename))
