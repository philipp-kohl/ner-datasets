# NER Datasets

Data collection from [Scoping Review](https://github.com/philipp-kohl/scoping-review-active-learning-er).

You have to request or investigate several corpora for your use case  and download the data by yourself. Please add downloaded data to the according directory in `raw_data`.
You can use our script to convert the data: `python -m raw_data.<corpus>.process_data`

## List of datasets with license information:

- CoNLL 2003 English NER [register & download]:
    - Download it via huggingface and register for a license.
    - https://huggingface.co/datasets/conll2003#licensing-information
- CoNLL 2002 Spanish [register & download]
    - Download it via huggingface and register for a license.
    - https://huggingface.co/datasets/conll2002#licensing-information
- CoNLL 2002 Dutch [register & download]
    - Download it via huggingface and register for a license.
    - https://huggingface.co/datasets/conll2002#licensing-information
- NCBI Disease [included]
    - "The data is freely available to the public for use"
    - https://huggingface.co/datasets/ncbi_disease#licensing-information
- MedMentions [included]
    - CC0: public domain
- Paramopama [unoffical source]
    - Could not find any license information
    - https://goo.gl/9e3O1O Official Link does not work anymore
    - Alternative: https://github.com/davidsbatista/NER-datasets/blob/master/Portuguese/Paramopama/
- Second HAREM [included]
    - Creative Commons Licence 3.0 (see Readme: https://www.linguateca.pt/HAREM/)
- WNUT2016 [included]
    - GNU General Public License v3.0
- CSIRO Adverse Drug Event Corpus (CADEC) [included]
    - Free for research purposes, cite the paper:  https://data.csiro.au/collection/csiro:10948v3
- SCIERC [included]
    - 'Publicly available' cited from the paper: https://aclanthology.org/D18-1360.pdf
- i2b2/VA 2010 NLP [request]
    - Free for research purpose
    - Request at: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/
- Broad Twitter Corpus [included]
    - Creative Commons Attribution 4.0 International (CC BY 4.0)
- Disease Names and Adverse Effect Corpus (DISAE) [included]
    - 'Therefore, a newly annotated corpora is made publicly available.' cited from the paper
- OntoNotes 5.0 English [request]
    - LDC User Agreement for Non-Members: https://catalog.ldc.upenn.edu/LDC2013T19
- JNLPBA [investigate & download]
    - Original link broken
    - No known license
    - https://huggingface.co/datasets/jnlpba
- Herodotos Project [included]
    - Cite paper: https://github.com/Herodotos-Project/Herodotos-Project-Latin-NER-Tagger-Annotation
- GermEval 2014 NER Shared Task [included]
    - CC-BY license
- Papers selected by computational neuroscientist (COR) [included]
    - 'The corpus and the NER tools are available via GitHub (See: https://github.com/nactem/TM4NS)' no explicit license
      stated
- AURC-8 (also referred to as ARG) [included]
    - Cite paper: https://github.com/trtm/AURC
- GeneReg Corpus (MedLine abstracts) [included]
    - Creative Commons Attribution-Noncommercial 3.0
    - 'The corpus and annotation guidelines are freely available for academic purposes at http://www.julielab.de' cited
      from paper (http://www.lrec-conf.org/proceedings/lrec2010/pdf/407_Paper.pdf)
- CORA-Headers [investigate & download]
  - No known license; root data was publicly available, but the domain was sold
  - https://people.cs.umass.edu/~mccallum/data.html
- CORA-References [investigate & download]
  - No known license; root data was publicly available, but the domain was sold
  - https://people.cs.umass.edu/~mccallum/data.html
- Sig+Reply [investigate & download]
  - No known license
  - https://www.cs.cmu.edu/%7Evitor/codeAndData.html
- SigIE [included]
  - 'Feel free to use them in your own work, and be sure to cite the papers listed in README files, if appropriate' cited from the website
  - https://pages.cs.wisc.edu/~bsettles/data/
- FTD [included]
  - Research purpose: 'The dataset is available at http://cs.stanford.edu/people/sonal/fta for the research community.'
- CoNLL 2000 English [investigate & download]
  - Chunking task, no ER, but listed for other researchers
  - https://huggingface.co/datasets/eriktks/conll2000
