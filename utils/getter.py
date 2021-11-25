def get_subjectId_and_stayId_by_dicomId(cxr_df, dicom_id):
    matches = cxr_df[cxr_df['dicom_id'] == dicom_id]

    if (len(matches)> 0):
        return matches.iloc[0]['subject_id'], matches.iloc[0]['stay_id']

    return None

def get_cxr_match_by_dicom_ids(cxr_df, dicom_ids):
    matches = cxr_df[cxr_df['dicom_id'].isin(dicom_ids)]
    return matches

def get_stayId(cxr_df, dicom_id):
    matches = cxr_df[cxr_df['dicom_id'] == dicom_id]

    if (len(matches)> 0):
        return matches.iloc[0]['stay_id']
        
    return None

def get_stayId_string(cxr_df, dicom_id):
    stay_id =  get_stayId(cxr_df, dicom_id)
    if (stay_id is None):
        return None
    
    return str(stay_id)