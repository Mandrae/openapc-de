#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

PUBLISHER_MAPPINGS = {
    # Journals
    "The Optical Society": "Optical Society of America (OSA)",
    "Impact Journals": "Impact Journals LLC",
    "American Society for Biochemistry &amp; Molecular Biology (ASBMB)": "American Society for Biochemistry & Molecular Biology (ASBMB)",
    "Institute of Electrical and Electronics Engineers (IEEE)": "Institute of Electrical & Electronics Engineers (IEEE)",
    "Cold Spring Harbor Laboratory": "Cold Spring Harbor Laboratory Press",
    "Institute of Electrical &amp; Electronics Engineers (IEEE)": "Institute of Electrical & Electronics Engineers (IEEE)",
    "Hindawi Limited": "Hindawi Publishing Corporation",
    "Oxford University Press": "Oxford University Press (OUP)",
    "Wiley": "Wiley-Blackwell",
    "Bioscientifica": "BioScientifica",
    "Springer Nature America, Inc": "Springer Nature",
    "Springer Science and Business Media LLC": "Springer Nature",
    "F1000 ( Faculty of 1000 Ltd)": "F1000 Research, Ltd.",
    "F1000 Research Ltd": "F1000 Research, Ltd.",
    "Scientific and Academic Publishing": "Scientific & Academic Publishing",
    "Science and Education Publishing Co., Ltd.": "Science and Education Publishing",
    "Horizon Research Publishing Co., Ltd.": "Horizon Research Publishing",
    "Osterreichische Akademie der Wissenschaften": "Österreichische Akademie der Wissenschaften",
    "Element d.o.o.": "Ele-Math",
    "Element": "Ele-Math",
    "Institute of Physiology of the Czech Academy of Sciences": "Academia Scientiarum Bohemoslovaca",
    "Future Science Ltd": "Future Science, LTD",
    "Edinburgh University Global Health Society": "International Global Health Society",
    "Scientific Research Publishing, Inc,": "Scientific Research Publishing, Inc.",
    # books
    "DE GRUYTER": "De Gruyter",
    "DE GRUYTER SAUR": "De Gruyter",
    "De Gruyter Oldenbourg": "De Gruyter",
    "De Gruyter Mouton": "De Gruyter",
    "De Gruyter Saur": "De Gruyter",
    "Walter de Gruyter – K. G. Saur": "De Gruyter",
    "BRILL": "Brill",
    "Brill | Nijhoff": "Brill",
    "Peter Lang UK": "Peter Lang",
    "Peter Lang D": "Peter Lang",
    "PETER LANG LTD International Academic Publishers": "Peter Lang",
    "Intellect Books": "Intellect",
    "Intellect Ltd": "Intellect",
    "Bloomsbury Academic": "Bloomsbury Publishing",
    "Bloomsbury Publishing Plc": "Bloomsbury Publishing",
    "T&T Clark": "Bloomsbury Publishing",
    "Bloomsbury T & T Clark": "Bloomsbury Publishing",
    "Bloomsbury T&T Clark": "Bloomsbury Publishing",
    "Bloomsbury Visual Arts": "Bloomsbury Publishing",
    "Bloomsbury Publishing Inc": "Bloomsbury Publishing",
    "University of Hawai'i / Hawai‘i Press": "University of Hawaii Press",
    "University of Hawai'i Press": "University of Hawaii Press",
    "Tectum – ein Verlag in der Nomos Verlagsgesellschaft": "Tectum Wissenschaftsverlag",
    "Amsterdam university Press": "Amsterdam University Press",
    "NUS Press Pte Ltd": "NUS Press"
}

