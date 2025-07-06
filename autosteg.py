import subprocess
import os

def create():
    secret = input("enter the text to be hidden: ")
    txt = "secret.txt"
    with open(txt, "w") as f:
        f.write(secret)

    password = input("enter the password: ")
    command1 = ["steghide", "embed", "-cf", pic, "-ef", txt, "-p", password]

    result1 = subprocess.run(command1, capture_output=True, text=True)
    print("result:", result1.stdout)
    print("error:", result1.stderr)

    delete = ["rm", txt]
    subprocess.run(delete)


def read():
    password = input("enter password: ")
    command2 = ["steghide", "extract", "-sf", pic, "-p", password]

    result2 = subprocess.run(command2, capture_output=True, text=True)
    print("result:", result2.stdout.strip())
    print("error:", result2.stderr.strip())


def auto(brute_all=False):
    folder = "."
    wordlist = "wordlist.txt"

    for file in os.listdir(folder):
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            path = os.path.join(folder, file)

            command3 = ["strings", path]
            result3 = subprocess.run(command3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            lines = result3.stdout.splitlines()
            line6 = lines[5] if len(lines) > 5 else " "
            line8 = lines[7] if len(lines) > 7 else " "
            sus = len(line6) > 10 and len(line8) > 10

            if sus:
                print(f"{file} might have hidden text.")
                if brute_all:
                    extracted = False
                    try:
                        with open(wordlist, "r") as f:
                            for password in f:
                                password = password.strip()
                                output_file = f"{file}_extracted.txt"

                                result4 = subprocess.run(
                                    ["steghide", "extract", "-sf", path, "-p", password, "-xf", output_file],
                                    capture_output=True,
                                    text=True
                                )

                                if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                                    print(f"password found for {file}: {password}")
                                    print(f"file extracted: {output_file}")
                                    extracted = True
                                    break
                        if not extracted:
                            print(f"extraction failed for {file}")
                    except FileNotFoundError:
                        print("wordlist.txt not found")
                else:
                    print("brute force is off. skipping.")
            else:
                print(f"{file} is clean.")

def main():
    global pic
    while True:
        print("\n1. embed a text inside an image")
        print("2. extract text from an image")
        print("3. auto detect and brute force")
        option = input("choose: ")

        if option == "1":
            pic = input("enter image name: ")
            create()
            break
        elif option == "2":
            pic = input("enter image name: ")
            read()
            break
        elif option == "3":
            brute = input("brute force all detected images? (y/n): ").lower()
            brute_all = brute == "y"
            auto(brute_all)
            break
        else:
            print("invalid choice")


main()

