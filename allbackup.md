<p>Deep learning technologies have been widely adopted in medical imaging due to their ability to extract features from images and make accurate diagnoses automatically. Medical imaging technologies are particularly useful because they can be trained to detect subtle differences in images that are hard to detect for human radiologists. In the real world, radiologists must rely on various types of patient information to assess medical images confidently. However, most DL applications in medical imaging only utilize image data, mainly because the literature on medical datasets combining different data modalities is scarce. In this study, we present MIMIC-EYE, a dataset that encompasses a comprehensive integration of several datasets related to MIMIC. This dataset includes a comprehensive range of patient information, including medical images and reports (MIMIC CXR and MIMIC JPG), clinical data (MIMIC IV ED), a detailed account of the patient&#39;s hospital journey (MIMIC IV), and eye tracking data containing gaze information and pupil dilations together with image annotations (REFLACX and EYE GAZE). Integrating eye tracking data with the various MIMIC modalities may provide a more comprehensive understanding of radiologists&#39; visual search behavior patterns and facilitate the development of more robust, accurate, and reproducible deep-learning models for medical imaging diagnosis.</p>


<p>Medical image diagnosis is the task of identifying lesions and diseases based on medical images, such as chest X-ray images, CT scans or MRI scans. The skills and knowledge of performing this task are owned by specialists, such as doctors and radiologists. However, statistics [1] showed a 6.4 million, 30.6 million, and 2.9 million worldwide shortage of physicians, nurses, and pharmacists respectively in 2019. Due to the disproportionate impact of the pandemic on healthcare workers, the situation has become more dire. One potential solution to alleviate this shortage is to adopt AI-driven diagnostic systems to facilitate the process.</p>

<p>In AI-driven systems, deep learning (DL) is a popular technique for delivering promising results. Deep learning is based on neural networks, which is a computing system that imitates the biological nerve systems in animal brains. In medical image diagnosis, DL approaches have proven effective and efficient. Several studies have achieved or even surpassed human-level performance by applying DL to medical image tasks, such as breast imaging [2, 3], left ventricular assessment [4, 5], dermoscopy analysis [6, 7],and chest X-Rays [8 &ndash; 11]. DL learns knowledge from the dataset it is trained on. This means its performance is highly commensurate with the quality and quantity of the dataset.</p>

<p>Except for providing more robust data to DL models, exposing other aspects of instances to the model can also be beneficial. Multi-modal learning, multi-task learning, and contrastive learning are three popular deep learning technologies. A variety of modalities are employed to better describe or extend the scenarios to models, which enhances their performance and generalisation. Multimodal learning involves more than one input modality, which allows the model to perceive various aspects of the input phenomenon and comprehend the scenario better. The term &quot;<strong>modality</strong>&quot; is then used to describe the collected information from each sensor. When several different sensors are set up to observe a phenomenon, the information collected is known as <strong>multi-modal data</strong> [12, 13]. In multi-task learning, the model is trained through multiple tasks, which require various types of labels. When a model is learned from more than one task, it will accommodate each task and generalise better. Contrastive learning is a self-supervised technique, which trains the model to contrast its inputs against each other by mapping different modalities to the same semantic vector space. All these techniques take advantage of the additional information given by the variety of modalities. &nbsp;</p>

<p>The Medical Information Mart for Intensive Care (MIMIC) IV dataset [14] is the dataset used in this work, which is sourced from two in-hospital database systems, a custom hospital wide EHR and an ICU specific clinical information system, at Beth Israel Deaconess Medical Center (BIDMC) from 2011 to 2019. Since the popularity of the MIMIC-IV dataset, several of its subsets have been built to provide additional information and modalities. Two categories of additional data are crucial to include in research. The first type is the patient&#39;s <strong>clinical data</strong>. Clinical data is highly informative and essential for radiologists to diagnose precisely [15]. The second type of data is <strong>human-centric data</strong>, which is gathered when radiologists are making diagnoses. This includes eye-tracking data, audio recordings, and time-stamped transcriptions. Since medical diagnosis is a skill owned by experts, it is beneficial to study and analyse their diagnosis patterns. Human-centric data allows us to explore the decision-making process that radiologists undertake while interpreting medical images.</p>

<p>&nbsp;</p>

