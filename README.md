<h1>Subdomain Lister</h1>

<p>Subdomain Lister is a Python script that lists subdomains of a target domain. It retrieves subdomains by combining them with a target domain and checks their existence using HTTP requests.</p>

<h2>Files</h2>

<p>The project includes the following file:</p>

<ul>
    <li><strong>subdomainlist.txt:</strong> Text file containing a list of common subdomains.</li>
    <li><strong>with_threading.py:</strong> Python script that lists subdomains with threading for improved performance.</li>
</ul>

<h2>Usage</h2>

<ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Create a text file named <code>subdomainlist.txt</code> and populate it with the list of subdomains you want to check.</li>
    <li>Run the <code>with_threading.py</code> script in your terminal:</li>
    <pre><code>python with_threading.py</code></pre>
    <li>Enter the target domain when prompted.</li>
    <li>Wait for the script to finish checking the existence of subdomains. The results will be printed to the console.</li>
</ol>

<h2>Threading Usage</h2>

<p>The <code>with_threading.py</code> script utilizes threading to improve performance when checking the existence of subdomains. Threading allows multiple HTTP requests to be made concurrently, reducing the overall execution time of the script.</p>

<h2>Contributing</h2>

<p>If you would like to contribute, please open an issue or submit a pull request. Your constructive contributions are welcome!</p>
