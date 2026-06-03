class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, cipher_text, key):
        num_cols = key
        num_rows = -(-len(cipher_text) // num_cols) 
        num_shaded = (num_cols * num_rows) - len(cipher_text)

        plain_text = [''] * num_rows
        col = 0
        row = 0
        for symbol in cipher_text:
            plain_text[row] += symbol
            row += 1
            if (row == num_rows) or \
               (row == num_rows - 1 and col >= num_cols - num_shaded):
                col += 1
                row = 0
        return ''.join(plain_text)