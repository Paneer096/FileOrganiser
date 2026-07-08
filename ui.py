import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QFileDialog, QTextEdit)
from PySide6.QtCore import Qt

class OrganizerUI(QWidget):
    def __init__(self, start_organizer_callback):
        super().__init__()
        # Store the function passed from fileorganiser.py
        self.start_organizer_callback = start_organizer_callback
        self.init_ui()
        
    def init_ui(self):
        # Window setup
        self.setWindowTitle("File Organizer")
        self.resize(500, 350)
        
        # Layouts
        main_layout = QVBoxLayout()
        path_layout = QHBoxLayout()
        
        # Widgets
        self.label = QLabel("Select the folder you want to organize:")
        self.path_input = QLineEdit()
        self.browse_btn = QPushButton("Browse")
        self.run_btn = QPushButton("Organize Folder")
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True) # Make it read-only for logs
        
        # Assemble Path Row
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.browse_btn)
        
        # Assemble Main Layout
        main_layout.addWidget(self.label)
        main_layout.addLayout(path_layout)
        main_layout.addWidget(self.run_btn)
        main_layout.addWidget(self.log_output)
        
        self.setLayout(main_layout)
        
        # Connect Buttons to Actions
        self.browse_btn.clicked.connect(self.browse_folder)
        self.run_btn.clicked.connect(self.trigger_organization)

    def browse_folder(self):
        # Opens a native Windows folder selector dialog
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_selected:
            self.path_input.setText(folder_selected)

    def trigger_organization(self):
        target_path = self.path_input.text().strip()
        if not target_path:
            self.log_output.append("Error: Please select a valid folder path first.")
            return
            
        # Clear previous logs
        self.log_output.clear()
        self.log_output.append(f"Starting organization on: {target_path}\n")
        
        # Call the backend function from fileorganiser.py and pass the text area for logging
        self.start_organizer_callback(target_path, self.log_output)