JOURNAL_MAPPINGS = {
    "PLoS ONE": "PLOS ONE",
    "Phys. Chem. Chem. Phys.": "Physical Chemistry Chemical Physics",
    "J. Mater. Chem. A": "Journal of Materials Chemistry A",
    "J. Mater. Chem. B": "Journal of Materials Chemistry B",
    "PLoS Pathogens": "PLOS Pathogens",
    "PLoS Genetics": "PLOS Genetics",
    "PLoS Biology": "PLOS Biology",
    "PLoS Computational Biology": "PLOS Computational Biology",
    "PLoS Neglected Tropical Diseases": "PLOS Neglected Tropical Diseases",
    "Oncotarget": "OncoTarget",
    "Journal of Lipid Research": "The Journal of Lipid Research",
    "Plastic and Reconstructive Surgery Global Open": "Plastic and Reconstructive Surgery - Global Open",
    "RSC Adv.": "RSC Advances",
    "Zeitschrift für die neutestamentliche Wissenschaft": "Zeitschrift für die Neutestamentliche Wissenschaft und die Kunde der älteren Kirche",
    "Chem. Soc. Rev.": "Chemical Society Reviews",
    "Journal of Elections, Public Opinion and Parties": "Journal of Elections, Public Opinion & Parties",
    "Scientific Repor.": "Scientific Reports",
    "PAIN": "Pain",
    "G3&amp;#58; Genes|Genomes|Genetics": "G3: Genes|Genomes|Genetics",
    "Transactions of the Royal Society of Tropical Medicine and Hygiene": "Transactions of The Royal Society of Tropical Medicine and Hygiene",
    "Org. Biomol. Chem.": "Organic & Biomolecular Chemistry",
    "PLoS Medicine": "PLOS Medicine",
    "AJP: Heart and Circulatory Physiology": "American Journal of Physiology - Heart and Circulatory Physiology",
    "Naturwissenschaften": "The Science of Nature",
    "Dalton Trans.": "Dalton Transactions",
    "Chem. Sci.": "Chemical Science",
    "J. Anal. At. Spectrom.": "Journal of Analytical Atomic Spectrometry",
    "Geospatial health": "Geospatial Health",
    "Journal of the European Optical Society-Rapid Publications": "Journal of the European Optical Society: Rapid Publications",
    "J. Mater. Chem. C": "Journal of Materials Chemistry C",
    "Chem. Commun.": "Chemical Communications",
    "Cognition and Emotion": "Cognition & Emotion",
    "Catal. Sci. Technol.": "Catalysis Science & Technology",
    "Journal of Epidemiology & Community Health": "Journal of Epidemiology and Community Health",
    "JRSM": "Journal of the Royal Society of Medicine",
    "Green Chem.": "Green Chemistry",
    "Stochastics and  Partial Differential Equations: Analysis and Computations": "Stochastics and Partial Differential Equations: Analysis and Computations",
    "Journal of Mass Communication & Journalism": "Journal of Mass Communication and Journalism",
    "Journal of Child and Adolescent Behavior": "Journal of Child and Adolescent Behaviour",
    "Journal of Otolaryngology - Head and Neck Surgery": "Journal of Otolaryngology - Head & Neck Surgery",
    "manuscripta mathematica": "Manuscripta Mathematica",
    "CPT Pharmacometrics Syst. Pharmacol.": "CPT: Pharmacometrics & Systems Pharmacology",
    "Taal en tongval": "Taal en Tongval",
    "Notfall +  Rettungsmedizin": "Notfall + Rettungsmedizin",
    "The Journal of Neuroscience": "Journal of Neuroscience",
    "British Editorial Society of Bone &amp; Joint Surgery": "British Editorial Society of Bone & Joint Surgery",
    "Proceedings of the Royal Society A: Mathematical, Physical and Engineering Science": "Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences",
    "The FEBS Journal": "FEBS Journal",
    "PLANT PHYSIOLOGY": "Plant Physiology",
    "IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control": "IEEE Transactions on Ultrasonics, Ferroelectrics and Frequency Control",
    "Cellular and Molecular Gastroenterology and Hepatology": "CMGH Cellular and Molecular Gastroenterology and Hepatology",
    "Tellus B: Chemical and Physical Meteorology": "Tellus B",
    "Natural Hazards and Earth System Science": "Natural Hazards and Earth System Sciences",
    "interactive Journal of Medical Research": "Interactive Journal of Medical Research",
    "EP Europace": "Europace",
    "Prostate Cancer and Prostatic Disease": "Prostate Cancer and Prostatic Diseases",
    "CARTILAGE": "Cartilage",
    "Annals of Clinical Biochemistry": "Annals of Clinical Biochemistry: An international journal of biochemistry and laboratory medicine",
    "JNCI: Journal of the National Cancer Institute": "JNCI Journal of the National Cancer Institute",
    "Journal of the National Cancer Institute": "JNCI Journal of the National Cancer Institute",
    "European Heart Journal – Cardiovascular Imaging": "European Heart Journal - Cardiovascular Imaging",
    "Transplantation": "Transplantation Journal",
    "SHOCK": "Shock",
    "Endocrine-Related Cancer": "Endocrine Related Cancer",
    "The American Journal of Tropical Medicine and Hygiene": "American Journal of Tropical Medicine and Hygiene",
    "American Journal of Physiology - Endocrinology And Metabolism": "AJP: Endocrinology and Metabolism",
    "Neurology - Neuroimmunology Neuroinflammation": "Neurology: Neuroimmunology & Neuroinflammation",
    "eneuro": "eNeuro",
    "The Journal of Experimental Biology": "Journal of Experimental Biology",
    "The Plant Cell Online": "The Plant Cell",
    "Journal of Agricultural, Biological, and Environmental Statistics": "Journal of Agricultural, Biological and Environmental Statistics",
    "PalZ": "Paläontologische Zeitschrift",
    "Lighting Research and Technology": "Lighting Research & Technology",
    "The Journal of Infectious Diseases": "Journal of Infectious Diseases",
    "Planning Practice and Research": "Planning Practice & Research",
    "Learning and Individual Differences": "Learning & Individual Differences",
    "Water Science and Technology": "Water Science & Technology",
    "Antimicrobial Resistance & Infection Control": "Antimicrobial Resistance and Infection Control",
    "European Journal of Public Health": "The European Journal of Public Health",
    "Journal of Vacuum Science & Technology B, Nanotechnology and Microelectronics: Materials, Processing, Measurement, and Phenomena": "Journal of Vacuum Science & Technology B: Microelectronics and Nanometer Structures",
    "Briefings In Bioinformatics": "Briefings in Bioinformatics",
    "Notes and Records: the Royal Society journal of the history of science": "Notes and Records of the Royal Society",
    "Journal Of Logic And Computation": "Journal of Logic and Computation",
    "Health:: An Interdisciplinary Journal for the Social Study of Health, Illness and Medicine": "Health: An Interdisciplinary Journal for the Social Study of Health, Illness and Medicine",
    "INTERNATIONAL JOURNAL OF SYSTEMATIC AND EVOLUTIONARY MICROBIOLOGY": "International Journal of Systematic and Evolutionary Microbiology",
    "Protein Engineering Design and Selection": "Protein Engineering, Design and Selection",
    "The Journals of Gerontology: Series A": "The Journals of Gerontology Series A: Biological Sciences and Medical Sciences",
    "MHR: Basic science of reproductive medicine": "Molecular Human Reproduction",
    "Research on Language and Social Interaction": "Research on Language & Social Interaction",
    "Psychology and Sexuality": "Psychology & Sexuality",
    "BJA: British Journal of Anaesthesia": "British Journal of Anaesthesia",
    "Journal of Development Studies": "The Journal of Development Studies",
    "Tellus A: Dynamic Meteorology and Oceanography": "Tellus A",
    "International journal of methods in psychiatric research": "International Journal of Methods in Psychiatric Research",
    "Polym. Chem.": "Polymer Chemistry",
    "ISME Journal": "The ISME Journal",
    "Interface": "Journal of The Royal Society Interface",
    "Medical Engineering and Physics": "Medical Engineering & Physics",
    "Forensic Science, Medicine, and Pathology": "Forensic Science, Medicine and Pathology",
    "Lab Chip": "Lab on a Chip",
    "Mater. Horiz.": "Materials Horizons",
    "AoB PLANTS": "AoB Plants",
    "Elem Sci Anth": "Elementa: Science of the Anthropocene",
    "Cell Death & Disease": "Cell Death and Disease",
    "Scandinavian Journal of Work, Environment & Health": "Scandinavian Journal of Work Environment and Health",
    "The Bone & Joint Journal": "Bone & Joint Journal",
    "British Journal of Psychiatry": "The British Journal of Psychiatry",
    "American Journal of Physiology-Heart and Circulatory Physiology": "American Journal of Physiology - Heart and Circulatory Physiology",
    "American Journal of Physiology-Endocrinology and Metabolism": "AJP: Endocrinology and Metabolism",
    "Milbank Quarterly": "The Milbank Quarterly",
    "Faraday Discuss.": "Faraday Discussions",
    "Journal of Management and Governance": "Journal of Management & Governance",
    "Journal für Verbraucherschutz und Lebensmittelsicherheit": "Journal of Consumer Protection and Food Safety",
    "Nanoscale Horiz.": "Nanoscale Horizons",
    "BeitrÃ¤ge zur Algebra und Geometrie / Contributions to Algebra and Geometry": "Beiträge zur Algebra und Geometrie / Contributions to Algebra and Geometry",
    "Energy Environ. Sci.": "Energy & Environmental Science",
    "Raumforschung und Raumordnung |  Spatial Research and Planning": "Raumforschung und Raumordnung",
    "Mol. BioSyst.": "Molecular BioSystems",
    "Physics in Medicine & Biology": "Physics in Medicine and Biology",
    "Anal. Methods": "Analytical Methods",
    "The American Journal of Clinical Nutrition": "American Journal of Clinical Nutrition",
    "International Journal of Clinical and Experimental Pathology ": "International Journal of Clinical and Experimental Pathology",
    "Forestry": "Forestry: An International Journal of Forest Research",
    "BJPsych Open": "British Journal of Psychiatry Open",
    "JOURNAL OF FORENSIC SCIENCE & CRIMINOLOGY": "Journal of Forensic Science & Criminology",
    "New J. Chem.": "New Journal of Chemistry",
    "The British Journal of Criminology": "British Journal of Criminology",
    "Journal of Alzheimer's disease": "Journal of Alzheimer's Disease",
    "Cell Death & Differentiation": "Cell Death and Differentiation",
    "Nat. Prod. Rep.": "Natural Product Reports",
    "Bone & Joint Research": "Bone and Joint Research",
    "Psychology of Well-Being": "Psychology of Well-Being: Theory, Research and Practice",
    "Genes & Immunity": "Genes and Immunity",
    "Biomater. Sci.": "Biomaterials Science",
    "BDJ": "British Dental Journal",
    "QJM: An International Journal of Medicine": "QJM",
    "American Journal of Physiology-Lung Cellular and Molecular Physiology": "American Journal of Physiology - Lung Cellular and Molecular Physiology",
    "American Journal of Physiology-Renal Physiology": "AJP: Renal Physiology",
    "The Journal of Nutrition": "Journal of Nutrition",
    "Microbial Ecology in Health and Disease": "Microbial Ecology in Health & Disease",
    "The Journals of Gerontology: Series B": "The Journals of Gerontology Series B: Psychological Sciences and Social Sciences",
    "American Journal of Physiology-Lung Cellular and Molecular Physiology": "American Journal of Physiology - Lung Cellular and Molecular Physiology",
    "CIRP Annals": "CIRP Annals - Manufacturing Technology",
    "Environment and Planning A": "Environment and Planning A: Economy and Space",
    "Mathematical Medicine and Biology: A Journal of the IMA": "Mathematical Medicine and Biology",
    "American Journal of Physiology-Cell Physiology": "American Journal of Physiology - Cell Physiology",
    "Geological Society of America Bulletin": "GSA Bulletin",
    "Structural Health Monitoring: An International Journal": "Structural Health Monitoring",
    "Quarterly Journal of Experimental Psychology": "The Quarterly Journal of Experimental Psychology",
    "Aging and disease": "Aging and Disease",
    "physica status solidi (RRL) – Rapid Research Letters": "physica status solidi (RRL) - Rapid Research Letters",
    "JOURNAL OF CLINICAL AND DIAGNOSTIC RESEARCH": "Journal of Clinical and Diagnostic Research",
    "genesis": "Genesis",
    "TRANSACTIONS OF THE JAPAN SOCIETY FOR AERONAUTICAL AND SPACE SCIENCES, AEROSPACE TECHNOLOGY JAPAN": "Transactions of the Japan Society for Aeronautical and Space Sciences, Aerospace Technology Japan",
    "Anales de PsicologÃ­a": "Anales de Psicología",
    "jwhg": "Journal of Women's Health and Gynecology",
    "E&amp;G Quaternary Science Journal": "E&G Quaternary Science Journal",
    "Work, employment and society": "Work, Employment and Society",
    "Software and Systems Modeling": "Software & Systems Modeling",
    "Photochem. Photobiol. Sci.": "Photochemical & Photobiological Sciences",
    "Statistical Modelling: An International Journal": "Statistical Modelling",
    "ael": "Agricultural & Environmental Letters",
    "ua": "Urban Agriculture & Regional Food Systems",
    "Journal of Orthopaedic Research®": "Journal of Orthopaedic Research",
    "BJPscyh Advances": "BJPsych Advances",
    "Clinical Orthopaedics and Related Research®": "Clinical Orthopaedics and Related Research",
    "Essays In Biochemistry": "Essays in Biochemistry",
    "Chemistry – A European Journal": "Chemistry - A European Journal",
    "Proceedings of the Institution of Civil Engineers - Geotechnical Engineering": "Proceedings of the ICE - Geotechnical Engineering",
    "BJS": "British Journal of Surgery",
    "Annals of Clinical Biochemistry: International Journal of Laboratory Medicine": "Annals of Clinical Biochemistry: An international journal of biochemistry and laboratory medicine",
    "The British Journal of Social Work": "British Journal of Social Work",
    "Med. Chem. Commun.": "MedChemComm",
    "Notes and Records: the Royal Society Journal of the History of Science": "Notes and Records of the Royal Society",
    "Journal of Web Semantics": "Web Semantics: Science, Services and Agents on the World Wide Web",
    "The Review of Financial Studies": "Review of Financial Studies",
    "Raumforschung und Raumordnung Spatial Research and Planning": "Raumforschung und Raumordnung",
    "Journal Of Environmental Law": "Journal of Environmental Law",
    "Eurasia Journal of Mathematics, Science and Technology Education": "EURASIA Journal of Mathematics, Science and Technology Education",
    "Journal of Vacuum Science & Technology A": "Journal of Vacuum Science & Technology A: Vacuum, Surfaces, and Films",
    "Nonlinear Analysis": "Nonlinear Analysis: Theory, Methods & Applications",
    "Journal of Water Sanitation and Hygiene for Development": "Journal of Water, Sanitation and Hygiene for Development",
    "Advances in Nutrition: An International Review Journal": "Advances in Nutrition",
    "Cellular & Molecular Immunology": "Cellular and Molecular Immunology",
    "AFRICAN JOURNAL OF FOOD, AGRICULTURE, NUTRITION AND DEVELOPMENT": "African Journal of Food, Agriculture, Nutrition and Development",
    "Journal of Psychiatry and Neuroscience": "Journal of Psychiatry & Neuroscience",
    "Chemistry – An Asian Journal": "Chemistry - An Asian Journal",
    "WIREs Computational Molecular Science": "Wiley Interdisciplinary Reviews: Computational Molecular Science",
    "Corporate Ownership and Control": "Corporate Ownership & Control",
    "Immunology & Cell Biology": "Immunology and Cell Biology",
    "Journal of Vacuum Science & Technology B": "Journal of Vacuum Science & Technology B: Microelectronics and Nanometer Structures"
}

