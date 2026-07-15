from PIL import Image, ImageDraw, ImageFont
import os
import sys
import configparser
import ctypes

# 取得 .py 檔案所在的路徑
# 如果是 EXE，取 EXE 所在路徑；否則取 .py 所在路徑
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

ini_path = os.path.join(base_dir, "add_watermark.ini")

# 讀取 ini 檔
config = configparser.ConfigParser()
if not os.path.exists(ini_path):
    ctypes.windll.user32.MessageBoxW(0, f"找不到設定檔：{ini_path}", "錯誤", 0)
    sys.exit(1)

config.read(ini_path, encoding="utf-8")

if "Settings" not in config:
    ctypes.windll.user32.MessageBoxW(0, "INI 檔案缺少 [Settings] 區段", "錯誤", 0)
    sys.exit(1)

settings = config["Settings"]
folder = settings["Input"]


# ✅ 檢查資料夾是否存在
if not os.path.exists(folder):
    ctypes.windll.user32.MessageBoxW(0, f"找不到輸入資料夾：{folder}", "錯誤", 0)
    sys.exit(1)
    
try:
    output = settings["Output"]
    x = int(settings["X"])
    y = int(settings["Y"])
    prefix = settings["Prefix"]
    color = settings["Color"]
    digits = int(settings["Digits"])
    fontsize = int(settings["FontSize"])
    fontpath = settings["FontPath"]
    start_number = int(settings["StartNumber"])
except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, f"設定檔格式錯誤：{e}", "錯誤", 0)
    sys.exit(1)    

# 使用 ini 設定的字型檔路徑與大小
try:
    font = ImageFont.truetype(fontpath, fontsize)
except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, f"字型載入失敗：{e}", "錯誤", 0)
    sys.exit(1)
    
os.makedirs(output, exist_ok=True)

    
count = 0
for i, filename in enumerate(os.listdir(folder), start=start_number):
    if filename.lower().endswith((".jpg", ".png")):
        try:
            img = Image.open(os.path.join(folder, filename))
            draw = ImageDraw.Draw(img)

            # 流水號位數由 ini 控制，起始數字也由 ini 控制
            text = f"{prefix}{i:0{digits}d}"
            draw.text((x, y), text, font=font, fill=color)

            # 保持原始副檔名
            img.save(os.path.join(output, filename))
            count += 1
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"處理檔案 {filename} 時發生錯誤：{e}", "錯誤", 0)
            sys.exit(1)

# 執行成功訊息
ctypes.windll.user32.MessageBoxW(0, f"已完成 {count} 張圖片的浮水印處理！\n輸出路徑：{output}", "執行成功", 0)        
