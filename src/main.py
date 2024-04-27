from textnode import TextNode
def main():
    david = TextNode("xxx", "style", "http://www.google.com")
    radek = TextNode("xxx", "style", "http://www.google.com")
    if david == radek:
        print("success")
    else:
        print("nope")
main()