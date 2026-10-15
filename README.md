# Employee Data Cleaning with Pandas & NumPy

A beginner-friendly data cleaning project in Python. It takes a small, messy employee dataset and cleans it step by step using Pandas and NumPy: removing duplicates, filling missing values, rebuilding emails, reordering columns, and adding a derived column.

## Overview

Real-world data is rarely clean. This project starts with an employee table that has:

- Missing names, departments, salaries, and emails
- A duplicate record (same employee ID appearing twice)
- Invalid ages (e.g. `101`, `-2`)
- A broken email with no username (`@gmail.com`)

The script walks through a practical cleaning workflow and produces a tidy, analysis-ready DataFrame.

## Cleaning Steps

1. **Create the raw dataset** from a Python dictionary and keep an untouched copy (`old`) for comparison.
2. **Drop unnecessary columns**: `S.No` and `Age` (the age data contains invalid values).
3. **Remove the duplicate row** (the repeated employee ID `108`).
4. **Fill missing salaries** with the mean salary of the dataset.
5. **Fill missing departments** with `"IT"`, the most common department.
6. **Rename and reposition the ID**: move `Id` to the first column as `Emp Id`.
7. **Fill missing names** using the part of the email before the `@`.
8. **Rebuild email addresses** as `name@gmail.com`, then drop the original `email` column.
9. **Add a `YOE` column** (years of experience) using `np.where`: salary >= 40000 gives 5, otherwise 2.

## Final Columns

| Emp Id | name | Dept | salary | mail | YOE |
|--------|------|------|--------|------|-----|

## Tech Stack

- Python 3
- Pandas
- NumPy

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Install dependencies
pip install pandas numpy

# Run the script
python main.py
```

If you are using a Jupyter Notebook, paste the code into a cell and the last line (`df`) will display the cleaned table.

## What I Learned

- Handling missing values with `fillna()`
- Dropping rows and columns with `drop()`
- Reordering columns with `pop()` and `insert()`
- Extracting text with `str.split()`
- Creating conditional columns with `np.where()`

## Notes and Limitations

- The `YOE` column is a placeholder rule based on salary, not real experience data.
- Filling salaries with the mean and departments with `"IT"` are simple strategies, suitable for practice but not for production data.
- Emails are rebuilt using a fixed `@gmail.com` domain.

## Future Improvements

- Validate ages and emails with rules instead of dropping columns
- Detect duplicates automatically with `drop_duplicates()`
- Wrap the steps into reusable functions
- Export the cleaned data to CSV or Excel

## License

This project is open source and available under the [MIT License](LICENSE).
