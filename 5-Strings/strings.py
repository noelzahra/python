# Various string

""" This a docstring
    Here are various string formats
"""
sentence = "Developing with python"
print(type(sentence))


string1 = 'Test string'
string2 = "Standard string"
string3 = 'A statement within a string "go big" he said'
string4 = "He said, \"What time is it?\""

string_array = [string1, string2, string3, string4]

for string in string_array:
    print(f"string variety: {string} has len {len(string)}")
    
long_string = """The format_spec field contains a specification of how the value should be presented, including such details as field width, alignment, padding, decimal precision and so on."""
print (long_string)

paragraph = """\nTemplate strings provide simpler string substitutions as described in PEP 292.\n A primary use case for template strings is for internationalization (i18n)\nsince in thatcontext, the simpler syntax and\n functionality makes it easier to translate than other built-in string\n formatting facilities in Python."""

print(paragraph)
