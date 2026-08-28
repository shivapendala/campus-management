"""
EduCore Framework - Department of Computer Science & Engineering (CSE) Detailed Course Syllabi v2

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced CSE courses:
- CS601: Software Engineering (SE)
- CS701: Cloud Computing (CC)
"""

from typing import Dict, Any

CSE_DETAILED_COURSES_CATALOG_V2: Dict[str, Dict[str, Any]] = {
    "CS601": {
        "code": "CS601",
        "title": "Software Engineering",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Software Process Models",
                "topics": [
                    "Software engineering definition, software development life cycle (SDLC) phases",
                    "Process models: Waterfall model, incremental process models, evolutionary process models (Prototyping, Spiral)",
                    "Unified Process (UP), Agile software development paradigms, Scrum framework, Extreme Programming (XP)",
                    "Software engineering ethics, professional practices, statutory software quality standards"
                ]
            },
            {
                "unit": 2,
                "title": "Requirements Engineering & Analysis",
                "topics": [
                    "Requirements engineering tasks: Inception, elicitation, elaboration, negotiation, specification, validation, management",
                    "Software Requirements Specification (SRS) document structure, IEEE 830 standard",
                    "Requirements modeling: Scenario-based modeling (use cases, activity diagrams), data modeling (class diagrams)",
                    "Behavioral modeling: State machine diagrams, sequence diagrams, collaboration diagrams"
                ]
            },
            {
                "unit": 3,
                "title": "Software Design Concepts",
                "topics": [
                    "Design process and design quality guidelines, abstraction, refinement, modularity, information hiding",
                    "Functional independence: Cohesion types, coupling types, design trade-offs",
                    "Software architecture designs: Data-centered, data-flow, call and return, layered architectures",
                    "User Interface (UI) design guidelines, golden rules of interface design, user analysis and task modeling"
                ]
            },
            {
                "unit": 4,
                "title": "Software Testing Strategies",
                "topics": [
                    "Strategic approach to software testing: Unit testing, integration testing (top-down, bottom-up, regression)",
                    "Validation testing, system testing: Recovery, security, stress, and performance testing",
                    "Black-box testing techniques: Equivalence partitioning, boundary value analysis, decision table testing",
                    "White-box testing techniques: Basis path testing, cyclomatic complexity calculation, control structure testing"
                ]
            },
            {
                "unit": 5,
                "title": "Software Project Management & Quality",
                "topics": [
                    "Project metrics: Size-oriented metrics (LOC), function-oriented metrics (FP), empirical estimation models (COCOMO)",
                    "Software quality assurance (SQA): Software quality factors (McCall's factors), ISO 9000, CMMI levels",
                    "Risk management: Risk identification, projection, mitigation, monitoring, and management (RMMM) plan",
                    "Software configuration management (SCM): Version control (Git), change control process, build automation"
                ]
            }
        ],
        "textbooks": [
            "Roger S. Pressman and Bruce Maxim, 'Software Engineering: A Practitioner's Approach', McGraw-Hill, 9th Edition.",
            "Ian Sommerville, 'Software Engineering', Pearson, 10th Edition."
        ]
    },
    "CS701": {
        "code": "CS701",
        "title": "Cloud Computing",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Cloud Computing Fundamental Concepts",
                "topics": [
                    "Evolution of cloud computing, cloud definition, NIST cloud computing reference architecture",
                    "Cloud service models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS)",
                    "Cloud deployment models: Public, Private, Hybrid, and Community clouds",
                    "Benefits and challenges of cloud computing, economic models, CAPEX vs OPEX models"
                ]
            },
            {
                "unit": 2,
                "title": "Virtualization Technology",
                "topics": [
                    "Virtualization definitions, hypervisors Type 1 (bare-metal) and Type 2 (hosted), hypervisor architecture",
                    "Full virtualization, para-virtualization, hardware-assisted virtualization techniques",
                    "Virtual machines (VMs) lifecycle: Provisioning, migration (live migration), cloning, templates",
                    "Containerization technology: Docker, namespace isolation, control groups, containers vs virtual machines"
                ]
            },
            {
                "unit": 3,
                "title": "Cloud Infrastructure & Resource Management",
                "topics": [
                    "Virtual compute resources, CPU virtualization, memory virtualization, I/O virtualization",
                    "Cloud storage systems: Block storage, object storage (Amazon S3), file storage, software-defined storage",
                    "Virtual networking: Virtual LANs (VLANs), Software Defined Networking (SDN), virtual routers and firewalls",
                    "Resource scheduling, load balancing algorithms: Round Robin, Least Connections, load indicators"
                ]
            },
            {
                "unit": 4,
                "title": "Cloud Programming & Orchestration",
                "topics": [
                    "Cloud programming models: MapReduce framework, Hadoop architecture, distributed file systems (HDFS)",
                    "Serverless computing: Function as a Service (FaaS), event-driven execution paradigms",
                    "Cloud orchestration: Infrastructure as Code (IaC), Terraform, AWS CloudFormation, Ansible configuration management",
                    "Microservices architecture, API gateways, service discovery in distributed environments"
                ]
            },
            {
                "unit": 5,
                "title": "Cloud Security & SLA Management",
                "topics": [
                    "Cloud security challenges, shared responsibility security model, data privacy and residency compliance",
                    "Access control in clouds: Identity and Access Management (IAM) roles, OAuth 2.0 and SAML standards",
                    "Service Level Agreements (SLAs): SLA components, performance metrics, penalty Slabs for SLA violations",
                    "Cloud monitoring tools, auto-scaling policy configurations, cost optimization strategies"
                ]
            }
        ],
        "textbooks": [
            "Kai Hwang, Geoffrey C. Fox, and Jack J. Dongarra, 'Distributed and Cloud Computing: From Parallel Processing to the Internet of Things', Morgan Kaufmann.",
            "Rajkumar Buyya, Christian Vecchiola, and S. Thamarai Selvi, 'Mastering Cloud Computing', Tata McGraw-Hill."
        ]
    }
}
