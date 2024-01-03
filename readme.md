## Semantic Search Engine with ElasticSearch

  ___
  ## Table of contents
  * [Introduction](#Introduction)
  * [Getting Started](#Getting-Started)
  * [Features](#Features)
  * [Future Work](#Future-Work)
  
  ___
  ## Introduction
  ![Python 3.10](https://img.shields.io/badge/Python-3.10-brightgreen.svg)
  ![Sentence-Tokenizer](https://img.shields.io/badge/SentenceTokenizer-red.svg)
  ![ElasticSearch](https://img.shields.io/badge/ElasticSearch-blue.svg)
  
  
  <p>
      <b>SSE</b> is a powerful tool that leverages power for Semantic Search Engine to extract the most relevant information from the legal document. It uses <b> ElasticSearch </b> to index the data and <b> Sentence Tokenizer - <i>all-distilroberta-v1</i> </b> to extract the most relevant sentences from the document.
      <br>
      It used data from <b> Caselaw Access Project: Hovard Law School [North Carolina]</b> <a href="https://case.law/bulk/download/">Link </a>. 
      
  </p>
  
  ___
  ## Getting Started

  **Steps**
  - Create a virtual environment
  ``` 
    git clone https://github.com/Vice777/Semantic-Search-Engine.git
    conda create -n venv python=3.10
    conda activate venv
    conda install -r requirements.txt
  ```
  
  - Setup ElasticSearch
  ```
    ## windows:  https://www.elastic.co/downloads/elasticsearch
    
    ## Locate the path, where downloaded the file. Open cmd
    cd bin
    elasticsearch.bat

    ## Save the crediential for later use in .env file

  ```
  
  
  ___
  ## Features
  
  | Feature                    | Description                                                                                                       |
  |----------------------------|-------------------------------------------------------------------------------------------------------------------|
  | Fast and Efficient          | Search quicklt through multiple documents and provide results with maximum similarity score.  |
  | Versatile Use Cases         | Just by changing the source dataset it would be used in any software, to increase the searching capabilities. |
  
  ## Future Work
    Create a proper Streamlit UI to leverage uses of sematic search.
    Enable Web Crawling to better results.
  ___
  ## About Me
    [Vivek Dharewa](https://github.com/Vice77)<br>
    If you have any questions, feedback, or feature requests, please don't hesitate to reach out.<br>
    We hope you find SSE a valuable addition to your toolkit for efficient knowledge and extraction for legal documents.<br>
    Thank you for using our app!
  