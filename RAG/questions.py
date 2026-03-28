# Q1. Why do we pass context to LLM instead of raw documents database?
# Ans= We pass only retrieved context to reduce noise, improve relevance, and stay within token limits, so the LLM focuses only on information relevant to the query.

# Q2. What happens if retrieved documents are irrelevant?
# Ans=If retrieved documents are irrelevant, the LLM will generate incorrect or misleading answers because it relies on the provided context.
# Key idea: RAG  is only as good as retrieval 

# Q3 why do we limit context size(tokens) ?
# ans = We limit context size because LLMs have token limits, and too much context increases cost, latency, and noise, which can degrade answer quality.

