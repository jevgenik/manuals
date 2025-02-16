==
Nx
==

Nx is a smart, extensible build framework that helps you maintain, scale, and manage monorepos. It provides a set of tools for architecting, testing, and building multiple full-stack applications in a single workspace.

* `Official Documentation <https://nx.dev/getting-started/intro>`_

Key Features
============

* **Monorepo Support**: Manage multiple applications and libraries in a single workspace
* **Smart Rebuilds**: Only rebuilds what is affected by your changes
* **Powerful Tooling**: Integrated tools for testing, linting, and building
* **Extensible**: Rich plugin ecosystem for various frameworks and tools


Installation
============

.. code-block:: bash

   # Using npm
   npm install -g nx

   # Using yarn
   yarn global add nx


Creating a New Workspace
========================

There are two main ways to create an Nx workspace:

* ``npx create-nx-workspace`` - Creates a new workspace from scratch with interactive prompts to:
   * Choose a preset (empty, React, Angular, etc.)
   * Set up the initial configuration
   * Create the first application
   * Configure additional tools and features

* ``nx init`` - Adds Nx to an existing project:
   * Converts an existing repository into an Nx workspace
   * Keeps existing code and configuration
   * Adds Nx configuration files
   * Useful for migrating existing projects to Nx


Basic Commands
==============

* ``nx generate <schematic>`` - Runs a generator that creates and/or modifies files based on a generator 
  from a plugin. *e.g. nx generate @nx/react:component libs/my-lib/src/lib/my-component*
* ``nx build <project>`` - Build a project
* ``nx serve <project>`` - Serve a project
* ``nx test <project>`` - Run tests for a project
* ``nx affected:*`` - Run tasks only for affected projects 
* ``npx nx list`` - To get a list of installed plugins.
* ``npx nx list <plugin-name>`` - To learn about more specific capabilities of a particular plugin
