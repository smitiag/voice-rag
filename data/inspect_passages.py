import pyarrow.parquet as pq


DATASET_PATH = (
    "hf://datasets/ai4bharat/MSMARCO-XI/"
    "train/hintrain.parquet"
)


print("Checking passages metadata only...")


with pq.ParquetFile(DATASET_PATH) as parquet_file:

    row_group = parquet_file.metadata.row_group(0)

    for i in range(row_group.num_columns):

        column = row_group.column(i)

        if "passages" in column.path_in_schema:
            print(
                column.path_in_schema,
                "|",
                "rows:", column.num_values,
                "|",
                "compressed:", column.total_compressed_size,
                "|",
                "offset:", column.data_page_offset,
            )


print("\nMetadata check complete.")