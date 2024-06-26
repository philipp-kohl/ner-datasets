import pandas as pd
import json
import spacy
from spacy.tokens import Doc
from spacy.training import biluo_tags_to_spans, iob_to_biluo
from sklearn.model_selection import train_test_split
import srsly

train_size = 0.7
dev_size = 0.15
test_size = 0.15
"""
  Class to convert CoNLL NER data to JSONLine.
"""

class CONLL2JSON:
    def __init__(self):
        self._sep_list = [' ', '\t']
        self._fmt_list = ['json', 'jsonl']

    @staticmethod
    def _load_text(txt_path):
        """
        Opens the container and reads file
        Returns a list[string]
        :param txt_path: filepath
        """
        with open(txt_path, 'rt') as infile:
            content = infile.readlines()

        return content

    @staticmethod
    def _process_text(content, sep):
        """
        given a list of txt_paths
        -process each
        :param content: list of strings
        :param sep: string representing separator
        :return: list of dicts
        """
        list_dicts = []
        words = []
        nlp = spacy.blank("en")
        # detect newline and make sentences
        for line_num, line in enumerate(content):
            if line != '\n':
                words.append(line.strip('\n'))
            else:
                sentence = " ".join([word.split(sep)[0] for word in words])
                words = [word.split(sep) for word in words]
                df_words = pd.DataFrame(data=words, columns=['word', 'ner'])
                
                doc = nlp(sentence)
                tokens = [token.text for token in doc]
                spaces = len(words) * [True]
                doc = Doc(nlp.vocab, words=df_words['word'], spaces=spaces)

                tmp = biluo_tags_to_spans(doc, iob_to_biluo(df_words['ner']))

                char_spans = [(span.start_char, span.end_char, span.label_) for span in tmp]

                list_dicts.append({'tokens': tokens, 'text': sentence, 'labels': char_spans})

                words = []
        return list_dicts

    @staticmethod
    def _write_text(list_dicts, fmt, output_file):
        """
        :param list_dicts: list of dicts formatted in json
        :param fmt: format of json file either JSON object or JSON Line file
        :param output_file: file to save data
        :return:
        """

    def parse(self, input_file: str, output_file: str, sep: str, fmt, with_split = False) -> None:
        if sep not in self._sep_list:
            raise RuntimeError(f'Separator should be in "{self._sep_list}", provided separator was "{sep}"')

        if fmt not in self._fmt_list:
            raise RuntimeError(f'Format should be in "{self._fmt_list}", provided file format was "{fmt}"')

        content = self._load_text(input_file)
        list_dicts = self._process_text(content, sep)

        if not with_split:
            srsly.write_jsonl(output_file,list_dicts)

        else: # With train test dev split
            train, rest = train_test_split(list_dicts, train_size=train_size, test_size=1-train_size)
            test, dev = train_test_split(rest, train_size=test_size/(test_size+dev_size), test_size=dev_size/(test_size+dev_size))
            sets = {"train": train, "test": test, "dev": dev}
            for name in sets:
                srsly.write_jsonl(output_file+name+".jsonl", sets[name])
 
def process_conll_format_to_jsonl(input_path: str, output_path: str):
    converter = CONLL2JSON()
    converter.parse(input_path, output_path, '\t', 'jsonl')