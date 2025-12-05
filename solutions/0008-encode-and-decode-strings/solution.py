class Codec:
    def encode(self, strs):
        # Use a unique delimiter that does not appear in the strings
        delimiter = chr(257)  # Using a character outside the typical ASCII range
        encoded = []
        for s in strs:
            # Append the length of the string followed by the string itself
            encoded.append(f"{len(s)}{delimiter}{s}")
        # Join all encoded strings with the delimiter
        return delimiter.join(encoded)

    def decode(self, s):
        # Use the same delimiter to split the encoded string
        delimiter = chr(257)
        decoded = []
        i = 0
        while i < len(s):
            # Find the next delimiter
            j = s.find(delimiter, i)
            # Extract the length of the string
            length = int(s[i:j])
            # Extract the string based on the length
            decoded.append(s[j + 1:j + 1 + length])
            # Move the index past the current encoded string
            i = j + 1 + length
        return decoded