import json
import os


CREDENTIAL_FILE = "configs/credentials.json"


def get_api_key(service_name):

    os.makedirs("configs", exist_ok=True)

    if not os.path.exists(CREDENTIAL_FILE):

        with open(CREDENTIAL_FILE, "w") as f:
            json.dump({}, f)

    with open(CREDENTIAL_FILE, "r") as f:
        creds = json.load(f)

    # If key already exists
    if service_name in creds:

        print(f"🔑 Using stored API key for {service_name}")

        return creds[service_name]

    # Ask user if not stored
    print(f"\n⚠ API key required for: {service_name}")

    api_key = input(f"Enter API key for {service_name}: ")

    creds[service_name] = api_key

    with open(CREDENTIAL_FILE, "w") as f:
        json.dump(creds, f, indent=4)

    print(f"✅ API key saved for {service_name}")

    return api_key