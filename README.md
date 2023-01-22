# MIMIC-Eye: Integrating MIMIC Datasets with REFLACX and Eye Gaze for Multimodal Deep Learning Applications

## Folder structure
```
patient_{subject_id}/
     Hsop/
     ICU/
     ED/
     CXR-JPG/
     CXR-DICOM/
     REFLACX/
     EyeGaze/

spreadsheets/
     CXR-JPG/
     Hosp/
     REFLACX/
     EyeGaze/ 
     ICU/
     cxr_meta.csv
```
     cxr_meta_with_stay_id_only.csv

```
patient_{patient_id}/
     Hsop/
          admissions.csv
          diagnoses_icd.csv
          drgcodes.csv
          labevents.csv
          microbiologyevents.csv
          omr.csv
          pharmacy.csv
          poe.csv
          poe_detail.csv
          prescriptions.csv
          procedures_icd.csv
          services.csv
          transfers.csv
     ICU/
          chartevents.csv         
          datetimeevents.csv      
          icustays.csv            
          ingredientevents.csv    
          inputevents.csv         
          outputevents.csv        
          procedureevents.csv
     ED/
          diagnosis.csv   
          edstays.csv     
          medrecon.csv    
          pyxis.csv       
          triage.csv      
          vitalsign.csv
     CXR-JPG/
          cxr_chexpert.csv
          cxr_meta.csv
          cxr_negbio.csv
          cxr_split.csv
          s{study_id}/
               {dicom_id}.jpg
     CXR-DICOM/
          s{study_id}.txt
     REFLACX/
          gaze_data/
               {reflacx_id}/
                    gaze.csv
          main_data/
               {reflacx_id}/
                    anomaly_location_ellipses.csv
                    chest_bounding_box.csv
                    fixations.csv
                    timestamps_transcription.csv
                    transcription.txt
          metadata.csv
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
          eye_gaze.csv
          fixations.csv
          master_sheet.csv
spreadsheets\
     CXR-JPG\
          cxr_chexpert.csv
          cxr_negbio.csv
          cxr_split.csv
     Hosp\
          d_hcpcs.csv
          d_icd_diagnoses.csv
          d_icd_procedures.csv
          d_labitems.csv                        
     REFLACX\
          metadata.csv              
     EyeGaze\ 
          bounding_boxes.csv
          eye_gaze.csv
          fixations.csv
          master_sheet_with_updated_stayId.csv                               
     ICU\
          d_items.csv                            
     cxr_meta.csv
     cxr_meta_with_stay_id_only.csv
```


Let's try describe each folder first. layer by layer.


In the root folder, The folders are arranged according to the patient's id. The information related to the patient extracted from parent datasets  is stored in the folders. And, the spreadsheets folder is then used to store the data correspond to the whole dataset.

spreadsheets/
     Except the folder for patients, we also created a spreadsheet folder to store global information or table not related to patients. One important table we created for 

If the paitents miss some folders, they don't have related information in that module.  
If the patients miss some folders, then they don't have related information in that module.

Except the folder for patients, we also created a spreadsheet folder to store global information or table not related to patients. One important table we created for

Another cxr_meta.csv

​

  

 

patient_{patient_id}/ Core/ patients.csv transfer.csv CXR-JPG/ cxr_chexpert.csv cxr_meta.csv cxr_negbio.csv cxr_split.csv s{study_id}/ {dicom_id-1}.jpg ED/ diagnosis.csv edstays.csv pyxis.csv triage.csv REFLACX/ metadata.csv P{reflacx_id}\ anomaly_location_ellipses.csv chest_bounding_box.csv fixations.csv timestamps_transcription.csv transcription.txt EyeGaze/ audio_segmentation_transcripts\ {dicom_id}\ aortic_knob.png left_lung.png mediastanum.png right_lung.png audio.mp3 audio.wav transcript.json bounding_boxes.csv fixations.csv master_sheet.csv

 

In the root folder, folders are arranged according to the patient's ID. The information related to the patient extracted from parent datasets is stored in the folders. And, the spreadsheets folder is then used to store the data associated with the whole dataset.

 

Patient

 

In each patient folder, several folders can be seen. Each of them contains tables extracted from a module or dataset. If the patients miss some folders, then they don't have related information in that module The following describe the information contained in these folders:

 

Core: It contains demographics for patients and tracking information for ward stays.

Hosp: This folder includes data derived from the hospital wide EHR, which stores measurements during the hospital stay.

ICU: ICU level data contains information related to items and events occurring during the ICU stay, including patients' input and output events.

ED: This folder stores the information extracted from MIMIC-IV-ED, which contains the patients' data collected while they are in the emergency department. The triage assessment in this folder is a vital piece of clinical evidence for human radiologists to use when diagnosing patients.

MIMIC-CXR: This folder contains radiology reports retrieved from the MIMIC-CXR dataset. This dataset contains chest X-ray images in DICOM format, which is the standard format used in hospitals. Nevertheless, this format is not feasible for machine learning models. We then retrieve the images from the MIMIC-CXR-JPG dataset instead, which has CXRs in JPG format.

MIMIC-CXR-JPG: The folder contains the chest X-ray images in JPG format, which are ready for machine models to process. Their DICOM metadata is also converted into CSV files and stored here.

REFLACX: The folder contains information collected from five radiologists while they were reading chest X-ray images. REFLACX asked radiologists to annotate the lesions in CXR images using ellipses. During the process of interpretation, radiologists' eye movements and utterances are also collected. The utterances are then transformed into time-stamped transcriptions. Lastly, this folder also contains chest bounding boxes indicating the lung and heart areas.

