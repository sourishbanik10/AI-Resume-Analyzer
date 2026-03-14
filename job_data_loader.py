import pandas as pd

def load_jobs():

    df = pd.read_csv("job_dataset.csv")

    # Print columns once to see dataset structure
    print("Dataset Columns:", df.columns)

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Possible column name options
    title_cols = ["title","job title","job_title","position"]
    desc_cols = ["description","job description","job_description","details"]

    title_col = None
    desc_col = None

    for col in title_cols:
        if col in df.columns:
            title_col = col
            break

    for col in desc_cols:
        if col in df.columns:
            desc_col = col
            break

    if title_col is None or desc_col is None:
        raise Exception("Could not find job title or description column in dataset")

    df = df[[title_col, desc_col]]

    df = df.rename(columns={
        title_col: "title",
        desc_col: "description"
    })

    df = df.dropna()

    return df