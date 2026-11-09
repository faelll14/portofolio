import os
import sys
from html import escape
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svg_assets

ASSETS = os.path.join(ROOT, "assets")

SITE = "https://raffaelsec.my.id"
EMAIL = "raffael.dev.sec@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/raffael-sec/"
GH_PROJECTS = "https://github.com/TheRealRafael00"
GH_MAIN = "https://github.com/faelll14"
INSTAGRAM = "https://www.instagram.com/ell_bugs"
YEARS = "2025-2026"

C = {
    "bg": "0b1020",
    "gold": "f2c14e",
    "ember": "ff8a5b",
    "ice": "8fb8ff",
    "slate": "2a3556",
    "line": "4a5a85",
}
SKILL_COLOR = {"warm": "ember", "lime": "ice"}

AWARDS = [
    ("ggg.jpg", "Stored XSS on News Page", "Bali Provincial Government", "Oct 2026"),
    ("gggg.jpg", "Letter of Recognition and Appreciation", "PT Arunika Vistara Digital (Digifolks)", "Recognition"),
    ("ggggg.jpg", "Certificate of Appreciation", "PT Arunika Vistara Digital (Digifolks)", "Appreciation"),
    ("gg.jpg", "Appreciation Certificate", "DKI Jakarta Provincial Government", "Jun 2026"),
    ("g.jpg", "National Informatics Competition", "Olimnesia and Mapresnas", "Competition"),
]

CERTS = [
    ("CC Course Conclusion", "ISC2"),
    ("Classical Cryptography for Beginners", "Cyberacademy.id"),
    ("Intro to Dark Web, Anonymity and Cryptocurrency", "EC-COUNCIL"),
    ("ChatGPT for Cybersecurity", "Simplilearn"),
    ("Cybersecurity Essentials with Kali Linux", "BISA AI"),
    ("Cyber Threat Intelligence 101", "arcX"),
    ("Cybersecurity Fundamentals", "IBM Skills Build"),
    ("CompTIA Security+", "Cursa"),
    ("Ethical Hacker", "Cisco Networking Academy"),
    ("Ethical Hacking: Introduction", "Cybrary"),
    ("Introduction to Cybersecurity", "Cisco Networking Academy"),
    ("Cybersecurity for Business", "EC-COUNCIL"),
    ("Introduction to Cybersecurity", "Cyberacademy.id"),
    ("IT Security by Google Careers", "Cursa"),
    ("Google Analytics Certification", "Google"),
    ("Fortinet Certified Associate in Cybersecurity", "Fortinet"),
    ("Prompt Engineering", "Codecademy"),
    ("DevSecOps in AWS Course", "Codecademy"),
    ("Ethical Hacker for Dummies", "Komdigi / Kominfo"),
    ("CyberSecurity", "ADBI Institute"),
    ("Certificate of Participation", "HackerVerse / EC-COUNCIL"),
    ("How to Prevent E-Waste?", "United Nations"),
    ("SQL Basic", "HackerRank"),
    ("SQL Intermediate", "HackerRank"),
    ("SQL Advanced", "HackerRank"),
    ("Basic AI Fundamentals", "Dicoding, Indosat, Google Cloud"),
    ("Seminar Nasional IT Holic", "Himatif UTB"),
    ("Webinar Broken Access Control", "Merdeka Siber"),
    ("Building a Virtual Lab and Linux Basics", "Digital Talent Scholarship, Komdigi"),
    ("Securing and Protecting Your Data in Amazon S3", "AWS Training and Certification"),
    ("Claude 101", "Anthropic"),
    ("Claude Code in Action", "Anthropic"),
    ("Modular Summit 2026: Optimizing Artificial Intelligence in Student Learning", "Kemendikdasmen"),
]

