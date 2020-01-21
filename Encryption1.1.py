class code:
    #(working!!)
    def __init__(self, message, key):
        self.m = message
        self.k = key
        self.p = self.key_prep()
        self.g = self.grid()
        self.e = self.encrypt()
        self.d = self.decrypt()
        self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '."

    
    def key_prep(self):
        """returns a string containing the repeated key until
        it is the same length as the message"""
        key_string = ""
        while len(key_string) < len(self.m):
            for c in self.k:
                if len(key_string) < len(self.m):
                    key_string += c
        return key_string

    def encrypt(self):
        """encrypts the message"""
        cypher = ""
        for i in range(0, len(self.m)):
            cypher += self.retrieve_char(self.m[i], self.p[i])
        return cypher

    def retrieve_char(self, m_char, k_char):
        #gets the co-ordinates i, j of the char to be returned
        column_list = []
        i = self.g[0].index(ord(m_char))
        for n in range(0, len(self.g)):
            column_list += [self.g[n][0]]
        j = column_list.index(ord(k_char))
        #uses the co-ordinates to locate and return the char
        return chr(self.g[j][i])

    def decrypt(self):
        decrypted_message = ""
        column_list = []
        top_row = []
        #makes the top row of the grid
        for q in range(32, 127):
            top_row += [q]
        #makes the first column of the grid
        for n in range(0, len(self.g)):
            column_list += [self.g[n][0]]
        #gets the position of the each encrypted character for the row
        #starting with the corresponding character in the key
        for i in range(0, len(self.m)):
            decrypted_message += chr(top_row[self.g[column_list.index(ord(self.p[i]))].index(ord(self.m[i]))])
        return decrypted_message
        
        
