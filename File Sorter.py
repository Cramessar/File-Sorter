import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QFileDialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.observer = None
        self.root_directory = None

    def initUI(self):
        self.setWindowTitle("File Organizer")
        self.setGeometry(100, 100, 600, 400)
        
        self.layout = QVBoxLayout()
        
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.layout.addWidget(self.log_output)
        
        self.select_folder_btn = QPushButton("Select Folder")
        self.select_folder_btn.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_btn)
        
        self.start_btn = QPushButton("Start Organizing")
        self.start_btn.clicked.connect(self.start_organizing)
        self.layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Stop Organizing")
        self.stop_btn.clicked.connect(self.stop_organizing)
        self.stop_btn.setEnabled(False)
        self.layout.addWidget(self.stop_btn)
        
        self.setLayout(self.layout)
    
    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.root_directory = folder
            self.log_output.append(f"Selected folder: {self.root_directory}")
            
    def start_organizing(self):
        if not self.root_directory:
            self.log_output.append("Please select a folder first.")
            return
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.observer = Observer()
        event_handler = FileHandler(self.root_directory, self.log_output)
        self.observer.schedule(event_handler, self.root_directory, recursive=False)
        self.observer.start()
        self.log_output.append("Started monitoring folder...")
    
    def stop_organizing(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.log_output.append("Stopped monitoring folder.")
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

class FileHandler(FileSystemEventHandler):
    def __init__(self, root_directory, log_output):
        self.root_directory = root_directory
        self.log_output = log_output
        self.destinations = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
            "Videos": [".mp4", ".mov", ".avi", ".mkv"],
            "Music": [".mp3", ".wav", ".flac"],
            "Archives": [".zip", ".rar", ".tar", ".gz"],
            "Executables": [".exe", ".msi", ".sh", ".bat"],
            "Game ROMs": [".gba", ".nds", ".nsp", ".iso", ".bin", ".cso"],
            "Others": []
        }
        for folder in self.destinations.keys():
            os.makedirs(os.path.join(self.root_directory, folder), exist_ok=True)
    
    def on_modified(self, event):
        if event.is_directory:
            return
        self.log_output.append("Folder modification detected. Checking for new files...")
        self.organize_files()
    
    def organize_files(self):
        for filename in os.listdir(self.root_directory):
            file_path = os.path.join(self.root_directory, filename)
            if os.path.isfile(file_path):
                file_ext = os.path.splitext(filename)[1].lower()
                self.log_output.append(f"Detected file: {filename} (Extension: {file_ext})")
                moved = False
                
                for folder, extensions in self.destinations.items():
                    if file_ext in extensions:
                        destination_path = os.path.join(self.root_directory, folder)
                        shutil.move(file_path, os.path.join(destination_path, filename))
                        self.log_output.append(f"Moved: {filename} -> {folder}")
                        moved = True
                        break
                
                if not moved:
                    shutil.move(file_path, os.path.join(self.root_directory, "Others", filename))
                    self.log_output.append(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerApp()
    window.show()
    sys.exit(app.exec_())
