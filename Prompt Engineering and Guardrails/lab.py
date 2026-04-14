# 1. Updated Prompt 
prompt = f"""
You are a strict question-answering assistant.

Rules:
1. Answer ONLY using the provided context.
2. Do NOT use any external knowledge.
3. If the answer is not explicitly present in the context, respond with EXACTLY:
   "I don't know"
4. Do NOT explain your answer.
5. Do NOT add any extra text.

------
Example 1:
Context: iPhone refund policy is 7 days
Question: What is iPhone refund policy?
Answer: iPhone refund policy is 7 days

Example 2: 
Context: Refunds are processed in 5 days
Question: What is the price of iPhone?
Answer: I don't know

Context:
{context}
"""

2. 

docs = [
  "Samsung return policy is 10 days",
  "Refunds are processed within 5 days",
  "iPhone 15 refund policy is 7 days",
  "The Amazon river is the largest by discharge volume.",
  "Amazon.com is a leading e-commerce company."
]

query = "How long does iPhone refund take?"

for the above docs and query the model generate the answer:
    most of the times "I don't know", But sometimes "Refunds are processed within 5 days" so i want to know which is correct for the query or is my model hallucainating.