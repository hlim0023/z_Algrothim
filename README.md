# z_Algrothim
This question consists of two functions “z_Algorithm(pat, text)” and “pattern_Matching(text, pat)”. The pattern_Matching(text, pat) function is the main function that deals with one transposition error using the z_Algorithm(pat, text) function.

# Pattern Matching with Transposition Error Handling

This project implements a pattern-matching algorithm that can detect a pattern within a text, even if a single character transposition error exists. It consists of two primary functions:
- `z_Algorithm(pat, text)`: Constructs a Z array to assist in pattern matching.
- `pattern_Matching(text, pat)`: The main function that leverages `z_Algorithm(pat, text)` to handle pattern matching, including transposition errors.

## Approach

The algorithm uses a list-based approach to check for potential transpositions by processing the text both forwards and backwards:
1. `z`: The Z array for the forward direction.
2. `suffix`: The Z array for the reversed direction.

### Main Logic

1. **Case 1: Exact Match**
   - If any position in `z` has a length equal to the pattern length, it indicates an exact match, and the position is saved.

2. **Case 2: Single Transposition Match**
   - Allows one pair of adjacent characters in the text to be transposed.
   - Compares pairs of characters that differ by one position. For instance, if `text[X] == pattern[X]` and `text[Y] == pattern[Y]`, they match, even if transposed.
   - The condition is checked using `m - z[i] - 2` compared to `suffix[i + m - 1]`. If they match, and the transposed characters align, it is considered a single transposition match.

This approach reduces the number of comparisons required, thereby optimizing performance.

### Z Algorithm

The Z algorithm is used to construct an array (`z`) that efficiently captures the length of the longest prefix of the pattern. The Z array allows the algorithm to perform pattern matching by iterating through the pattern and comparing segments with the text.

- For efficiency, the algorithm maintains a window (`L`, `R`) for the current rightmost match. For any index within this window, it reuses the previously computed Z values. If outside the window, it performs a naive comparison.

## Complexity Analysis

### Time Complexity
The worst-case time complexity is \( O(m + n) \):
- **Z Algorithm**: \( O(m + n) \)
- **String Reversal and List Slicing**: \( O(m) + O(n) \)
- **Looping Through Arrays**: \( O(n) \)

### Space Complexity
The space complexity is \( O(m + n) \):
- **Two Z Arrays**: \( O(n) \)
- **Suffix Arrays**: \( O(m) + O(n) \)
  
Thus, the combined space complexity is \( O(m + n) \).

---

## Usage

1. **Function Definitions**
   - `z_Algorithm(pat, text)`: Constructs the Z array for a given pattern and text.
   - `pattern_Matching(text, pat)`: Uses the Z array to detect patterns in the text, allowing for a single transposition error.

2. **Running the Code**
   - Define your pattern and text strings.
   - Call `pattern_Matching(text, pat)` to find matches with the pattern in the text.

## Example

```python
pattern = "abc"
text = "cabdcabc"
matches = pattern_Matching(text, pattern)
print(matches)  # Output will include exact and transposition matches.

