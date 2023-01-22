<p><u>I</u>n this section, we present a strategy for preprocessing and integrating various modalities in MIMIC-IV, MIMIC-IV-ED, MIMIC-CXR, REFLACX, and Eye Gaze datasets. We demonstrate our strategy step by step. We also mention some issues and challenges we encountered while developing this strategy. Before explaining the strategy, we first explain the ten clinical features we found significant during interviews with radiologists. The radiologists indicated that these ten clinical features are highly informative and essential for them to make accurate diagnoses in practice. The MIMIC-IV patient table contains two demographic attributes, age and gender. Eight other clinical features are extracted from MIMI-IV ED triage table. The explanations for these eight clinical features in the MIMIC-IV documentation are:</p>

<ol>
	<li><code>temperature</code>: The patient&rsquo;s temperature in degrees Fahrenheit.</li>
	<li><code>heartrate</code>: The patient&rsquo;s heart rate in beats per minute.</li>
	<li><code>resprate</code>: The patient&rsquo;s respiratory rate in breaths per minute.</li>
	<li><code>o2sat</code>: The patient&rsquo;s peripheral oxygen saturation as a percentage.</li>
	<li><code>sbp</code>, <code>dbp</code>: The patient&rsquo;s systolic and diastolic blood pressure, respectively, measured in millimetres of mercury (mmHg).</li>
	<li><code>pain</code>: The level of pain self-reported by the patient, on a scale of 0-10.</li>
	<li><code>acuity</code>: An order of priority. Level 1 is the highest priority, while level 5 is the lowest priority.</li>
</ol>

<p>&nbsp;</p>

<p>And, these are the 7 tables that contain the modatlies we desire or can be used for intergration :</p>

<ul>
	<li><code>MIMIC-IV Core patients</code>: Information that is consistent for the lifetime of a patient is stored in this table, including age and gender.</li>
	<li><code>MIMIC-IV ED triage</code>: This table includes information about the patient when they were first triaged in the emergency department, including temperature, heart rate and more clinical data.</li>
	<li><code>MIMIC-IV Core edstays</code>: It provides the time the patient entered the emergency department and the time they left the emergency department, which helps us to identify the stay id for CXR images.</li>
	<li><code>MIMIC-IV CXR metadata</code>: It contains information about the CXR image (radiograph), including the time taken, height and width.</li>
	<li><code>REFLACX anomaly location ellipses</code>: This table contains the coordinates of bounding ellipses that radiologists use for annotating abnormalities.</li>
	<li><code>REFLACX fixations</code> &amp; <code>Eye Gaze fixations</code>: The two files provide eye-tracking data from radiologists. Although both of these two datasets collect eye-tracking data, they have some differences in instruments setup, capturing frequency, UI interface, and number of radiologists.</li>
	<li><code>REFLACX timestamps transcription and Eye Gaze transcript</code>: These files contain time-stamped utterances that were transcribed from audio recordings of radiologists reading chest X-ray images. REFLACX stored those transcriptions in csv files while Eye Gaze used json files.</li>
</ul>

<p>&nbsp;</p>

<h3><strong>Preprocessing:</strong></h3>

<p>The ultimate goal of this part is to extract the desired modalities from datasets, then assemble them as a multimodal dataset, MIMIC-Eye.</p>

<p><strong>Step 1</strong>: <em>Identify stay_id for CXR images.</em></p>

<p>The stay_id is necessary for us to retrieve clinical data from MIMIC-IV ED. However, the stay id provided in MIMIC-CXR is outdated and not compatible with the current MIMIC-IV dataset. To identify the stay id, EyeGaze [70] has proposed an approach of searching stay_id for each radiograph. The idea is to find out which stay has the timespan covering the time point the radiograph was taken. Therefore, we can say the chest X-ray image is from that particular stay.&nbsp;Let&nbsp;<math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>i</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mi>C</mi> <mi>X</mi> <mi>R</mi> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{CXR}_{p,i}</annotation> </semantics> </math>&nbsp;be&nbsp;to be the time that a CXR image taken for patient&nbsp;<math> <semantics> <mi>p</mi> <annotation encoding="application/x-tex">p</annotation> </semantics> </math>&nbsp;at unknown stay <math> <semantics> <mi>i</mi> <annotation encoding="application/x-tex">i</annotation> </semantics> </math>. The&nbsp;<math> <semantics> <mi>i</mi> <annotation encoding="application/x-tex">i</annotation> </semantics> </math> is determined by:</p>

