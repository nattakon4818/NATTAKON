# def register_member():
#     name = input("Enter member name : ")
#     table = input("Enter table number : ")

#     with open("member.txt", "a", encoding="utf-8") as f:
#         f.write(f"MEMBER : {name} | TABLE : {table}\n")

#     print(f"Member '{name}' registered at Table {table}")
#     return name, table

# def delete_member():
#     while True:
#         name_to_delete = input("Enter member name to delete (Enter to exit) : ")

#         if name_to_delete.strip() == "":
#             break

#         try:
#             with open("member.txt", "r", encoding="utf-8") as f:
#                 lines = f.readlines()

#             found = False
#             new_lines = []

#             for line in lines:
#                 line = line.strip()

#                 if line.startswith("MEMBER : "):
#                     try:
#                         member_part = line.split("|")[0].strip()
#                         member_name = member_part.replace("MEMBER : ", "").strip()

#                         if member_name.lower() == name_to_delete.lower():
#                             found = True
#                             continue
#                     except Exception:
#                         pass

#                 new_lines.append(line + "\n")

#             if not found:
#                 print(f"Member '{name_to_delete}' not found. Please try again.\n")
#                 continue

#             with open("member.txt", "w", encoding="utf-8") as f:
#                 f.writelines(new_lines)

#             print(f"Member '{name_to_delete}' has been removed successfully.\n")
#             break

#         except FileNotFoundError:
#             print("Error: member.txt not found. Please register a member first.\n")
#             break

# def daily_sales_report():
#     while True:
#         date_input = input("Enter the date to view sales (YYYYMMDD) or press Enter to exit : ").strip()

#         if date_input == "":
#             return
        
#         if len(date_input) != 8 or not date_input.isdigit():
#             print("Invalid date format. Please enter in YYYYMMDD format.")
#             continue
        
#         formatted_date = f"{date_input[:4]}-{date_input[4:6]}-{date_input[6:]}"
        
#         total_sales = 0
#         current_block_date = None

#         try:
#             with open("sales.txt", "r", encoding="utf-8") as f:
#                 for line in f:
#                     line = line.strip()
#                     if "DATE:" in line:
#                         date_part = line.split("DATE:")[1].strip().split()[0]
#                         current_block_date = date_part
                    
#                     if "Total Price:" in line and current_block_date == formatted_date:
#                         price = float(line.replace("Total Price:", "").replace("Baht", "").strip())
#                         total_sales += price
#         except FileNotFoundError:
#             print("No sales data found.")
#             return

#         if total_sales == 0:
#             print(f"No sales found for {formatted_date}. Please try again.")
#             continue
#         else:
#             print("\n=== DAILY SALES REPORT ===", f"Date: {formatted_date}", f"Total Sales: {total_sales} Baht", sep='\n')
#             break
