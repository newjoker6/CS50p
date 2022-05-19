


def convert(emote_text):
    if ":)" in emote_text:
        emote_text = emote_text.replace(":)", "🙂")
    if ":(" in emote_text:
        emote_text = emote_text.replace(":(", "🙁")
    return emote_text

def main():
    text = input("insert text with smiley or frowny face ")
    new_text = convert(text)
    print(new_text)


main()