FINDINGS = [
    ("19", "Exposed .git Directory", "TNI", "2025", []),
    ("18", "Reflected XSS", "BMKG, Indonesian Meteorology, Climatology and Geophysics Agency", "2025", ["XSS"]),
    ("17", "Sensitive Internal Configuration and Active Sentry DSN Exposed via Runtime Object", "Zooplus", "2026", []),
    ("16", "Exposed JavaScript Source Map Revealing Internal Source Files", "U.S. Department of Defense", "2026", []),
    ("15", "User Enumeration via Distinct Authentication Error Messages", "Whoop", "2026", []),
    ("14", "Exposed Sentry DSN in Production JavaScript Bundle", "Zooplus", "2026", []),
    ("13", "Unauthenticated IDOR on Cart API Exposing Shopping Data at Scale", "Zooplus", "2026", ["IDOR"]),
    ("12", "Exposed Telerik RadAsyncUpload and DialogHandler Endpoints", "U.S. Department of State", "2026", ["CVE-2019-18935", "CVE-2017-11317"]),
    ("11", "Missing Error Rollback Causing Persistent Orphan Wallet State Corruption", "Chia Network", "2026", []),
    ("10", "Unauthenticated Confluence REST API Exposing Internal Meeting Credentials and Personnel Data", "NASA", "2026", []),
    ("09", "Unauthenticated System Architecture Disclosure via Exposed Health Endpoints on an AI API Hub", "NASA", "2026", []),
    ("08", "Internal IP Address Disclosure via Content-Security-Policy Header", "Jakarta Provincial Government", "2026", []),
    ("07", "Publicly Accessible AEM Author Instance on Production Environment", "NASA", "2026", []),
    ("06", "Unauthenticated Access to Internal API Documentation on Staging Environment", "NASA", "2026", []),
    ("05", "No Rate Limiting on E-Learning Login", "TNI (Mil-CSIRT)", "2026", ["CWE-307"]),
    ("04", "No Rate Limiting on Zimbra SOAP Authentication", "TNI (Mil-CSIRT)", "2026", ["CWE-307"]),
    ("03", "Internal Error Field Disclosure and Single-Line CRLF Validation", "PT Arunika Vistara Digital", "2026", ["CWE-209", "CWE-93"]),
    ("02", "Contact Form Server Action Rate Limiting Deficiency", "PT Arunika Vistara Digital", "2026", ["CWE-799"]),
    ("01", "Stored XSS on News Page", "Bali Provincial Government", "2026", ["XSS"]),
]

SKILLS = [
    ("Offensive Security", "warm", [("Penetration Testing", None), ("Red Teaming", None), ("Web App Security", None), ("OSINT and Recon", None), ("Social Engineering", None), ("Vulnerability Analysis", None), ("Bug Bounty", None)]),
    ("Defensive Security", "lime", [("Incident Response", None), ("Threat Intelligence", None), ("Digital Forensics", None), ("System Hardening", None), ("Linux Administration", "linux"), ("Vulnerability Assessment", None)]),
    ("Networking and Wireless", "lime", [("Network Architecture", None), ("TCP/IP", None), ("WiFi Auditing", None), ("Bluetooth Testing", None), ("Protocol Analysis", None), ("3G / 4G / DCS", None), ("GSM", None), ("GPS", None), ("SS7 Basics", None)]),
    ("Cryptography and Malware", "warm", [("Classical Encryption", None), ("Modern Encryption", None), ("Hash Cracking", None), ("Malware Identification", None), ("Malware Analysis", None), ("Ransomware Cleanup", None), ("OS Recovery", None)]),
    ("Development", "lime", [("Python", "python"), ("SQL", None), ("Bash", "gnubash"), ("HTML", "html5"), ("CSS", "css3"), ("JavaScript", "javascript"), ("Kotlin", "kotlin"), ("C++ (learning)", "cplusplus"), ("Security Tooling", None), ("Automation", None), ("Android Apps", "android")]),
    ("IoT and Embedded", "warm", [("Building IoT Devices", None), ("Hardware Vulnerability Research", None), ("Protocol Research", None), ("Embedded Systems", None)]),
]

