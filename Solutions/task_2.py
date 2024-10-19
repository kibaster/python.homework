def play(words):
    seen_words = set() 
    error_indices = []
    for i in range(len(words)):
        current_word = words[i]
        if current_word in seen_words:
            error_indices.append(i + 1) 
            continue
        seen_words.add(current_word)
        if i > 0:  
            last_word = words[i - 1]
            if current_word[0] != last_word[-1] and last_word not in seen_words: 
                error_indices.append(i + 1) 
        
    return error_indices
#print(play(["river", "rabbit", "tree", "eagle", "elephant", "tree", "tank"]))