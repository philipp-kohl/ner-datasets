from typing import Optional
from datasets import load_dataset
from main import save_to_jsonl

import argparse

def load_corpus_from_huggingface(name: str, config: Optional[str] = None):
    """ Loads Corpus from huggingface datasets library. List of available corpora: list_datasets()
    Args:
        - name (str): Name of the dataset
        - str (str|None): config, if needed (e.g. 'nl' for dutch version of conll2002)
    
    Returns:
        - tuple: train, dev, test set
    """

    if config:
        corpus = load_dataset(name, config, trust_remote_code=True)
    else:
        corpus = load_dataset(name, trust_remote_code=True)

    train = corpus["train"]
    dev = corpus["validation"]
    test = corpus["test"]

    return (train, dev, test)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='Name of the corpus on huggingface')
    parser.add_argument('--config', help="Configuration if needed for loading of corpus, default: None", default=None)
    args = parser.parse_args()
    train, dev, test = load_corpus_from_huggingface(args.name, args.config)

    save_to_jsonl(train, "processed_data/"+args.name+"/train.jsonl")
    save_to_jsonl(dev, "dev.jsonl")
    save_to_jsonl(test, "test.jsonl")

if __name__=="__main__":
    main()