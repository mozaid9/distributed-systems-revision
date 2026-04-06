import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="diagrams">
<h2 class="section-title">17. Key Diagrams to Memorise <span class="priority p-high">HIGH — repeated mark source</span></h2>
<p>This module repeatedly rewards simple labelled diagrams. They do not need to be pretty. They do need to be <strong>clear, labelled and referred to in your written explanation</strong>.</p>

<h3>17.1 High-value diagrams</h3>
<ul>
  <li>Client -&gt; API Gateway -&gt; multiple microservices.</li>
  <li>Client -&gt; Load Balancer -&gt; multiple app instances across two availability zones.</li>
  <li>Deployment -&gt; old ReplicaSet and new ReplicaSet -&gt; pods during a rolling update.</li>
  <li>Browser -&gt; Identity Provider -&gt; code -&gt; token exchange -&gt; protected app resource.</li>
  <li>Browser -&gt; certificate/handshake -&gt; session keys -&gt; encrypted traffic.</li>
  <li>Producer -&gt; queue or exchange -&gt; one consumer or many subscribers.</li>
  <li>Primary database -&gt; read replicas -&gt; read traffic spread out.</li>
</ul>

<h3>17.2 Tiny diagram templates</h3>
<pre><code>API Gateway
Client -> Gateway -> Service A
                 -> Service B
                 -> Service C

Load Balancer
Users -> LB -> App 1 (AZ1)
           -> App 2 (AZ2)

Rolling update
Deployment -> Old ReplicaSet -> old pods
           -> New ReplicaSet -> new pods
</code></pre>

<h3>17.3 What labels you must not forget</h3>
<div class="box key"><div class="box-title">Label checklist</div>
<ul>
  <li>Direction arrows</li>
  <li>Role names such as browser, gateway, IdP, queue, load balancer, ReplicaSet</li>
  <li>Where the security or trust check happens</li>
  <li>Where traffic is distributed or where events flow</li>
  <li>Which step is synchronous and which is asynchronous where relevant</li>
</ul>
</div>

<div class="box quiz"><div class="box-title">Quick Quiz — Diagrams</div>
<ol>
  <li>Why can a simple diagram earn marks in this module?</li>
  <li>What is the most common problem with weak exam diagrams?</li>
  <li>What should arrows show?</li>
  <li>Which diagram is especially useful for messaging questions?</li>
  <li>Why should you refer to the diagram in your written answer?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>Because it makes the flow, architecture or sequence clearer and can directly capture labelled process marks.</li>
  <li>They are unlabelled or too vague to explain the actual mechanism.</li>
  <li>The direction of data, control or event flow.</li>
  <li>Producer -> queue/exchange -> consumer/subscriber flow diagrams.</li>
  <li>Because the marks are usually for both the diagram and the explanation tied to it.</li>
</ol>
</details>
</div>
</section>
"""
insert(GUIDE, S)
