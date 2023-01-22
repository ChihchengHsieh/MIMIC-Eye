<pre>
<code>patient_{patient_id}/
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
           </code></pre>

<p>In the root folder, folders are arranged according to the patient&#39;s ID. The information related to the patient extracted from parent datasets is stored in the folders. And, the spreadsheets folder is then used to store the data associated with the whole dataset.</p>

<p>&nbsp;</p>

<h3><strong>Patient</strong></h3>

<p>In each patient folder, several folders can be seen. Each of them contains tables extracted from a module or dataset. If the patients miss some folders, then they don&#39;t have related information in that module. The following describes the information contained in these folders:</p>

<ul>
	<li>
	<p><strong>Core</strong>: This folder is derived from the <a href="https://physionet.org/content/mimiciv/2.0/">MIMIC-IV</a> Hosp module, which contains demographics for patients, tracking information for ward stays, and measurements during the hospital stay.</p>
	</li>
	<li>
	<p><strong>ICU</strong>: This folder is retreived from the <a href="https://physionet.org/content/mimiciv/2.0/">MIMIC-IV</a> ICU module including ICU level data contains information related to items and events occurring during the ICU stay, including patients&#39; input and output events.</p>
	</li>
	<li>
	<p><strong>ED</strong>: This folder is obtained from <a href="https://physionet.org/content/mimic-iv-ed/2.0/">MIMIC-IV-ED</a>, which contains the patients&#39; data collected while they are in the emergency department. The triage assessment in this folder is a vital piece of clinical evidence for human radiologists to use when diagnosing patients.</p>
	</li>
	<li>
	<p><strong>MIMIC-CXR</strong>: This folder contains radiology reports retrieved from the <a href="https://physionet.org/content/mimic-cxr/2.0.0/">MIMIC-CXR</a> dataset. This dataset contains chest X-ray images in DICOM format, which is the standard format used in hospitals. Nevertheless, this format is not feasible for machine learning models. We then retrieve the images from the MIMIC-CXR-JPG dataset instead, which has CXRs in JPG format.</p>
	</li>
	<li>
	<p><strong>MIMIC-CXR-JPG</strong>: The folder includes chest X-ray images in JPG format, which are retrieved from the <a href="https://physionet.org/content/mimic-cxr-jpg/2.0.0/">MIMIC-CXR-JPG</a> dataset. This format is ready for machine models to process. Their DICOM metadata is also converted into CSV files and stored here.</p>
	</li>
	<li>
	<p><strong>REFLACX</strong>: The folder contains information collected from five radiologists while they were reading chest X-ray images. <a href="https://physionet.org/content/reflacx-xray-localization/1.0.0/">REFLACX</a> asked radiologists to annotate the lesions in CXR images using ellipses. During the process of interpretation, radiologists&#39; eye movements and utterances are also collected. The utterances are then transformed into time-stamped transcriptions. Lastly, this folder also contains chest bounding boxes indicating the lung and heart areas.</p>
	</li>
	<li>
	<p><strong>EyeGaze</strong>:&nbsp;The EyeGaze folder contains data extracted from the <a href="https://physionet.org/content/egd-cxr/1.0.0/">Eye Gaze</a> dataset. As with the REFLACX dataset, it also records audio and eye movements during interpretation. The Eye Gaze dataset only contains information generated by a radiologist, while REFLACX has five radiologists involved. Moreover, this folder provides segmentation and bounding boxes for anatomical structures as supplemental sources for further analysis of the correlation with anatomical structures.</p>
	</li>
</ul>

<p>&nbsp;</p>

<h3><strong>Spreadsheets</strong></h3>

<p>We also created a spreadsheet folder to store information or tables that are not related to a specific patient. The file, cxr_meta.csv, is extended from the original <code>metadata.csv</code> in MIMIC-CXR-JPG. In this file, three columns are added:</p>

<ul>
	<li><code>stay_id</code>: With this stay_id associated with chest X-ray images, the image can then be linked to corresponding clinical data in the MIMIC-IV-ED dataset.</li>
	<li><code>in_reflacx</code>: A boolean value indicating whether this image is used in the REFLACX dataset.</li>
	<li><code>in_eye_gaze</code>: A boolean value indicating whether this image is used in the Eye Gaze dataset.</li>
</ul>


