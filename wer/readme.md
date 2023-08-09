1. 若只計算拼音的錯誤率，請先準備text.csv和ref.csv，然後使用wer.py，但需更換wer.py中的reference_file_path和test_file_path變數。有參考檔案和espnet的結果對照。
```
$ python wer.py
```
2.  若要得到更詳細的插入、刪除、取代錯誤以利後續調整，請先用seperate.py重新格式化text.csv和ref.csv，產生句對句對齊後ref.txt與text.txt，再用wer程式計算插入、刪除、取代錯誤。
```
$ pyhton seperate.py
$ pip install asr-evaluation
$ wer -c ref.txt text.txt > wer.txt
```
