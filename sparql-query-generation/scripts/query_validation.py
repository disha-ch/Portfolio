import rdflib

# Load the generated query
with open('data/processed/generated_query.txt', 'r') as f:
    query = f.read()

# Validate query using endpoint schema
g = rdflib.Graph()
g.parse('data/processed/knowledge_graph_data_clean.csv', format='csv')

# Execute query
results = g.query(query)

# Save validated results
with open('data/processed/validated_results.csv', 'w') as f:
    for row in results:
        f.write(','.join(row) + '\n')
