
1. 若只計算漢字的錯誤率，請先準備text.csv和ref.csv（格式為 Sent. ID, transcription。不管句子順序），然後使用cer.py，但需更換cer.py中的reference_file_path和test_file_path變數。有參考檔案和espnet的結果對照。
```
python cer.py
```
2.  若要得到更詳細的插入、刪除、取代錯誤以利後續調整，請先用seperate.py重新格式化text.csv和ref.csv，產生句對句對齊後ref.txt與text.txt（格式為 Sent. ID, transcription。要對齊句子順序），再用安裝好的wer指令計算插入、刪除、取代錯誤。
```
python seperate.py
pip install asr-evaluation
wer -c ref.txt text.txt > cer.txt
```
