Download git:
Windows:
https://github.com/git-for-windows/git/releases/download/v2.37.3.windows.1/Git-2.37.3-64-bit.exe

Try "git --version" in your terminal.  If it says that it is not recognized then go here to see how to fix it:
https://stackoverflow.com/questions/4492979/git-is-not-recognized-as-an-internal-or-external-command

Modifying PATH on Windows 10:

In the Start Menu or taskbar search, search for "environment variable".
Select "Edit the system environment variables".
Click the "Environment Variables" button at the bottom.
Double-click the "Path" entry under "System variables".
With the "New" button in the PATH editor, add C:\Program Files\Git\bin\ and C:\Program Files\Git\cmd\ to the end of the list.
Close and re-open your console.

Open terminal window and type "git init"