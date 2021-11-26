import os

disk_location = "E:/AI-VR dataset"
# disk_location = "/Volumes/New Volume/AI-VR dataset"

# Define the path for all of the folders.
ED_FOLDER_PATH = os.path.join(disk_location, "MIMIC-IV ED")
CLINICAL_FOLDER_PATH = os.path.join(
    disk_location, "MIMIC-IV Clinical Database")
CXR_FOLDER_PATH = os.path.join(
    disk_location, "MIMIC-CXR-JPG", "physionet.org", "files", "mimic-cxr-jpg", "2.0.0")
CXR_DICOM_FOLDER_PATH = os.path.join(
    disk_location, "MIMIC-CXR", "physionet.org", "files", "mimic-cxr", "2.0.0")
EYEGAZE_FOLDER_PATH = os.path.join(
    disk_location, "eye-gaze-data-for-chest-x-rays-1.0.0")
REFLACX_FOLDER_PATH = os.path.join(disk_location, "reflacx-reports-and-eye-tracking-data-for-localization-of-abnormalities-in-chest-x-rays-1.0.0",
                                   "reflacx-reports-and-eye-tracking-data-for-localization-of-abnormalities-in-chest-x-rays-1.0.0")
XAMI_MIMIC_PATH = os.path.join(disk_location, "XAMI-MIMIC")
XAMI_SPREADSHEET_FOLDER_PATH = os.path.join(XAMI_MIMIC_PATH, "speadsheets")
