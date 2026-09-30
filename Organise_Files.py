from pathlib import Path
import shutil


# ============================================================
# FILE CATEGORIES
# ============================================================

FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg", ".tiff"
    },

    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm"
    },

    "Music": {
        ".mp3", ".wav", ".flac",
        ".aac", ".ogg", ".m4a"
    },

    "Documents": {
        ".txt", ".doc", ".docx",
        ".odt", ".rtf"
    },

    "PDFs": {
        ".pdf"
    },

    "Spreadsheets": {
        ".xls", ".xlsx", ".csv",
        ".ods"
    },

    "Presentations": {
        ".ppt", ".pptx", ".odp"
    },

    "Archives": {
        ".zip", ".rar", ".7z",
        ".tar", ".gz", ".bz2"
    },

    "Code": {
        ".py", ".java", ".cpp", ".c",
        ".h", ".html", ".css", ".js",
        ".json", ".xml"
    }
}


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():

    print("\n" + "=" * 55)
    print("                 FILE ORGANIZER")
    print("=" * 55)

    print("1. Select Folder")
    print("2. Preview Organization")
    print("3. Organize Files")
    print("4. Show File Statistics")
    print("5. Exit")

    print("=" * 55)


# ============================================================
# SELECT FOLDER
# ============================================================

def select_folder():

    path = input("\nEnter folder path: ").strip()

    folder = Path(path).expanduser()

    if not folder.exists():
        print("\n❌ Folder does not exist.")
        return None

    if not folder.is_dir():
        print("\n❌ The path you entered is not a folder.")
        return None

    return folder


# ============================================================
# GET FILES
# ============================================================

def get_files(folder):

    files = []

    for item in folder.iterdir():

        # Ignore directories
        if not item.is_file():
            continue

        # Ignore hidden files
        if item.name.startswith("."):
            continue

        files.append(item)

    return files


# ============================================================
# IDENTIFY CATEGORY
# ============================================================

def get_category(file):

    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"


# ============================================================
# GET ORGANIZATION PLAN
# ============================================================

def create_organization_plan(files):

    plan = {}

    for file in files:

        category = get_category(file)

        if category not in plan:
            plan[category] = []

        plan[category].append(file)

    return plan


# ============================================================
# PREVIEW
# ============================================================

def preview_organization(folder):

    files = get_files(folder)

    if not files:
        print("\nNo files found.")
        return None

    plan = create_organization_plan(files)

    print("\n" + "=" * 55)
    print("              ORGANIZATION PREVIEW")
    print("=" * 55)

    for category, category_files in plan.items():

        print(f"\n📁 {category}/")

        for file in category_files:

            print(f"   └── {file.name}")

    print("\n" + "=" * 55)

    return plan


# ============================================================
# CREATE UNIQUE DESTINATION
# ============================================================

def get_unique_destination(destination):

    if not destination.exists():
        return destination

    counter = 1

    while True:

        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = (
            destination.parent / new_name
        )

        if not new_destination.exists():
            return new_destination

        counter += 1


# ============================================================
# CREATE CATEGORY FOLDERS
# ============================================================

def create_category_folders(folder, plan):

    for category in plan:

        category_folder = folder / category

        category_folder.mkdir(
            exist_ok=True
        )


# ============================================================
# MOVE FILES
# ============================================================

def organize_files(folder, plan):

    create_category_folders(
        folder,
        plan
    )

    moved = 0
    failed = 0

    print("\n" + "=" * 55)
    print("                 ORGANIZING")
    print("=" * 55)

    for category, files in plan.items():

        destination_folder = (
            folder / category
        )

        for file in files:

            destination = (
                destination_folder / file.name
            )

            destination = get_unique_destination(
                destination
            )

            try:

                shutil.move(
                    str(file),
                    str(destination)
                )

                print(
                    f"✓ {file.name} → {category}/"
                )

                moved += 1

            except PermissionError:

                print(
                    f"✗ Permission denied: "
                    f"{file.name}"
                )

                failed += 1

            except OSError as error:

                print(
                    f"✗ Could not move "
                    f"{file.name}: {error}"
                )

                failed += 1

    print("\n" + "=" * 55)
    print("Organization complete.")
    print(f"Files moved : {moved}")
    print(f"Files failed: {failed}")
    print("=" * 55)


# ============================================================
# FILE STATISTICS
# ============================================================

def show_statistics(folder):

    files = get_files(folder)

    if not files:
        print("\nNo files found.")
        return

    plan = create_organization_plan(files)

    print("\n" + "=" * 55)
    print("                 FILE STATISTICS")
    print("=" * 55)

    total = len(files)

    print(f"\nTotal files: {total}")

    for category, category_files in sorted(
        plan.items()
    ):

        print(
            f"{category:<20} "
            f"{len(category_files)} file(s)"
        )

    print("=" * 55)


# ============================================================
# MAIN
# ============================================================

def main():

    selected_folder = None

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # SELECT FOLDER
        # ----------------------------------------------------

        if choice == "1":

            folder = select_folder()

            if folder is not None:

                selected_folder = folder

                print(
                    f"\n✓ Selected folder:"
                    f"\n  {selected_folder}"
                )


        # ----------------------------------------------------
        # PREVIEW
        # ----------------------------------------------------

        elif choice == "2":

            if selected_folder is None:

                print(
                    "\n❌ Please select a folder first."
                )

            else:

                preview_organization(
                    selected_folder
                )


        # ----------------------------------------------------
        # ORGANIZE
        # ----------------------------------------------------

        elif choice == "3":

            if selected_folder is None:

                print(
                    "\n❌ Please select a folder first."
                )

                continue

            plan = preview_organization(
                selected_folder
            )

            if plan is None:
                continue

            confirmation = input(
                "\nDo you want to move these files? "
                "(y/n): "
            ).strip().lower()

            if confirmation == "y":

                organize_files(
                    selected_folder,
                    plan
                )

            else:

                print(
                    "\nOrganization cancelled."
                )


        # ----------------------------------------------------
        # STATISTICS
        # ----------------------------------------------------

        elif choice == "4":

            if selected_folder is None:

                print(
                    "\n❌ Please select a folder first."
                )

            else:

                show_statistics(
                    selected_folder
                )


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "5":

            print(
                "\nExiting File Organizer. Goodbye! 👋"
            )

            break


        # ----------------------------------------------------
        # INVALID CHOICE
        # ----------------------------------------------------

        else:

            print(
                "\n❌ Invalid choice. "
                "Please choose 1–5."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()