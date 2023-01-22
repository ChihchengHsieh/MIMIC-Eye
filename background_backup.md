

Medical image diagnosis is the process or task of identifying lesions or diseases, based on reading and interpreting medical images, such as chest X-ray images, CT scans or MRI scans. The skills and knowledge of performing this task are owned by specialists, such as doctors or radiologists. However, statistics showed a 6.4 million, 30.6 million, and 2.9 million worldwide shortage of physicians, nurses, and pharmacists respectively in 2019 [1]. Due to the disproportionate impact of the pandemic on healthcare workers, the situation has become more dire. One solution to alleviate the shortage is to adopt AI-driven diagnostic systems to facilitate the process.

Deep Learning (DL) technology is widely used to deliver promising results in AI-driven systems. Its excellent performance is highly commensurate with the quality and quantity of the dataset that the model is trained on. In medical image diagnosis, DL approaches have proven effective and efficient. Several studies have achieved human-level performance by applying DL to medical image tasks, such as breast imaging [2, 3], left ventricular assessment [4, 5], dermoscopy analysis [6, 7] and chest X-Rays [8 – 11].

Multi-label learning, multi-task learning, and contrastive learning are currently the most common deep learning technologies. They use a variety of modalities in the output and input layers to improve DL models. Multimodal learning uses different modalities as input to the model, which allows the model to perceive various aspects of a phenomenon and comprehend the input scenario better. The term "\textit{modality}" is then used to describe the collected information from each sensor. When several different instruments are set up to observe a phenomenon, the information collected is known as \textit{multi-modal} data [12, 13]. In multi-task learning, the model is trained through a variety of tasks, which require many modalities as labels. Contrastive learning is a self-supervised technique, which trains the model to contrast inputs against each other by mapping modalities to a semantic vector space. All these technologies require multiple modalities in either input or output layers to perform.

The Medical Information Mart for Intensive Care (MIMIC) IV dataset [14] is sourced from two in-hospital database systems, a custom hospital wide EHR and an ICU specific clinical information system, at Beth Israel Deaconess Medical Center (BIDMC) from 2011 to 2019. Multiple subsets of MIMIC-IV contain a variety of modalities. Two categories of data are critical for DL models to consider during building and training. The first type is the patient's clinical information. According to [15], clinical data is highly informative and essential for radiologists to interpret and diagnose properly. Secondly, there is the information that is gathered when radiologists are making diagnoses, including eye-tracking data, audio recordings, and time-stamped transcriptions. Since medical diagnosis is a skill that is only owned by experts, it is beneficial for models to learn the diagnosis pattern from them. This category allows us to explore the decision-making process that radiologists go through while interpreting medical images.

In this work, we propose a strategy to integrate the valuable modalties from MIMIC-IV [14] and its subsets. Several studies have attempted to involve more modalities in their training process since multi-modal, multi-task, and contrastive learning became popular and effective. However, the standard for constructing a dataset with various modalities has not been created, which hinders comparison between different studies. To enhance the convenience and reproducibility of medical image diagnosis, it is crucial to have a single dataset with available modalities.

Five datasets are used to construct the MIMIC-Eye dataset, including MIMIC-IV [14], MIMIC-IV-ED [16], MIMIC-CXR [17], Eye Gaze [18], and REFLACX [19] datasets. Each of them contains valuable information about patients and radiologists. MIMIC-IV and MIMIC-IV-ED provide information about the patient's clinical data. MIMIC-CXR provides the medical image and radiology report, which are considered as the input and output of the model respectively. The labels commonly used to train DL models are extracted from these reports via Nature Language Processing (NLP) labelers. REFLACX and Eye Gaze datasets collect eye-tracking data and audio when radiologists are reading images. REFLACX dataset also asked radiologists to manually annotate lesions by using bounding boxes to locate lesions, which gives the required label types for performing object/lesion detection. The normal image diagnosis task can only tell what lesions are present in a given image, whereas lesion detection can also indicate their locations.

To summarise, the key contributions of this work are:

Provide a single source dataset with various modalities.

Provide a scalable strategy to combine datasets related to MIMIC-IV.

Provide a ready-to-train dataset to simplify the process before training.

Provide a strategy to preprocess those five datasets.

# Refs

