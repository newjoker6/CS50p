def convert(time):
    if "am" in time.lower() or "pm" in time.lower():
        time = time.lower().replace("am", "")
        time = time.lower().replace("pm", "")
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute) / 60

    return hour + minute

def main():
    time = input("What is the time? ")
    result = convert(time)
    print(result)


if __name__ == "__main__":
    main()