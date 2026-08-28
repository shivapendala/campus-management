/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 6
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v6 = {
  CSE: {
    semesters: [
      {
        semester: 7,
        courses: [
          {
            code: "CS701",
            title: "Cloud Computing",
            units: [
              {
                unit: 1,
                title: "Cloud Computing Fundamental Concepts",
                topics: [
                  "Evolution of cloud computing, cloud definition, NIST cloud computing reference architecture.",
                  "Cloud service models: Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS).",
                  "Cloud deployment models: Public, Private, Hybrid, and Community clouds.",
                  "Benefits and challenges of cloud computing, economic models, CAPEX vs OPEX models."
                ],
                learning_objectives: "Classify cloud computing service models and explain virtualization architecture benefits."
              },
              {
                unit: 2,
                title: "Virtualization Technology",
                topics: [
                  "Virtualization definitions, hypervisors Type 1 (bare-metal) and Type 2 (hosted), hypervisor architecture.",
                  "Full virtualization, para-virtualization, hardware-assisted virtualization techniques.",
                  "Virtual machines (VMs) lifecycle: Provisioning, migration (live migration), cloning, templates.",
                  "Containerization technology: Docker, namespace isolation, control groups, containers vs virtual machines."
                ],
                learning_objectives: "Configure hypervisors and build isolated Docker container services."
              },
              {
                unit: 3,
                title: "Cloud Infrastructure & Resource Management",
                topics: [
                  "Virtual compute resources, CPU virtualization, memory virtualization, I/O virtualization.",
                  "Cloud storage systems: Block storage, object storage (Amazon S3), file storage, software-defined storage.",
                  "Virtual networking: Virtual LANs (VLANs), Software Defined Networking (SDN), virtual routers and firewalls.",
                  "Resource scheduling, load balancing algorithms: Round Robin, Least Connections, load indicators."
                ],
                learning_objectives: "Design software-defined storage architectures and apply load balancing policies."
              },
              {
                unit: 4,
                title: "Cloud Programming & Orchestration",
                topics: [
                  "Cloud programming models: MapReduce framework, Hadoop architecture, distributed file systems (HDFS).",
                  "Serverless computing: Function as a Service (FaaS), event-driven execution paradigms.",
                  "Cloud orchestration: Infrastructure as Code (IaC), Terraform, AWS CloudFormation, Ansible configuration management.",
                  "Microservices architecture, API gateways, service discovery in distributed environments."
                ],
                learning_objectives: "Develop MapReduce functions and orchestrate microservices using Terraform scripts."
              },
              {
                unit: 5,
                title: "Cloud Security & SLA Management",
                topics: [
                  "Cloud security challenges, shared responsibility security model, data privacy and residency compliance.",
                  "Access control in clouds: Identity and Access Management (IAM) roles, OAuth 2.0 and SAML standards.",
                  "Service Level Agreements (SLAs): SLA components, performance metrics, penalty categories for SLA violations.",
                  "Cloud monitoring tools, auto-scaling policy configurations, cost optimization strategies."
                ],
                learning_objectives: "Enforce IAM roles and monitor system performance against SLA metrics."
              }
            ],
            textbooks: [
              "Kai Hwang, Geoffrey C. Fox, and Jack J. Dongarra, 'Distributed and Cloud Computing: From Parallel Processing to the Internet of Things'.",
              "Rajkumar Buyya, Christian Vecchiola, and S. Thamarai Selvi, 'Mastering Cloud Computing'."
            ]
          }
        ]
      }
    ]
  },
  AIML: {
    semesters: [
      {
        semester: 6,
        courses: [
          {
            code: "AI601",
            title: "Computer Vision",
            units: [
              {
                unit: 1,
                title: "Image Formation & Processing",
                topics: [
                  "Pinhole camera model, camera calibration, intrinsic and extrinsic parameters.",
                  "Image filtering: Gaussian blur, median filter, bilateral filter.",
                  "Edge detection: Sobel, Laplacian of Gaussian, Canny edge detector.",
                  "Scale-Invariant Feature Transform (SIFT), Speeded-Up Robust Features (SURF), Harris corner detector."
                ],
                learning_objectives: "Calibrate camera models and extract Scale-Invariant local image features."
              },
              {
                unit: 2,
                title: "Image Classification & CNNs",
                topics: [
                  "Image classification pipeline, linear classifiers, loss functions: Multiclass SVM, Softmax.",
                  "Convolutional Neural Networks (CNNs) for vision, architectural evolution: VGG, ResNet, EfficientNet.",
                  "Data augmentation techniques, transfer learning, fine-tuning strategies."
                ],
                learning_objectives: "Construct deep convolutional neural networks and apply transfer learning weights."
              },
              {
                unit: 3,
                title: "Object Detection & Segmentation",
                topics: [
                  "Object detection concepts, bounding box regression, Intersection over Union (IoU), non-maximum suppression.",
                  "Two-stage detectors: R-CNN, Fast R-CNN, Faster R-CNN (Region Proposal Networks).",
                  "One-stage detectors: YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector).",
                  "Semantic segmentation: Fully Convolutional Networks (FCN), U-Net, DeepLab.",
                  "Instance segmentation: Mask R-CNN architecture."
                ],
                learning_objectives: "Train YOLO object detectors and implement U-Net semantic segmentation."
              },
              {
                unit: 4,
                title: "Object Tracking & Video Analysis",
                topics: [
                  "Optical flow: Lucas-Kanade and Horn-Schunck algorithms.",
                  "Object tracking paradigms: Kalman filtering, Mean-Shift, DeepSORT tracker.",
                  "Action recognition in video: 3D CNNs, Two-stream networks, LSTM-based models."
                ],
                learning_objectives: "Track moving target objects in raw video sequences using DeepSORT trackers."
              },
              {
                unit: 5,
                title: "Generative Models in Vision",
                topics: [
                  "Variational Autoencoders (VAEs): Mathematical formulation, reparameterization trick.",
                  "Generative Adversarial Networks (GANs): Minimax game, DCGAN, CycleGAN, StyleGAN.",
                  "Diffusion models: Denoising Diffusion Probabilistic Models (DDPM), Stable Diffusion architecture.",
                  "Evaluation of generative models: Inception Score (IS), Frechet Inception Distance (FID)."
                ],
                learning_objectives: "Synthesize photorealistic images using GAN minimax networks and Stable Diffusion."
              }
            ],
            textbooks: [
              "Richard Szeliski, 'Computer Vision: Algorithms and Applications'.",
              "David A. Forsyth and Jean Ponce, 'Computer Vision: A Modern Approach'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v6;
