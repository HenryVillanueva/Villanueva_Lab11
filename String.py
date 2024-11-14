Word_List= []

for x in range(10):
    word = input(f"Enter a word { x + 1}:")
    Word_List.append(word)

while True:
    length = input("Enter number of characters wanted:")
    if length.isdigit():
        length = int(length)
        break
    else:
        print("You have entered an invalid character")
        
words = [word for word in Word_List if len(word) == length]

if words:
    print("Words matching the given number count:", ', '.join(words))
else:
    print("No words found with the given number of characters")