<p>In this work, we present MIMIC-Eye, which integrates valuable modalities from MIMIC-IV [14] and its subsets. Several studies have attempted to involve more than one modality in their training process since multi-modal, multi-task, and contrastive learning became popular and effective. However, the approach to construct a multi-modal dataset for MIMIC-IV has not been standardized. Studies applied different preprocessing and integration strategies, which hinders comparisons between them. To enhance the reproducibility and convenience of medical image diagnosis, it is indispensable to have a dataset with all available modalities, which results in the MIMIC-Eye dataset.&nbsp;</p>

<p>Five datasets are used to construct the MIMIC-Eye dataset, including MIMIC-IV [14], MIMIC-IV-ED [16], MIMIC-CXR [17], Eye Gaze [18], and REFLACX [19] datasets.&nbsp;Each of them contains useful information about patients or radiologists. MIMIC-IV and MIMIC-IV-ED provide clinical data about patients. MIMIC-CXR provides Chest X-Ray (CXR) images and radiology reports. The radiology reports can be used with Nature Language Processing (NLP) labelers to generate labels for CXR images. The REFLACX and Eye Gaze datasets collected eye-tracking data and audio when radiologists were reading images. The REFLACX dataset also asked radiologists to manually annotate lesions using bounding ellipses. In this work, we integrate the mentioned modalities from different datasets to create the MIMIC-Eye dataset. The key contributions are:</p>

<p>&nbsp;</p>

<ul>
	<li>MIMIC-Eye allows researchers to explore and study the relationships between modes.</li>
	<li>It has integrated clinical data, which simulates the same situation as radiologists have in practice.&nbsp;</li>
	<li>MIMIC-Eye contains human-centric data, which allows the exploration of diagnosis patterns by radiologists.</li>
	<li>We fixed some data quality issues in the REFLACX and EyeGaze datasets.</li>
	<li>MIMIC-Eye is a patient-level dataset that each patient has their own folder to store information and modalties related to them. This is more intuitive and memory-efficient for debugging and researching.</li>
	<li>We provide a single-source and ready-to-train dataset to ensure reproducibility and facilitate the training of AI models.<br />
	&nbsp;</li>
</ul>

<p>&nbsp;</p>

<p>In this section, we first present you a brief introduction to the valuable modalities in the MIMIC-IV dataset. Then we propose a strategy for preprocessing and integrating various modalities in the MIMIC-IV, MIMIC-IV-ED, MIMIC-CXR, REFLACX, and Eye Gaze datasets. The challenges and the issues we encountered are also mentioned in this section.&nbsp;</p>

<h3>Clinical and Human-Centred Data</h3>

<p>The MIMIC-Eye dataset was initially motivated by two types of data. The first type is the patient&#39;s clinical information relevant to the chest X-ray image. By including clinical data in the dataset, this allows the model to take into account clinical information related to patients, such as body temperature, heart rate, and blood pressure. This is the same approach radiologists apply in their daily work. To make an accurate diagnosis, they need clinical data to provide comprehensive information. For example, while Ateletasis looks identical to Consolidation on the radiograph, Consolidation usually comes with infection. Body temperature plays a crucial role in classifying them in this case.&nbsp;</p>

<p>Totally, ten clinical features are used in this work. The <strong>MIMIC-IV Core </strong><em>patients&nbsp;</em>table includes only two clinical attributes, age and gender. And, the other eight clinical features are extracted from the MIMI-IV ED <em>traige</em>&nbsp;table. The explanations for these eight clinical features in the MIMIC-IV documentation are:</p>

<ol>
	<li><code>temperature</code>: The patient&rsquo;s temperature in degrees Fahrenheit.</li>
	<li><code>heartrate</code>: The patient&rsquo;s heart rate in beats per minute.</li>
	<li><code>resprate</code>: The patient&rsquo;s respiratory rate in breaths per minute.</li>
	<li><code>o2sat</code>: The patient&rsquo;s peripheral oxygen saturation as a percentage.</li>
	<li><code>sbp</code>, <code>dbp</code>: The patient&rsquo;s systolic and diastolic blood pressure, respectively, measured in millimetres of mercury (mmHg).</li>
	<li><code>pain</code>: The level of pain self-reported by the patient, on a scale of 0-10.</li>
	<li><code>acuity</code>: An order of priority. Level 1 is the highest priority, while level 5 is the lowest priority.</li>
</ol>

