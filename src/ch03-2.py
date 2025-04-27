# 7. Splitting and Joining Strings
sentence = "Python,is,a,great,language"
words = sentence.split(",")  # Split by comma
print("\n7. Splitting and Joining Strings:")
print("Split words:", words)
joined_sentence = " ".join(words)  # Join with space
print("Joined sentence:", joined_sentence)


# Boolean Logic
age = 25
is_adult = age >= 18
print(f"Is Adult: {is_adult}, Type: {type(is_adult)}")