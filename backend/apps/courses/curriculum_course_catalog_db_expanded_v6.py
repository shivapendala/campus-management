"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 7

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for CSE, ECE, EEE, and CIVIL courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V6: Dict[str, Dict[str, Any]] = {
    "CS601": {
        "code": "CS601",
        "title": "Software Engineering",
        "credits": 4,
        "ltp": "3-0-0",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Software Process Models",
                "topics": [
                    "Software engineering definition, software development life cycle (SDLC) phases.",
                    "Process models: Waterfall model, incremental process models, evolutionary process models (Prototyping, Spiral).",
                    "Unified Process (UP), Agile software development paradigms, Scrum framework, Extreme Programming (XP).",
                    "Software engineering ethics, professional practices, statutory software quality standards."
                ]
            },
            {
                "unit": 2,
                "title": "Requirements Engineering & Analysis",
                "topics": [
                    "Requirements engineering tasks: Inception, elicitation, elaboration, negotiation, specification, validation, management.",
                    "Software Requirements Specification (SRS) document structure, IEEE 830 standard.",
                    "Requirements modeling: Scenario-based modeling (use cases, activity diagrams), data modeling (class diagrams).",
                    "Behavioral modeling: State machine diagrams, sequence diagrams, collaboration diagrams."
                ]
            },
            {
                "unit": 3,
                "title": "Software Design Concepts",
                "topics": [
                    "Design process and design quality guidelines, abstraction, refinement, modularity, information hiding.",
                    "Functional independence: Cohesion types, coupling types, design trade-offs.",
                    "Software architecture designs: Data-centered, data-flow, call and return, layered architectures.",
                    "User Interface (UI) design guidelines, golden rules of interface design, user analysis and task modeling."
                ]
            },
            {
                "unit": 4,
                "title": "Software Testing Strategies",
                "topics": [
                    "Strategic approach to software testing: Unit testing, integration testing (top-down, bottom-up, regression).",
                    "Validation testing, system testing: Recovery, security, stress, and performance testing.",
                    "Black-box testing techniques: Equivalence partitioning, boundary value analysis, decision table testing.",
                    "White-box testing techniques: Basis path testing, cyclomatic complexity calculation, control structure testing."
                ]
            },
            {
                "unit": 5,
                "title": "Software Project Management & Quality",
                "topics": [
                    "Project metrics: Size-oriented metrics (LOC), function-oriented metrics (FP), empirical estimation models (COCOMO).",
                    "Software quality assurance (SQA): Software quality factors (McCall's factors), ISO 9000, CMMI levels.",
                    "Risk management: Risk identification, projection, mitigation, monitoring, and management (RMMM) plan.",
                    "Software configuration management (SCM): Version control (Git), change control process, build automation."
                ]
            }
        ],
        "textbooks": [
            "Roger S. Pressman and Bruce Maxim, 'Software Engineering: A Practitioner's Approach', McGraw-Hill, 9th Edition.",
            "Ian Sommerville, 'Software Engineering', Pearson, 10th Edition."
        ]
    },
    "AI601": {
        "code": "AI601",
        "title": "Computer Vision",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Artificial Intelligence & Data Science",
        "units": [
            {
                "unit": 1,
                "title": "Image Formation & Processing",
                "topics": [
                    "Pinhole camera model, camera calibration, intrinsic and extrinsic parameters.",
                    "Image filtering: Gaussian blur, median filter, bilateral filter.",
                    "Edge detection: Sobel, Laplacian of Gaussian, Canny edge detector.",
                    "Scale-Invariant Feature Transform (SIFT), Speeded-Up Robust Features (SURF), Harris corner detector."
                ]
            },
            {
                "unit": 2,
                "title": "Image Classification & CNNs",
                "topics": [
                    "Image classification pipeline, linear classifiers, loss functions: Multiclass SVM, Softmax.",
                    "Convolutional Neural Networks (CNNs) for vision, architectural evolution: VGG, ResNet, EfficientNet.",
                    "Data augmentation techniques, transfer learning, fine-tuning strategies."
                ]
            },
            {
                "unit": 3,
                "title": "Object Detection & Segmentation",
                "topics": [
                    "Object detection concepts, bounding box regression, Intersection over Union (IoU), non-maximum suppression.",
                    "Two-stage detectors: R-CNN, Fast R-CNN, Faster R-CNN (Region Proposal Networks).",
                    "One-stage detectors: YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector).",
                    "Semantic segmentation: Fully Convolutional Networks (FCN), U-Net, DeepLab.",
                    "Instance segmentation: Mask R-CNN architecture."
                ]
            },
            {
                "unit": 4,
                "title": "Object Tracking & Video Analysis",
                "topics": [
                    "Optical flow: Lucas-Kanade and Horn-Schunck algorithms.",
                    "Object tracking paradigms: Kalman filtering, Mean-Shift, DeepSORT tracker.",
                    "Action recognition in video: 3D CNNs, Two-stream networks, LSTM-based models."
                ]
            },
            {
                "unit": 5,
                "title": "Generative Models in Vision",
                "topics": [
                    "Variational Autoencoders (VAEs): Mathematical formulation, reparameterization trick.",
                    "Generative Adversarial Networks (GANs): Minimax game, DCGAN, CycleGAN, StyleGAN.",
                    "Diffusion models: Denoising Diffusion Probabilistic Models (DDPM), Stable Diffusion architecture.",
                    "Evaluation of generative models: Inception Score (IS), Frechet Inception Distance (FID)."
                ]
            }
        ],
        "textbooks": [
            "Richard Szeliski, 'Computer Vision: Algorithms and Applications', Springer, 2nd Edition.",
            "David A. Forsyth and Jean Ponce, 'Computer Vision: A Modern Approach', Pearson, 2nd Edition."
        ]
    }
}
