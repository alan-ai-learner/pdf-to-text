import pdfplumber
import os
file_name = []
input_path = input("Enter the input folder path:-")
ouput_path = input("Enter the output folder path:-")

for file in os.listdir(input_path):
    if str(file).endswith('.pdf'):
        file_name.append(file)
    else:
        continue

    
 
 
for ap in file_name:
    all_text =''
    try:
        with pdfplumber.open(input_path+ap) as pdf:
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                all_text = all_text + '\n' + single_page_text

        f = open(f'{ouput_path}/{ap[:-4]}.txt',"w+",encoding='utf-8')
        f.write(all_text)
        f.close()
        print(f":::::::DONE--{ap} :::::::::")
    except:
        continue