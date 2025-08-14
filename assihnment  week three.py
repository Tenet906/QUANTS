# Step 1: Create input.txt with at least five lines of text

with open('input.txt', 'w') as file:
    file.write(input_content)

# Step 2: Read input.txt, process content, and write to output.txt
try:
    # Read the contents
    with open('input.txt', 'r') as input_file:
        text = input_file.read()
    
    # Count words (split by whitespace and filter out empty strings)
    words = [word for word in text.split() if word]
    word_count = len(words)
    
    # Convert text to uppercase
    processed_text = text.upper()
    
    # Write to output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write(f"Processed Text:\n{processed_text}\n\n")
        output_file.write(f"Total Word Count: {word_count}\n")
    
    # Print success message
    print("Success: output.txt has been created with processed text and word count.")

except FileNotFoundError:
    print("Error: input.txt not found.")
except Exception as e:
    print(f"Error: An unexpected error occurred: {e}")
