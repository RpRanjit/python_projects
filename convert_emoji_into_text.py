import demoji

demoji.download_codes()

text ='''Instead of having to say “that makes me sad,” or “I am in awe!” you can simply reach for ☹️ or 🤩 to do the job for you. Why say “okay, message received” when 👍 will do? What faster way of letting someone know where you are than with ✈️ or 🎡? A perky sparkle can let someone know that you are in a good mood or that you mean light-hearted fun 💫, and ten angry-face emojis in a row can let someone else know that you meant your original message with the rage of a thousand suns 😡😡😡😡😡😡😡😡😡😡.'''
print()
print(demoji.findall(text))
print()
emoji_list = demoji.findall(text)

new_text = text

for emoji, emoji_name in emoji_list.items():
    new_text = new_text.replace(emoji, emoji_name)
print(new_text)    
    