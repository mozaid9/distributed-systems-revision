import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="code-reading">
<h2 class="section-title">16. Code-Reading Practice <span class="priority p-med">MEDIUM — useful exam skill</span></h2>
<p>Some papers give code or config and ask what it does. The fastest way to improve here is to stop reading character-by-character and instead identify the <strong>role</strong> of each block.</p>

<h3>16.1 A four-step method</h3>
<ol class="steps">
  <li><strong>Identify the language or file type</strong>: Express JS, Dockerfile, compose YAML, Terraform, Kubernetes YAML.</li>
  <li><strong>Find the high-level purpose</strong>: routing, deployment, networking, persistence, token handling.</li>
  <li><strong>Look for the key nouns</strong>: route, middleware, image, volume, Deployment, ReplicaSet, provider, resource.</li>
  <li><strong>Translate the block into plain English</strong> before writing your answer.</li>
</ol>

<h3>16.2 What to look for in common file types</h3>
<table>
  <tr><th>File type</th><th>What to look for first</th></tr>
  <tr><td>Express code</td><td>Route method, path, middleware order, response codes</td></tr>
  <tr><td>Dockerfile</td><td>Base image, copied files, exposed port, startup command</td></tr>
  <tr><td>Compose YAML</td><td>Services, ports, environment variables, volumes, networks</td></tr>
  <tr><td>Kubernetes YAML</td><td>Kind, replicas, image, service type, selectors</td></tr>
  <tr><td>Terraform</td><td>Provider, resource blocks, variables, provisioners, null_resource</td></tr>
</table>

<h3>16.3 How to write the answer</h3>
<div class="box key"><div class="box-title">Useful exam wording</div>
<ul>
  <li>"This block defines..."</li>
  <li>"The purpose of this line is..."</li>
  <li>"This would cause the application to..."</li>
  <li>"In the wider architecture, this allows..."</li>
</ul>
</div>

<div class="box warn"><div class="box-title">Common mistake</div>Students often describe syntax but never explain the operational meaning. Marks are usually for <strong>purpose</strong>, not for reading symbols aloud.</div>

<div class="box quiz"><div class="box-title">Quick Quiz — Code Reading</div>
<ol>
  <li>What should you identify before reading individual lines in detail?</li>
  <li>What is usually the first thing to find in an Express snippet?</li>
  <li>What does a volume line in Compose usually suggest?</li>
  <li>Why are selectors important in Kubernetes YAML?</li>
  <li>What do examiners normally want more than raw syntax description?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>The file type and the high-level purpose of the code or config.</li>
  <li>The route method/path and any middleware involved.</li>
  <li>That persistence or host-folder mapping is being configured.</li>
  <li>They connect services or controllers to the correct set of pods.</li>
  <li>The practical purpose and effect of the code or config.</li>
</ol>
</details>
</div>
</section>
"""
insert(GUIDE, S)
