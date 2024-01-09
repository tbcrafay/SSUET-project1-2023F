# SSUET-project1-2023F
<h1>Project name :- Student housing portal.  </h1>
<h5> Description:- </h5> Providing students, the ease of search functionality to search the hostels. 

<h2> Don't Forget to Install Virtual Environment to execute the project!</h2>

 <b> Here are the steps to install and use a virtual environment in PowerShell: </b>
 

<h4> 1. Check for Python Installation: </h4>

- Open PowerShell and type:

   ```powershell
   python --version
   ```

- If Python is installed, you'll see the version number. If not, download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

<h5>2. Create a Virtual Environment:</h5>

- Navigate to the desired directory:

   ```powershell
   cd <path_to_your_project_directory>
   ```

- Create the virtual environment named "env" (you can choose any name):

   ```powershell
   python -m venv env
   ```

<h5>3. Activate the Virtual Environment:</h5>

- Run the activation script:

   ```powershell
   .\env\Scripts\activate.ps1
   ```

- You'll see the virtual environment's name in parentheses before your prompt.

<h5> 4. Install Packages:</h5>

- Use `pip` to install packages within the virtual environment:

   ```powershell
   pip install <package_name>
   ```

<h5>5. Deactivate the Virtual Environment (when finished):</h5>

- Type:

   ```powershell
   deactivate
   ```

**Additional Notes:**

- **Execution Policy:** If you encounter errors running scripts, set the execution policy to "RemoteSigned" or "Unrestricted":

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

- **Windows Subsystem for Linux (WSL):** If you're using WSL, you'll need to install Python and create virtual environments within the WSL environment.

- **Multiple Virtual Environments:** You can create separate virtual environments for different projects to manage dependencies effectively.

- **Virtual Environment Management Tools:** Consider using tools like `virtualenvwrapper` or `pipenv` for advanced virtual environment management.