TOOLBOX = [
    ("Recon", [("Amass", None), ("Subfinder", None), ("theHarvester", None), ("Shodan", None), ("Recon-ng", None)]),
    ("Scanning", [("Nmap", None), ("Masscan", None), ("Nikto", None), ("Nuclei", None), ("Katana", None), ("ffuf", None)]),
    ("Web", [("Burp Suite", "burpsuite"), ("OWASP ZAP", None), ("SQLmap", None), ("BeEF", None)]),
    ("Exploitation and credentials", [("Metasploit", "metasploit"), ("Mimikatz", None), ("Hydra", None), ("Hashcat", None), ("John the Ripper", None), ("CrackMapExec", None)]),
    ("Network and wireless", [("Wireshark", "wireshark"), ("Aircrack-ng", None), ("Bettercap", None), ("Responder", None), ("Kismet", None), ("Wifite", None)]),
    ("Reverse and forensics", [("Ghidra", None), ("Volatility", None), ("YARA", None), ("Log Hunting", None)]),
    ("Operating systems", [("Kali Linux", "kalilinux"), ("BlackArch", None), ("Arch Linux", "archlinux"), ("Ubuntu", "ubuntu"), ("Fedora", "fedora"), ("Windows", "windows")]),
]

INTERESTS = ["Vulnerability Research", "Security Assessment", "Web Application Security", "Bug Bounty Hunting", "Ethical Hacking", "Penetration Testing", "Information Security", "Security Automation", "Cybersecurity Tools"]
PRINCIPLES = ["Integrity", "Analytical thinking", "Curiosity", "Discipline", "Ethics"]

TIMELINE = [
    ("Grade 7", "Wrote the first lines of code through Termux on an Android phone."),
    ("Grade 8", "Discovered cybersecurity through the game Watch Dogs 2 and never looked back."),
    ("Self-study years", "Courses, competitions, certifications and a lot of hands-on practice."),
    ("Dec 2025", "Joined Mavendra Ascarya as secretary of division 5."),
    ("9 Mar 2026", "Started applying skills legally and responsibly through responsible disclosure."),
    ("Jun 2026", "Recognized by the DKI Jakarta Provincial Government for a vulnerability discovery."),
    ("Oct 2026", "Recognized by the Bali Provincial Government for a Stored XSS discovery."),
]

PROJECTS = [
    ("Cwabs", "Flagship", "Cyber Web Analysis and Basic Scanner", "A web analysis and basic scanning tool for first-pass reconnaissance of web applications."),
    ("PatSec", "Android", "Android application", "A security-focused APK for Android, built as a hands-on mobile project."),
    ("PatSecWeb", "Web", "Web edition of PatSec", "The browser version of PatSec, so the same ideas work on any screen."),
    ("Open-source tools", "Open source", "Python tools and utilities", "Python tools, scripts and utilities published on GitHub for the community."),
    ("Private projects", "Private", "Commercial and confidential", "Commercial and confidential work that stays out of public repositories."),
    ("Learning projects", "Learning", "Experiments and educational builds", "Experiments and educational builds made to understand how things really behave."),
    ("Wireless protocols, network analysis and offensive security", "Ongoing research", "Current research", "Current research digs into wireless protocols, traffic and network behavior, and offensive security techniques, always inside legal and authorized boundaries."),
]

LEGAL = (
    "Copyright (c) " + YEARS + " Raffael Putra Hermawan. All rights reserved. The text, design, source code, graphics, structure and every other original element of this repository and of "
    "[raffaelsec.my.id](" + SITE + ") are protected under Law No. 28 of 2014 on Copyright of the Republic of Indonesia and applicable international treaties. "
    "Certificates and documents shown here remain the property of their respective issuers and are displayed for portfolio purposes only.\n>\n"
    "> Copying, scraping, mirroring, cloning, reproducing, redistributing, republishing screenshots, or reverse engineering any part of this content, including the certificate documents, "
    "without prior written permission is prohibited. Unauthorized access to, extraction of, or circumvention of protection measures on electronic information may also violate Law No. 11 of 2008 "
    "on Electronic Information and Transactions, as amended. Automated collection by bots and crawlers, and use for AI or machine learning training, is not permitted. "
    "For permission requests, write to " + EMAIL + "."
)


