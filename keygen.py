"""
public class Vault {
    private static boolean checkPassword(String password) {
        if (password.length() != 32)
            return false;

        char[] buffer = new char[32];
        int i;
        for (i = 0; i < 8; i++) {
            buffer[i] = password.charAt(i);
        }

        for (; i < 16; i++) {
            buffer[i] = password.charAt(23 - i);
        }
        
        for (; i < 32; i += 2) {
            buffer[i] = password.charAt(46 - i);
        }

        for (i = 31; i >= 17; i -= 2) {
            buffer[i] = password.charAt(i);
        }

        return new String(buffer).equals("jU5t_a_sna_31pm17ga45_u_4_mbrf4c");
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: ./vault [password]");
        }

        System.out.println(checkPassword(args[0]));
    }
}
"""

import retromutator

def transform_password(in_seq, out_seq):
    for i in range(8):
        out_seq[i] = in_seq[i]
    
    for i in range(8, 16):
        out_seq[i] = in_seq[23 - i]
    
    for i in range(16, 32, 2):
        out_seq[i] = in_seq[46 - i]
    
    for i in range(31, 16, -2):
        out_seq[i] = in_seq[i]

if __name__ == "__main__":
    print(retromutator.find(transform_password, "jU5t_a_sna_31pm17ga45_u_4_mbrf4c"))