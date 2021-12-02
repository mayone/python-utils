#!/usr/bin/env python3

import csv
from CSV import CSV
import config


def main():
    in_csv = CSV(config.INPUT_PATH, "r")
    fit_csv = CSV(config.OUTPUT_FIT_PATH, "w+")
    fat_csv = CSV(config.OUTPUT_FAT_PATH, "w+")

    overweight_bmi = 25

    print("input.csv")
    print(in_csv)

    for row in in_csv.lines:
        # Write header
        if "Name" in row[0]:
            fit_csv.write(row)
            fat_csv.write(row)
            continue

        [name, height_cm, weight] = row
        height_m = float(height_cm) / 100
        weight = float(weight)
        bmi = (lambda h, w: w / (h * h))(height_m, weight)

        if bmi < overweight_bmi:
            print(f"{name}\t{bmi:.1f} -> fit")
            fit_csv.write(row)
        else:
            print(f"{name}\t{bmi:.1f} -> fat")
            fat_csv.write(row)

    fit_csv.read()
    fat_csv.read()
    print("fit.csv")
    print(fit_csv)
    print("fat.csv")
    print(fat_csv)

    in_csv.close()
    fit_csv.close()
    fat_csv.close()


def main_pure():
    in_file = open(config.INPUT_PATH, "r")
    fit_out_file = open(config.OUTPUT_FIT_PATH, "w")
    fat_out_file = open(config.OUTPUT_FAT_PATH, "w")

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

        if bmi < overweight_bmi:
            print(f"{name}\t{bmi:.1f} -> fit")
            fit_writer.writerow(row)
        else:
            print(f"{name}\t{bmi:.1f} -> fat")
            fat_writer.writerow(row)

    in_file.close()
    fit_out_file.close()
    fat_out_file.close()


if __name__ == "__main__":
    main()
