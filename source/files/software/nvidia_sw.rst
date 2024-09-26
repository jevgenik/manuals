=========================
NVIDIA Software Ecosystem
=========================

NGC
===
NVIDIA NGC™ is the portal of enterprise services, software, management tools, and support 
for end-to-end AI and digital twin workflows. Bring your solutions to market faster with 
fully managed services, or take advantage of performance-optimized software to build and 
deploy solutions on your preferred cloud, on-prem, and edge systems.

* `Official website <https://www.nvidia.com/en-eu/gpu-cloud/>`_


NGC Catalog
------------
NGC Catalog is a curated set of GPU-optimized software for AI, HPC and Visualization. 
The content provided by NVIDIA and third-party ISVs simplifies building, customizing, and 
integrating GPU-optimized software into workflows, accelerating the time to solutions for users.

* `NGC Catalog <https://ngc.nvidia.com/catalog>`_


nvcr.io
-------
NVIDIA Container Registry (nvcr.io) is a container registry provided by NVIDIA as part of 
the NVIDIA GPU Cloud (NGC) platform.
Contains pre-built, GPU-accelerated Docker containers
It's similar to Docker Hub but tailored for NVIDIA's GPU-accelerated containers.


Nvidia NIMs (Nvidia inference microservices)
===========================================
Nvidia NIMs (Nvidia inference microservices) are a collection of easy to use API driven microservices to interact with AI models. 
`Explore NIMs <https://build.nvidia.com/explore/discover>`_

* Metropolis NIM Workflows. This repository **hosts reference workflows** that show how to build applications using NVIDIA 
  Inference Microservices (NIMs). `GitHub <https://github.com/nvidia/metropolis-nim-workflows>`_

* NVIDIA VIA (Visual Insight Agent) Microservices are **cloud-native building blocks to build AI agents** capable of **processing large amounts 
  of live or archived videos** and images with Vision-Language Models (VLM) - whether deployed at the edge or cloud. This new generation of visual 
  AI agents will help nearly every industry summarize, search, and extract actionable insights from video using natural language.
  `More about VIA <https://developer.nvidia.com/visual-insight-agent-early-access>`_

`Webinar Build Visual AI Agents With Generative AI and NVIDIA NIM <https://event.on24.com/eventRegistration/console/apollox/mainEvent?&eventid=4676776&sessionid=1&username=&partnerref=&format=fhvideo1&mobile=&flashsupportedmobiledevice=&helpcenter=&key=57089A8A66742C678071FE4152CA6CD1&newConsole=true&nxChe=true&newTabCon=true&consoleEarEventConsole=false&consoleEarCloudApi=false&text_language_id=en&playerwidth=748&playerheight=526&eventuserid=702670853&contenttype=A&mediametricsessionid=604518425&mediametricid=6584720&usercd=702670853&mode=launch>`_

Use Cases
---------
* Can create a workflow for **semantic search** among large set of images (e.g. "show me all images with a red car")
  `Example on GitHub <https://github.com/NVIDIA/metropolis-nim-workflows/tree/main/nim_workflows/nvclip_semantic_search>`_

* NVDINOv2 (general purpose vision embedding model) Few Shot Classification. By using the NVDINOv2 NIM API, you can quickly generate 
  embeddings on a set of images. These embeddings can stored in a vector database, clustered and searched to build a **few shot 
  classification pipeline** with no model training or local GPU required.
  `Example on GitHub <https://github.com/NVIDIA/metropolis-nim-workflows/tree/main/nim_workflows/nvdinov2_few_shot>`_

* **Structured text extraction from images** (e.g. from ID cards). 
  `Example on GitHub <https://github.com/NVIDIA/metropolis-nim-workflows/tree/main/nim_workflows/vision_text_extraction>`_

* **VLM alerts**. For example can set an alarm by natural language
  prompt "is there a fire on the image?" And a camera video stream will be analyzed by the pipeline and if a fire is detected
  an alarm will be triggered (sent a request by a WebSocket) 
  `Example on GitHub <https://github.com/NVIDIA/metropolis-nim-workflows/tree/main/nim_workflows/vlm_alerts>`_

**Nvidia Metropolis** is a platform that enables the development of AI applications for video analytics.
`Website <https://www.nvidia.com/en-eu/autonomous-machines/intelligent-video-analytics-platform/>`_


NVIDIA TAO
==========
The open-source NVIDIA TAO (Train, Adapt, Optimize), built on TensorFlow and PyTorch, uses the power of transfer 
learning while simultaneously simplifying the model training process and optimizing the model for inference throughput 
on practically any platform. The result is an ultra-streamlined workflow. 

Take one of the pretrained models, adapt them to your own real or synthetic data, then optimize for inference throughput. 
All without needing AI expertise or large training datasets.

`Official website <https://developer.nvidia.com/tao-toolkit>`_


NVIDIA AI Foundry
=================
NVIDIA AI Foundry is the end-to-end platform and service for building custom models for generative AI.
Just as TSMC manufactures chips designed by other companies, NVIDIA AI Foundry enables organizations to develop their own AI models.

* NVIDIA Edify,  a multimodal AI architecture that can use simple text prompts to generate images, videos, 3D assets, 360-degree 
  high-dynamic-range imaging and physically based rendering (PBR) materials.
  `Test Edify models online <https://build.nvidia.com/nim?q=edify>`_

`Official website <https://www.nvidia.com/en-us/ai/foundry/>`_