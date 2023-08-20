import os

def clear_dmg_files(download_folder):
    for item in os.listdir(download_folder):
        item_path = os.path.join(download_folder, item)
        if item.lower().endswith('.dmg') and os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Removed: {item_path}")

def main():
    user_home = os.path.expanduser("~")
    download_folder = os.path.join(user_home, "Downloads")

    if os.path.exists(download_folder):
        clear_dmg_files(download_folder)
        print("Cleanup completed.")

    else:
        print("Downloads folder not found.")

if __name__ == "__main__":
    main()
