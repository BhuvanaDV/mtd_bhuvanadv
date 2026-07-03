# mtd_bhuvanadv

This repository is created for the 1st Batch of 2026 at MTD for the course Competitive Programming and Java Full Stack.

## Notes

### Organizing Your System
We must organize all files and folders properly in our system.

#### Step 1: Create a Software Folder
- Create a folder named `Software` in the `C:` drive.
- Inside the `Software` folder, create one folder for each software you wish to install.
- Download the software setup file (`.exe` or `.msi`).
- Move the downloaded installer from the `Downloads` folder into its respective folder inside the `Software` folder.
- Install the software by double-clicking the installer from that location.

### What Gets Installed?
Whenever we install software, the following components may be installed:

- Program code
- Libraries / Modules / Packages
- Compiler (if applicable)
- Runtime / Execution Environment (if applicable)

To use the software, we generally get one or both of the following types of applications:

- CLI (Command Line Interface)
- GUI (Graphical User Interface)

### Examples

#### Python
When Python is installed, we get:

- CLI: `python`, `pip`
- GUI: `IDLE` (Python Shell)

#### Node.js
When Node.js is installed, we get:

- CLI: `node`, `npm`

#### MySQL
When MySQL is installed, we get:

- CLI: `mysql`
- GUI (Optional): MySQL Workbench

### Environment Variables (PATH)
Some software installations do not make their CLI commands available globally.

In such cases:

1. Copy the installation path of the executable.
2. Add this path to the Environment Variables → PATH.
3. Close and reopen the Command Prompt or Terminal.

> Note: The currently opened terminal will not recognize the changes until it is restarted.

### Required Software Installations

| Software | Purpose |
|---|---|
| Notepad++ | Quick note taking |
| Visual Studio Code (VS Code) | IDE / Code Editor |
| Eclipse IDE | Java Development |
| JDK (Java Development Kit) | Java Compiler, JVM, and Libraries |
| Python | Python Interpreter, Libraries, and IDLE Shell |
| Git | Run Git commands |
| GitHub Desktop | Perform Git operations using GUI |
| MySQL | Practice SQL / RDBMS |
| MongoDB | Practice NoSQL (Server & Compass) |
| Node.js | Practice JavaScript |

### Learning Folder
Choose one drive in your laptop (preferably `D:` or `E:` instead of `C:`) for learning purposes.

Create a folder named:

- `Learning`

If your laptop has only the `C:` drive, create:

- `C:\Learning`

## GitHub Setup

### Step 1: Create a GitHub Account
Create a GitHub account using:

- Your permanent email address
- Your permanent phone number
- Login to your account

### Step 2: Create a Repository
Create a new repository with the following name:

- `mtd2026`

### Step 3: Clone the Repository
Clone the repository into your Learning folder.

#### Steps
1. Open the Learning folder.
2. Open the terminal in that folder.
3. Run the following command using your repository URL:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/your-username/mtd2026.git
```

This creates a copy of your GitHub repository inside the Learning folder. The repo on your laptop will be a folder, and Git can recognize it as a special folder, which is a repository folder.

## Git Basics

### PUSH and PULL
- `push` is used to upload from the local repository to the remote/cloud repository.
- `pull` is used to download from the remote repository to the local repository.

### Common Notes
- `length()` in Java
- `strlen()` in C
- Java: `byte`, `short`, `int`, `long`
- MySQL: `tinyint`, `smallint`, `int`, `bigint`

To avoid plagiarism, copy rights, trademarks, etc., companies use different names for the same thing.

### Update Local Repo with Remote Repo
To update our local repository with respect to the remote repository, we must pull/download:

```bash
git pull
git pull origin main
```

In all repositories, at least one branch is always created and its name is `main`. So when we run:

```bash
git pull
```

we are actually running (by default):

```bash
git pull origin main
```

### Steps to Push
1. Tell Git to list the files and folders that are modified, created, or deleted:

```bash
git add <PATH>
```

2. Commit the changes. Git will create an object and save the content of all files from Step 1 into that object and encrypt it:

```bash
git commit -m "MESSAGE"
```

3. Push the changes:

```bash
git push origin <branch name>
```