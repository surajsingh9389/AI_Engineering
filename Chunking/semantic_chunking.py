# Semantic chunking flow 

# Sentence Split → Embedding → Similarity Check → Semantic Groups → Chunking

# Psuedo Code 

# for i in range(len(sentences) - 1):
#     sim = similarity(embed(sentences[i]), embed(sentences[i+1]))
    
#     if sim > threshold:
#         add to current chunk
        
#     else: 
#         start new chunk



# ans = if thershold is to high even though the sentences semantically connected to each other because of high threshold the sentence can not group together, because to group them togather require high semantic connection between them, this can produce important sentences split because of this embedding and retrievel become ambigous. If the threshold is to low the sentence can merge easily in chunking this will produce high chunk size also the embedding become ambigous and unnecessary information in retrievel.