SECTIONS = [
    ("about", "user", "WHO I AM"),
    ("skills", "cpu", "WHAT I USE"),
    ("projects", "layers", "WHAT I BUILD"),
    ("findings", "bug", "WHAT I FOUND"),
    ("awards", "award", "RECOGNITION"),
    ("certifications", "badge", "TRAINING"),
    ("contact", "mail", "SAY HELLO"),
]

BUTTONS = [
    ("website", "globe", "Website", "raffaelsec.my.id"),
    ("linkedin", "linkedin", "LinkedIn", "raffael-sec"),
    ("github-projects", "github", "GitHub projects", "TheRealRafael00"),
    ("github-main", "github", "GitHub main", "faelll14"),
    ("instagram", "instagram", "Instagram", "ell_bugs"),
    ("email", "mail", "Email", "say hello"),
]
BUTTON_HREF = {
    "website": SITE,
    "linkedin": LINKEDIN,
    "github-projects": GH_PROJECTS,
    "github-main": GH_MAIN,
    "instagram": INSTAGRAM,
    "email": "mailto:" + EMAIL,
}

CERT_GROUPS = [
    ("Cybersecurity foundations", "shield", [1, 7, 8, 11, 12, 13, 14, 16, 20]),
    ("Ethical hacking and offensive security", "bug", [3, 5, 9, 10, 19, 21, 28]),
    ("Cryptography and threat intelligence", "key", [2, 6]),
    ("Cloud and DevSecOps", "network", [18, 30]),
    ("AI and prompt engineering", "cpu", [4, 17, 26, 31, 32, 33]),
    ("Data, SQL and analytics", "database", [15, 23, 24, 25]),
    ("Linux, seminars and awareness", "terminal", [22, 27, 29]),
]

SKILL_ICONS = ["bug", "shield", "wifi", "key", "code", "cpu"]
PROJECT_ICONS = ["radar", "phone", "globe", "github", "lock", "book", "wifi"]


def qb(text):
    return quote(text.replace("-", "--").replace("_", "__"), safe="")


def badge_url(message, color, label=None, logo=None, logo_color=None):
    if label is None:
        path = f"{qb(message)}-{color}"
    else:
        path = f"{qb(label)}-{qb(message)}-{color}"
    params = ["style=flat-square"]
    if label is not None:
        params.append(f"labelColor={C['bg']}")
    if logo:
        params.append(f"logo={logo}")
        params.append(f"logoColor={logo_color or (C['gold'] if label is not None else 'ffffff')}")
    return f"https://img.shields.io/badge/{path}?{'&'.join(params)}"


def img(url, alt, extra=""):
    return f'<img alt="{escape(alt, quote=True)}" src="{escape(url, quote=True)}"{extra}>'


def chip(text, color, logo=None):
    return img(badge_url(text, C[color], logo=logo), text)


def local(path, alt, extra=""):
    return f'<img src="{path}" alt="{escape(alt, quote=True)}"{extra}>'


def tile(name, size=44):
    return local(f"assets/icons/{name}.svg", "", f' width="{size}" height="{size}"')


def divider(key):
    return f'<img src="assets/dividers/{key}.svg" alt="" width="100%">'


def follower_badge(user):
    url = f"https://img.shields.io/github/followers/{user}?style=flat-square&label={quote(user)}%20followers&labelColor={C['bg']}&color={C['slate']}&logo=github&logoColor={C['gold']}"
    return img(url, f"{user} followers on GitHub")


