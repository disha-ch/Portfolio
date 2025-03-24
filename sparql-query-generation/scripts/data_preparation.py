### `data_preparation.py`

```python
import pandas as pd
import numpy as np

# Load the raw data
data = pd.read_csv('data/raw/knowledge_graph_data.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Save the processed data
data.to_csv('data/processed/knowledge_graph_data_clean.csv', index=False)