EyeGaze: EyeGaze folder contains data extracted from the Eye Gaze dataset. As with the REFLACX dataset, it also records audio and eye movements during interpretation. The Eye Gaze dataset only contains information generated by a radiologist, while REFLACX has five radiologists involved. Moreover, this folder provides segmentation and bounding boxes for anatomical structures as supplemental sources for further analysis of the correlation with anatomical structures.

 

Spreadsheets

 



# Background



Medical image diagnosis is the process or task of identifying lesions or diseases, based on reading and interpreting medical images, such as chest X-ray images, CT scans or MRI scans. The skills and knowledge of performing this task are owned by specialists, such as doctors or radiologists. However, statistics showed a 6.4 million, 30.6 million, and 2.9 million worldwide shortage of physicians, nurses, and pharmacists respectively in 2019. Due to the disproportionate impact of the pandemic on healthcare workers, the situation has become more dire. One solution to alleviate the shortage is to adopt AI-driven diagnostic systems to facilitate the process.

Deep Learning (DL) technology is widely used to deliver promising results in AI-driven systems. Its excellent performance is highly commensurate with the quality and quantity of the dataset that the model is trained on. In medical image diagnosis, DL approaches have proven effective and efficient. Several studies have achieved human-level performance by applying DL to medical image tasks (%some references here).

Multi-label learning, multi-task learning, and contrastive learning are currently the most common deep learning technologies. They use a variety of modalities in the output and input layers to improve DL models. Multimodal learning uses different modalities as input to the model, which allows the model to perceive various aspects of a phenomenon and comprehend the input scenario better. The term "\textit{modality}" is then used to describe the collected information from each sensor. When several different instruments are set up to observe a phenomenon, the information collected is known as \textit{multi-modal} data \citep{Lahat2015MultiModalDataFusion, Ramachandram2017DeepMultiModalSurvey}. In multi-task learning, the model is trained through a variety of tasks, which require many modalities as labels. Contrastive learning is a self-supervised technique, which trains the model to contrast inputs against each other by mapping modalities to a semantic vector space. All these technologies require multiple modalities in either input or output layers to perform.

The Medical Information Mart for Intensive Care (MIMIC) IV dataset is sourced from two in-hospital database systems, a custom hospital wide EHR and an ICU specific clinical information system, at Beth Israel Deaconess Medical Center (BIDMC) from 2011 to 2019. Multiple subsets of MIMIC-IV contain a variety of modalities. Two categories of data are critical for DL models to consider during building and training. The first type is the patient's clinical information. According to \citet{Castillo21}, clinical data is highly informative and essential for radiologists to interpret and diagnose properly. Secondly, there is the information that is gathered when radiologists are making diagnoses, including eye-tracking data, audio recordings, and time-stamped transcriptions. Since medical diagnosis is a skill that is only owned by experts, it is beneficial for models to learn the diagnosis pattern from them. This category allows us to explore the decision-making process that radiologists go through while interpreting medical images.

In this work, we propose a strategy to integrate the valuable modalties from MIMIC-IV and its subsets. Several studies have attempted to involve more modalities in their training process since multi-modal, multi-task, and contrastive learning became popular and effective. However, the standard for constructing a dataset with various modalities has not been created, which hinders comparison between different studies. To enhance the convenience and reproducibility of medical image diagnosis, it is crucial to have a single dataset with available modalities.

Five datasets are used to construct the MIMIC-Eye dataset, including MIMIC-IV, MIMIC-IV-ED, MIMIC-CXR, Eye Gaze, and REFLACX datasets. Each of them contains valuable information about patients and radiologists. MIMIC-IV and MIMIC-IV-ED provide information about the patient's clinical data. MIMIC-CXR provides the medical image and radiology report, which are considered as the input and output of the model respectively. The labels commonly used to train DL models are extracted from these reports via Nature Language Processing (NLP) labelers. REFLACX and Eye Gaze datasets collect eye-tracking data and audio when radiologists are reading images. REFLACX dataset also asked radiologists to manually annotate lesions by using bounding boxes to locate lesions, which gives the required label types for performing object/lesion detection. The normal image diagnosis task can only tell what lesions are present in a given image, whereas lesion detection can also indicate their locations.

To summarise, the key contributions of this work are:

Provide a single source dataset with various modalities.

Provide a scalable strategy to combine datasets related to MIMIC-IV.

Provide a ready-to-train dataset to simplify the process before training.

Provide a strategy to preprocess those five datasets.




# "##" -> means it go to spreadsheets folder

# Hosp module 
admissions
## d_hcpcs
## d_icd_diagnoses
## d_icd_procedures
## d_labitems
diagnoses_icd
drgcodes
emar
emar_detail
hcpcsevents
labevents
microbiologyevents
omr
patients
pharmacy
poe
poe_detail
prescriptions
procedures_icd
services
transfers

# ICU module
chartevents			
## d_items				
datetimeevents		     
icustays
ingredientevents
inputevents
outputevents
procedureevents

# ED module

diagnosis
edstays
medrecon
pyxis
triage
vitalsign

# CXR module

Chest X-ray images (.DICOM)
mimic-cxr-reports

# CXR-JPG module

Chest X-ray image (.JPG)

mimic-cxr-2.0.0-metadata
## mimic-cxr-2.0.0-chexpert
## mimic-cxr-2.0.0-negbio
## mimic-cxr-2.0.0-split

# REFLACX 
gaze_data
anomaly_location_ellipses
chest_bounding_box
fixations
timestamps_transcription
transcription (plain text)
## metadata

# EyeGaze

anotomical segmentations
audio
transcript
bounding_boxes (chest)
eye_gaze
fixations
## master_sheet # mention the stay_id is updated.



# The second figure is to explain how stay_id is indentified.




# Purpose of assigning them into each patient folder:
then when users are checking information of the patients, they do not need to work with a spreadsheet, which has enormerous instances to slow down the process. 

# 