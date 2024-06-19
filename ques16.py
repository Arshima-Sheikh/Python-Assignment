    def character_frequency(string):
      frequency = {}
      for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
   print(character_frequency("Hello")
