# Further Instructions

- use Regex to fix word-matching issue -> death_squad, deathlike being used for death {7355491 is the exact ID for death}
    - [ ]{3,} - Regex
- stemming removed, lemmatize only
- figure out H L P meaning (.txt)
- will receive figma and resources

## Approach
[we considered levenstein distance but now removed because it doesn't take semantics into account]

    3. BERT + embeddings
        - MongoDB, Pinecone for database - Pinecone for now
        - First check {word} 

