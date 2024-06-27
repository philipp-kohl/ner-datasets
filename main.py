from sklearn.model_selection import train_test_split
from typing import List
import srsly
import re
import spacy
import pandas as pd
from spacy.tokens import Doc
from spacy.training import biluo_tags_to_spans, iob_to_biluo


train_size = 0.7
dev_size = 0.15
test_size = 0.15

def process_and_split_local_corpus(dataset, output_name):
    result = []

    raw_text = dataset.read().strip()
    raw_docs = re.split(r'\n\t?\n', raw_text)

    for doc in raw_docs:
        tokens = []
        tags = []
        for line in doc.split('\n'):
            token, tag = line.split('\t')
            tokens.append(token)
            tags.append(tag)
        text = " ".join(tokens)

        labels: List[(int,int,str)] = []
        count_character: int = 0
        for i,token in enumerate(tokens):
            start: int = count_character
            count_character += len(token)+1 # Add number of character plus whitespace
            end: int = count_character

            if tags[i] != 'O':
                labels.append((start,end,tags[i]))

        datapoint = {
            "tokens": tokens,
            "text": text,
            "labels": labels,
        }
        result.append(datapoint)

    train, rest = train_test_split(result, train_size=train_size, test_size=1-train_size)
    test, dev = train_test_split(rest, train_size=test_size/(test_size+dev_size), test_size=dev_size/(test_size+dev_size))

    srsly.write_jsonl(output_name+"train.jsonl", train)
    srsly.write_jsonl(output_name+"test.jsonl", test)
    srsly.write_jsonl(output_name+"dev.jsonl", dev)


def save_to_jsonl(dataset, output_name):
    nlp = spacy.blank("en")
    result = []
    for example in dataset:
        def replace_tag(tag_number: int):
            return dataset.features["ner_tags"].feature.names[tag_number]

        datapoint = {
            "tokens": example["tokens"],
            "text": " ".join(example["tokens"]),
            "tags": [replace_tag(tag) for tag in example["ner_tags"]],
        }

        words_with_empty = example["tokens"]
        words = []
        for word in words_with_empty:
            if word != "":
                words.append(word)

        spaces = len(words) * [True]
        doc = Doc(nlp.vocab, words=words, spaces=spaces)

        tmp = biluo_tags_to_spans(doc, iob_to_biluo(datapoint["tags"]))

        char_spans = [(span.start_char, span.end_char, span.label_) for span in tmp]

        datapoint["labels"] = char_spans
        result.append(datapoint)

    srsly.write_jsonl(output_name, result)

def read_files_and_split():
    result = []
    jsonObj = pd.read_json(path_or_buf='your_path', lines=True)
    result.extend(jsonObj.to_dict('records'))
    jsonObj = pd.read_json(path_or_buf='your_path', lines=True)
    result.extend(jsonObj.to_dict('records'))
    
    train, rest = train_test_split(result, train_size=0.7, test_size=0.3)
    test, dev = train_test_split(rest, train_size=0.5, test_size=0.5)

    srsly.write_jsonl("split_train.jsonl", train)
    srsly.write_jsonl("split_test.jsonl", test)
    srsly.write_jsonl("split_dev.jsonl", dev)