COLUMN_NAMES = {
    "institution": ["institution"],
    "doi": ["doi"],
    "euro": ["apc", "kosten", "cost", "euro", "eur"],
    "period": ["period", "jahr"],
    "is_hybrid": ["is_hybrid", "is hybrid", "hybrid"],
    "publisher": ["publisher", "PublisherName"],
    "journal_full_title": ["journal_full_title", "journal", "journal title", "journal full title", "journaltitle", "journal_title"],
    "issn": ["issn", "issn.1", "issn0"],
    "issn_print": ["issn_print"],
    "issn_electronic": ["issn_electronic"],
    "issn_l": ["issn_l"],
    "license_ref": ["licence", "license", "license_ref"],
    "indexed_in_crossref": ["indexed_in_crossref"],
    "pmid": ["pmid", "pubmed id"],
    "pmcid": ["pmcid", "pubmed central (pmc) id"],
    "ut": ["ut"],
    "url": ["url"],
    "doaj": ["doaj"],
    "book_title": ["book_title"],
    "backlist_oa": ["backlist_oa"],
    "isbn": ["isbn"],
    "isbn_print": ["isbn_print"],
    "isbn_electronic": ["isbn_electronic"]
}

ISSN_L_CORRECTIONS = {
    "0266-7061": "1367-4803", # "Bioinformatics". 1460-2059(issn_e) -> 0266-7061, but 1367-4803(issn_p) -> 1367-4803
    "1654-6628": "1654-661X",  # "Food & Nutrition Research". 1654-6628(issn_p) -> 1654-6628, but 1654-661X(issn_e) -> 1654-661X
    "1474-7596": "1465-6906", # "Genome Biology".  1465-6906(issn_p) -> 1465-6906, but 1474-760X(issn_e) -> 1474-7596
    "0959-8138": "1756-1833", # BMJ. The BMJ has a bunch of ISSNs assigend, but the ISSN-L mappings are all fixed points. Unknown if this is intended.
    "0957-5820": "NA" # 0957-5820 clearly belongs to "Process Safety and Environmental Protection". Unfortunately there's the line 0263-8762 -> 0957-5820 which
                      # incorrectly maps the issn of "Chemical Engineering Research and Design" to the same value. We have no choice but to omit this value.
}
