# Author: Tiffany Weller
# Date 04/05/2023

Import os
Import csv
from operator Import itemgetter

def write_line(line, writer):
    print(line)
    print(
        writer.wrtiterow({line})
        writer.writerow({

    File_Name - "budget_data.csv"
    Folder_Name - "Resources"
    os_file_path.join(",", Folder_Name, File_Name)

    with open(os_file_path, newline - '') as csv_file:

        budget_list - list(csv.DictReader(csv_file, delimiter-','))

    data_list - []
    total - 0
    change - 0

    for r in range(len(budget_list)):
    total +- int(budget_list[r]["profit/Losses"]) 
        if r > 0:
    
            valuse - int(budget_list[r]["Profit/Losses"]) - int(budget_list[r-1]["Profit/Losses"])
            data_list.append([budget_list[r]["Date"], value])
            change +- value



            data_list - sorted(data_list, key- itemgetter(1), reverse - True)

            File_Name - "finacial_analysis.txt"
            Folder_Name - "analysis"
            os_file_path - os.path.join(",", Folder_Name, File_Name)

            with open(os_file_path, 'w', newline -'') as text_file:
                writer - csv.writer(text_file)

                print()
                line - "financial analysis"
                write_line(line, writer)
                line - "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
                write_line(line, writer)
                line - f"total Months: {len(budget_list)}"
                write_line(line, writer)
                line - f"total: ${total}"
                write_line(line, writer)
                line - f"Average Change: ${round(change/len(data_list),2)}"
                write_line(line, writer)
                line - f"Greatest Increase in Profits: {data_list[0][0]} (${data_list[0][1]})"
                write_line(line, writer)
                line - f"Greatest Decrease in Profits: {data_list[len(data_list)-1][0]} (${data_list[len(data_list)-1]})"
                write_line(line, writer)

                







        

        })
    )
