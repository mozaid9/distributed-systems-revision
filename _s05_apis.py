import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="apis">
<h2 class="section-title">5. APIs: REST, Endpoints &amp; JSON <span class="priority p-high">HIGH — design question potential</span></h2>
<p>API questions are usually very manageable marks if you stay practical. The examiner normally wants a <strong>clean endpoint</strong>, the <strong>right HTTP method</strong>, and a short explanation of why the design makes sense.</p>

<h3>5.1 Core building blocks</h3>
<table>
  <tr><th>Term</th><th>Meaning</th><th>Example</th></tr>
  <tr><td>API</td><td>The rules that let one program talk to another</td><td>A web app calling a backend service</td></tr>
  <tr><td>Endpoint</td><td>A specific method + URL combination</td><td><code>GET /books/42</code></td></tr>
  <tr><td>JSON</td><td>Text format for structured data</td><td><code>{"name":"Ava","age":20}</code></td></tr>
  <tr><td>Path parameter</td><td>Identifies the main resource</td><td><code>/books/42</code></td></tr>
  <tr><td>Query parameter</td><td>Filters or narrows results</td><td><code>?author=Orwell</code></td></tr>
</table>

<h3>5.2 Method choice</h3>
<ul>
  <li><strong>GET</strong> = retrieve data</li>
  <li><strong>POST</strong> = create something new</li>
  <li><strong>PUT</strong> = replace a resource</li>
  <li><strong>PATCH</strong> = partially update a resource</li>
  <li><strong>DELETE</strong> = remove a resource</li>
</ul>

<div class="box key"><div class="box-title">Simple design rule</div>
<strong>Path points to the thing.</strong><br>
<strong>Query qualifies the thing.</strong>
</div>

<h3>5.3 Example endpoint design</h3>
<p>A sensible bookstore endpoint could be:</p>
<pre><code>GET /books/hardback/dystopian?author=George%20Orwell&amp;title=1984&amp;maxPrice=10.99</code></pre>
<p>Here, the path gives the main resource context and the query adds optional filters.</p>

<h3>5.4 JSON quick-practice</h3>
<p>JSON questions are usually easy marks if you stay calm and focus on <strong>keys</strong>, <strong>values</strong>, <strong>objects</strong> and <strong>arrays</strong>.</p>
<pre><code>{
  "age": 25,
  "firstName": "Bob",
  "lastName": "Martin",
  "children": ["Jim", "Jane", "Susan"]
}</code></pre>
<div class="box tip"><div class="box-title">Quick JSON rules</div>
Use double quotes for keys and string values. Use square brackets for a list. Do not put random prose into the structure.
</div>

<h3>5.5 REST and HATEOAS</h3>
<p>A REST-style API normally uses predictable resource-oriented URLs and standard HTTP methods. <strong>HATEOAS</strong> is a stricter idea where responses include links to what the client can do next.</p>
<div class="box tip"><div class="box-title">Exam-safe wording</div>If you mention HATEOAS, keep it simple: <strong>the response helps guide the client to valid next actions</strong>.</div>

<h3>5.6 SQL injection — new-year priority</h3>
<p><strong>SQL injection</strong> happens when unsafe user input is mixed directly into SQL so the input changes the meaning of the query.</p>
<pre><code>Bad idea:
SELECT * FROM users WHERE username = ' " + userInput + " '
</code></pre>
<div class="box warn"><div class="box-title">Why it matters</div>An attacker may read data they should not see, change data, or bypass login checks if the query is built unsafely.</div>
<div class="box key"><div class="box-title">How to prevent it</div>
<ul>
  <li>Use parameterised queries / prepared statements.</li>
  <li>Validate input sensibly.</li>
  <li>Use least-privilege database accounts.</li>
  <li>Do not concatenate raw user input into SQL strings.</li>
</ul>
</div>

<h3>5.7 How it appears in past papers</h3>
<ul>
  <li>2024/25 main asked for endpoint design and example calls.</li>
  <li>2023/24 refer/defer asked for an API URL returning banking transactions.</li>
  <li>2022/23 reassessment included HATEOAS as an examinable extra.</li>
  <li>The lecturer's revision strategy explicitly lists SQL injection as a new-year topic to know thoroughly.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — API Basics</div>
<ol>
  <li>What is the difference between a path parameter and a query parameter?</li>
  <li>Why is JSON so common in web APIs?</li>
  <li>Which HTTP method is most suitable for retrieving data only?</li>
  <li>When might you use PATCH instead of PUT?</li>
  <li>What is the safest main way to prevent SQL injection?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>A path parameter usually identifies the resource itself, while a query parameter usually filters or limits the results.</li>
  <li>Because it is lightweight, text-based, widely supported and easy for systems to read and write.</li>
  <li>GET.</li>
  <li>When you want to update only part of a resource rather than replace the whole thing.</li>
  <li>Use parameterised queries or prepared statements so user input is treated as data, not executable SQL logic.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam answer pattern</div>
<p>For an endpoint design question: <strong>state method -> write endpoint -> explain path vs query split -> give one example call -> mention JSON response</strong>. For a SQL injection question: <strong>define the attack -> explain the risk -> state prevention using parameterised queries</strong>.</p>
</div>
</section>
"""
insert(GUIDE, S)
