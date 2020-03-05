"""

	Remove vowels from a string
	By : Palak Goel
	
"""

def removeVowel(s):
	vowels = ['a','e','i','o','u']
	result = []
	for i in s:
		if i not in vowels:   # Check if character is not a vowel, add it to output string 
			result.append(i)
	
	return(''.join(result))   # To return it as a string, not list
			
def main():
	input_str = "leetcodeisacommunityforcoders"
	output_str = removeVowel(input_str)
	print("The output string is %s" %output_str)

main()