
import spacy
import sys

if len(sys.argv) != 2:
	print("Usage: python script_name.py <input_string>")
	sys.exit(1)

# Load the pre-trained model
nlp = spacy.load("./textcat_model/model-best")
text = sys.argv[1].lower()
doc = nlp(text)
print(doc.cats)
