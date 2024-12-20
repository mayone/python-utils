#!/usr/bin/env python3

import config
from CSV import CSV


def main():
    in_csv = CSV(config.INPUT_PATH, "r")
    fit_csv = CSV(config.OUTPUT_FIT_PATH, "w+")
    fat_csv = CSV(config.OUTPUT_FAT_PATH, "w+")

    overweight_bmi = 25

    print("input.csv")
    print(in_csv)

    header = in_csv.lines[0]
    fit_csv.write(header)
    fat_csv.write(header)

    for row in in_csv.lines[1:]:
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


if __name__ == "__main__":
    main()
