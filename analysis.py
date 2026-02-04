import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("iran_hospital_dataset_1000.csv")
print(df.head(10))
print("Shape of dataset:", df.shape)
print("Columns:", df.columns)
print(df.info())
print("\nDATA TYPES:")
print(df.dtypes)
print("\nMISSING VALUES PER COLUMN:")
print(df.isna().sum())
print("\nTOTAL MISSING VALUES IN DATASET:", df.isna().sum().sum())
print("\nDUPLICATE ROWS:", df.duplicated().sum())
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\nCLEANED COLUMN NAMES:")
print(df.columns)
print("\nTOP 10 VISIT REASONS:")
print(df["visit_reason"].value_counts().head(10))
print(df["city"].value_counts().head(10))
print(df["age"].mode())
print(df["age"].value_counts().head(10))
print(df["gender"].value_counts())
bins = [0, 17, 34, 49, 64, 120]
labels = ["0-17", "18-34", "35-49", "50-64", "65+"]

df["age_band"] = pd.cut(df["age"], bins=bins, labels=labels)

print("\nAGE BAND DISTRIBUTION:")
print(df["age_band"].value_counts())
top_cities = df["city"].value_counts().head(10)

top_cities.plot(kind="bar")
plt.title("Top 10 Cities by Number of Patients")
plt.xlabel("City")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
top_reasons = df["visit_reason"].value_counts().head(10)

top_reasons.plot(kind="bar")
plt.title("Top 10 Visit Reasons")
plt.xlabel("Visit Reason")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
df["age_band"].value_counts().sort_index().plot(kind="bar")
plt.title("Patient Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.show()
print("\nAGE GROUP BY DEPARTMENT:")
age_dept = pd.crosstab(df["department"], df["age_band"])
print(age_dept)
age_disease = pd.crosstab(df["age_band"], df["visit_reason"])
print(age_disease)
age_disease_percent = pd.crosstab(df["age_band"], df["visit_reason"], normalize="index") * 100
print(age_disease_percent)
top_by_age = age_disease.idxmax(axis=1)
print("Most common disease in each age group:\n", top_by_age)
# Get the count of the most common disease for each age band
top_counts = age_disease.max(axis=1)

# Combine names and counts into one table
visual_df = pd.DataFrame({
    "Most_Common_Disease": top_by_age,
    "Patient_Count": top_counts
})

print("\nTable for visualization:\n", visual_df)


plt.figure(figsize=(8,5))

plt.bar(visual_df.index.astype(str), visual_df["Patient_Count"])

plt.title("Most Common Disease in Each Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")

for i, (disease, count) in enumerate(zip(visual_df["Most_Common_Disease"], visual_df["Patient_Count"])):
    plt.text(i, count + 1, disease, ha="center", fontsize=9)

plt.tight_layout()
plt.show()
gender_disease = pd.crosstab(df["visit_reason"], df["gender"])

print("\nDISEASE BY GENDER (COUNTS):")
print(gender_disease)
gender_disease_percent = pd.crosstab(
    df["visit_reason"], 
    df["gender"], 
    normalize="index"
) * 100

print("\nDISEASE BY GENDER (PERCENTAGES):")
print(gender_disease_percent)
gender_disease_percent.plot(kind="bar", stacked=True, figsize=(12,6))

plt.title("Gender Distribution by Disease")
plt.xlabel("Visit Reason")
plt.ylabel("Percentage")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()

