"""
The function compares two strings to see if the second string is a substring of the first string.
The compare_string function uses a nested loop to compare each character in the two strings.
It first loops through every possible substring of str1 that is the same length as str2, and then loops through each character in the substring and compares it with the corresponding character in str2.
If all the characters match, the function returns True.
If no matching substring is found, the function returns False.
In the example, the function is called to check whether "Sajjad" is a substring of "SajjadRahmani".
"""


def compare_string(str1, str2):
    # Loop through every possible substring of str1 that is the same length as str2
    for i in range(len(str1) - len(str2) + 1):
        # Compare each character in the substring with the corresponding character in str2
        for k in range(len(str2)):
            ch1 = str1[i + k]
            ch2 = str2[k]
            if ch1 != ch2:
                # If the characters don't match, break out of the inner loop
                break
        else:
            # If the inner loop completes without breaking, the substrings match
            return True
    # If no matching substring was found, return False
    return False


# Test the function
print(compare_string("SajjadRahmani", "Sajjad"))
