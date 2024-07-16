import argparse

def add_domain_to_usernames(input_file, output_file, domain):
    with open(input_file, 'r') as infile:
        usernames = infile.read().splitlines()

    usernames_with_domain = [f"{username}@{domain}" for username in usernames]

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(usernames_with_domain))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add domain to usernames in a file")
    parser.add_argument("-i","input_file", help="Path to input file containing usernames")
    parser.add_argument("-o","output_file", help="Path to output file for modified usernames")
    parser.add_argument("-d","domain", help="Domain name to append (e.g., example.com)")

    args = parser.parse_args()

    add_domain_to_usernames(args.input_file, args.output_file, args.domain)
    print(f"Usernames with domain added have been saved to {args.output_file}")