def ref(r):
    if r.startswith("CWE-"):
        return f'<a href="https://cwe.mitre.org/data/definitions/{r[4:]}.html"><code>{r}</code></a>'
    if r.startswith("CVE-"):
        return f'<a href="https://nvd.nist.gov/vuln/detail/{r}"><code>{r}</code></a>'
    return f"<code>{r}</code>"


def short_org(o):
    return o.split(",")[0].strip()


def section_hero():
    buttons = "\n".join(
        f'<a href="{escape(BUTTON_HREF[k], quote=True)}">{local(f"assets/buttons/{k}.svg", f"{label}: {sub}", " width=\"270\" height=\"56\"")}</a>'
        for k, _, label, sub in BUTTONS
    )
    status = [
        img(badge_url("open to work", C["gold"], label="status"), "Status: open to work"),
        img(badge_url("offensive security", C["ember"], label="focus"), "Focus: offensive security"),
        img(badge_url("python", C["ice"], label="second focus", logo="python"), "Second focus: Python"),
        img(badge_url("responsible only", C["line"], label="disclosure"), "Disclosure: responsible only"),
        follower_badge("TheRealRafael00"),
        follower_badge("faelll14"),
    ]
    nav = " &nbsp;&middot;&nbsp; ".join(
        f'<a href="#{a}">{t}</a>'
        for a, t in [("about", "About"), ("skills", "Skills"), ("projects", "Projects"), ("findings", "Findings"), ("awards", "Awards"), ("certifications", "Certifications"), ("contact", "Contact")]
    )
    return (
        '<div align="center">\n'
        '<img src="assets/hero.svg" alt="Raffael Putra Hermawan, Cybersecurity Researcher, Ethical Hacker, Bug Bounty Hunter and Python Developer" width="100%">\n'
        f"<p>\n{buttons}\n</p>\n"
        f"<p>\n{chr(10).join(status)}\n</p>\n"
        '<img src="assets/stats.svg" alt="19 responsible disclosures, 5 awards, 33 certifications, 4 languages" width="100%">\n'
        f"<p>{nav}</p>\n"
        '<img src="assets/terminal.svg" alt="Terminal: whoami, focus, responsible disclosure, bug status" width="100%">\n'
        "</div>"
    )


def kv_table(rows):
    body = "".join(f'<tr><td width="200"><b>{escape(k)}</b></td><td>{escape(v)}</td></tr>' for k, v in rows)
    return f'<table width="100%">{body}</table>'


def section_about():
    profile = kv_table([
        ("Full name", "Raffael Putra Hermawan"),
        ("Goes by", "Ell"),
        ("Base", "Depok, Indonesia"),
        ("Focus", "Offensive security"),
        ("Second focus", "Python development"),
        ("Disclosure", "Responsible only"),
        ("Status", "Open to work"),
        ("Languages", "Indonesian (native), English (professional), French, Russian"),
    ])
    interests = "\n".join(chip(t, "slate") for t in INTERESTS)
    principles = "\n".join(chip(t, "ember") for t in PRINCIPLES)
    timeline = "".join(f'<tr><td width="200" valign="top"><b>{escape(w)}</b></td><td>{escape(t)}</td></tr>' for w, t in TIMELINE)
    return f"""{divider("about")}

## About

**Raffael Putra Hermawan** (also spelled Rafael Putra Hermawan, and known online as **Ell**) is an independent cybersecurity researcher, ethical hacker, bug bounty hunter and Python developer based in Depok, Indonesia.

I am interested in information security, vulnerability research, ethical hacking and Python development. It began with simple curiosity about how systems, applications and digital infrastructure really work. That curiosity grew into finding security weaknesses, understanding the risk behind them and helping strengthen the environment around them.

I work by the principle of responsible disclosure: find it, document it, report it, never abuse it. My long-term goal is to become a cybersecurity professional, contribute to security research, collaborate with the global community and build solutions that make the digital world safer.

{profile}

**Main interests**

<p>
{interests}
</p>

**Principles**

<p>
{principles}
</p>

### The journey so far

<table width="100%">{timeline}</table>

### Organizations

- **Mavendra Ascarya**: Secretary, division 5 (Sekbid 5), Dec 2025 to present
- **MPK OSIS SMAN 14 Depok**: Student council member"""


