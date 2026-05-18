# 📺 Extracting TV Data Insights: Super Bowl Analysis

## 📌 Project Overview

The **Super Bowl** is more than just a football championship—it is one of the biggest entertainment and media events globally. From dramatic games and record-breaking TV audiences to iconic halftime performances and multimillion-dollar advertisements, the event offers rich data for analysis.

This project explores **52 Super Bowls (through 2018)** using datasets scraped and refined from Wikipedia to uncover trends in:

* 📈 TV viewership growth
* 🏈 Game competitiveness
* 🎤 Halftime show performances
* 📺 Entertainment and advertising impact

Using **Python** and **Pandas**, the analysis extracts meaningful insights from historical Super Bowl data.

---

## 🎯 Project Objectives

This analysis aims to answer key questions such as:

* Has Super Bowl TV viewership increased over time?
* How common are extremely one-sided games?
* Which halftime performer delivered the most songs?
* What entertainment and sporting patterns emerge from the data?

---

## 📂 Dataset Description

The project uses **three datasets**.

### 1. halftime_musicians.csv

Contains information about Super Bowl halftime performers.

| Column     | Description                |
| ---------- | -------------------------- |
| super_bowl | Super Bowl edition number  |
| musician   | Performer or musical group |
| num_songs  | Number of songs performed  |

### 2. super_bowls.csv

Contains game-related information.

Key fields include:

* Date
* Stadium
* Winning team
* Losing team
* Winning points
* Losing points
* `difference_pts` (score margin)

### 3. tv.csv

Contains television and advertising statistics.

Includes:

* Average US viewers
* Household ratings
* Ad costs

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Matplotlib**

---

## ⚙️ Project Workflow

### Step 1: Import Libraries

```python
import pandas as pd
from matplotlib import pyplot as plt
```

### Step 2: Load Datasets

```python
super_bowls = pd.read_csv("datasets/super_bowls.csv")
tv = pd.read_csv("datasets/tv.csv")
halftime_musicians = pd.read_csv("datasets/halftime_musicians.csv")
```

### Step 3: Merge and Prepare Data

```python
viewership = pd.merge(super_bowls, tv, on='super_bowl')

viewership['date'] = pd.to_datetime(viewership['date'])

viewership = viewership.sort_values('date')
```

### Step 4: Perform Analysis

The project investigates:

* Viewership trends
* Game score differences
* Halftime performance records

---

## 🔍 Key Insights

### 📈 1. Super Bowl Viewership Increased Over Time

Analysis confirms that average US viewership generally increased over the years.

```python
viewership_increased = True
```

### Insight

The Super Bowl evolved from a sporting event into a **mass entertainment and advertising phenomenon**, attracting increasingly larger audiences.

---

### 🏈 2. Blowouts Were Rare

Games decided by more than **40 points** were extremely uncommon.

```python
difference = 1
```

### Insight

Out of 52 Super Bowls analyzed, **only one game** had a point difference greater than 40.

This suggests that:

* Most Super Bowls remained reasonably competitive
* Extreme dominance was rare
* Competitive balance likely contributed to sustained audience interest

---

### 🎤 3. Most Songs Performed at Halftime

The performer with the highest number of songs was:

```python
Justin Timberlake
```

### Insight

Halftime performances are major entertainment spectacles.

**Justin Timberlake** delivered the largest song count among performers in the dataset, highlighting how halftime shows increasingly function as full-scale music productions rather than short intermissions.

---

## 📊 Summary of Findings

| Question                           | Result            |
| ---------------------------------- | ----------------- |
| Did viewership increase over time? | ✅ Yes             |
| Number of 40+ point blowouts       | 1                 |
| Performer with most songs          | Justin Timberlake |

---

## 💡 Business & Entertainment Insights

This analysis reveals several broader patterns:

### Media Growth

The steady rise in TV audiences demonstrates the Super Bowl's expanding media power and cultural relevance.

### Competitive Sports Matter

Close games help sustain audience engagement and preserve event prestige.

### Entertainment Drives Attention

Halftime performances contribute significantly to viewer experience and overall event popularity.

---

## 🚀 Future Improvements

Possible extensions include:

* Visualizing TV ratings trends
* Exploring advertising cost inflation
* Analyzing team dominance across eras
* Studying halftime performer popularity
* Building an interactive dashboard using **Power BI** or **Plotly**

---

## 📁 Repository Structure

```text
├── datasets/
│   ├── super_bowls.csv
│   ├── tv.csv
│   └── halftime_musicians.csv
│
├── notebook.py
├── README.md
```

---

## 📚 Conclusion

The Super Bowl represents a unique intersection of **sports, entertainment, and media economics**.

Through data analysis, this project shows that:

* Viewership consistently expanded
* One-sided games were rare
* Halftime entertainment became increasingly significant

The findings reinforce how data can uncover trends hidden behind one of the world's most watched annual events.

