# Simple Sentiment Analysis

## About
This sentiment analysis tool uses the textcat module of the spaCy natural language processing library, in conjunction with a dataset of Tweets categorized as "positive" and "negative", to perform sentiment analysis. It represents one of my first forays into NLP and can be used as an example by anyone trying to learn.

## Installation

1. Ensure you have Python installed

2. Clone this repository to your local machine using the following command:

`git clone https://github.com/samnoyes/SentimentAnalysis.git`

3. Install the required dependencies. In terminal: navigate to the project directory and run the following command:

`pip install -r requirements.txt` (`pip3` if you are using python3)

This will install the necessary packages, including spaCy.

4. Download spaCy's English language model by running the following command:

`python -m spacy download en` (or `python3`)

This will download the required language model for performing sentiment analysis.

## Usage
`python simple_sentiment_analysis.py <string to analyze>` (or `python3` depending on your version)

Examples:

`python simple_sentiment_analysis.py "i love this movie"`

Output:
`{'positive': 0.8196957111358643, 'negative': 0.18030422925949097}`

`python simple_sentiment_analysis.py "i hate this movie"`

Output:
`{'positive': 0.21716347336769104, 'negative': 0.7828364968299866}`

## Process/Credits
- Downloaded Sentiment Analysis dataset from Kaggle: [Twitter Sentiment Analysis](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis)
- Created the convert_csv_to_json.py script, which converted the dataset from .csv to .jsonl, with the help of ChatGPT (and some significant tweaks). Ran the .csv training dataset through this script.
- Got the convert.py script, which converted the dataset from .jsonl to .spacy, from [this textcat demo project](https://github.com/explosion/projects/tree/v3/pipelines/textcat_demo). Ran the .jsonl training dataset through this script twice to create dev.spacy and train.spacy.
	- In the future, I would like to figure out how to convert the .csv directly to .spacy, without the intermediate step.
- Trained the model, waiting ~24 hours for it to complete.

[Also want to give credit to this tutorial on text classification by Catherine Breslin](https://catherinebreslin.medium.com/text-classification-with-spacy-3-0-d945e2e8fc44), which was very helpful

## Customization
Feel free to reuse this project to train based on your own dataset. It doesn't just have to be sentiment analysis: you can use this for other things such as text classification – for example, [categorizing a news article based on the topic.](https://catherinebreslin.medium.com/text-classification-with-spacy-3-0-d945e2e8fc44) If you have a csv dataset that you would like to use, you will need to follow these steps:
1. Import it into the project directory and edit convert_csv_to_json.py lines 16-26 to process the data based on the format of your csv.
2. Run `python convert_csv_to_json.py <dataset.csv> <dataset_jsonl.jsonl>` to convert it to jsonl.
3. Run `python convert.py <dataset_jsonl.jsonl> train.spacy` and `python convert.py <dataset_jsonl.jsonl> dev.spacy` to create the dev and train splits of your data, formatted for processing by spaCy.
4. Run `python -m spacy train config.cfg --paths.train ./train.spacy  --paths.dev ./dev.spacy --output textcat_model` to train the model. The output will look something like this:
~~~
============================= Training pipeline =============================
ℹ Pipeline: ['textcat']
ℹ Initial learn rate: 0.001
E    #       LOSS TEXTCAT  CATS_SCORE  SCORE 
---  ------  ------------  ----------  ------
  0       0          0.25       50.77    0.51
  0     200         47.06       68.29    0.68
  0     400         43.01       70.78    0.71
  0     600         39.88       72.59    0.73
  0     800         38.64       74.03    0.74
  0    1000         37.12       74.90    0.75
  0    1200         35.03       75.58    0.76
  0    1400         35.23       75.92    0.76
  0    1600         34.22       76.62    0.77
  0    1800         34.85       76.84    0.77
  0    2000         32.66       77.30    0.77
  0    2200         32.77       77.54    0.78
  0    2400         32.39       77.72    0.78`
~~~
  You may have to wait ~24 hours for this to run, although feel free to stop it once it is no longer improving.
  
5. Run simple_sentiment_analysis.py with your input to check the results.

## Notes
Please note that the datasets are not included in this repo. If you want to recreate them, just download the CSVs from [the dataset from Kaggle](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis), and run them through convert_csv_to_json.py and convert.py.
