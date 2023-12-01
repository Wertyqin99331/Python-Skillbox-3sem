import requests
from re import findall

response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
result_beta = findall(r'>.+</h3>', response)
release = list(map(lambda x: x[1:-5], result_beta))
print(release)
