# File modes

input_file = 'country_info.txt'
with open(input_file) as country_file:
#### simple print rows on each file as list #######
    # for row in country_file:
    #     print(row)
    # print("*" * 80)
###### replace the delimeter with , and make a list
    for row in country_file:
        print(row.strip("\n").split("|"))
        out = row.strip("\n").split("|")
# Writing a file to another text file
data = ["Andra - Telagu",
        "Tamil - Tamil",
        "Karnataka - Kannada",
        "Delhi - Hindi"]
# Writing a file to another text file via print statements
out_file = "write_out_data.txt"
with open(out_file, "w") as write_out_data:
    for row in data:
        print(row, file=write_out_data)

# Writing a file to another text file via .write methods
out_file1 = "write_out_data1.txt"
with open(out_file1, "w") as write_out_data1:
    for row in data:
        write_out_data1.write(row)





