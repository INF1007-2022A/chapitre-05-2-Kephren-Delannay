#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	sous_total = 0
	for element in data:
		item = element[0]
		qty = element[1]
		unit_price = element[2]
		sous_total += unit_price * qty

	taxes = 0.15 * sous_total
	total = sous_total + taxes

	result = name

	result += "\n" + f"SOUS TOTAL {sous_total : >10.2f} $"
	result += "\n" + f"TAXES      {taxes : >10.2f} $"
	result += "\n" + f"TOTAL      {total : >10.2f} $"

	return result


def format_number(number, num_decimal_digits):
	ent = int(abs(number))
	dec = abs(number) % 1.00
	# format decimal part
	formated_dec = f"{dec :.{num_decimal_digits}f}"[1:]

	# format ent part
	formated_ent = ""
	while ent >= 1000:
		formated_ent = f' {ent % 1000}' + formated_ent
		ent //= 1000
	formated_ent = str(ent) + formated_ent

	#add signe
	result = ""
	if number < 0:
		result = "-" + formated_ent + formated_dec
	else:
		result = formated_ent + formated_dec
	return result

def get_triangle(num_rows):
	width = num_rows * 2 + 1
	result = '+' * width + '\n'
	for i in range(num_rows):
		coef = (i * 2 + 1)
		num_of_spaces = width - coef - 2
		line = '+' + ' ' * int(num_of_spaces/2) + 'A' * coef + ' ' * int(num_of_spaces/2) + '+\n'
		result += line
	result += '+' * width
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
