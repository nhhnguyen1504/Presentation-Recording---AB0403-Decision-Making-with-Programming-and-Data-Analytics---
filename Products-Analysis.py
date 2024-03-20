def get_cleaned_row_keys(row):
    """Clean and return the row keys to handle potential BOM or whitespace issues."""
    cleaned_keys = {}
    for key in row:
        cleaned_keys[key.strip()] = key
    return cleaned_keys

def read_csv_and_calculate_total_profit(file_path):
    """Reads CSV data, focusing on the year 2022, and calculates the profits by products each quarter."""
    data = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        cleaned_headers = get_cleaned_row_keys(headers)
        year_index = None
        product_index = None
        profit_index = None
        month_name_index = None
        for index, key in enumerate(cleaned_headers):
            if "Year" in key:
                year_index = index
            elif "Product" in key:
                product_index = index
            elif "Profit" in key:
                profit_index = index
            elif "Month Name" in key:
                month_name_index = index

        for line in lines[1:]:
            row = line.strip().split(',')
            if row[year_index].strip() == '2022':
                product = row[product_index].strip()
                month_name = row[month_name_index].strip()
                profit = float(row[profit_index].strip())
                quarter = 'Q' + str((['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'].index(month_name) // 3) + 1)
                if product not in data:
                    data[product] = {}
                if quarter not in data[product]:
                    data[product][quarter] = []
                data[product][quarter].append(profit)

    total_profit = {product: {quarter: sum(profit) for quarter, profit in quarters.items()} for product, quarters in data.items()}
    return total_profit

def print_table_and_summary(total_profit):
    # Question 1 - The profit each quarter by product for the year 2022
    """Prints the calculated profits in a tabulated format and provides a summary of insights."""
    header = "| Product   | Quarter 1 | Quarter 2  | Quarter 3 | Quarter 4 |  Total      |"
    print("_" * len(header))
    print(header)
    print("|" + "-" * (len(header) - 2) + "|")
    
    for product, profit in total_profit.items():
        q1, q2, q3, q4 = profit.get('Q1', 0), profit.get('Q2', 0), profit.get('Q3', 0), profit.get('Q4', 0)
        total = sum(profit.values())
        print(f"| {product:9} | {q1:10.2f} | {q2:10.2f} | {q3:9.2f} | {q4:9.2f} | {total:5.2f} |")
    print("|" + "_" * (len(header) - 2) + "|")

    # Question 2 - Summary of Insights
    max_product = max(total_profit, key=lambda x: sum(total_profit[x].values()))
    min_product = min(total_profit, key=lambda x: sum(total_profit[x].values()))
    
    print("\nProfit Table Analysis:")
    print(f"The product '{max_product}' generated the highest overall profit across all quarters in the year 2022.")
    print(f"This insight suggests that '{max_product}' performed exceptionally well and contributed significantly to the company's revenue during the year.")
    print(f"On the other hand, '{min_product}' had the lowest overall profit, indicating areas for potential improvement or optimization in marketing or product strategies.")
    print("Analyzing the performance of each product by quarter provides valuable insights for strategic decision-making and resource allocation.")

def main():
    file_path = 'product_data.csv'
    total_profit = read_csv_and_calculate_total_profit(file_path)
    print_table_and_summary(total_profit)

if __name__ == "__main__":
    main()
    
    
"""
Question 3:

The marketing director can consider using different pricing strategies targeting different markets, by adjusting accordingly. Here, many methods to 
place a price tag on certain products are available. For instance, competitive pricing strategy can be used in such cases where a product is noticeably 
more profitable in one country compared to the other.
"""