[1] for Health Collaborators, G. . H. R. Measuring the availability of human resources for health and its relationship to universal health coverage for 204 countries and territories from 1990 to 2019: a systematic analysis for the global burden of disease study 2019. LANCET (2022) .

[2] Maicas, G., Bradley, A. P., Nascimento, J. C., Reid, I. & Carneiro, G.Pre and post-hoc diagnosis and interpretation of malignancy from breast DCE-MRI. Medical Image Analysis 58 (2019). https://doi.org/10.1016/j.media.2019.101562 .

[3] Shen, L. et al. Deep learning to improve breast cancer detection on screening mammography. Scientific Reports 9, 2045–2322 (2019) .

[4] Liu, X. et al. Deep learning-based automated left ventricular ejectionfraction assessment using 2-d echocardiography. Journal of Physiology Heart and Circulatory Physiology 321, H390–H399 (2020) .

[5] Medley, D. O., Santiago, C. & Nascimento, J. C. Cycoseg: A cyclic collaborative framework for automated medical image segmentation. IEEE Transactions on Pattern Analysis and Machine Intelligence 44 (11), 8167–8182 (2022). https://doi.org/10.1109/TPAMI.2021.3113077 .

[6] Pham, T.-C., Luong, C.-M., Hoang, V.-D. & Doucet, A. Ai outperformed every dermatologist in dermoscopic melanoma diagnosis, using an opti461 mized deep-cnn architecture with custom mini-batch logic and loss function. Scientific Reports 11, 17485 (2021) .

[7] Haenssle, H. et al. Man against machine: diagnostic performance of a deep learning convolutional neural network for dermoscopic melanoma recognition in comparison to 58 dermatologists. Annals of oncology 29, 1836–1842 (2018) .


[8] Irvin, J. et al. Chexpert: A large chest radiograph dataset with uncertainty labels and expert comparison, 590–597 (2019).

[9] Rajpurkar, P. et al. Chexnet: Radiologist-level pneumonia detection on chest x-rays with deep learning. CoRR abs/1711.05225 (2017). https://arxiv.org/abs/1711.05225 .

[10] Rajpurkar, P. et al. Deep learning for chest radiograph diagnosis: A retro473 spective comparison of the chexnext algorithm to practicing radiologists. PLOS Medicine 15 (11), 1–17 (2018). https://doi.org/10.1371/journal.pmed.1002686 .

[11] Yates, E., Yates, L. & Harvey, H. Machine learning “red dot”: open source, cloud, deep convolutional neural networks in chest radiograph binary normality classification. Clinical Radiology 73 (9), 827–831 (2018). https://doi.org/10.1016/j.crad.2018.05.015 .

[12] Lahat, D., Adali, T., and Jutten, C. (2015). Multimodal data fusion: An overview of methods, challenges, and prospects. Proceedings of the IEEE, 103(9):1449–1477.

[13] Ramachandram, D. and Taylor, G. W. (2017). Deep multimodal learning: A survey on recent advances and trends. IEEE Signal Processing Magazine, 34(6):96–108. 

[14] Johnson, A. et al. Mimic-iv (2021). URL https://physionet.org/content/mimiciv/1.0/.

[15] Castillo, C., Steffens, T., Sim, L. & Caffery, L. The effect of clinical information on radiology reporting: A systematic review. Journal of Medical Radiation Sciences 68 (1), 60–74 (2021). https://doi.org/10.1002/jmrs.424 .

[16] Johnson, A. et al. Mimic-iv-ed (2021). URL https://physionet.org/content/mimic-iv-ed/1.0/.

[17] Johnson, A. E. W., Pollard, T., Mark, R., Berkowitz, S. & Horng, S. The mimic-cxr database (2019). URL https://physionet.org/content/mimic-cxr/.

[18] Karargyris, A., Kashyap, S., Lourentzou, I., Wu, J. T., Sharma, A., Tong, M., Abedin, S., Beymer, D., Mukherjee, V., Krupinski, E. A., and Moradi, M. (2021). Creation and validation of a chest x-ray dataset with eye-tracking and report dictation for AI development. Scientific Data, 8(1).

[19] Bigolin Lanfredi, R. et al. Reflacx, a dataset of reports and eye-tracking data for localization of abnormalities in chest x-rays. Scientific Data 9 (2022) .

[20] 