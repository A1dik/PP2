def rev_sen(sentence):
    words = sentence.split()
    new_sen = [word[::-1] for word in words]
    return ' '.join(new_sen)

sent = input("Enter a sentence: ")
new_sen = rev_sen(sent)
print("Reversed sentence:", new_sen)