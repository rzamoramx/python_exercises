
def longest_substring(digits):
    max_substr = ""
    current_substr = digits[0]

    for i in range(1, len(digits)):
        print(f"current_substr: {current_substr}, max_substr: {max_substr}")
        if (int(digits[i]) % 2 == 0 and int(digits[i - 1]) % 2 != 0) or (int(digits[i]) % 2 != 0 and int(digits[i - 1]) % 2 == 0):
            current_substr += digits[i]
        else:
            if len(current_substr) > len(max_substr):
                max_substr = current_substr
            current_substr = digits[i]

    if len(current_substr) > len(max_substr):
        max_substr = current_substr

    return max_substr

# should be "272163254"
print(longest_substring("225424272163254474441338664823"))
