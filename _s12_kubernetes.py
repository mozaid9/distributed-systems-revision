import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="kubernetes">
<h2 class="section-title">12. Kubernetes &amp; Rolling Updates <span class="priority p-high">HIGH — current-syllabus favourite</span></h2>
<p>Kubernetes questions are easier once you remember the object hierarchy. Most lost marks come from mixing up <strong>pod</strong>, <strong>ReplicaSet</strong>, <strong>Deployment</strong> and <strong>Service</strong>.</p>

<h3>12.1 The hierarchy you must remember</h3>
<div class="box key"><div class="box-title">Core chain</div>
<strong>Deployment -&gt; ReplicaSet -&gt; Pods -&gt; Service</strong>
</div>
<table>
  <tr><th>Object</th><th>Main job</th></tr>
  <tr><td>Pod</td><td>Smallest deployable unit that runs one or more containers</td></tr>
  <tr><td>ReplicaSet</td><td>Keeps the required number of identical pod replicas running</td></tr>
  <tr><td>Deployment</td><td>Manages ReplicaSets and handles rolling updates and rollbacks</td></tr>
  <tr><td>Service</td><td>Gives stable network access to the pods</td></tr>
</table>

<h3>12.2 Service types</h3>
<ul>
  <li><strong>ClusterIP</strong>: internal access only inside the cluster.</li>
  <li><strong>NodePort</strong>: exposes the service on a port of each node.</li>
  <li><strong>LoadBalancer</strong>: integrates with cloud load balancing for external access.</li>
</ul>

<h3>12.3 Rolling update process</h3>
<ol class="steps">
  <li><strong>The Deployment sees a new version is required</strong>.</li>
  <li><strong>It creates a new ReplicaSet</strong> for the new version.</li>
  <li><strong>New pods start and must become healthy</strong>.</li>
  <li><strong>Traffic can move to the new healthy pods</strong>.</li>
  <li><strong>The old ReplicaSet is scaled down gradually</strong>.</li>
</ol>

<div class="box tip"><div class="box-title">Why no downtime?</div>Because Kubernetes does <strong>not</strong> delete all old pods first. It brings healthy new pods into service before fully removing the old ones.</div>

<h3>12.4 How it appears in past papers</h3>
<ul>
  <li>2023/24 asked for the function of Kubernetes components and service types.</li>
  <li>2024/25 main asked how rolling updates work using Deployment and ReplicaSet.</li>
  <li>Refer/defer asked what rolling upgrades mean and how they work.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Kubernetes</div>
<ol>
  <li>What is the smallest deployable unit in Kubernetes?</li>
  <li>What does a ReplicaSet do?</li>
  <li>Why is a Deployment needed on top of a ReplicaSet?</li>
  <li>What is the difference between ClusterIP and NodePort?</li>
  <li>Why can rolling updates avoid downtime?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>A pod.</li>
  <li>It keeps the required number of pod replicas running.</li>
  <li>Because a Deployment manages change over time, including rolling updates and rollbacks.</li>
  <li>ClusterIP is internal only; NodePort exposes the service on a port of each node.</li>
  <li>Because healthy new pods are brought into service before the old ones are fully removed.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam answer line to remember</div>
<p><strong>New ReplicaSet up first, old ReplicaSet down later.</strong> That one line anchors most rolling-update explanations.</p>
</div>
</section>
"""
insert(GUIDE, S)
