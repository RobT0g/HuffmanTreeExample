# Project Description
This project uses the Huffman coding algorithm to generate the compressed binary form of a given text.
I tried following a Test Driven Development (TDD) for this project, so make sure to check the testing section!

## How to Run
1. Ensure you have Python installed on your system (version 3.6 or higher).
2. Install the required dependencies by running:
    ```
    bash
    pip install -r reqs.txt
    ```
3. Use the Example folder to get the sample text
    1. Or create a new folder with a text.txt file in it 
4. Make sure you have the folder you want to convert inside of the `if __name__ == '__main__'` clause
    1. You can just instantiate another `HuffmanTree` using `HuffmanTree(folderName, True)`
    2. Note that the second parameter allows you to select whether to map the tree at instantiation or not
    3. Additionally you can also give a third optional argument that specifies whether you are using the strict folder path or not
        1. if you pass `False` (this is the default), the folder path will be set to `f'Examples/{folderPath}'`
        2. if you pass `True`, the folder will be `folderPath`
5. Run the script using the following command:
    ```
    bash
    python huffman.py
    ```

## Expected Results
- If you just instantiate the `HuffmanTree`, nothing happens
- When the tree is mapped you get enable all the other functions to work, such as `HuffmanTree.getHuffmanBinaryString`
    - You can then invoke the method `HuffmanTree.getSummary()` to see a summary of the process. This will show you a count of the chararcters on the original string, as well as the bit counters on both binary strings, the ASCII and Huffman

## Running Tests
To run the test files, follow these steps:

1. Ensure you have `pytest` installed. If not, you can install it using:
    ```bash
    pip install pytest
    ```

2. Run the tests using the following commands:
    ```bash
    pytest test_DataStructures.py
    pytest test_huffman.py
    ```

These commands will execute the test cases defined in the respective files and display the results in the terminal.