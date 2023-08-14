**Program Name**: Malware Scanner GUI

**Description**:
The Malware Scanner GUI is a cross-platform graphical user interface application designed to help users scan a specified directory for potential malware files. The application provides an intuitive interface for users to input a directory path, initiate the scanning process, and view the results.

**Features**:
- **Directory Selection**: Users can browse their computer's file system and select a directory to scan for potential malware files.
- **Scanning**: The application searches the selected directory and its subdirectories for files with specific extensions commonly associated with malware.
- **Results Display**: When the scanning is complete, the application displays the list of potential malware files found in a scrollable text area.
- **User-Friendly**: The program uses common GUI components like text entry fields, buttons, and text areas, making it easy for users to understand and interact with.

**Usage**:
1. Launch the application.
2. Use the "Browse" button to select the directory you want to scan for malware files.
3. Click the "Scan" button to initiate the scanning process.
4. After scanning, the application will display the list of potential malware files found in the selected directory and its subdirectories.

**Dependencies**:
The application requires the `wxPython` library to create the graphical user interface.

**Compatibility**:
The application is cross-platform and can be used on various operating systems, including Windows, macOS, and Linux.

**Note**:
While the Malware Scanner GUI provides a user-friendly way to identify potential malware files, it's important to note that malware detection based solely on file extensions is not comprehensive. Advanced malware can use various techniques to avoid detection by traditional methods. For robust malware detection, consider using dedicated antivirus software and security solutions.
