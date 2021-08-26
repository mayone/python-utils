# -*- coding: utf-8 -*-
#!/usr/bin/python

import csv

if __name__ == "__main__":
    in_file = open("input.csv", "r")
    fit_out_file = open("fit.csv", "w")
    fat_out_file = open("fat.csv", "w")

    fit_writer = csv.writer(fit_out_file)
    fat_writer = csv.writer(fat_out_file)

    lines = csv.reader(in_file, delimiter=',')

    overweight_bmi = 25

    for row in lines:
        # Write header
        if "Name" in row[0]:
            fit_writer.writerow(row)
            fat_writer.writerow(row)
            continue

        [name, height_cm, weight] = row
        height_m = float(height_cm) / 100
        weight = float(weight)
        bmi = (lambda h, w: w / (h * h))(height_m, weight)
        print(f"{name}\t{bmi}")

        if bmi < overweight_bmi:
            fit_writer.writerow(row)
        else:
             fat_writer.writerow(row)

    in_file.close()
    fit_out_file.close()
    fat_out_file.close()
