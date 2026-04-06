import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="terraform">
<h2 class="section-title">15. Infrastructure as Code: Terraform <span class="priority p-high">HIGH — recent-paper value</span></h2>
<p>Terraform is lower-frequency than TLS or messaging, but it has appeared with high marks in recent papers, so it is worth knowing the <strong>core vocabulary</strong> and the <strong>declarative vs imperative</strong> distinction.</p>

<h3>15.1 Declarative vs imperative</h3>
<table>
  <tr><th>Style</th><th>Main idea</th><th>Simple memory line</th></tr>
  <tr><td>Imperative</td><td>You tell the system the steps to perform</td><td>"How to do it"</td></tr>
  <tr><td>Declarative</td><td>You describe the target state you want</td><td>"What I want"</td></tr>
</table>

<h3>15.2 Terraform building blocks</h3>
<ul>
  <li><strong>Provider:</strong> plugin that talks to the cloud provider API.</li>
  <li><strong>Resource:</strong> block representing something to create or manage.</li>
  <li><strong>Variable:</strong> reusable input value.</li>
  <li><strong>State file:</strong> Terraform's record of what exists.</li>
  <li><strong>Provisioner:</strong> extra action such as copying files or running commands.</li>
  <li><strong>null_resource:</strong> lets you run provisioners without claiming a real infrastructure object exists.</li>
</ul>

<div class="box key"><div class="box-title">Why IaC is valuable</div>
It makes infrastructure <strong>repeatable</strong>, <strong>versionable</strong>, <strong>reviewable</strong> and easier to rebuild than clicking around manually in a portal.
</div>

<h3>15.3 Provisioners in plain English</h3>
<ul>
  <li><strong>file provisioner:</strong> copy a file to a machine.</li>
  <li><strong>remote-exec:</strong> run commands on the remote machine.</li>
  <li><strong>local-exec:</strong> run commands on the local machine.</li>
</ul>

<h3>15.4 How it appears in past papers</h3>
<ul>
  <li>2024/25 main asked why declarative programming is favoured for IaC.</li>
  <li>The same paper asked about <code>null_resource</code>, <code>file</code> and <code>remote-exec</code> provisioners using line references.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Terraform</div>
<ol>
  <li>What is Infrastructure as Code?</li>
  <li>Why is declarative IaC often preferred over imperative scripting?</li>
  <li>What is the job of Terraform's state file?</li>
  <li>What does a file provisioner do?</li>
  <li>Why might a <code>null_resource</code> be useful?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>It is the practice of describing and managing infrastructure using code rather than manual portal clicks.</li>
  <li>Because it is more repeatable and lets the tool handle ordering and dependencies.</li>
  <li>It records what infrastructure exists so Terraform can compare reality with the desired state in code.</li>
  <li>It copies files from the local machine to the target machine.</li>
  <li>Because it lets you run provisioners or trigger logic without pretending that action itself is a real infrastructure resource.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">How to answer line-reference questions</div>
<p>Do not just repeat the syntax. Explain the <strong>purpose</strong> of the block in the wider deployment flow.</p>
</div>
</section>
"""
insert(GUIDE, S)
