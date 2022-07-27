def solution(S):
  sentences = S.split('.')
  print(f"{sentences}")
  # k: v = sentence : num_of_words_in_sentence
  mydict = {}
  for sent in sentences:
    words = sent.split(' ')
    words_without_spaces = [w for w in words if w != '']
    mydict[sent] = len(words_without_spaces)
    
  print(f'{mydict}')
  return max(mydict.values())
