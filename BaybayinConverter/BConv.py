class TagToBaybayin:
    """
    Converts Tagalog To Baybayin

    Methods:
        convert(text: str) -> str
    
    Static Methods:
        list_to_str(s: list) -> str
    """
    
    def convert(self, text: str) -> str:
        """
        Returns passed text into a Baybayin Format

        Parameters:
            text (str): the string which is to be passed
        
        Returns:
            new_str (text): the newly formatted baybayin string
        """
        toOriginal = []
        split_text = list(text)
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
    def list_to_str(s: list) -> str:
        """
        converts a list to string

        Parameters: 
            s (list): the list to convert to string

        Returns:
            str1 (str): The result string
        """
        str1 = None

        for ele in s:
            str1 += ele

        return str1