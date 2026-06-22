class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        q=deque()

        set_wordlist=set(wordList)
        if endWord not in set_wordlist:
            return 0
        q.append((beginWord,1))

        while q:
            word,steps=q.popleft()
            word_chars=list(word)

            for i in range(len(word_chars)):
                orignal_char=word_chars[i]

                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c==orignal_char:
                        continue
                    
                    word_chars[i]=c
                    next_word=''.join(word_chars)

                    if next_word in set_wordlist:
                        if next_word==endWord:
                            return steps+1
                        q.append((next_word,steps+1))
                        set_wordlist.remove(next_word)
                word_chars[i]=orignal_char
        
        return 0