<p>The second type of data is human-centred data, which are collected while radiologists are reading chest X-ray images and making diagnoses. There are primarily two modalities included in the REFLACX and EyeGaze datasets, including time-stamped transcripts and eye-tracking data. Additionally, the bounding boxes annotated by radiologists that indicate lesions can be accessed from the REFALCX dataset. As the MIMIC-IV dataset only includes global labels extracted from corresponding radiology reports, it can only train the model to make diagnoses from a global perspective. With the ground-truth bounding boxes from REFLACX, the model can be used to perform object/lesion detection to locate pathology.</p>

<h3>IDs used in the MIMIC-IV</h3>

<p>Before explaining the creation process, it is necessary to introduce some important IDs and tables in the MIMIC-IV dataset. Four important IDs are used in MIMIC-IV to link the information across tables. They are:</p>

<ul>
	<li><em><strong>subject_id (patient_id)</strong></em>: ID specifying an individual patient.</li>
	<li><em><strong>stay_id</strong></em>: ID specifying a single emergency department stay for a patient.</li>
	<li><em><strong>study_id</strong></em>: ID specifying a radiology report written for the given chest x-ray. It is rarely mentioned because we do not use the report as the groundtruth label in this paper.</li>
	<li><em><strong>dicom_id</strong></em>: ID specifying a chest x-ray image (radiograph).</li>
</ul>

<h3>MIMIC-Eye Construction</h3>

<p>In this part, we describe the methods we used to build the MIMIC-Eye dataset. The overall process is divided into the following three phases:</p>

<ol>
	<li><strong><em>stay_id</em> identification</strong>: This process is inspired by the EyeGaze dataset. In their work, they showed us the approach to identifying <em>stay_id</em>&nbsp;for CXR images. After this, we also updated the <em>stay_id</em> in EyeGaze since they used an outdated version of the dataset, which is incompatible with the <em>stay_id</em> in v2.0.</li>
	<li><strong>Pre-processing each module</strong>: In this phase, we pre-processed datasets to make them ready for merging with others. The issues we encountered will also be mentioned and fixed here. To ensure that the dataset is scalable and flexible, a minimum amount of preprocessing is done for MIMIC-Eye, which allows users to choose the preprocessing they need for their task. And MIMIC-Eye only fixes bugs or errors that can be solved with a particular approach.&nbsp;</li>
	<li><strong>Integration</strong>: At the end, we combine all the datasets and modalities into a single source with a specific folder structure.</li>
</ol>

<p><strong>Phase 1 - <em>stay_id</em> identification</strong></p>

<p>As we mentioned in previously the <em>stay_id</em>&nbsp;is used to identify stays in the emergency department. However, the MIMIC-CXR dataset only offers images&#39; <em>subject_id</em> but not their <em>stay_id</em>, which causes a dilemma in retrieving the corresponding clinical data from <strong>MIMIC-IV-ED</strong>. To solve this issue, two tables, <strong>MIMIC-IV-ED</strong>&nbsp;<em>edstays</em>&nbsp;and <strong>MIMIC-IV-CXR-JPG</strong> <em>metadata</em>, are used to identify <em>stay_id</em> for CXR images through the following steps:</p>

<ol>
	<li>For each CXR image, we first search for stays that belong to the patient.&nbsp;</li>
	<li>For each stay, we simply search their time-spans in the MIMIC-IV-ED <em>edstays</em> table, which can tell us when is the start (<em>intime</em>) and end (<em>outtime</em>) time of a stay.</li>
	<li>Once we obtain the time-span of the stay, we then check what time the radiograph was captured. In the MIMIC-CXR-JPG metadata table, the <em>StudyDate</em> and <em>StudyTime</em>&nbsp;columns can tell us the exact time that the radiograph was taken.</li>
	<li>Having the duration of the stay and the time the radiograph was taken, we can determine whether this radiograph was taken during the stay. If the time point of the radiograph falls within the time-span, then its $stay\_id$ is found. If not, we continue looking for the patient&#39;s stays with the time-span containing the time point.</li>
</ol>

<p>Mathematically, Let&nbsp;<math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>i</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mi>C</mi> <mi>X</mi> <mi>R</mi> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{CXR}_{p,i}</annotation> </semantics> </math>&nbsp;be&nbsp;to be the time that a CXR image taken for patient&nbsp;<math> <semantics> <mi>p</mi> <annotation encoding="application/x-tex">p</annotation> </semantics> </math>&nbsp;at unknown stay <math> <semantics> <mi>i</mi> <annotation encoding="application/x-tex">i</annotation> </semantics> </math>. The&nbsp;<math> <semantics> <mi>i</mi> <annotation encoding="application/x-tex">i</annotation> </semantics> </math> is determined by:</p>

