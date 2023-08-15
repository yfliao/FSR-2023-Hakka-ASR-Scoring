import nltk

# 編號在第一行，文本在第二行
reference_file_path = "hakka_transcript.csv"

with open(reference_file_path, "r", encoding="utf-8") as file:
    ref_lines = file.readlines()

# 答案放在reference_data
reference_data = {}
for line in ref_lines:
    line = line.strip().split(",")
    if len(line) == 2:
        reference_data[line[0]] = line[1]

def word_error_rate(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()

    edit_distance = nltk.edit_distance(ref_words, hyp_words)
    len_ref = len(ref_words)

    wer = float(edit_distance) / len_ref

    return wer

def sentence_error_rate(reference, hypothesis):
    ref_sentences = reference.split("\n")
    hyp_sentences = hypothesis.split("\n")

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

test_data = {}
for line in lines:
    line = line.strip().split(",")
    if len(line) == 2:
        test_data[line[0]] = line[1]


# 計算WER和SER並輸出結果
total_wer = 0
total_ser = 0
for num, text in test_data.items():
    if num in reference_data:
        reference_text = reference_data[num]
        wer = word_error_rate(reference_text, text)
        ser = sentence_error_rate(reference_text, text)
        print(f"編號 {num} 的WER： {wer:.4f}, SER: {ser:.4f}")
        total_wer += wer
        total_ser += ser

average_wer = total_wer / len(test_data)
average_ser = total_ser / len(test_data)
print(f"平均WER： {average_wer:.4f}")
print(f"平均SER： {average_ser:.4f}")

