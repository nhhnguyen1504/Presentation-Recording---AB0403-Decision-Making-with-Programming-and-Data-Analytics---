"""
Recording link: https://youtu.be/1efCiAwVTTw

Scenario 2: Discount Analysis
You are given product_data.csv file by the interviewer during an
interview for an intern position in a department. 
The dataset contains product data collected in different countries 
between the year 2022 and 2023. You are to analyse the impact of discounts offered to 
the various Discount Bands based on the dataset given and provide some insights to the 
marketing director of the company from the output of the analysis.

The following are the deliverables of your analysis:
1.  Tabulate the total discount by discount bands for the year 2023 in the following format::
_____________________________________________________________________________________
|Discount Bands | 	Quarter 1  |  Quarter 2  |	 Quarter 3	 |  Quarter 4  |  Total  |
|------------------------------------------------------------------------------------|
|               |              |             |               |             |         |
|____________________________________________________________________________________|
					
	
2.	You program should include capability to provide a summary of the insights based on 
the results of your profit table in point 1.

3.	To value add to the analysis, you are required to think of one additional analysis that the 
marketing director may be interested to find out. Present the solution and explain how such analysis 
adds value to the analysis.

IMPORTANT: You must use the original dataset given, you are not allowed to use excel or any other 
application software to modify the data before importing it to your python program.

"""

# 1. Tabulate the total discount by discount bands for the year 2023:

def read_csv(file_path):
    cleaned_file = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file: 
        lines = file.readlines() 
        headers = lines[0].strip().split(',') 
        for line in lines[1:]:
            values = line.strip().split(',')
            row = {header.strip(): value.strip() for header, value in zip(headers, values)}
            cleaned_file.append(row)
    return cleaned_file