<div><math display="block"> <semantics> <mrow> <mi>i</mi> <mo stretchy="false">←</mo> <mi>j</mi> <mo>:</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>j</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>start</mtext> </mrow> </msubsup> <mo>&lt;</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>i</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>CXR</mtext> </mrow> </msubsup> <mo>&lt;</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>j</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>end</mtext> </mrow> </msubsup> <mo>,</mo> </mrow> <annotation encoding="application/x-tex">i \leftarrow j: T^{\text{start}}_{p,j} &lt; T^{\text{CXR}}_{p,i} &lt; T^{\text{end}}_{p,j},</annotation> </semantics> </math></div>

<p>where <math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>i</mi> <mo>,</mo> <mi>p</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>start</mtext> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{\text{start}}_{i,p}</annotation> </semantics> </math>&nbsp;and&nbsp;<math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>j</mi> <mo>,</mo> <mi>p</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>end</mtext> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{\text{end}}_{j,p}</annotation> </semantics> </math>&nbsp;are starting time and ending time of a stay respectively.</p>

<p>At this step, 55.99% of CXRs could not identify their <em>stay_id</em>, since the CXRs may have been taken after they left ED. To explore this issue, we ran different conditions to test how many instances would be lost in each condition. We found that when we increased the condition to 7 days, we could identify 23.26% more CXRs. The goal of this experiment is to use clinical information that is close to the time of the CXR. Therefore, only the CXRs taken <strong>within the range</strong>&nbsp;are used.</p>

<h4><strong>Phase 2 - Pre-processing each module</strong></h4>

<p>In this section, we describe the preprocessing we have done for each module. For most of the data quality issues in the parent datasets, we left them to users to decide what techniques to apply. We only provide minimum preprocessing to a few issues that significantly affect the dataset. Below, we list the modules that we have preprocessed:</p>

<ul>
	<li><strong>REFLACX</strong>: The REFLACX dataset provides two versions of labels for radiologists to use when annotating the same lesion.&nbsp;The REFLACX dataset contains 3052 cases in total. 2757 of them are annotated with v1 labels, and the other 295 cases use v2 labels. To make the dataset concise, we interviewed radiologists and used their opinion to merge the labels from two versions, which resolves conflicts. At the end, we have 21 types of classes (lesions) left.&nbsp;</li>
	<li><strong>EyeGaze</strong>: Because we consider raw gaze information to be equally valuable to investigate as fixations, we have also included it in the MIMIC-Eye dataset. However, some values of <em>DICOM_ID</em>&nbsp;in <em>eye_gaze.csv</em>&nbsp;had been trimmed with the last 5 digits, which makes them unrelatable to their chest X-ray images. In some cases, both incorrect and valid IDs exist in the table. And the erroneous one is usually shorter than the correct one. In order to fix the data quality issue, we then delete the faulty ID if both the valid and the faulty ID are present. When only the faulty ID appears in the table, it is replaced with the valid one.</li>
</ul>

<h4><strong>Phase 3 - Integration</strong></h4>

<p>MIMIC-Eye is designed so that each patient has their own folder in which they can store their own information. These folders are named as <em>subject_id</em>. Using a patient-level folder structure instead of a stay-level folder structure is found to be more intuitive and more convenient for human users. Information related to the patient can now be easily accessed in the same folder, which considerably simplifies the debugging process. For radiologists, it is easier for them to check the patient&#39;s clinical data or history. Additionally, we have another folder, called <em>spreadsheets</em>, that contains information that is not related to a specific patient. For example, some tables store the definition of codes used in other tables.</p>

<p>Totally, seven MIMIC-IV modules are used to create MIMIC-Eye dataset, as shown in this <a href="https://github.com/ChihchengHsieh/MIMIC-Eye/blob/master/data_modules_assignment.png">Figure</a>. They are assigned to respective folders according to their purposes mentioned previously. &nbsp;</p>

<pre>
<code>patient_{patient_id}/
     Hosp/
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

<p>As shown above, in the root folder, folders are arranged according to the patient&#39;s ID. As mentioned in the previous section, we designed two types of folders in MIMIC-Eye:</p>