def group_table(rows, icons=None):
    out = []
    for i, (name, color, items) in enumerate(rows):
        chips = "\n".join(chip(t, color, logo) for t, logo in items)
        lead = f'<td width="64" valign="middle" align="center">{tile(icons[i], 40)}</td>' if icons else ""
        out.append(f'<tr>{lead}<td width="190" valign="middle"><b>{escape(name)}</b></td><td>\n{chips}\n</td></tr>')
    return '<table width="100%">\n' + "\n".join(out) + "\n</table>"


def section_skills():
    cats = [(n, SKILL_COLOR[c], items) for n, c, items in SKILLS]
    tools = group_table([(n, "slate", items) for n, items in TOOLBOX])
    return f"""{divider("skills")}

## Skills

Offense and defense, networks and code. Learned by breaking things I was allowed to break.

<img src="assets/marquee.svg" alt="Tools in rotation" width="100%">

{group_table(cats, SKILL_ICONS)}

### Toolbox

{tools}"""


def section_projects():
    rows = "".join(
        f'<tr><td width="64" align="center" valign="middle">{tile(PROJECT_ICONS[i], 40)}</td><td valign="middle"><b>{escape(n)}</b><br>{chip(tag, "gold" if i < 3 else "line")}</td><td valign="middle"><i>{escape(sub)}</i><br>{escape(d)}</td></tr>'
        for i, (n, tag, sub, d) in enumerate(PROJECTS)
    )
    return f"""{divider("projects")}

## Projects

Things I build between hunts. Public repositories live at [github.com/TheRealRafael00]({GH_PROJECTS}).

<table width="100%">
{rows}
</table>"""


def section_findings():
    years = {}
    orgs = {}
    for _, _, o, y, _ in FINDINGS:
        years[y] = years.get(y, 0) + 1
        orgs[short_org(o)] = orgs.get(short_org(o), 0) + 1
    ychips = "\n".join(img(badge_url(str(n), C["gold"], label=y), f"{n} findings in {y}") for y, n in sorted(years.items()))
    ochips = "\n".join(img(badge_url(str(n), C["slate"], label=o), f"{n} findings for {o}") for o, n in sorted(orgs.items(), key=lambda kv: (-kv[1], kv[0])) if n > 1)
    rows = "".join(
        f'<tr><td align="right"><code>{n}</code></td><td><b>{escape(t)}</b></td><td>{escape(o)}</td><td align="center">{y}</td><td>{" ".join(ref(r) for r in refs)}</td></tr>'
        for n, t, o, y, refs in FINDINGS
    )
    return f"""{divider("findings")}

## Findings

Responsible disclosure log. {len(FINDINGS)} reported findings across {len(orgs)} organizations. Target hostnames and technical details are withheld on purpose, because good manners are part of the job.

<p>
{ychips}
{ochips}
</p>

<table width="100%">
<tr><th>#</th><th align="left">Finding</th><th align="left">Organization</th><th>Year</th><th align="left">Reference</th></tr>
{rows}
</table>"""


def doc_table(head_cells, rows):
    th = "".join(f'<th align="left">{h}</th>' for h in head_cells)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table width="100%">\n<tr>{th}</tr>\n{body}\n</table>'


def website_button(anchor, text):
    url = badge_url(text, C["gold"], label="documents", logo="googlechrome", logo_color=C["gold"])
    return f'<a href="{SITE}/#{anchor}">{img(url, text)}</a>'


