import nltk

# 編號在第一行，文本在第二行
reference_file_path = "aishell_transcript_v0.8.csv"

with open(reference_file_path, "r", encoding="utf-8") as file:
    ref_lines = file.readlines()

# 答案分成編號和文本，放在reference_data
reference_data = {}
for line in ref_lines:
    line = line.strip().split(",")
    if len(line) == 2:
        reference_data[line[0]] = line[1]

def character_error_rate(reference, hypothesis):
    ref_chars = list(reference)
    hyp_chars = list(hypothesis)

    edit_distance = nltk.edit_distance(ref_chars, hyp_chars)
    len_ref = len(ref_chars)

    # 計算CER
    cer = float(edit_distance) / len_ref

    return cer

def sentence_error_rate(reference, hypothesis):
    ref_sentences = reference.split("。")
    hyp_sentences = hypothesis.split("。")

    ref_sentences = [sent.strip() for sent in ref_sentences if sent.strip()]
    hyp_sentences = [sent.strip() for sent in hyp_sentences if sent.strip()]

    sentence_error = len(ref_sentences) - len(hyp_sentences)

    # 計算SER
    for ref_sent, hyp_sent in zip(ref_sentences, hyp_sentences):
        if ref_sent != hyp_sent:
            sentence_error += 1

    ser = float(sentence_error) / len(ref_sentences)

    return ser

# 測試檔案
test_file_path = "text.csv"

# 編號在第一行，文本在第二行
with open(test_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 測試資料分成編號和文本
test_data = {}
for line in lines:
    line = line.strip().split(",")
    if len(line) == 2:
        test_data[line[0]] = line[1]

# 計算CER和SER並輸出結果
total_cer = 0
total_ser = 0
for num, text in test_data.items():
    if num in reference_data:
        reference_text = reference_data[num]
        cer = character_error_rate(reference_text, text)
        ser = sentence_error_rate(reference_text, text)
        print(f"編號 {num} 的CER： {cer:.4f}, SER: {ser:.4f}")
        total_cer += cer
        total_ser += ser

average_cer = total_cer / len(test_data)
average_ser = total_ser / len(test_data)
print(f"平均CER： {average_cer:.4f}")
print(f"平均SER： {average_ser:.4f}")
