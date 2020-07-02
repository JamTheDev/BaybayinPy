class BConv:
    txt = None

    def __init__(self, text):
        self.txt = text

    def convert(self):
        toOriginal = []
        split_text = list(self.txt)
        for i in range(0, len(split_text) - 1):
            current = split_text[i]
            next = split_text[i + 1]
            if current.lower() == "a" or current.lower() == "e" or current.lower() == "i" or current.lower() == "o" or current.lower() == "u" or current.isspace():

                if next.lower() == "a" or next.lower() == "e" or next.lower() == "i" or next.lower() == "o" or next.lower() == "u":
                    toOriginal.append(current + "+")
                else:
                    toOriginal.append(current)
            else:
                toOriginal.append(current + "+")

        if next.lower() == "a" or next.lower() == "e" or next.lower() == "i" or next.lower() == "o" or next.lower() == "u":
            toOriginal.append(next)
        else:
            toOriginal.append(next + "+")

        new_str = " "

        for item in toOriginal:
            new_str += item

        return new_str

    @staticmethod
    def listToString(s):
        str1 = None

        for ele in s:
            str1 += ele

        return str1
