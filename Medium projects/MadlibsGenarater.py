with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_ind = -1

start_char = '<'
end_char = '>'

for i,char in enumerate(story):
    if char == start_char:
        start_ind = i

    if char == end_char and start_ind != -1:
        word = story[start_ind:i+1]
        words.add(word)
    
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])

print(story)

    