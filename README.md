# Find Relevant Federal Awards Notifications

## Problem Statement

Fedbizopps.gov used to be a website where small businesses could search for federal contract opportunities. While the collection of soliciations and award notifications was searchable based on key terms, finding opportunities of interest based on similarity, rather than key term search, as far as I know, was not available. As a result, looking for contract opportunities took a considerable time, which could potentially put a strain on lightly staffed small businesses. The successor of Fedbizopps.gov, Beta.SAM.gov, provides a wide array of filtering options besides the search by key terms and the browsing function. Those new to the system would benefit, however, from an application that recommends opportunities of interest based on topic and/or wording similarity.

## Executive Summary

#### The purpose of this project:
1. Stretching the limits of natural language processing, build an application that, based on topic similarities would recommend contract notifications of interest.
2. Observe how well a content based recommender system is capable of finding not only similar but also relevant notifications.

#### Data:
Using the [Get Opportunities Public API](https://open.gsa.gov/api/get-opportunities-public-api/), a collection of **50_000** contract notifications was pulled from the Beta.SAM.gov website between Jan. 1, 2020 - June 7, 2020. The size of the dataset is continuously growing, as new notifications are downloaded and added to it daily.

#### Recommender System:
The search engine is built on a content based recommender that provides notifications of interest based on topic similarity.

#### Limitations of the System:
One of the challenges of building such a system is the difficulty of getting sufficient amount of data to train the model to make meaningful comparisons between the different documents. In absence of longer documents the vocabulary of the recommender is being built on the titles of the notifications. However, the succinct sentences lack the adequate amount of context-rich verbal cues to make the recommender operational, which in turn is going to test the limits and limitations of natural language processing algorithms.

#### Conclusion
Despite the challenges, when scrutinized by common sense, the system finds both similar and relevant notifications. However, further test runs are required, to identify and correct possible shortcomings. 

## Table of Contents
##### Notebooks

  [Data Collection](001_dataGathering.ipynb)<br>
  [EDA](002_EDA.ipynb)<br>
  [Recommender - Tf-Idf Vectorizer](004_tfidf.ipynb)<br>
  [Recommender - Doc2Vec](005_doc2vec.ipynb)<br>
  [Keyword - Search](006_search_data_by_query.ipynb)

##### Data
  [Contract Notifications](https://drive.google.com/file/d/11yVkQKdPVIzUTCcrFdDiNEQk1kC4gFUl/view?usp=sharing)<br>
  [Tokenized Titles](https://drive.google.com/file/d/1AsKKAohC4Qc6S3GrdWEA64qF6lOvZkrh/view?usp=sharing)

##### Other
  [Trained Doc2Vec Model](models/doc2vec_model)<br>
  [Notes](Notes.txt)
  
___
#### Next Steps:
- Automate daily data retrieval and model-rebuild to keep the content of the search engine up-to-date
- Add filtering options to the search application
