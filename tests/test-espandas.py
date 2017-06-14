import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch,helpers
from elasticsearch.exceptions import RequestError, ConnectionError

# ES variables
INDEX = 'unit_tests_index'
TYPE = 'foo_bar'

# Example data frame
df = pd.DataFrame(np.random.rand(100, 5))
df.columns = ['A', 'B', 'C', 'D', 'E']
df['_id'] = df['A'] + df['B']

a = json.loads(records)


es = Elasticsearch()
try:
	es.indices.create(INDEX)
except RequestError:
	print 'Index already exists skipping tests'
	assert True
except ConnectionError:
	print  'The ElasticSearch backend is not running. Skipping tests.'
	assert True
except Exception as e:
	print 'An unknown error occured: %s' % e


es.indices.delete(INDEX)