import glassdor_scraper as gs
import pandas as pd

path="D:/Machine Learning/DataAnalysis/chromedriver"
df = gs.get_jobs('data scientist',1000, False, path, 15)