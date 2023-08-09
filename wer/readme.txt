更換reference_file_path和test_file_path，且須為csv檔
wer為計算拼音結果的程式，有參考檔案和espnet的結果在旁對照
seperate.py可以用來產出text.csv和對應在ref.csv的純文本並分入兩個檔案
安裝套件pip install asr-evaluation
指令:wer -c ref.txt text.txt > wer.txt
可得到詳細的插入、刪除、取代錯誤以利後續調整
