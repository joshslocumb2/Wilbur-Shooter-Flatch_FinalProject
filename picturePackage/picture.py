# File Name : picture.py
# Student Name: Hailey Manuel
# email:manuelhv@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  04/31/2025
# Course #/Section:   IS 4010-001
# Semester/Year:  Spring 2025
# Brief Description of the assignment: This assignment decrypts a campus meeting location and movie title then displays the team’s photo taken at that location.

# Brief Description of what this module does: defines a simple class called PictureViewer that loads and displays an image using matplotlib
# Citations: Perplexity AI, ChatGPT

import matplotlib.pyplot as plt
import os

class PictureViewer:
    def __init__(self, data_folder="Data"):
        """
        Initialize PictureViewer with data folder.
        
        Args:
            data_folder (str): Path to folder containing the team photo
        """
        self.data_folder = data_folder
        self.team_name = "Wilbur (Shooter) Flatch"
        self.picture_path = None
        
    def set_picture_path(self, path):
        """Set the path to the team photo."""
        self.picture_path = path
        
    def load_and_display_photo(self):
        """
        Load and display the team photo using matplotlib.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.picture_path:
            print("Picture path not set. Please set it with set_picture_path method.")
            return False
            
        try:
            # Using matplotlib to display the image
            img = plt.imread(self.picture_path)
            plt.figure(figsize=(10, 8))
            plt.imshow(img)
            plt.axis('off')  # Hide axes
            plt.title(f"Team {self.team_name} at the decrypted location")
            plt.show()
            return True
        except FileNotFoundError:
            print(f"Error: Image file not found at {self.picture_path}")
            return False
        except Exception as e:
            print(f"Error displaying image: {type(e).__name__} - {str(e)}")
            return False

