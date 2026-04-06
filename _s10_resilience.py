import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="resilience">
<h2 class="section-title">10. Resilience, Availability Zones &amp; Elastic Compute <span class="priority p-high">HIGH — diagram-friendly topic</span></h2>
<p>This topic is about keeping a system running when demand changes or components fail. The exam often rewards very clear diagrams here.</p>

<h3>10.1 Key distinctions</h3>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td>High availability</td><td>Staying up through expected failures</td></tr>
  <tr><td>Resilience</td><td>Withstanding and recovering from wider failure</td></tr>
  <tr><td>Availability zone (AZ)</td><td>A separate cloud location within a region used for fault tolerance</td></tr>
  <tr><td>Load balancer</td><td>A front component that spreads traffic across healthy instances</td></tr>
  <tr><td>Elastic compute</td><td>Scaling resources up or down with demand</td></tr>
</table>

<h3>10.2 Typical resilient architecture</h3>
<pre><code>Clients
   |
Load Balancer
  / \
AZ1 AZ2
 |   |
App App
</code></pre>
<p>The load balancer gives one front door. Multiple instances sit behind it, ideally across more than one availability zone. If one instance or one zone fails, traffic can continue going elsewhere.</p>

<h3>10.3 Horizontal vs vertical scaling</h3>
<ul>
  <li><strong>Horizontal scaling</strong> = add more instances.</li>
  <li><strong>Vertical scaling</strong> = make one machine bigger.</li>
</ul>
<div class="box tip"><div class="box-title">Exam preference</div>Distributed-systems questions usually favour <strong>horizontal</strong> scaling because it fits resilience and elasticity better.</div>

<h3>10.4 How it appears in past papers</h3>
<ul>
  <li>2024/25 resit asked directly about the purpose and operation of a load balancer in elastic-compute solutions.</li>
  <li>Refer/defer asked for benefits of availability zones for resilience.</li>
  <li>Older cloud design questions also rewarded highly available, elastically scalable diagrams.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Resilience</div>
<ol>
  <li>What is the difference between high availability and resilience?</li>
  <li>Why can a load balancer improve both performance and resilience?</li>
  <li>What does an availability zone help protect you against?</li>
  <li>What is horizontal scaling?</li>
  <li>Why is elastic compute valuable to a business as well as technically useful?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>High availability focuses on staying up during expected failures, while resilience is broader and includes recovery from wider disruption.</li>
  <li>Because it spreads traffic across healthy instances and can stop sending traffic to failed or overloaded ones.</li>
  <li>Failure of a single site or data-centre location within a region.</li>
  <li>Adding more instances or machines instead of making one existing machine bigger.</li>
  <li>Because it helps the system meet demand while avoiding paying for too much idle capacity when demand is low.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">What examiners want in diagram answers</div>
<p>Show <strong>one front door</strong>, <strong>multiple backend instances</strong>, and ideally <strong>more than one availability zone</strong>. Then explain both normal traffic flow and what happens during failure.</p>
</div>
</section>
"""
insert(GUIDE, S)
