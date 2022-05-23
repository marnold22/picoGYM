# Vault-Door-1

## FLAG: picoCTF{}

## Status: Incomplete

Category: Reverse-Engineer

Description: This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

## STEPS

1. > wget "https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java"
2. Inspecting the java file we see this

    ```java
    import java.util.*;

    class VaultDoor1 {
        public static void main(String args[]) {
            VaultDoor1 vaultDoor = new VaultDoor1();
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
        }

        // I came up with a more secure way to check the password without putting
        // the password itself in the source code. I think this is going to be
        // UNHACKABLE!! I hope Dr. Evil agrees...
        //
        // -Minion #8728
        public boolean checkPassword(String password) {
            return password.length() == 32 &&
                password.charAt(0)  == 'd' &&
                password.charAt(29) == '9' &&
                password.charAt(4)  == 'r' &&
                password.charAt(2)  == '5' &&
                password.charAt(23) == 'r' &&
                password.charAt(3)  == 'c' &&
                password.charAt(17) == '4' &&
                password.charAt(1)  == '3' &&
                password.charAt(7)  == 'b' &&
                password.charAt(10) == '_' &&
                password.charAt(5)  == '4' &&
                password.charAt(9)  == '3' &&
                password.charAt(11) == 't' &&
                password.charAt(15) == 'c' &&
                password.charAt(8)  == 'l' &&
                password.charAt(12) == 'H' &&
                password.charAt(20) == 'c' &&
                password.charAt(14) == '_' &&
                password.charAt(6)  == 'm' &&
                password.charAt(24) == '5' &&
                password.charAt(18) == 'r' &&
                password.charAt(13) == '3' &&
                password.charAt(19) == '4' &&
                password.charAt(21) == 'T' &&
                password.charAt(16) == 'H' &&
                password.charAt(27) == '5' &&
                password.charAt(30) == '2' &&
                password.charAt(25) == '_' &&
                password.charAt(22) == '3' &&
                password.charAt(28) == '0' &&
                password.charAt(26) == '7' &&
                password.charAt(31) == 'e';
        }
    }
    ```

3. In here we see a checkpassword() function that checks for a length of 32 charactrers and specific characters at designated positions
4. Using some string magic (ie find and replace we can condense the data to lists for python)
5. Stitching it together we see the password is `d35cr4mbl3_tH3_cH4r4cT3r5_75092e`

    ```text
    0 :'d'
    1 :'3'
    2 :'5'
    3 :'c'
    4 :'r'
    5 :'4'
    6 :'m'
    7 :'b'
    8 :'l'
    9 :'3'
    10:'_'
    11:'t'
    12:'H'
    13:'3'
    14:'_'
    15:'c'
    16:'H'
    17:'4'
    18:'r'
    19:'4'
    20:'c'
    21:'T'
    22:'3'
    23:'r'
    24:'5'
    25:'_'
    26:'7'
    27:'5'
    28:'0'
    29:'9'
    30:'2'
    31:'e'
    ```

6. flag = "picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}"
