class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Encode each string by adding its length, a colon, and the string
            encoded += str(len(s)) + ":" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the colon that separates the length and the string
            colon_index = s.find(":", i)
            length = int(s[i:colon_index])

            # Move the index to the start of the string
            i = colon_index + 1

            # Extract the string and add it to the result
            decoded.append(s[i:i + length])

            # Move the index to the start of the next length
            i += length

        return decoded
