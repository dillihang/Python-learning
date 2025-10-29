def filter_forbidden(string: str, forbidden: str):
    return "".join([char if char not in forbidden else "" for char in string])
  

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)

