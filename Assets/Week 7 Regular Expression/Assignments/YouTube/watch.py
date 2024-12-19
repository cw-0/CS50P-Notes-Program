import re
import sys




def main():
    print(parse(input("HTML: ").strip()))



def parse(s):
    match = re.search(r"(http|https){1}(://){1}(www\.)?(youtube\.com/embed/){1}(?P<id>[a-zA-Z0-9]+){1}", s, flags=re.I)
    if match:
        id = match.group("id")
        url = "https://youtu.be/" + id
        return url
    else:
        return "Invalid URL"


if __name__ == "__main__":
    main()
