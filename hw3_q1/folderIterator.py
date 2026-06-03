from pathlib import Path

class FolderIterator:
    def __init__(self, foldername='base'):
        self.foldername = Path(foldername)
        self.uniques = []
        self.duplicates = dict()  # dict instance
        # # Other attributes may follow
        self.current_folder = [self.foldername]

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        for folder in self.current_folder:
            for item in folder.iterdir():
                if item.is_dir():
                    self.current_folder.append(item)
                
                if item.is_file():
                    file_content =item.read_bytes()
                    is_duplicate = False
                    for unique_name, unique_content in self.uniques:
                        if file_content == unique_content:
                            # This files content already exists - its a duplicate
                            if unique_name not in self.duplicates:
                                self.duplicates[unique_name] = []
                            self.duplicates[unique_name].append(item.name)
                            is_duplicate = True
                            break
                    if not is_duplicate:
                        self.uniques.append((item.name, file_content))
        print("Unique files: ")
        for name, content in self.uniques:
            print(f" {name}: {content}")
        print("\nDuplicates: ")
        for parent_name, dup_names in self.duplicates.items():
            print(f" {parent_name}: {dup_names}")
        pass

if __name__ == "__main__":
    FolderIterator().iter_folder()