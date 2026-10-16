def func(text="whisper"):
    def whisper(text="whisper"):
        return text.lower() + '...'

    def shout(text="shout"):
        return text.upper() + '!'

    if text == "whisper":
        return whisper
    else:
        return shout


print(func("PPP")("Valeria"))
