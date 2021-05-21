import pytest
import requests


url = "https://csit314-testing-tool.herokuapp.com"
res = requests.get(url)

print(res)