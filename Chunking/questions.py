# You have this document:

# Section 1: Introduction to AI
# AI is the simulation of human intelligence...

# Section 2: Machine Learning
# Machine learning is a subset of AI...

# Section 3: Deep Learning
# Deep learning uses neural networks...

# -------------------------------------------------

# Q1. How would YOU chunk this document?
# ans= i can split this document based on sections and with there respective data. the firs chunk cantain section 1, second chunk section 2 and so on.

# ans2. = Section = boundary, not always a chunk, Respect sections, BUT still split large sections further

# Q2. What chunk size would you choose? 
# ans = Embedding models work best around, 200–500 tokens per chunk. 

# Why?

# Too small → weak meaning
# Too large → noisy retrieval

# ans2=I would use ~300 tokens per chunk, ensuring semantic completeness

# Q3. Would you use overlap? If yes, how much? 
# ans = Overlap: 10–20% of chunk size
# If chunk = 300 tokens → overlap ≈ 30–60 tokens
# This preserves semantic continuity

# Q4. What mistakes could happen here?
# ans = Real Mistakes You Missed:
# 1. Topic mixing
# If chunk accidentally contains:
# end of Section 1
# start of Section 2
# → retrieval confusion
# 2. Chunk too generic
# “Introduction to AI” alone is useless
# 3. Embedding dilution
# Large chunks = multiple ideas → weak vector signal
# 4. Ignoring headings
# Headings are GOLD for retrieval

# -----------------------------------------------------------

# Q1. Would you include the section title inside the chunk?
# ans = yes, Title inside the chunk clearly specify topic, the chunk belong to what topic.

# ans2 = Titles act like metadata inside the embedding, They improve Retrieval accuracy, Disambiguation, 

# but tadeoff - Titles repeated in every chunk → embedding bias, Too many repeated words = noisy vectors 

# So better approach:

# Include title, but avoid unnecessary repetition (or store as metadata separately)

# Q2. Suppose Section 2 is VERY LARGE (1000 tokens)
# ans = take token length of 200-300 of each chunk, yes also do overlap so the meaning of sentences remain consistent, for ovelaping i use around 20 to 30 token bounderies limit so the senteces realate to each other. 


# ans: Don’t split blindly at 300 tokens, Instead Prefer splitting at Sentence boundaries, paragraph boundaries. Semantic boundaries > fixed token limits

# Q3. What happens if user query is:

# “What is AI?”

# Which chunk will be retrieved and WHY?

# ans = the section 1 chunk the Introduction to AI with the sentence AI is the simulation of human intelligence, because this chunk as the highest similarity to query because of AI keyword.


# ans2 - Embeddings capture semantic meaning, not just keywords, The correct chunk will be retrieved because, It defines AI, It has high semantic similarity, not just keyword match

# Good chunking ensures clear intent per chunk



# Q4. When would overlap actually hurt performance?
# ans = when the documents are small and divided by sentences, means we do not need to do ovelaping there, because overlaping take more token which increase the cost.

# ans2 = 1. Duplicate retrievals
# Overlap creates similar chunks
# Retriever may return:
# Chunk A
# Chunk A (overlap version)

# 👉 Wastes context window

# 2. Increased latency
# More chunks = more embeddings = slower search
# 3. Context pollution
# LLM sees repeated information
# Can confuse or bias output
# 4. Storage cost
# More chunks = larger vector DB

# 👉 So:

# Overlap improves recall but hurts efficiency 