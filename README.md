# Find your friends Date of Birth

#### Find the DOB and CGPA of anyone with just using their USN

### Link to the website: [DOB Finder](https://dob-finder-sis.streamlit.app/)

## How to use

1. Enter the USN of the person
2. Click on the "Find DOB" button
3. The DOB of the person will be displayed

## How it works

1. The USN is sent to the server
2. Then it takes the year from the USN and subtracts 18 from it to get the year of birth
3. Then it Brute-forces the month and date in that whole year till it finds the correct DOB
4. If the year fails to find the DOB, it tries the previous year and the next year
5. If the DOB is not found, it displays an error message
6. If the DOB is found, it displays the Name and DOB of the person

## How to run the code

1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`
3. Run the code using `streamlit run app.py`
4. Open the link in the terminal in your browser

## How to contribute

1. Fork the repository
2. Clone the repository
3. Make the changes
4. Commit the changes
5. Push the changes
6. Create a pull request
7. Wait for the pull request to be merged
8. Celebrate
9. Repeat

## Contributors

- [Shravan](https://myselfshravan.github.io)
- [Amith](https://github.com/amith225)
