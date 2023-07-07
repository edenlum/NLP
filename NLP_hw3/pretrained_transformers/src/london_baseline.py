# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import sys
import utils
from tqdm import tqdm

def all_london(eval_corpus_path):
  predictions = ["London" \
    for line in tqdm(open(eval_corpus_path, encoding='utf-8'))]
  total, correct = utils.evaluate_places(eval_corpus_path, predictions)
  print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))

if __name__ == "__main__":
  all_london(sys.argv[1])