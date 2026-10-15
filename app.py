
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="EduPro Learner Analysis",
    page_icon="📚",
    layout="wide"
)

sns.set_theme(style="whitegrid")

st.title("EduPro Learner Demographics & Enrollment Analysis")
st.write(
    "Explore learner demographics, course preferences, "
    "and enrollment behavior."
)

# --------------------------------------------------
# 2. LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("data/edupro_dashboard_data.csv")

    data["TransactionDate"] = pd.to_datetime(
        data["TransactionDate"], errors="coerce"
    )

    data["Age"] = pd.to_numeric(data["Age"], errors="coerce")

    return data


try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Dataset not found. Check that "
        "data/edupro_dashboard_data.csv exists."
    )
    st.stop()

required_columns = [
    "TransactionID", "UserID", "CourseID", "Age", "AgeGroup",
    "Gender", "CourseCategory", "CourseType", "CourseLevel",
    "TransactionDate"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()

# Remove rows missing essential analysis fields
df = df.dropna(
    subset=[
        "TransactionID", "UserID", "CourseID",
        "AgeGroup", "Gender", "CourseCategory",
        "CourseType", "CourseLevel"
    ]
).copy()

if df.empty:
    st.warning("No valid enrollment records are available.")
    st.stop()

# --------------------------------------------------
# 3. SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.title("Dashboard Filters")

age_options = df["AgeGroup"].dropna().unique().tolist()
gender_options = sorted(df["Gender"].dropna().unique())
category_options = sorted(df["CourseCategory"].dropna().unique())
level_options = sorted(df["CourseLevel"].dropna().unique())

# Keep age bands in the intended order
age_order = ["Under 18", "18–25", "26–35", "36–45", "45+"]

age_options = sorted(
    age_options,
    key=lambda x: age_order.index(x) if x in age_order else len(age_order)
)

selected_age = st.sidebar.multiselect(
    "Age Group",
    options=age_options,
    default=age_options
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=gender_options,
    default=gender_options
)

selected_category = st.sidebar.multiselect(
    "Course Category",
    options=category_options,
    default=category_options
)

selected_level = st.sidebar.multiselect(
    "Course Level",
    options=level_options,
    default=level_options
)

# --------------------------------------------------
# 4. FILTER DATA
# --------------------------------------------------

filtered_df = df[
    df["AgeGroup"].isin(selected_age)
    & df["Gender"].isin(selected_gender)
    & df["CourseCategory"].isin(selected_category)
    & df["CourseLevel"].isin(selected_level)
].copy()

if filtered_df.empty:
    st.warning("No enrollments match the selected filters.")
    st.stop()

# --------------------------------------------------
# 5. LEARNER DEMOGRAPHIC OVERVIEW
# --------------------------------------------------

st.header("Learner Demographic Overview")

total_enrollments = len(filtered_df)
unique_learners = filtered_df["UserID"].nunique()

courses_per_learner = filtered_df.groupby("UserID").size()

average_courses = (
    courses_per_learner.mean()
    if not courses_per_learner.empty else 0
)

col1, col2, col3 = st.columns(3)

col1.metric("Unique Learners", f"{unique_learners:,}")
col2.metric("Total Enrollments", f"{total_enrollments:,}")
col3.metric("Average Courses per Learner", f"{average_courses:.2f}")

# Gender participation among unique learners
st.subheader("Gender Participation")

unique_gender = filtered_df[
    ["UserID", "Gender"]
].drop_duplicates()

gender_summary = (
    unique_gender["Gender"]
    .value_counts()
    .rename_axis("Gender")
    .reset_index(name="Learners")
)

gender_summary["Percentage"] = (
    gender_summary["Learners"]
    / gender_summary["Learners"].sum()
    * 100
).round(2)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(gender_summary, use_container_width=True, hide_index=True)

with col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=gender_summary,
        x="Gender",
        y="Percentage",
        ax=ax
    )
    ax.set_title("Unique Learners by Gender")
    ax.set_ylabel("Learners (%)")
    ax.set_xlabel("Gender")
    ax.set_ylim(0, 100)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# --------------------------------------------------
# 6. AGE-WISE ENROLLMENT ANALYSIS
# --------------------------------------------------

st.header("Age-Wise Enrollment Analysis")

age_enrollment = (
    filtered_df.groupby("AgeGroup", observed=True)
    .size()
    .reindex(selected_age, fill_value=0)
    .rename("Enrollments")
    .reset_index()
)

age_enrollment.columns = ["AgeGroup", "Enrollments"]

age_enrollment["Percentage"] = (
    age_enrollment["Enrollments"]
    / age_enrollment["Enrollments"].sum()
    * 100
).round(2)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Enrollments by Age Group")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        data=age_enrollment,
        x="AgeGroup",
        y="Enrollments",
        ax=ax
    )
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Enrollments")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("Enrollment Share by Age Group")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        data=age_enrollment,
        x="AgeGroup",
        y="Percentage",
        ax=ax
    )
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Enrollments (%)")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.dataframe(age_enrollment, use_container_width=True, hide_index=True)

# --------------------------------------------------
# 7. COURSE CATEGORY POPULARITY
# --------------------------------------------------

st.header("Course Category Popularity")

category_summary = (
    filtered_df.groupby("CourseCategory")
    .size()
    .sort_values(ascending=False)
    .rename("Enrollments")
    .reset_index()
)

