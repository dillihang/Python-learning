import difflib
"""
Spell Checker with Suggestions.

Asks the user to type a line of text, highlights misspelled words with stars (*),
and prints suggestions for each misspelled word based on a provided word list.

Uses:
- Part7/wordlist2.txt for spell checking
- Part7/similarwords.txt for generating suggestions

Example:
Input:  this is acually a good and usefull program
Output: this is *acually* a good and *usefull* program
        suggestions:
        acually: actually, tactually, factually
        usefull: usefully, useful, museful
"""
line_list=[]
notcorrect=[]
final_string=""

string_list= input("write text: ")
stringpart=string_list.split(" ")

with open("Part7/wordlist2.txt") as file:

    for line in file:

        line=line.replace("\n", "")
        part=line.split(" ")

        for words in part:

            line_list.append(words.lower())

for values in stringpart:
    if values.lower() in line_list:
        final_string+=values + " "
    
    else:
        notcorrect.append(values)
        final_string += f"*{values}*" + " "

print(final_string)

word_list=[]
suggest_dict={}

with open("Part7/similarwords.txt") as words_file:

    for spellings in words_file:
        spellings=spellings.strip()
        word_list.append(spellings)

for items in notcorrect:
    matches = difflib.get_close_matches(items, word_list)
    matchstring= ", " .join(matches)
    suggest_dict[items]=matchstring

print("suggestions:")
for keys, val in suggest_dict.items():
    print(f"{keys}: {val}")



