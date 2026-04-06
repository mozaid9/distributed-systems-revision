import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="express">
<h2 class="section-title">6. Express, Middleware &amp; CORS <span class="priority p-high">HIGH — practical explanation marks</span></h2>
<p>These questions are usually about <strong>flow</strong>. If you can explain what happens to a request in the right order, you are in a strong position.</p>

<h3>6.1 Express request flow</h3>
<ol class="steps">
  <li><strong>A request arrives</strong> with a method, path, headers and maybe a body.</li>
  <li><strong>Middleware runs in registration order</strong>.</li>
  <li><strong>Each middleware either ends the response or calls <code>next()</code></strong>.</li>
  <li><strong>The matching route handler runs</strong>.</li>
  <li><strong>The server sends a response</strong> with a status code and optional body.</li>
</ol>

<h3>6.2 What middleware is for</h3>
<ul>
  <li>Logging requests</li>
  <li>Checking authentication</li>
  <li>Validating input</li>
  <li>Parsing JSON</li>
  <li>Applying CORS policy</li>
</ul>

<pre><code>app.use((req, res, next) =&gt; {
  console.log(req.method, req.path);
  next();
});</code></pre>

<div class="box key"><div class="box-title">Memory line</div>Middleware = <strong>code that runs before the final endpoint response is sent</strong>.</div>

<h3>6.3 Response codes you should know</h3>
<table>
  <tr><th>Code</th><th>Meaning</th><th>Typical use</th></tr>
  <tr><td>200</td><td>OK</td><td>Successful GET or update</td></tr>
  <tr><td>201</td><td>Created</td><td>Successful POST that created a resource</td></tr>
  <tr><td>400</td><td>Bad Request</td><td>Invalid input from client</td></tr>
  <tr><td>401</td><td>Unauthorised</td><td>Missing or invalid authentication</td></tr>
  <tr><td>404</td><td>Not Found</td><td>Route or resource does not exist</td></tr>
  <tr><td>500</td><td>Internal Server Error</td><td>Unexpected server-side failure</td></tr>
</table>

<h3>6.4 Same-origin policy and CORS</h3>
<p>An <strong>origin</strong> is <strong>scheme + domain + port</strong>. Browsers block some cross-origin requests by default. <strong>CORS</strong> is the rule system that lets the server say which origins, methods or headers are allowed.</p>
<div class="box warn"><div class="box-title">Important distinction</div>CORS is mainly a <strong>browser</strong> rule. It is not the same as normal server-to-server authorisation.</div>

<h3>6.5 How it appears in past papers</h3>
<ul>
  <li>2023/24 asked for the concept and operation of Express middleware.</li>
  <li>2024/25 main asked how Express handles requests so the right endpoint runs.</li>
  <li>2022/23 main and refer/defer papers tested CORS directly.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Express &amp; CORS</div>
<ol>
  <li>What does <code>next()</code> do in Express middleware?</li>
  <li>Why does middleware order matter?</li>
  <li>Give one situation where a server should return 404.</li>
  <li>What is an origin in web security terms?</li>
  <li>Why does the browser block some cross-origin requests by default?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>It passes control to the next middleware function or route handler.</li>
  <li>Because earlier middleware can change the request, block it, or end the response before later code runs.</li>
  <li>When the requested route or resource does not exist.</li>
  <li>The scheme, domain and port taken together.</li>
  <li>To stop web pages reading or sending data across origins without the server's permission.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam answer skeleton</div>
<p>If the question mentions Express, explain the <strong>ordered request flow</strong>. If it mentions CORS, define <strong>origin</strong> and explain that the <strong>browser checks the server's policy</strong> before allowing the request.</p>
</div>
</section>
"""
insert(GUIDE, S)
