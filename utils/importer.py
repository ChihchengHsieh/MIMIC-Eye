import os
from data_path import XAMI_MIMIC_PATH
from tqdm.notebook import tqdm


def import_to_stay_folder(cxr_df, import_df, save_folder_name, save_table_name, import_df_stay_key="stay_id"):
    all_cxr_stay_ids = set(cxr_df['stay_id'])

    # get the stay_id that are valid in the import df
    valid_stay_ids = [id for id in list(
        set(import_df[import_df_stay_key])) if id in all_cxr_stay_ids]

    valid_stay_ids.sort()

    # foreach stay_id, we import the data to its folder
    for stay_id in tqdm(valid_stay_ids):

        # Create the folder for this stay.
        matches = import_df[import_df[import_df_stay_key] == stay_id]

        if (len(matches) < 1):
            raise StopIteration("Should have matches in the CXR meta table")

        # Find who is the subject_id
        subject_id = matches.iloc[0]['subject_id']

        # Create a folder for this stay
        save_folder_path = os.path.join(
            XAMI_MIMIC_PATH, f"patient_{subject_id}", f"stay_{stay_id}", save_folder_name)
        os.makedirs(save_folder_path, exist_ok=True)

        # Store the matches in the folder.
        matches.to_csv(os.path.join(
            save_folder_path, f"{save_table_name}.csv"))


def import_to_patient_folder(cxr_df, import_df, save_table_name, import_df_subject_id="subject_id"):
    all_cxr_subjet_ids = set(cxr_df['subject_id'])

    # get the stay_id that are valid in the import df
    valid_subject_ids = [id for id in list(
        set(import_df[import_df_subject_id])) if id in all_cxr_subjet_ids]

    valid_subject_ids.sort()

    # foreach stay_id, we import the data to its folder
    for subject_id in tqdm(valid_subject_ids):

        # Create the folder for this stay.
        matches = import_df[import_df[import_df_subject_id] == subject_id]

        if (len(matches) < 1):
            raise StopIteration("Should have matches in the CXR meta table")

        # Create a folder for this stay
        save_folder_path = os.path.join(
            XAMI_MIMIC_PATH, f"patient_{subject_id}")
        os.makedirs(save_folder_path, exist_ok=True)

        # Store the matches in the folder.
        matches.to_csv(os.path.join(
            save_folder_path, f"{save_table_name}.csv"))


def import_to_patient_sub_folder(cxr_df, import_df, subfolder_name, save_table_name, import_df_subject_id="subject_id"):
    all_cxr_subjet_ids = set(cxr_df['subject_id'])

    # get the stay_id that are valid in the import df
    valid_subject_ids = [id for id in list(
        set(import_df[import_df_subject_id])) if id in all_cxr_subjet_ids]

    valid_subject_ids.sort()

    # foreach stay_id, we import the data to its folder
    for subject_id in tqdm(valid_subject_ids):

        # Create the folder for this stay.
        matches = import_df[import_df[import_df_subject_id] == subject_id]

        if (len(matches) < 1):
            raise StopIteration("Should have matches in the CXR meta table")

        # Create a folder for this stay
        save_folder_path = os.path.join(
            XAMI_MIMIC_PATH, f"patient_{subject_id}", subfolder_name)
        os.makedirs(save_folder_path, exist_ok=True)

        # Store the matches in the folder.
        matches.to_csv(os.path.join(
            save_folder_path, f"{save_table_name}.csv"))
