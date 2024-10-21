def reverseWords( s: str ) -> str:
        w = s.split()
        return " ".join(reversed(w))


s = "the sky is blue"
print(reverseWords(s))