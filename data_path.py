import os

# disk_location = "D:/"
disk_location = "/Users/jrhs/Desktop/"

# /Users/jrhs/Desktop/
# disk_location = "/Volumes/Seagate Backup "



# Define the path for all of the folders.
PHYSIONET_PATH = os.path.join(disk_location, "physionet.org/files/")
ED_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "mimic-iv-ed/2.0/ed/")
MIMICIV_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "mimiciv/2.0/")
ICU_FOLDER_PATH = os.path.join(MIMICIV_FOLDER_PATH, "icu/")
HOSP_FOLDER_PATH = os.path.join(MIMICIV_FOLDER_PATH, "hosp/")
CXR_DICOM_FOLDER_PATH = os.path.join(PHYSIONET_PATH, )
CXR_JPG_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "mimic-cxr-jpg/2.0.0")
EYEGAZE_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "egd-cxr/1.0.0/")
REFLACX_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "reflacx-xray-localization/1.0.0/")
CXR_REPORT_FOLDER_PATH = os.path.join(PHYSIONET_PATH, "mimic-cxr-reports/")

# Store place.

XAMI_MIMIC_PATH = "./mimic-eye"
XAMI_SPREADSHEET_FOLDER_PATH = os.path.join(XAMI_MIMIC_PATH, "spreadsheets")

# ED_FOLDER_PATH = os.path.join(disk_location, "MIMIC-IV ED")
# CLINICAL_FOLDER_PATH = os.path.join(
#     disk_location, "MIMIC-IV Clinical Database")
# CXR_FOLDER_PATH = os.path.join(
#     disk_location, "MIMIC-CXR-JPG", "physionet.org", "files", "mimic-cxr-jpg", "2.0.0")
# CXR_DICOM_FOLDER_PATH = os.path.join(
#     disk_location, "MIMIC-CXR", "physionet.org", "files", "mimic-cxr", "2.0.0")
# EYEGAZE_FOLDER_PATH = os.path.join(
#     disk_location, "eye-gaze-data-for-chest-x-rays-1.0.0")
# REFLACX_FOLDER_PATH = os.path.join(disk_location, "reflacx-reports-and-eye-tracking-data-for-localization-of-abnormalities-in-chest-x-rays-1.0.0")
# XAMI_MIMIC_PATH = os.path.join(disk_location, "XAMI-MIMIC")
# # XAMI_MIMIC_PATH = "./XAMI-MIMIC"
# XAMI_SPREADSHEET_FOLDER_PATH = os.path.join(XAMI_MIMIC_PATH, "spreadsheets")
    

# /Volumes/LaCie/physionet.org/files/mimic-iv-ed/2.0/ed