def analyze_text(text):
    # Your code here   
    length_of_alpha_char = 0
    
    for char in text:
        if char.isalpha() == True:
            length_of_alpha_char += 1
            
    e_count = int(text.count('e')) + int(text.count('E'))
    percent_of_e = (e_count / length_of_alpha_char) * 100
    rounded_percent = "%.2f" % percent_of_e
    return_string = '''The text contains {0} alphabetic characters, of which {1} ({2}%) are 'e'.'''
    
    return return_string.format(length_of_alpha_char, e_count, rounded_percent)
