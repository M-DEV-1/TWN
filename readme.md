
# TempoWordNet Processing Notebook

This Jupyter Notebook is designed to process sentences using TempoWordNet, a lexical resource. It reads a dataset, processes input sentences to calculate temporal probabilities, and outputs the results to a text file.

## Files
- **TempoWordNet Dataset:** This notebook assumes a file located at `./TempoWordNet/TempoWnL_1.0.txt`. Ensure this file is present before running the notebook.
- **Output File:** Processed results are saved to `processed_results.txt`.

## Requirements
Ensure that these libraries are installed in your environment. You can install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Load the Dataset:**
   The dataset is loaded using the `read_tempowordnet_manually()` function, which reads and processes the TempoWordNet file.

2. **Input a Sentence:**
   You will be prompted to input a sentence. This sentence will be processed to calculate temporal probabilities.

3. **View Results:**
   The processed results are appended to `processed_results.txt`. If the sentence does not contain any words found in TempoWordNet, the file may not show relevant results.

## Future Improvements

- **Error Handling:** Add more robust error handling and validation to ensure that the file paths exist, inputs are valid, and the processing logic is resilient.
- **Logging:** Implement logging to track the execution flow and identify any issues.
- **Refactoring:** Clean up the code by removing outdated comments and refactoring the functions for better readability and maintainability.
- **Testing:** Add unit tests to verify the functionality of each component.

## License

This project is open-source and available under the MIT License.
