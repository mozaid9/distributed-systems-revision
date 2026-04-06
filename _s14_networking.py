import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="networking">
<h2 class="section-title">14. Networking, VNets &amp; CIDR <span class="priority p-med">MEDIUM — older paper but still examinable</span></h2>
<p>This is one of the more technical-looking topics, but the exam usually wants a <strong>sensible network layout</strong> and a <strong>clear explanation of public vs private access</strong>, not deep networking theory.</p>

<h3>14.1 Key terms in plain English</h3>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td>VNet / virtual network</td><td>Your private cloud network space</td></tr>
  <tr><td>Subnet</td><td>A smaller network carved out inside the larger VNet</td></tr>
  <tr><td>CIDR</td><td>The notation such as <code>/16</code> or <code>/24</code> that describes the size of the IP block</td></tr>
  <tr><td>Public subnet</td><td>Used for components that need direct public access</td></tr>
  <tr><td>Private subnet</td><td>Used for components that should not be directly reachable from the public internet</td></tr>
  <tr><td>Bastion host</td><td>A controlled jump box used for admin access into private resources</td></tr>
</table>

<h3>14.2 CIDR intuition</h3>
<p>The <code>/</code> number tells you how much of the address is fixed for the network. A <strong>smaller suffix number</strong> means a <strong>bigger block</strong> of addresses.</p>
<div class="box key"><div class="box-title">Easy memory pattern</div>
<code>/16</code> = big block<br>
<code>/24</code> = smaller block<br>
<code>/28</code> = very small block
</div>

<h3>14.3 Typical secure layout</h3>
<pre><code>Internet
   |
Public subnet: load balancer / bastion / web
   |
Private subnet: app / database
</code></pre>
<p>The public-facing parts sit where outside traffic can reach them. Sensitive components such as databases should normally sit in private subnets.</p>

<h3>14.4 Network peering</h3>
<p><strong>Network peering</strong> links two separate virtual networks so resources in them can communicate privately as if the networks were connected, without sending that traffic over the public internet.</p>
<div class="box key"><div class="box-title">Why use peering?</div>
It is useful when related systems sit in different VNets but still need low-latency private communication, for example an application VNet talking to a shared services VNet.
</div>
<div class="box warn"><div class="box-title">Exam point</div>Peering is about <strong>private network-to-network connectivity</strong>. Do not describe it as if it were just exposing one network publicly to another.</div>

<h3>14.5 How it appears in past papers</h3>
<ul>
  <li>2022/23 reassessment asked for a VNet CIDR block to be divided across availability zones and subnets.</li>
  <li>The same question also wanted a justified architecture including public-user and admin-user access.</li>
  <li>The lecturer's revision strategy explicitly highlights bastion hosts and network peering as new-year topics to know thoroughly.</li>
</ul>

<div class="box tip"><div class="box-title">What the examiner is really checking</div>They want to see that you understand <strong>segmentation</strong>, <strong>limited exposure</strong>, and <strong>why some resources should stay private</strong>.</div>

<div class="box quiz"><div class="box-title">Quick Quiz — Networking</div>
<ol>
  <li>What is a VNet?</li>
  <li>What is the purpose of a subnet?</li>
  <li>What does the CIDR suffix tell you?</li>
  <li>Why should a database usually be in a private subnet?</li>
  <li>What is network peering used for?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>A private virtual network space in the cloud.</li>
  <li>To divide the larger network into smaller sections with different roles or access rules.</li>
  <li>How large the address block is; smaller suffix numbers mean bigger blocks.</li>
  <li>Because it should not be directly exposed to the public internet.</li>
  <li>To let two separate virtual networks communicate privately without using the public internet.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam approach</div>
<p>For CIDR allocation questions, show your logic clearly. For architecture questions, explain <strong>who can reach which subnet and why</strong>. If peering appears, explain why private network-to-network access is useful.</p>
</div>
</section>
"""
insert(GUIDE, S)
