import sys 

def get_book_text(path_to_file):
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        for word in file_contents.split():
            word_count += 1
        # print(f"Found {word_count} total words")
        return word_count

def char_count(path_to_file): 
    new_dict = {}
    with open(path_to_file) as f: 
        file_contents = f.read()
        file_list = file_contents.lower().split() 
        for item in file_list: 
            for char in item: 
                if char not in new_dict: 
                    new_dict[char] = 1
                elif char in new_dict: 
                    new_dict[char] += 1
    # print(new_dict)
    return new_dict

my_dict = char_count("books/frankenstein.txt")
book_wc = get_book_text(sys.argv[1])

def sort_on(items):
    return items["num"]

def sort_it(some_dict): 
    sorted_dicts = []
    for k, v in some_dict.items(): 
        if k.isalpha(): 
            sorted_dicts.append({"char": k, "num": v})
    sorted_dicts.sort(key=sort_on, reverse=True)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {book_wc} total words
--------- Character Count -------
          """)
    for pair in sorted_dicts: 
        print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")

# sort_it(my_dict)