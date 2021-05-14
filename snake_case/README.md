snake_case
Since we are learning Python, sometimes it might be useful to convert text from lowerCamelCase to snake_case. The main trick is to find the correct place where to insert an underscore. Let's make a rule that it's right before a capital letter of the next word. If the first letter is capital, convert it to lowercase, but don't insert an underscore before it.

The input format:

Read a word or a phrase written in lowerCamelCase.

The output format:

Print out words in lowercase and separate them by underscores.

Hint


Sample Input:
python

Sample Output:
python


Sample Input:
parselTongue

Sample Output:
parsel_tongue
