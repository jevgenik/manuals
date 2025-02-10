===========
Kubernetes
===========
Kubernetes (K8s) is an open-source container orchestration platform that automates the deployment, scaling, and 
management of containerized applications. It groups containers that make up an application into logical units 
for easy management and discovery. Kubernetes provides a framework to run distributed systems resiliently, 
taking care of scaling and failover for your applications. 

* `Official Documentation <https://kubernetes.io/docs/home/>`_ 

.. figure:: images/kubernetes_architecture.png
   :alt: Kubernetes Architecture
   :width: 100%

   Kubernetes cluster architecture


Kubectl
=======
Kubectl is a command-line tool for controlling the Kubernetes cluster. It allows you to manage your cluster and 
applications through the Kubernetes API.

* `Kubectl Documentation <https://kubernetes.io/docs/reference/kubectl/>`_ 

.. note::
   Kubernetes config files are stored in the ``.kube`` directory of the user's home directory.


Components and Terminology
==========================

* `Namespace <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>`_ - a namespace is a 
  logical grouping of resources in a cluster.


Commands
========
* ``kubectl get nodes`` - list all nodes in the cluster
* ``kubectl create ns <namespace>`` - create a new namespace (`more info <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>`_)





