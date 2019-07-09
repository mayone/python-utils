# -*- coding: utf-8 -*-

try:
	import github
except Exception as e:
	print("venv test FAILED")
	exit(0)

if __name__ == "__main__":
	print("venv test SUCCESS")