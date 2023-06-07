# Simple Sentiment Analysis
A Python sentiment analysis script trained on a dataset of Tweets that are classified as positive or negative. Created by Sam Noyes in 2023.

## About
This sentiment analysis script uses the textcat module of the spaCy natural language processing library, in conjunction with a dataset of Tweets categorized as "positive" and "negative", to perform sentiment analysis. It represents one of my first forays into NLP and can be used as an example by anyone trying to learn.

## Usage
`python3 simple_sentiment_analysis.py <string to analyze>`

Examples:
`python3 simple_sentiment_analysis.py "i love this movie"`
Output:
`{'positive': 0.8196957111358643, 'negative': 0.18030422925949097}`

`python3 simple_sentiment_analysis.py "i hate this movie"`
Output:
`{'positive': 0.21716347336769104, 'negative': 0.7828364968299866}`

## Process
- Downloaded Sentiment Analysis dataset from Kaggle: [Twitter Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)
- Created the convert_csv_to_json.py script, which converted the dataset from .csv to .jsonl, with the help of ChatGPT (and some significant tweaks). Ran the .csv training dataset through this script.
- Got the convert.py script, which converted the dataset from .jsonl to .spacy, from [this textcat demo project](https://github.com/explosion/projects/tree/v3/pipelines/textcat_demo). Ran the .jsonl training dataset through this script
	- In the future, I would like to figure out how to convert the .csv directly to .spacy, without the intermediate step.

[Also want to give credit to this tutorial on text classification by Catherine Breslin](https://catherinebreslin.medium.com/text-classification-with-spacy-3-0-d945e2e8fc44), which was very helpful