<div><math display="block"> <semantics> <mrow> <mi>i</mi> <mo stretchy="false">←</mo> <mi>j</mi> <mo>:</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>j</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>start</mtext> </mrow> </msubsup> <mo>&lt;</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>i</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>CXR</mtext> </mrow> </msubsup> <mo>&lt;</mo> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>p</mi> <mo>,</mo> <mi>j</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>end</mtext> </mrow> </msubsup> <mo>,</mo> </mrow> <annotation encoding="application/x-tex">i \leftarrow j: T^{\text{start}}_{p,j} &lt; T^{\text{CXR}}_{p,i} &lt; T^{\text{end}}_{p,j},</annotation> </semantics> </math></div>

<p>where <math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>i</mi> <mo>,</mo> <mi>p</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>start</mtext> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{\text{start}}_{i,p}</annotation> </semantics> </math>&nbsp;and&nbsp;<math> <semantics> <msubsup> <mi>T</mi> <mrow class="MJX-TeXAtom-ORD"> <mi>j</mi> <mo>,</mo> <mi>p</mi> </mrow> <mrow class="MJX-TeXAtom-ORD"> <mtext>end</mtext> </mrow> </msubsup> <annotation encoding="application/x-tex">T^{\text{end}}_{j,p}</annotation> </semantics> </math>&nbsp;are starting time and ending time of a stay respectively.</p>

<p>At this step, 55.99% of CXRs could not identify their stay id, since the CXRs may have been taken after they left ED. To explore this issue, we ran different conditions to test how many instances would be lost. We found that when we increased the condition to 7 days, we could identify 23.26% more CXRs. The goal of this experiment is to use clinical information that is close to the time of the CXR. Therefore, only CXRs taken within the range are used.</p>

<p>&nbsp;</p>

<p><strong>Step 2</strong>: <em>Merge tables</em>.</p>

<p>Once the IDs of the stays have been identified, we merged the tables according to stay id and subject id. In this work, all the modalities mentioned above are merged to form our multimodal dataset. The clinical data is retrieved from MIMIC-IV and MIMIC-IV ED. MIMIC-CXR provides chest X-ray images. REFLACX and Eye Gaze datasets provide eye-tracking data, time-stamped transcripts, and lesion bounding boxes.</p>

<p>&nbsp;</p>

<p><strong>Step 3</strong>: <em>Remove unidentified cases</em>.</p>

<p>Currently, both MIMIC-IV and MIMIC-IV ED have been updated to the 2.0 version. MIMIC-CXR, however, remains compatible with version 0.4, causing a version conflict between MIMIC-CXR and other datasets. The ids of patients are regenerated in the updated version, and no method found can map the current ids to the previous version. Since this issue, we have only 670 left, which is around 21% of the REFLACX dataset.</p>

<p><strong>Step 4</strong>: <em>Transform bounding ellipses into bounding boxes</em>.</p>

<p>In the REFLACX dataset, the radiologist is asked to annotate abnormalities using ellipses. In DL, the bounding box approach is more common, which leads us to perform this step to transform the ellipses to boxes for easier calculation of Intersection over Union (IoU) and Intersection over predicted Bounding Boxes (IoBB).</p>

<p>&nbsp;</p>

<p><strong>Step 5</strong>: <em>Replace the missing value (NaN).</em></p>

<p>In terms of the strategy for filling missing values, we replace numerical and categorical missing values with the mean value and most frequent value, respectively.</p>

<p>&nbsp;</p>

<p><strong>Step 6</strong>: <em>Integrate repetitive abnormalities</em>.</p>

<p>The REFLACX dataset provides two versions of names for radiologists to use when annotating the same lesion. In the REFLACX dataset, different names are associated with the same lesion. The REFLACX dataset contains 3052 cases in total. 2757 of them are annotated with V1 labels, and the other 295 cases use V2 labels. To make the dataset concise, we interviewed radiologists and used their opinion to merge the labels from two versions, which resolves conflicts. At the end, we have 21 remaining types of classes (lesions).</p>

<p>&nbsp;</p>

<p><strong>Step 7</strong>: <em>Dataset Split.</em></p>

<p>Since we only have a limited amount of data available to train and evaluate the model, we set a large portion of the dataset for validation and testing, which provides a robust evaluation. We split the dataset into training, validation, and test datasets with portions of 70%, 15% and 15%, respectively.</p>
