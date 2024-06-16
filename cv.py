from docx import Document

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
        "Designed and developed custom momentum indicators and signal filters for specific market conditions, along with ML models targeting modern financial instruments.",
        "Engaged in reverse engineering and code translation from PineScript to Go for multiple indicators and their customization.",
    ]),
    ("2022-2023: Software Engineer - HiAuto", [
        "Participated in maintenance of the computerized drive-thru order taking system to ensure operational efficiency and reliability.",
        "Provided support for business analytics tools, assisting with data integration and system troubleshooting to enhance decision-making processes.",
        "Maintained HiAuto on-premises devices, ensuring continuous operation of the deployed systems and addressing technical issues.",
    ]),
    ("2018-2022: Software Engineer - Cyren", [
        "Participated in the design and development of leading email and network security products.",
        "Maintained a complex SaaS system integrating a range of popular software products.",
        "Contributed to the development of advanced phishing and spam detection engines."
    ]),
    ("2016-2018: Software Engineer - Secdo", [
        "Defined, designed, and developed the driver for the company Linux endpoint, integrating it with the existing code base.",
        "Developed a solution capable of collecting and analyzing tens of millions of system events per second on busy multicore systems with minimal system impact.",
        "Supported the development of the company Windows endpoint software, including Windows kernel driver and user space code.",
        "Contributed to the security research team by improving data processing performance and creating behavioral models."
    ]),
    ("2012-2016: Software Engineer - Megabridge", [
        "Developed a video monitoring and control system for HLS, including hardware module verification and low-level embedded firmware development for ARM-based processors, Freescale Power PC, and 8-bit ATMEGA micro-controllers.",
        "Designed and developed drivers and significant parts of the firmware for the BDSL product line and Java-based web management for the BDSL.",
        "Led bring-up projects: Windows CE on PXA255 (ARM) board, Linux on multiple HW platforms (Atmel SAMA5D3x and OMAP L138 CPUs), customization of Linux root file systems using Yocto, and VxWorks on custom PPC boards.",
        "Defined and set up the company's automatic build infrastructure, continuous integration system, and knowledge database."
    ]),
    ("2009-2012: Software Engineer - Texas Instruments", [
        "Developed firmware for 802.11 ASIC, including pre and post-silicon verification of WLAN devices.",
        "Participated in WLAN Linux kernel development and defined/developed utilities for firmware build and debug in Linux.",
        "Led a streamlining process that improved productivity by 30% by advocating the replacement of ClearCase with GIT.",
        "Established a wiki-based search system that improved access to the company's knowledge base."
    ]),
    ("2005-2007: Software Engineer - Broadlight Ltd.", [
        "Contributed to the development of the world's first fully integrated GPON chip.",
        "Supported the hardware team in post-production verification and pre-fab processes.",
        "Prepared firmware for design verification, post-production chip verification, and a series of drivers."
    ]),
    ("2001-2004: Software Engineer - Terayon Israel/USA", [
        "Led a team of 5 engineers in the design and development of DSLAM systems, INTERCARD communication BSP for vxWorks, and various hardware drivers.",
        "Delivered customer-tailored systems, some of which are still in operation.",
        "Conducted employee training programs."
    ]),
    ("1995-2000: Software Engineer - TDSoft", [
        "Developed infrastructures and low-level drivers for embedded real-time systems in C, C++, and Java.",
        "Participated in several development projects, including a Windows management system for strategic customers such as Deutsche Telekom and ECI.",
        "Designed and implemented significant parts of a V5 Class 5 switch (LE) simulator with ISDN support and developed GUI management for the simulator."
    ])
]

for position, details in experience:
    doc.add_heading(position, level=2)
    for detail in details:
        doc.add_paragraph(detail, style='List Bullet')

doc.add_heading('Education', level=1)
doc.add_paragraph(
    'Software Practical Engineer - Tel Aviv University School of Practical Engineering\n'
    'B.A. in Business Administration - Netanya Academic College (2007-2009)\n'
    'Physics Department - St. Petersburg State University (1987-1989)'
)

# Save the document
file_path = './Arkady_Miasnikov_CV_Updated.docx'
doc.save(file_path)

file_path
