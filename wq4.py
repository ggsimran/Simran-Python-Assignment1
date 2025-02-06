word = str(input("enter any word: "))

index = int (input("enter the string index: "))

sub_string = word[index:]
print(f"Substring from index{index}: {sub_string}")