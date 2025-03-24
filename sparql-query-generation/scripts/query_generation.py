from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Example input
input_text = "What is the function of the gene BRCA1?"

# Generate query
inputs = tokenizer.encode(input_text, return_tensors='pt')
outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
query = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Save query
with open('data/processed/generated_query.txt', 'w') as f:
    f.write(query)
