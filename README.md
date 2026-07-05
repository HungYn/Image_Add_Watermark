# Image Add Watermark

## 📌 功能
為照片添加浮水印文字。  
您可以透過 **INI 檔案**自訂參數，以在新增浮水印後獲得最終的影像效果。

## 🚀 使用方式

1.先設定好add_watermark.ini參數
2.執行 add_watermark.exe

## ⚙️ add_watermark.ini參數說明
[Settings]
Input = D:\Python39\images        ; 輸入圖片資料夾
Output = D:\Python39\output       ; 輸出圖片資料夾
X = 122                           ; 浮水印文字 X 座標
Y = 152                           ; 浮水印文字 Y 座標
Prefix = 專案A                    ; 浮水印前綴文字
Color = #0000ff                   ; 浮水印文字顏色 (支援 #RRGGBB 或顏色名稱)
Digits = 3                        ; 流水號位數 (例如 3 → 001, 002)
FontSize = 40                     ; 字型大小
FontPath = C:/Windows/Fonts/msjh.ttc ; 字型檔路徑
StartNumber = 5                  ; 流水號起始數字

## 🎯 使用範例

設定 Prefix = 專案A、Digits = 3、StartNumber = 5  
→ 產生的浮水印文字為：
專案A-005
專案A-006
專案A-007
...
