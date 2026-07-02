# mtd_bhuvanadv
This repository is created for the 1st Batch of 2026 at MTD for the course Competitive Programming and Java Full Stack.

Notes
Organizing Your System
We must organize all files and folders properly in our system.

Step 1: Create a Software Folder
Create a folder named Software in the C: drive.
Inside the Software folder, create one folder for each software you wish to install.
Download the software setup (.exe/.msi) file.
Move (Cut & Paste) the downloaded installer from the Downloads folder into its respective folder inside the Software folder.
Install the software by double-clicking the installer from this location.
What Gets Installed?
Whenever we install software, the following components may be installed:

Program code
Libraries / Modules / Packages
Compiler (if applicable)
Runtime / Execution Environment (if applicable)
To use the software, we generally get one or both of the following types of applications:

CLI (Command Line Interface)
GUI (Graphical User Interface)
Examples
Python
When Python is installed, we get:

CLI:
python
pip
GUI:
IDLE (Python Shell)
Node.js
When Node.js is installed, we get:

CLI:
node
npm
MySQL
When MySQL is installed, we get:

CLI:
mysql
GUI (Optional):
MySQL Workbench
Environment Variables (PATH)
Some software installations do not make their CLI commands available globally.

In such cases:

Copy the installation path of the executable.
Add this path to the Environment Variables → PATH.
Close and reopen the Command Prompt or Terminal.
Note: The currently opened terminal will not recognize the changes until it is restarted.

Required Software Installations
Software	Purpose
Notepad++	Quick note taking
Visual Studio Code (VS Code)	IDE / Code Editor
Eclipse IDE	Java Development
JDK (Java Development Kit)	Java Compiler, JVM, and Libraries
Python	Python Interpreter, Libraries, and IDLE Shell
Git	Run Git commands
GitHub Desktop	Perform Git operations using GUI
MySQL	Practice SQL / RDBMS
MongoDB	Practice NoSQL (Server & Compass)
Node.js	Practice JavaScript
Learning Folder
Choose one drive in your laptop (preferably D: or E: instead of C:) for learning purposes.

Create a folder named:

Learning
If your laptop has only the C: drive, create:

C:\Learning
GitHub Setup
Step 1: Create a GitHub Account
Create a GitHub account using:

Your permanent email address
Your permanent phone number
Login to your account.

Step 2: Create a Repository
Create a new repository with the following name:

mtd2026
Step 3: Clone the Repository
Clone the repository into your Learning folder.

Steps
Open the Learning folder.
Open the terminal in that folder.
Run the following command using your repository URL:
git clone <repository-url>
Example:

git clone https://github.com/your-username/mtd2026.git
This creates a copy of your GitHub repository inside the Learning folder. The Repo in our laptop will be a folder. And Git can recognise this as a special folder nothing but a Repo folder.

PUSH and PULL:
push is to upload (from local repo to remote/server/cloud repo) pull is to download

length() java strlen() c

Java: byte, short, int, long mysql: tinyint, smallint, int, bigint

To avoid plagiarism, copy rights, trademarks etc. companies use different names for the same thing.

To update our local repo w.r.t. the remote repo, we must PULL/download.

git pull
git pull origin main
In all repos, at least one branch is always created and its name is main Thus when we run the command:

git pull
We are actually running (by default):

git pull origin main
Steps to Push:
We must 1st tell the git to list the names of the files and folders which are either modified or created or deleted.
git add <PATH>
Next step is to commit: Here, the git will create an object and save content of all the files from Step1 into the object and encript the object.
git commit -m "MESSAGE"
push
git push origin <branch name>
