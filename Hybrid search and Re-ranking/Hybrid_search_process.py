# [ User Query ] 

#              |
#       _______|_______
#      |               |
# [ Engine 1: BM25 ] [ Engine 2: FAISS ]
# (Keyword Match)    (Semantic Match)

#      |               |
#  [ List A ]      [ List B ]
#  (Ranked 1-10)   (Ranked 1-10)

#      |               |
#      \_______ _______/

#              |
#       [ RRF FUSION ]  <-- The "Magic" Step
#      (1 / (k + Rank))
#              |
#    [ Final Ranked List ]
#    (The "Consensus" Top Results)

# Split: The query goes to two "brains" at once.
# Lists: Each brain creates its own top-10 list.
# RRF: This is the bridge. It converts position (1st, 2nd, 3rd) into a score.
# Merge: If a document is on both lists, its scores are added together, pushing it to the #1 spot.