def filter_and_calculate_discounts(file_path):
    data = {} 
    lines = read_csv(file_path)
    for line in lines:
        year = line.get('Year', '')  
        if year == '2023':  
            discount_band = line.get('Discount Band', '')
            discounts = float(line.get('Discounts', ''))
            month_name = line.get('Month Name', '')
            quarter = 'Q' + str((['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November','December'].index(month_name) // 3) + 1) 
            if discount_band not in data: 
                data[discount_band] = {}
            if quarter not in data[discount_band]:
                data[discount_band][quarter] = []
            data[discount_band][quarter].append(discounts)
    total_discounts = {discount_band: {quarter: sum(discounts) for quarter, discounts in quarters.items()} for discount_band, quarters in data.items()} 
    return total_discounts  

def print_table_header(header):
    print()  
    print("_" * len(header))
    print(header)
    print("|" + "-" * (len(header) - 2) + "|")
    return

def format_number(number):
    if number >= 1e6:
        return f"{number / 1e6:,.2f}M"
    elif number >= 1e3:
        return f"{number / 1e3:,.2f}K"
    else:
        return f"{number:,.2f}"

def print_summary_table(total_discounts):
    header = f"""| {'Discount Bands':^7} | {'Quarter 1 $':^12} | {'Quarter 2':^10} | {'Quarter 3':^10} | {'Quarter 4':^12} | {'Total $':^12} |""" 
    print(f"\n{'-' * (len(header)//3)} 1. Total Discounts 2023 {'-' * (len(header)//3)}""")
    print_table_header(header)
    
    for discount_band, discounts in total_discounts.items():      
        q1 = discounts.get('Q1', 0) 
        q2 = discounts.get('Q2', 0)
        q3 = discounts.get('Q3', 0)
        q4 = discounts.get('Q4', 0) 
        total = sum(discounts.values())
        print(f"| {discount_band:^14} | {q1:^12,.2f} | {q2:^10,.2f} | {q3:^10,.2f} | {q4:^12,.2f} | {total:^12,.2f} |")
    print("|" + "_" * (len(header) - 2) + "|")

# 2. Summary of Insights
 
    total_discounts_2023 = sum(sum(discounts.values()) for discounts in total_discounts.values())
    max_discount_band = max(total_discounts, key=lambda x: sum(total_discounts[x].values()))
    min_discount_band = min(total_discounts, key=lambda x: sum(total_discounts[x].values()))
    max_discount_amount = max(sum(discounts.values()) for discounts in total_discounts.values())
    min_discount_amount = min(sum(discounts.values()) for discounts in total_discounts.values())

    print()  
    print(("-" * (len(header)//3)) + " 2. Summary of Insights" + ("-" * (len(header)//3)))

    print("\na) Overview:")
    print(f"- Overall: In 2023, a substantial total discount amount of ${format_number(total_discounts_2023)} indicated significant discounting activity utilising different bands by Travel on Bike Pte Ltd.")
    
    print("\nb) Discount Bands comparison:")
    print(f"- The '{max_discount_band}' band offered the highest discount amounts, at ${format_number(max_discount_amount)}, indicating a successful strategy in incentivizing customer purchases or capturing market share, albeit potentially impacting profit margins.")
    print("- This strategy can be used to quickly clear excess inventory or outdated stock, remain competitive in the market or to boost overall revenue if the volume of sales significantly outweights the discount.")
    print(f"- The '{min_discount_band}' band offered the lowest discount amounts, at ${format_number(min_discount_amount)}, suggesting the premium pricing strategy deployed or possibly high-profit-margin products that provide little incentive for the company to offer discounts to boost sales.")
    
    print("\nc) Discount offerings trends:")
    print(f"- Except for '{max_discount_band}' and '{min_discount_band}' band, there is a consistent increase in total discounts from Quarter 1 to Quarter 4, suggesting a potential trend of escalating discount offers as the year progresses.")
    print("- Quarter 4 stands out as the period with the highest total discounts across all discount bands, indicating a possible year-end promotion or sales push. The decrease in its discount amount in the first three quarters could be attributed to a strategic adjustment aimed at improving profit margins.")
    
    print("\nd) Conclusion:")
    print("- In conclusion, discount analysis holds a central position within the company's sales strategy, providing crucial insights for pricing optimization, revenue enhancement, and market alignment, adjusted based on varied discount bands and amounts.")

# 3. Additional Analysis

def units_sold_based_on_segment_and_discount(file_path):
    data = {} 
    lines = read_csv(file_path)
    for line in lines:
        year = line.get('Year', '')  
        if year == '2023':  
            discount_band = line.get('Discount Band', '')
            units_sold = float(line.get('Units Sold', ''))
            segment = line.get('Segment', '')
            if discount_band not in data: 
                data[discount_band] = {}
            if segment not in data[discount_band]:
                data[discount_band][segment] = []
            data[discount_band][segment].append(units_sold)
    avg_units_sold = {discount_band: {segment: sum(units_sold)/len(units_sold) for segment, units_sold in segments.items()} for discount_band, segments in data.items()}
    return avg_units_sold

def print_units_sold(avg_units_sold):
    
    header = f"| {'Discount Bands':^7} | {'Channel Partners':^12} | {'Enterprise':^9} | {'Government':^9} | {'Midmarket':^9} | {'Small Business':^10} | {'Total':^8} |" # Print the table header
    print(f"\n{'-' * (len(header)//5)} 3. Additional Analysis (Segment-wise Units Sold 2023) {'-' * (len(header)//5)}")
    print_table_header(header)

    for discount_band, segment_data in avg_units_sold.items():
        chpart = segment_data.get('Channel Partners', 0)
        ent = segment_data.get('Enterprise', 0)
        gov = segment_data.get('Government', 0)
        mid = segment_data.get('Midmarket', 0) 
        smb = segment_data.get('Small Business', 0)
        total = sum(segment_data.values())
        print(f"| {discount_band:^14} | {chpart:^16,.2f} | {ent:^10,.2f} | {gov:^10,.2f} | {mid:^9,.2f} | {smb:^14,.2f} | {total:^8,.2f} |")
    print("|" + "_" * (len(header) - 2) + "|")
    
    max_discount_band_units = max(avg_units_sold, key=lambda x: sum(avg_units_sold[x].values()))
    min_discount_band_units = min(avg_units_sold, key=lambda x: sum(avg_units_sold[x].values()))
    max_units_sold = max(sum(segment_data.values()) for segment_data in avg_units_sold.values())
    min_units_sold = min(sum(segment_data.values()) for segment_data in avg_units_sold.values())

    print()      
    print("ANALYSIS:")       
    
    print("\na) Total discounts:")
    print(f"- The '{max_discount_band_units}' discount band generated the highest total units sold, at {format_number(max_units_sold)} units.")
    print(f"- Meanwhile, the '{min_discount_band_units}' discount band generated the lowest total units sold, at {format_number(min_units_sold)} units.")
    print("- This result possibly suggests the inverse relationship between discounts and volume of sales, which might reflect the discount addiction behaviour in customers, causing delayed purchases as waiting for future deeper discounts.")
    
    print("\nb) Segments:")
    print("- In the absence of discounts, the Channel Partners and Enterprise segments exhibit the highest units sold, while the Low and Medium discount bands drive the highest units sold in Government, Midmarket, and Small Business segments.")
    print("- Conversely, no segment demonstrates the highest units sold under high discount levels.")

    print("\nc) Conclusion:")
    print("- In conclusion, Travel on Bike Pte Ltd should tailor its discounting strategy towards Midmarket segment which responds the most positively to discounts.")
    print("- However, caution is advised against excessive discounting over the long term, as it could potentially affect customer behavior and undermine brand perception.")


# Main execution
def main():
    total_discounts = filter_and_calculate_discounts(r"C:\Users\ADMIN\Downloads\product_data.csv")
    print_summary_table(total_discounts)
    units_sold = units_sold_based_on_segment_and_discount(r"C:\Users\ADMIN\Downloads\product_data.csv")
    print_units_sold(units_sold)

if __name__ == "__main__": 
    main()