# MIMIC-Eye: Integrating MIMIC Datasets with REFLACX and Eye Gaze for Multimodal Deep Learning Applications

## Folder structure
```
patient_{patient_id}/
     Core/
          patients.csv
          transfer.csv
     CXR-JPG/
          cxr_chexpert.csv
          cxr_meta.csv
          cxr_negbio.csv
          cxr_split.csv
          s{study_id}/
               {dicom_id-1}.jpg
     ED/
          diagnosis.csv
          edstays.csv
          pyxis.csv
          triage.csv
     REFLACX/
          metadata.csv
          P{reflacx_id}\
               anomaly_location_ellipses.csv
               chest_bounding_box.csv
               fixations.csv
               timestamps_transcription.csv
               transcription.txt
     EyeGaze/
          audio_segmentation_transcripts\
               {dicom_id}\
                    aortic_knob.png
                    left_lung.png
                    mediastanum.png
                    right_lung.png
                    audio.mp3
                    audio.wav
                    transcript.json
          bounding_boxes.csv
          fixations.csv
          master_sheet.csv
spreadsheets\
     cxr_meta_with_stay_id_only.csv
     cxr_meta.csv
     EyeGaze\
          bounding_boxes.csv
          fixations.csv
          master_sheet_with_updated_stayId.csv
     REFLACX\
          metadata.csv
     CXR-JPG\
          cxr_chexpert.csv
          cxr_negbio.csv
          cxr_split.csv

           
```


Let's try describe each folder first. layer by layer.


In the root folder, The folders are arranged according to the patient's id. The information related to the patient extracted from parent datasets  is stored in the folders. And, the spreadsheets folder is then used to store the data correspond to the whole dataset.


### More things to include 
1. Radiology report from MIMIC-CXR.
2. The data from each module. 
3. Only include the JPG file but not the DICOM.
4. gaze data from REFLACX and EyeGaze
