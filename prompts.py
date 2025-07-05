from langchain.prompts import PromptTemplate

QUESTION_PROMPTS = {
    "What is the objective of the study?": PromptTemplate.from_template("""
        What is the primary objective of the clinical study? Describe both the safety and effectiveness goals, 
        the success criteria (e.g., statistical thresholds), and how these outcomes will be measured or adjudicated.

        Context:
        {context}

        Answer:
    """),
    "What is the study indication?": PromptTemplate.from_template("""
        What is the medical indication or condition being studied in the clinical trial? 
        Include specific diseases or disorders, the targeted patient population, and the anatomical or physiological systems involved.

        Context:
        {context}

        Answer:
    """),
    "What is the investigational drug or procedure?": PromptTemplate.from_template("""
        What is the investigational product, drug, or procedure being studied? Provide the name, description of its function or mechanism, 
        and the intended therapeutic effect. If a device is involved, explain its design and usage.

        Context:
        {context}

        Answer:
    """),
    "How many participants are in the study?": PromptTemplate.from_template("""
        How many subjects or participants are included in the study? Mention the total planned or enrolled number, 
        and explain any relevant cohort divisions or phases if applicable.

        Context:
        {context}

        Answer:
    """),
    "What is the duration of the study?": PromptTemplate.from_template("""
        What is the duration of the study? Describe the total time frame, including enrollment, treatment, follow-up periods, 
        and any key milestone visits such as 30-day or 6-month evaluations.

        Context:
        {context}

        Answer:
    """),
    "What are the primary end points in the study?": PromptTemplate.from_template("""
        What are the primary endpoints of the study? Clearly define the clinical or procedural goals, 
        such as safety and effectiveness outcomes, the criteria used for evaluation, and how these are adjudicated 
        (e.g., by a core lab or committee).

        Context:
        {context}

        Answer:
    """),
    "What are the secondary end points in the study?": PromptTemplate.from_template("""
        What are the secondary endpoints of the study? Include the nature of the analyses (e.g., descriptive or statistical), 
        the type of clinical outcomes measured, and where applicable, reference to a statistical analysis plan.

        Context:
        {context}

        Answer:
    """),
    "What are the exploratory end points in the study?": PromptTemplate.from_template("""
        What are the exploratory endpoints in the study, if any? Include any research or hypothesis-generating goals, 
        such as biomarker analysis, imaging endpoints, or patient-reported outcomes. Clarify if they are for observational use only.

        Context:
        {context}

        Answer:
    """),
    "What are the treatment arms or groups in the study?": PromptTemplate.from_template("""
        Context:
        {context}

        Answer:
    """),
    "What are the different visits in the study?": PromptTemplate.from_template("""
        What are the different types of visits scheduled during the study? Describe the purpose and timing of each 
        (e.g., Screening, Baseline, Procedure Day, 30-day Follow-up, 6-month Follow-up), and mention what assessments occur at each.

        Context:
        {context}

        Answer:
    """),
    "What are the different forms in the study?": PromptTemplate.from_template("""
        List and describe the different forms used in the clinical trial. Include standard forms like the Informed Consent Form (ICF), 
        Case Report Forms (CRFs), Adverse Event forms, and any other documentation. For each, explain its purpose, what it records, 
        who completes it, and when it is used during the study.

        Context:
        {context}

        Answer:
    """)
}