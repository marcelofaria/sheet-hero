from openpyxl import *
import time

inicio = time.time()
wb = load_workbook("Intervals.xlsx", data_only=True)
print(wb.sheetnames)

sh = wb["Sheet1"]
print(type(sh["A1"].value))

val = "Something"
row = 2

while val is not None:
    frq = sh["B" + str(row)].value
    interval = sh["C" + str(row)].value

    #interval = sh["B" + str(row+1)].value - sh["B" + str(row)].value

    minor_value = frq - ((interval/2))
    major_value = frq + ((interval/2))

    result = (str(minor_value) + " - " + str(major_value))

    sh["D" + str(row)] = result

    row += 1
    val = sh["B" + str(row)].value

wb.save("Intervals.xlsx")

fim = time.time()

print("O tempo de processamento foi = " + str(fim - inicio))
