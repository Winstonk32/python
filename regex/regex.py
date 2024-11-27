#Question5
import re
pattern = "Mr"
replacement = "Ms"
text = "Mr Smith never wanted to leave"
substituted_text = re.sub(pattern, replacement, text)
print("Substituted text:", substituted_text)


#Question 1
import re
pattern = "a"
text = "Lebron James is better than Micheal Jordan!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))




#Question 4
import re
text = "Contact us at winstonkigonya@gmail.com or late@hotmail.com"
pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
emails = re.findall(pattern, text)
print(emails)
