import duckdb

DATASET_PATH = (
    "https://huggingface.co/datasets/ai4bharat/MSMARCO-XI/"
    "resolve/main/train/hintrain.parquet"
)

print("Connecting to MSMARCO-XI Hindi train data...")

con = duckdb.connect()

print("\nReading 5 sample rows...")

result = con.execute(
    f"""
    SELECT
        query_id,
        query_type,
        query,
        Answer,
        Eng_Query,
        Eng_Answer
    FROM read_parquet('{DATASET_PATH}')
    LIMIT 5
    """
).fetchall()

for i, row in enumerate(result, start=1):
    print(f"\n--- RECORD {i} ---")
    print("Query ID:", row[0])
    print("Query Type:", row[1])
    print("Query:", row[2])
    print("Answer:", row[3])
    print("English Query:", row[4])
    print("English Answer:", row[5])

print("\nSample inspection complete.")