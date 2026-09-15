# def categorize_dataset(row_count):
#     if 1 < row_count < 1000:
#         return "Small Dataset (use Pandas)"
#     elif 1000 <= row_count < 10000:
#         return "Medium Dataset (use pandas / In-memory)"
#     elif 10000 <= row_count < 100000:
#         return "Big Data (Consider PySpark or Dask)"
#     elif row_count <= 0:
#         return "Invalid row count"
#     else:
#         return "Dataset size not categorized"

# print("Enter the number of rows in the dataset:")
# n = int(input())

# row_count = n
# result = categorize_dataset(row_count)
# print(result)
# 1324

def clean_and_format_header(Header_name, uppercase=False):

    cleanName = Header-name.strip().replace(" ", "_")
    if uppercase:
        cleanName = cleanName.upper()
    return cleanName
