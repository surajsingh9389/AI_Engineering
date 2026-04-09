from sentence_transformers import CrossEncoder

# Load model 
model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

pairs = [
  ("refund for iPhone", "Samsung return policy is 10 days"),
  ("refund for iPhone", "iPhone 15 refund policy is 7 days")
]

scores = model.predict(pairs)

print(scores)