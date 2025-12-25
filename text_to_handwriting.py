import pywhatkit as pw


txt = '''Python was created in the early 1990s by Guido van Rossum at Stichting Mathematisch 
        Centrum in the Netherlands as a successor of a language called ABC. Guido remains Python’s principal author, although it includes many contributions from others.
      '''


# pw.text_to_handwrirting(var_name,filename/ default= "pywhat.png", for color)
pw.text_to_handwriting(txt, "converted.png", [0, 0, 255])
print("Text is successfully converted.")