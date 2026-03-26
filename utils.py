def summarize_data(df):
    print("\nDataset Shape:", df.shape)
    print("\nColumns:")
    print(df.columns)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nBasic Statistics:")
    print(df.describe())
