def extract_matching_and_original_sentences(test_filename, ref_filename):
    matching_sentences = {}
    original_sentences = {}
    
    with open(test_filename, "r", encoding="utf-8") as test_file:
        test_lines = test_file.readlines()
        for test_line in test_lines:
            test_line = test_line.strip().split(",")
            if len(test_line) == 2:
                test_id, test_text = test_line
                with open(ref_filename, "r", encoding="utf-8") as ref_file:
                    ref_lines = ref_file.readlines()
                    for ref_line in ref_lines:
                        ref_line = ref_line.strip().split(",")
                        if len(ref_line) == 2 and ref_line[0] == test_id:
                            matching_sentences[test_id] = ref_line[1]
                            original_sentences[test_id] = test_text
                            break  # 找到相符的句子後跳出內層迴圈
    return matching_sentences, original_sentences

def save_sentences_to_file(sentences, output_filename):
    with open(output_filename, "w", encoding="utf-8") as file:
        for sentence in sentences.values():
            sentence_with_spaces = " ".join(sentence)
            file.write(sentence_with_spaces + "\n")

matching_sentences, original_sentences = extract_matching_and_original_sentences("text.csv", "ref.csv")
save_sentences_to_file(matching_sentences, "ref.txt")
save_sentences_to_file(original_sentences, "text.txt")
