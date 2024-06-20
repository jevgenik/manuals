=======
Node.js
=======
Node.js is a cross-platform, open-source JavaScript runtime environment that can run on Windows, Linux, Unix, macOS, and more. 
Node.js runs on the V8 JavaScript engine, and executes JavaScript code outside a web browser.

Node.js uses an asynchronous event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time 
applications that run across distributed devices. Upon each connection, the callback is fired, but if there is no work to be done, Node.js will sleep.

`Official Website <https://nodejs.org/en/>`_


npm
===
npm is the default package manager for Node.js and is written entirely in JavaScript. It is used for managing and sharing 
packages of code with other developers.

npm is the world's largest Software Registry.

npm commands
------------

* ``npm init`` - Create a new package.json file (initialize a new project)

* ``npm i <package_name>`` - Install a package (locally, folder node_modules will be created)

* Running ``npm i`` will install all the dependencies listed in the package.json file

* ``npm i -g <package_name>`` - Install a package globally

* ``npm i -D <package_name>`` - Install a package as a development dependency

* ``npm uninstall <package_name>`` - Uninstall a package

* ``npm uninstall -g <package_name>`` - Uninstall a package globally

* ``npm uninstall -D <package_name>`` - Uninstall a development dependency

* ``npm run <script_name>`` - Run a script from the package.json file (e.g. ``npm run dev``)

* ``npm list`` - List all locally installed packages

* ``npm list -g`` - List all globally installed packages

* ``npm audit`` - Check for vulnerabilities in installed packages

* ``npm audit fix`` - Fix vulnerabilities in installed packages

* ``npm outdated`` - Check for outdated packages

* ``npm update`` - Update all packages to the latest version


Installation and Usage
======================

To install Node.js and npm, run the following command:

.. code-block:: bash

   sudo apt-get install nodejs npm


To install a package, run the following command:

.. code-block:: bash

   npm install <package_name>


Create Hello World Application
==============================

Simple console application that prints "Hello, World!" to the console.
-----------------------------------------------------------------------

1. ``mkdir hello-world`` - Create a new directory

2. ``cd hello-world`` - Change to the new directory

3. ``npm init -y`` - Create a new package.json file (-y flag will skip the questionnaire)

4. ``nano index.js`` - Create and open a new file

5. Add the following code to the file 

.. code-block:: javascript

    console.log('Hello, World!');

6. ``node index.js`` - Run the file


Web application that prints "Hello, World!" to the browser.
-----------------------------------------------------------

1. ``nano server.js`` - Create a new file
2. Add the following code to the file

.. code-block:: javascript

    const http = require('http');
    const hostname = '';
    const port = 3000;

    const server = http.createServer((req, res) => {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Hello, World!\n');
    });

    server.listen(port, hostname, () => {
      console.log(`Server running at http://${hostname}:${port}/`);
    });

3. ``node server.js`` - Run the file

Open a web browser and navigate to http://localhost:3000. You should see the message "Hello, World!".

Express.js
==========
Express.js is fast, unopinionated, minimalist web framework for Node.js
It is used for building web applications and APIs.

`Official Website <https://expressjs.com/>`_

Installation and Usage
----------------------

To install Express.js, run the following command:

.. code-block:: bash

   npm install express


npm and node commands
=====================

* ``npm init`` - Create a new package.json file (initialize a new project)

* ``npm i <package_name>`` - Install a package

* ``npme i -D <package_name>`` - Install a package as a development dependency

  - ``npm i -D typescript ts-node nodemon @types/express @types/socket.io`` 

* ``npm run <script_name>`` - Run a script from the package.json file

  - ``npm run dev`` - Run the script named "dev" from the package.json file
  - ``npm run start`` - Run the script named "start" from the package.json file

* ``node -v`` - Check the installed version of Node.js

* ``node <file_name>`` - Run a JavaScript file (e.g. node index.js)
