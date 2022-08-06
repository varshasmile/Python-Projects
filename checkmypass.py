import requests
import hashlib
import sys

def request_api_data(query_char):
	url = "https://api.pwnedpasswords.com/range/" + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f"Error Fetching : {res.status_code}, check api and try again!")
	return res

# def read_res(response):
# 	print(response.text)

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	# print(hashes)
	for h, count in hashes:
		# print(h, count)
		if h == hash_to_check:
			return count
	return 0

def pwned_api_check(password): #check password if it exist in api response
	sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	# print(first5_char, tail)
	response = request_api_data(first5_char)
	# print(response)
	# return read_res(response)
	return get_password_leaks_count(response, tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f"{password} is found {count} times, you should probably change it!")
		else:
			print(f"{password} is NOT found, Carry on!")
	return "done!"

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
	




