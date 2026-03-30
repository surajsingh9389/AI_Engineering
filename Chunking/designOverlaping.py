# 1. How will you implement ovelap?
# ans = first check semantic boundries in sentences, if sentence meanings are connected to each other by their boundries then we can implement overlap. if we can use sliding window approach to dynamically increase of decrease number of words needed of ovelaping.

# ans2 = After creating a chunk, the next chunk starts with last K sentences (or tokens) from previous chunk

# 2. What overlap size will you choose?
# ans = 15-20% overlap size is enough of conecting the sentences by meaning, very large ovelap size can provide duplicacy of chunks and very small size does not provide correct semantic boudries meaning not justify if two sentence are connected ot each other or not. which can cuase ambigous embedding and retrievel.

# 3. What new problems will overlap introduce?
# ans = ovelaing takes more token size, cost of system also increase, number of cunks also increase, if did not do ovelaping correctly can produce duplicate chunks.

# 1. Retrieval redundancy

# Retriever may return:

# Chunk 1
# Chunk 2 (overlapping)

# 👉 Wastes context window

# 2. LLM bias

# Repeated info →

# LLM thinks it's more important

# 3. Ranking confusion

# Two similar chunks:

# which one is better?

# 👉 Harder for retriever

# 4. Storage explosion

# Large corpora → serious issue

# 4. When would you REDUCE or REMOVE overlap?
# ans = Reduce/remove overlap when:
# Small documents
# Single chunk → no overlap
# Highly independent data
# FAQs, logs, structured data
# Latency-critical systems
# Need faster retrieval
# Cost-sensitive systems
# Large-scale pipelines