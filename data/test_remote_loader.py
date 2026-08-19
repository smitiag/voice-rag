from data.dataset_loader import DatasetLoader


print("Starting remote loader test...")
print("Reading only 5 lightweight records...")

loader = DatasetLoader()

records = list(loader.iter_records(max_records=5))

print(f"\nRecords received: {len(records)}")

for i, record in enumerate(records, start=1):
    print(f"\n--- RECORD {i} ---")
    print("Query ID:", record["query_id"])
    print("Query Type:", record["query_type"])
    print("Query:", record["query"])
    print("Answer:", record["Answer"])
    print("English Query:", record["Eng_Query"])
    print("English Answer:", record["Eng_Answer"])

print("\nRemote loader test complete.")