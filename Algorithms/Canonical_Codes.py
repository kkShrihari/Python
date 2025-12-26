# ==================================================
# Canonical Code Implementation
# ==================================================

class CanonicalCode:
    """
    Provides functionality to:
    - Decode a numeric value into a DNA k-mer
    - Check whether the value is a canonical code
    """

    # DNA base → 2-bit encoding
    Encode_dict = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}

    # 2-bit block → DNA base decoding
    Decode_dict = {"00": "A", "01": "C", "10": "G", "11": "T"}

    # Complement mapping for DNA bases
    rev_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, val: int = 0, k: int = 0):
        """
        Initialize the CanonicalCode object.

        Parameters:
        val (int): Encoded integer value
        k (int): Length of the k-mer
        """
        self.val = val
        self.k = k

    def IsCanoncial(self) -> tuple[bool, str]:
        """
        Check whether the stored value is a canonical code.

        Returns:
        tuple(bool, str):
            - True/False indicating canonical status
            - Corresponding decoded k-mer
        """

        # Convert integer value to binary (2k bits)
        bits_ = self.k * 2
        bit_binary = format(self.val, f'0{bits_}b')

        # Decode binary string into DNA k-mer
        result_str = ""
        for i in range(0, len(bit_binary), 2):
            block = bit_binary[i:i + 2]
            if block in self.Decode_dict:
                result_str += self.Decode_dict[block]

        # Compute canonical encoding
        canonical_val = self.KmerEncode(result_str)

        # Compare original value with canonical value
        if self.val == canonical_val:
            return True, result_str
        else:
            return False, result_str

    def KmerEncode(self, input_: str) -> int:
        """
        Encode a k-mer and its reverse complement,
        and return the canonical (minimum) encoding.

        Parameters:
        input_ (str): DNA k-mer

        Returns:
        int: Canonical encoding value
        """

        input_list = []

        # Add original k-mer
        input_list.append(input_)

        # Compute reverse complement
        rc = ""
        for b in reversed(input_):
            rc += self.rev_dict[b]
        input_list.append(rc)

        # Convert both sequences to binary strings
        binary_list = []
        for seq in input_list:
            val = ""
            for N in seq:
                if N in self.Encode_dict:
                    val += format(self.Encode_dict[N], "02b")
            binary_list.append(val)

        # Convert binary strings to decimal values
        dec_list = []
        for seq in binary_list:
            val, no = 0, 0
            for N in reversed(seq):
                val += int(N) * (2 ** no)
                no += 1
            dec_list.append(val)

        # Return canonical (minimum) encoding
        return min(dec_list)


# --------------------------------------------------
# Example usage of CanonicalCode
# --------------------------------------------------

cc = CanonicalCode()
print(cc.KmerEncode("ATTCGCG"))

cc = CanonicalCode(15, 4)
print(cc.IsCanoncial())

cc = CanonicalCode(109, 5)
print(cc.IsCanoncial())
