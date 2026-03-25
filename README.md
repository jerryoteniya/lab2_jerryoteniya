# Social Media Feed Analyzer Project

##  Project Overview

The **Social Media Feed Analyzer** is a data analysis project that processes a Twitter dataset to extract insights about user activity.

The main goal of this project is to identify the **Top 5 Most Active Users** based on how frequently they appear in the dataset.

This project combines:

* **Data processing (CSV handling)**
* **Python scripting (data analysis)**
* **Bash scripting (automation and command-line processing)**

---

##  Objectives

* Analyze a dataset of tweets
* Extract meaningful insights from raw data
* Identify the most active users
* Automate the analysis using scripts
* Practice working with real-world messy data

---

##  Project Structure

```id="ybo8dd"
lab2_jerryoteniya/
│── twitter_dataset.csv        # Raw dataset
│── feed-analyzer.sh          # Bash automation script
│── feed-analyzer.py          # Python analysis script (optional/advanced)
│── top_users_*.txt           # Generated output files
│── README.md                 # Project documentation
```

---

##  Technologies Used

* **Bash (Shell Scripting)** → Automation and command chaining
* **Python (Optional)** → Robust CSV parsing and data analysis
* **CSV Dataset** → Input data source

---

##  How to Run the Project

### 🔹 Option 1: Using Bash (Primary Requirement)

1. Open your terminal (Git Bash / WSL / Linux)
2. Navigate to your project folder:

```bash id="ml83g6"
cd ~/OneDrive/Desktop/lab2_jerryoteniya
```

3. Run the script:

```bash id="m6r2az"
bash feed-analyzer.sh
```

 The script will:

* Automatically detect the CSV file
* Process the data
* Display the Top 5 most active users
* Save results in a file

---

### 🔹 Option 2: Using Python (Advanced / Backup)

```bash id="htx7n0"
python feed-analyzer.py
```

This method is more reliable for complex CSV files with:

* Quotes
* Commas inside text
* Multi-line fields

---

##  Example Output

```id="q7vts2"
Top 5 Most Active Users:
  25 julie81
  22 richardhester
  20 williamsjoseph
  18 danielsmary
  15 carlwarren

Saved in top_users_2026-03-24_17-30-00.txt
```

---

##  How It Works (Bash Version)

The Bash script processes the dataset using a pipeline of commands:

### 1. Fix Dataset Formatting

```bash id="whgco0"
tr '\n' ' ' | sed 's/Tweet_ID/\nTweet_ID/g'
```

* Repairs rows broken by multi-line text fields

---

### 2. Extract Username Column

```bash id="jygxk6"
cut -d',' -f2
```

* Selects the second column (Username)

---

### 3. Remove Header Row

```bash id="16o3fc"
tail -n +2
```

---

### 4. Sort Usernames

```bash id="t6i6mx"
sort
```

---

### 5. Count Occurrences

```bash id="tw9m3d"
uniq -c
```

---

### 6. Rank by Activity

```bash id="e3b3my"
sort -nr
```

---

### 7. Display Top 5

```bash id="b7nb1o"
head -5
```

---

##  How It Works (Python Version)

* Reads CSV using `csv.DictReader`
* Extracts the `Username` field
* Counts occurrences using `collections.Counter`
* Sorts and retrieves top 5 users
* Saves results to a file

---

##  Key Concepts Learned

* Shell scripting and automation
* Command pipelines (`|`)
* Data extraction from CSV files
* Sorting and counting data efficiently
* Handling messy real-world datasets
* Differences between Bash and Python for data processing

---

##  Challenges Faced

* CSV file contained:

  * Commas inside text fields
  * Quoted strings
  * Multi-line text

These issues required additional preprocessing to ensure accurate results using Bash.

---

##  Conclusion

This project demonstrates how to:

* Analyze real-world datasets
* Automate workflows using Bash
* Combine multiple tools to solve data problems

It highlights the strengths of both **Bash (speed and simplicity)** and **Python (robust data handling)**.

---

##  Future Improvements

* Add support for more analytics (likes, retweets, etc.)
* Build a simple dashboard for visualization
* Improve CSV parsing for edge cases
* Convert into a full web-based analytics tool

---