category_summary["Percentage"] = (
    category_summary["Enrollments"]
    / category_summary["Enrollments"].sum()
    * 100
).round(2)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    data=category_summary,
    x="Enrollments",
    y="CourseCategory",
    ax=ax
)
ax.set_title("Enrollments by Course Category")
ax.set_xlabel("Enrollments")
ax.set_ylabel("Course Category")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.dataframe(category_summary, use_container_width=True, hide_index=True)

# --------------------------------------------------
# 8. COURSE TYPE AND COURSE LEVEL
# --------------------------------------------------

st.header("Course Type and Level Preferences")

col1, col2 = st.columns(2)

type_summary = (
    filtered_df.groupby("CourseType")
    .size()
    .rename("Enrollments")
    .reset_index()
)

type_summary["Percentage"] = (
    type_summary["Enrollments"]
    / type_summary["Enrollments"].sum()
    * 100
).round(2)

level_summary = (
    filtered_df.groupby("CourseLevel")
    .size()
    .rename("Enrollments")
    .reset_index()
)

level_summary["Percentage"] = (
    level_summary["Enrollments"]
    / level_summary["Enrollments"].sum()
    * 100
).round(2)

with col1:
    st.subheader("Enrollments by Course Type")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=type_summary,
        x="CourseType",
        y="Enrollments",
        ax=ax
    )
    ax.set_xlabel("Course Type")
    ax.set_ylabel("Enrollments")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with col2:
    st.subheader("Enrollments by Course Level")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(
        data=level_summary,
        x="CourseLevel",
        y="Enrollments",
        ax=ax
    )
    ax.set_xlabel("Course Level")
    ax.set_ylabel("Enrollments")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# --------------------------------------------------
# 9. GENDER VS COURSE CATEGORY
# --------------------------------------------------

st.header("Gender-Based Course Preferences")

gender_category = (
    filtered_df.groupby(["CourseCategory", "Gender"])
    .size()
    .reset_index(name="Enrollments")
)

fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(
    data=gender_category,
    x="CourseCategory",
    y="Enrollments",
    hue="Gender",
    ax=ax
)
ax.set_title("Course Category Enrollments by Gender")
ax.set_xlabel("Course Category")
ax.set_ylabel("Enrollments")
plt.setp(ax.get_xticklabels(), rotation=40, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# 10. GENDER VS COURSE LEVEL
# --------------------------------------------------

st.subheader("Course Level Enrollments by Gender")

gender_level = (
    filtered_df.groupby(["CourseLevel", "Gender"])
    .size()
    .reset_index(name="Enrollments")
)

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    data=gender_level,
    x="CourseLevel",
    y="Enrollments",
    hue="Gender",
    ax=ax
)
ax.set_xlabel("Course Level")
ax.set_ylabel("Enrollments")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# 11. AGE GROUP VS COURSE CATEGORY
# --------------------------------------------------

st.header("Age Group and Course Preferences")

age_category = pd.crosstab(
    filtered_df["AgeGroup"],
    filtered_df["CourseCategory"]
)

# Preserve the defined age order
age_category = age_category.reindex(
    [age for age in age_options if age in age_category.index]
)

fig, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(
    age_category,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=ax
)
ax.set_title("Enrollment by Age Group and Course Category")
ax.set_xlabel("Course Category")
ax.set_ylabel("Age Group")
plt.xticks(rotation=40, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# 12. AGE GROUP VS COURSE LEVEL
# --------------------------------------------------

st.subheader("Course Level Enrollments by Age Group")

age_level = pd.crosstab(
    filtered_df["AgeGroup"],
    filtered_df["CourseLevel"]
)

fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(
    age_level,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=ax
)
ax.set_xlabel("Course Level")
ax.set_ylabel("Age Group")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# 13. LEARNER ACTIVITY BEHAVIOR
# --------------------------------------------------

st.header("Learner Enrollment Behavior")

activity_counts = filtered_df.groupby("UserID").size()

st.write(f"**Learners in current selection:** {len(activity_counts):,}")
st.write(f"**Median courses per learner:** {activity_counts.median():.2f}")
st.write(f"**Minimum courses per learner:** {activity_counts.min()}")
st.write(f"**Maximum courses per learner:** {activity_counts.max()}")

activity_segments = pd.cut(
    activity_counts,
    bins=[0, 1, 2, 4, 10, float("inf")],
    labels=[
        "1 Course",
        "2 Courses",
        "3–4 Courses",
        "5–10 Courses",
        "11+ Courses"
    ]
)

activity_summary = (
    activity_segments.value_counts(sort=False)
    .rename_axis("ActivitySegment")
    .reset_index(name="Learners")
)

activity_summary["Percentage"] = (
    activity_summary["Learners"]
    / activity_summary["Learners"].sum()
    * 100
).round(2)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Learner Activity Segments")
    st.dataframe(
        activity_summary,
        use_container_width=True,
        hide_index=True
    )

with col2:
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(
        data=activity_summary,
        x="ActivitySegment",
        y="Learners",
        ax=ax
    )
    ax.set_xlabel("Courses Taken")
    ax.set_ylabel("Learners")
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# --------------------------------------------------
# 14. FILTERED DATA EXPORT
# --------------------------------------------------

st.header("Filtered Data")

st.download_button(
    label="Download Filtered Enrollment Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="edupro_filtered_enrollments.csv",
    mime="text/csv"
)

st.caption(
    "EduPro | Descriptive learner demographics and enrollment analysis. "
    "Results update according to the selected filters."
)
