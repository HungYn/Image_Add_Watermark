# Image Add Watermark

## 📌 功能
為照片添加浮水印文字。  
您可以透過 **INI 檔案**自訂參數，以在新增浮水印後獲得最終的影像效果。

## 🚀 使用方式

1.  先設定好add_watermark.ini參數
2.  執行 add_watermark.exe

## ⚙️ add_watermark.ini參數說明

| 參數 | 說明 |
| --- | --- |
| **Input** | 輸入圖片資料夾 |
| **Output** | 輸出圖片資料夾 |
| **X / Y** | 浮水印文字座標位置 |
| **Prefix** | 浮水印前綴文字 |
| **Color** | 文字顏色（支援 #RRGGBB 或顏色名稱） |
| **Digits** | 流水號位數（例如 3 → 001, 002） |
| **FontSize** | 字型大小 |
| **FontPath** | 字型檔路徑 |
| **StartNumber** | 流水號起始數字 |

```ni
[Settings]
Input = D:\Python39\images
Output = D:\Python39\output
X = 122
Y = 152
Prefix = 78011A
Color = #0000ff
Digits = 3
FontSize = 30
FontPath = C:/Windows/Fonts/mingliu.ttc
StartNumber = 2
```

## 🎯 使用範例

1. **設定**
  Prefix = 專案A、
  Digits = 3、
  StartNumber = 5
  
→ **產生的浮水印文字為**：
```
  專案A005
  專案A006
  專案A007
```
![screenshot]([https://github.com/HungYn/Image_Add_Watermark/blob/main/TEST.png])
