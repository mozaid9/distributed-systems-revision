import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="containers">
<h2 class="section-title">11. Containers, Docker &amp; Compose <span class="priority p-high">HIGH — practical deployment topic</span></h2>
<p>Container questions usually reward a simple explanation of <strong>what problem containers solve</strong>, <strong>how they differ from VMs</strong>, and <strong>how persistence/configuration are handled</strong>.</p>

<h3>11.1 VM vs container</h3>
<table>
  <tr><th>Feature</th><th>Virtual machine</th><th>Container</th></tr>
  <tr><td>OS model</td><td>Includes a full guest OS</td><td>Shares host kernel</td></tr>
  <tr><td>Weight</td><td>Heavier</td><td>Lighter</td></tr>
  <tr><td>Startup</td><td>Slower</td><td>Faster</td></tr>
  <tr><td>Isolation</td><td>Stronger full-machine isolation</td><td>Process-level isolation</td></tr>
</table>

<h3>11.2 Image vs container</h3>
<p>A <strong>Docker image</strong> is the packaged blueprint. A <strong>container</strong> is a running instance created from that image.</p>
<div class="box key"><div class="box-title">Memory line</div>Image = blueprint. Container = running instance.</div>

<h3>11.3 Docker Compose, volumes and env vars</h3>
<ul>
  <li><strong>Compose</strong> declaratively defines a multi-container setup.</li>
  <li><strong>Named volumes</strong> persist data outside the container's short-lived writable layer.</li>
  <li><strong>Environment variables</strong> keep configuration such as ports, hostnames and secrets out of hard-coded source files.</li>
</ul>

<div class="box warn"><div class="box-title">Important beginner point</div>If a database writes only inside the container and the container is removed, the data is lost. That is the problem the <strong>named volume</strong> solves.</div>

<h3>11.4 How it appears in past papers</h3>
<ul>
  <li>2022/23 main compared VMs and containers.</li>
  <li>2023/24 asked about environment variables in Compose and Kubernetes-style setups.</li>
  <li>2024/25 resit asked directly about Docker named volumes.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Containers</div>
<ol>
  <li>What is the difference between a Docker image and a Docker container?</li>
  <li>Why can containers start faster than virtual machines?</li>
  <li>What problem does a named volume solve for a database?</li>
  <li>What is one benefit of environment variables?</li>
  <li>What is the difference between a type 1 and type 2 hypervisor?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>An image is the packaged blueprint; a container is a running instance created from that image.</li>
  <li>Because they do not need to boot a full guest operating system in the same way a VM does.</li>
  <li>It keeps the database files outside the ephemeral container so the data survives container recreation.</li>
  <li>They let you change configuration without hard-coding values into the source code.</li>
  <li>A type 1 hypervisor runs directly on hardware, while a type 2 hypervisor runs on top of a host operating system.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam tip</div>
<p>If the question asks why a named volume is useful, answer three things clearly: <strong>what problem exists without it</strong>, <strong>how the volume solves that problem</strong>, and <strong>what the consequence is if you do not use one</strong>.</p>
</div>
</section>
"""
insert(GUIDE, S)