def section_awards():
    rows = "".join(
        f'<tr><td width="64" align="center" valign="middle">{tile("award", 40)}</td><td valign="middle"><b>{escape(t)}</b><br>{escape(p)}</td><td valign="middle" align="right"><code>{escape(n)}</code></td></tr>'
        for _, t, p, n in AWARDS
    )
    return f"""{divider("awards")}

## Awards

Recognition earned in the field. Awards and letters of appreciation from governments, companies and competitions. The documents themselves are shown in full on the website.

<p>{website_button("awards", "view awards on raffaelsec.my.id")}</p>

<table width="100%">
{rows}
</table>"""


def section_certs():
    covered = sorted(i for _, _, ids in CERT_GROUPS for i in ids)
    assert covered == list(range(1, len(CERTS) + 1)), covered
    blocks = []
    for title, ic, ids in CERT_GROUPS:
        rows = [(f"<code>{i:02d}</code>", f"<b>{escape(CERTS[i - 1][0])}</b>", escape(CERTS[i - 1][1])) for i in ids]
        blocks.append(f"### {title}\n\n<p>{tile(ic, 28)} {chip(str(len(ids)) + ' certificates', 'slate')}</p>\n\n" + doc_table(["#", "Certification", "Provider"], rows))
    return f"""{divider("certifications")}

## Certifications

Courses, exams and seminars. {len(CERTS)} certificates from global providers and national programs, grouped by topic. The documents themselves are shown in full on the website, where they can be searched by title or provider.

<p>{website_button("certifications", "view certifications on raffaelsec.my.id")}</p>

""" + "\n\n".join(blocks)


def section_contact():
    rows = [
        ("mail", "Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
        ("globe", "Website", f'<a href="{SITE}">raffaelsec.my.id</a>'),
        ("linkedin", "LinkedIn", f'<a href="{LINKEDIN}">linkedin.com/in/raffael-sec</a>'),
        ("github", "GitHub, projects", f'<a href="{GH_PROJECTS}">@TheRealRafael00</a>'),
        ("github", "GitHub, main", f'<a href="{GH_MAIN}">@faelll14</a>'),
        ("instagram", "Instagram", f'<a href="{INSTAGRAM}">@ell_bugs</a>'),
    ]
    body = "".join(f'<tr><td width="64" align="center">{tile(i, 40)}</td><td width="200"><b>{k}</b></td><td>{v}</td></tr>' for i, k, v in rows)
    open_to = "\n".join(chip(t, "ember") for t in ["Internships", "Collaboration", "CTF teams", "Research projects"])
    return f"""{divider("contact")}

## Contact

Let us work on something secure. Email gets a reply within 48 hours.

<p>
{open_to}
</p>

<table width="100%">{body}</table>"""


def section_legal():
    return f"""<img src="assets/footer.svg" alt="Thanks for stopping by. Hack responsibly, disclose ethically." width="100%">

> **Legal notice.** {LEGAL}

<div align="center">
<sub>Copyright (c) {YEARS} Raffael Putra Hermawan. All rights reserved. See <a href="LICENSE">LICENSE</a>. &nbsp;&middot;&nbsp; <a href="{SITE}">raffaelsec.my.id</a></sub>
</div>"""


def asset_data():
    names = [n for _, items in TOOLBOX for n, _ in items]
    return {
        "stats": [
            (str(len(FINDINGS)), "Responsible disclosures", "bug"),
            (str(len(AWARDS)), "Awards", "award"),
            (str(len(CERTS)), "Certifications", "badge"),
            ("4", "Languages", "globe"),
        ],
        "row1": names[0::2],
        "row2": names[1::2],
        "sections": SECTIONS,
        "buttons": BUTTONS,
    }


def main():
    os.makedirs(ASSETS, exist_ok=True)
    old = os.path.join(ASSETS, "banner.svg")
    if os.path.exists(old):
        os.remove(old)
    svg_assets.build_all(ASSETS, asset_data())
    parts = [
        section_hero(),
        section_about(),
        section_skills(),
        section_projects(),
        section_findings(),
        section_awards(),
        section_certs(),
        section_contact(),
        section_legal(),
    ]
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n\n".join(parts) + "\n")
    print("README.md written")


if __name__ == "__main__":
    main()
