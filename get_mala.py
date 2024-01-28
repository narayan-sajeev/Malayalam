import requests
from bs4 import BeautifulSoup
from ml2en import ml2en

# Convert Malayalam words to English
converter = ml2en()

# Retrieve list of words
url = 'https://1000mostcommonwords.com/1000-most-common-malayalam-words/'

# Parse HTML
tbody = BeautifulSoup(requests.get(url).content, 'html.parser').find('tbody')

# Create list of words
lst = [[td.text for td in tr.find_all('td')] for tr in tbody.find_all('tr')]

# Remove first element
lst.remove(lst[0])

# Remove first element of each sublist
lst = [_[1:] for _ in lst]
# Remove all words with length less than 3
lst = [_ for _ in lst if len(_) == 2]
lst2 = []

# Loop through list
for _ in lst:
    # Convert Malayalam word to English
    result = converter.transliterate(_[0])
    # Add to list
    lst2.append([_[0], result.lower(), _[1].lower()])

# Remove duplicates
lst2 = [_ for i, _ in enumerate(lst2) if _[0] not in [_[0] for _ in lst2[:i]]]
# Remove all words with same Malayalam and English words and words with length greater than 2
lst2 = [_ for _ in lst2 if _[0] != _[1] and len(_[0]) > 2 and len(_[1]) > 2]

# Write to file
with open('mala.txt', 'w') as f:
    # Loop through list
    for _ in lst2:
        # Write to file
        f.write('%s %s %s\n' % (_[0], _[1], _[2]))