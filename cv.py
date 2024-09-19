from docx import Document
import pypandoc
from docx2pdf import convert

ADD_TECHOLOGIES = False

# Create a new Document with the updated order
doc = Document()

# Add the content to the Document
doc.add_heading('Arkady Miasnikov', 0)
doc.add_paragraph('(054) 4681517 | arkady.miasnikov@gmail.com')

doc.add_heading('Software Engineer experienced in leading development projects from inception to full implementation', level=1)
doc.add_paragraph(
    'Expertise in design and development of mission-critical real-time systems, firmware, multi-threaded applications, automated trading platforms, and web-based applications.\n'
    'Practiced in pre-sales and post-sales support of Tier 1 telecom companies in Europe and North America.\n'
    'Technology-savvy with a broad business perspective, good interpersonal relations, and high attention to detail.\n'
    'Tools & Technologies: Linux, Go, Python, C, C++11/14'
)

doc.add_heading('Professional Experience', level=1)

# Add the remaining experience
experience = [
    ("2023-present: Software Engineer - Endotech", [
        "Collaboratively designed and developed custom momentum indicators and signal filters for specific market conditions, enhancing trading performance.",
        "Translated and customized multiple indicators from PineScript to Go, improving their efficiency and functionality.",
        "Developed indicators that are a central part of the company's trading algorithms."
    ], ['Go', 'Python', "ClickHouse", "SQL", "AI"], False),
    ("2022-2023: Software Engineer - HiAuto", [
        "Participated in the maintenance of the computerized drive-thru order-taking system as part of an international team to ensure operational efficiency and reliability.",
        "Enhanced business analytics tools by integrating data and troubleshooting systems, improving decision-making processes.",
        "Ensured continuous operation of on-premises devices, addressing technical issues promptly."
    ], ['Python', "BigQuery", "SQL", "AI"], False),
    ("2018-2022: Software Engineer - Cyren", [
        "Participated in the collaborative design and development of email and network security products, contributing to a increase in threat detection accuracy.",
        "Maintained a complex SaaS system, integrating a range of popular software products seamlessly.",
        "Developed advanced phishing and spam detection engines.",
        "Initiated and prepared multiple POCs, including headless browsers, image recognition services, fast Hamming distance calculations, and locality-sensitive hashing."
    ], ['Go', 'C++', "ElasticSearch", "Apache Kafka", "Prometheus", "Grafana", "Kibana", "Megalog", "Jaeger", "SQL"], True),
    ("2016-2018: Software Engineer - Secdo", [
        "Defined, designed, and developed the Linux endpoint driver, enhancing system performance with minimal impact.",
        "Developed a solution to analyze millions of system events per second on multicore systems efficiently.",
        "Supported Windows endpoint software development, including kernel driver and user space code.",
        "Improved data processing performance and developed behavioral models for the security research team."
    ], ['Python', 'C/C++', "Linux Kernel", "Windows kernel", "Vertica", "SQL"], False),
    ("2012-2016: Software Engineer - Megabridge", [
        "Developed a video monitoring and control system for HLS, including hardware verification and low-level embedded firmware development.",
        "Designed drivers and significant firmware components for the BDSL product line, including Java-based web management.",
        "Led bring-up projects for various HW platforms, customizing Linux root file systems using Yocto.",
        "Established the company's automatic build infrastructure and continuous integration system."
    ], ['C/C++', 'Python', "Linux kernel", "U-boot"], False),
    ("2009-2012: Software Engineer - Texas Instruments", [
        "Developed firmware for 802.11 ASIC, including pre and post-silicon verification of WLAN devices.",
        "Participated in WLAN Linux kernel development and defined/developed utilities for firmware build and debug in Linux.",
        "Led a streamlining process that improved productivity by 30% by advocating the replacement of ClearCase with GIT.",
        "Established a wiki-based search system that improved access to the company's knowledge base."
    ], ['C/C++', 'Python', "Linux kernel", "ASIC", "Bare metal"], False),
    # ("2005-2007: Software Engineer - Broadlight Ltd.", [
    #     "Contributed to the development of the world's first fully integrated GPON chip.",
    #     "Supported the hardware team in post-production verification and pre-fab processes.",
    #     "Prepared firmware for design verification, post-production chip verification, and a series of drivers."
    # ], ['C', 'Verilog', "Linux kernel", "Specman", "Bare metal"], True),
    # ("2001-2004: Software Engineer - Terayon Israel/USA", [
    #     "Led a team of 5 engineers in the design and development of DSLAM systems, INTERCARD communication BSP for vxWorks, and various hardware drivers.",
    #     "Delivered customer-tailored systems, some of which are still in operation.",
    #     "Conducted employee training programs."
    # ], ['C', "Linux kernel", "Bare metal"], False),
    # ("1995-2000: Software Engineer - TDSoft", [
    #     "Developed infrastructures and low-level drivers for embedded real-time systems in C, C++, and Java.",
    #     "Participated in several development projects, including a Windows management system for strategic customers such as Deutsche Telekom and ECI.",
    #     "Designed and implemented significant parts of a V5 Class 5 switch (LE) simulator with ISDN support and developed GUI management for the simulator."
    # ], ['C/C++', "Java", "Bare metal", "RTKernel", "pSOS"], False)
]

for position, details, technologies, page_break in experience:
    doc.add_heading(position, level=2)
    for detail in details:
        doc.add_paragraph(detail, style='List Bullet')
    if ADD_TECHOLOGIES and technologies:
        doc.add_heading('Technologies & Programming Languages', level=3)
        doc.add_paragraph(', '.join(technologies))
    if page_break:
        doc.add_page_break()

doc.add_heading('Education', level=1)
doc.add_paragraph(
    'B.A. in Business Administration - Netanya Academic College (2007-2009)\n'
    'Software Practical Engineer - Tel Aviv University School of Practical Engineering\n'
    'Physics Department - St. Petersburg State University (1987-1989)'
)

# Save the document
file_path = './Arkady_Miasnikov_CV_Updated.docx'
doc.save(file_path)

pdf_path = file_path.replace('.docx', '.pdf')
pypandoc.convert_file(
    file_path,
    'pdf',
    outputfile=pdf_path,
    extra_args=[
       '-V', 'geometry:top=0.5in',
       '-V', 'geometry:bottom=1in',
       '-V', 'geometry:left=1in',  
       '-V', 'geometry:right=1in'  
    ]
)

file_path