<p>&nbsp;</p>

<ul>
	<li><strong><em>patient_{subject_id}</em></strong>: This type of folder contains information related to a specific patient. There are up to 7 subfolders in a patient folder. Each sub-folder stores the data extracted from the respective MIMIC-IV module.&nbsp;</li>
	<li><em><strong>spreadsheets</strong></em>: While the patient folders hold information about patients. Other information is stored in this spreadsheet folder, such as the definition of codes. Other than that, this folder contains spreadsheets extracted directly from the module. Instead of dividing patients into their own folders, these spreadsheets contain information about all patients. Processing this kind of spreadsheet may occupy a huge amount of computer memory, but it can also minimise retrieval time in certain scenarios.&nbsp;</li>
</ul>

<h3><strong>Patient</strong></h3>

<p>In each patient folder, several folders can be seen. Each of them contains tables extracted from a module or dataset. If the patients miss some folders, then they don&#39;t have related information in that module. The following describes the information contained in these folders:</p>

<ul>
	<li>
	<p><strong>Core</strong>: This folder is derived from the <a href="/content/mimiciv/2.0/">MIMIC-IV</a> Hosp module, which contains demographics for patients, tracking information for ward stays, and measurements during the hospital stay.</p>
	</li>
	<li>
	<p><strong>ICU</strong>: This folder is retreived from the <a href="/content/mimiciv/2.0/">MIMIC-IV</a> ICU module including ICU level data contains information related to items and events occurring during the ICU stay, including patients&#39; input and output events.</p>
	</li>
	<li>
	<p><strong>ED</strong>: This folder is obtained from <a href="/content/mimic-iv-ed/2.0/">MIMIC-IV-ED</a>, which contains the patients&#39; data collected while they are in the emergency department. The triage assessment in this folder is a vital piece of clinical evidence for human radiologists to use when diagnosing patients.</p>
	</li>
	<li>
	<p><strong>MIMIC-CXR</strong>: This folder contains radiology reports retrieved from the <a href="/content/mimic-cxr/2.0.0/">MIMIC-CXR</a> dataset. This dataset contains chest X-ray images in DICOM format, which is the standard format used in hospitals. Nevertheless, this format is not feasible for machine learning models. We then retrieve the images from the MIMIC-CXR-JPG dataset instead, which has CXRs in JPG format.</p>
	</li>
	<li>
	<p><strong>MIMIC-CXR-JPG</strong>: The folder includes chest X-ray images in JPG format, which are retrieved from the <a href="/content/mimic-cxr-jpg/2.0.0/">MIMIC-CXR-JPG</a> dataset. This format is ready for machine models to process. Their DICOM metadata is also converted into CSV files and stored here.</p>
	</li>
	<li>
	<p><strong>REFLACX</strong>: The folder contains information collected from five radiologists while they were reading chest X-ray images. <a href="/content/reflacx-xray-localization/1.0.0/">REFLACX</a> asked radiologists to annotate the lesions in CXR images using ellipses. During the process of interpretation, radiologists&#39; eye movements and utterances are also collected. The utterances are then transformed into time-stamped transcriptions. Lastly, this folder also contains chest bounding boxes indicating the lung and heart areas.</p>
	</li>
	<li>
	<p><strong>EyeGaze</strong>:&nbsp;The EyeGaze folder contains data extracted from the <a href="/content/egd-cxr/1.0.0/">Eye Gaze</a> dataset. As with the REFLACX dataset, it also records audio and eye movements during interpretation. The Eye Gaze dataset only contains information generated by a radiologist, while REFLACX has five radiologists involved. Moreover, this folder provides segmentation and bounding boxes for anatomical structures as supplemental sources for further analysis of the correlation with anatomical structures.</p>
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


<p>This dataset includes a variety of inputs and labels. The user is then advised to use different combinations of inputs and labels to perform multi-modal, multi-task, and contrastive learning.&nbsp;We split the dataset into training, validation, and test datasets with portions of 70%, 15% and 15%, respectively.&nbsp;However, if the user doesn&#39;t concern about reproducibillity. The <em>split</em> column in <em>cxr_meta.csv</em> can also be ignored. Example of using clinical data and chest X-ray images to perform multi-modal learning can be found at <a href="http://github.com/ChihchengHsieh/multimodal-abnormalities-detection">https://github.com/ChihchengHsieh/multimodal-abnormalities-detection</a></p>
