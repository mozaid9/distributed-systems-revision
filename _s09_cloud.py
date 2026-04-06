import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="cloud">
<h2 class="section-title">9. Cloud: IaaS, PaaS, SaaS &amp; Shared Responsibility <span class="priority p-high">HIGH — common explain/compare topic</span></h2>
<p>Cloud questions are usually really about <strong>who manages what</strong>, <strong>how much control you keep</strong>, and <strong>why a business would choose one model over another</strong>.</p>

<h3>9.1 Service models</h3>
<table>
  <tr><th>Model</th><th>What you get</th><th>Who manages more?</th></tr>
  <tr><td>IaaS</td><td>Infrastructure such as VMs, storage and networking</td><td>You manage more</td></tr>
  <tr><td>PaaS</td><td>A managed platform to deploy your application</td><td>Provider manages more of the platform</td></tr>
  <tr><td>SaaS</td><td>The finished software as a service</td><td>Provider manages almost everything</td></tr>
  <tr><td>DBaaS</td><td>A managed database service</td><td>Provider manages the database platform</td></tr>
</table>

<h3>9.2 Shared responsibility in plain English</h3>
<p><strong>Shared responsibility</strong> means the cloud provider does not do everything. The split changes depending on the service model. In IaaS you still manage much more. In PaaS you hand over more platform responsibility. In SaaS you mostly just use the software.</p>

<div class="box key"><div class="box-title">Business value</div>
<ul>
  <li>Lower up-front cost than buying lots of hardware.</li>
  <li>Faster delivery of new environments.</li>
  <li>Easier scaling and global reach.</li>
  <li>Less day-to-day infrastructure work in more managed models.</li>
</ul>
</div>

<h3>9.3 When to choose which</h3>
<ul>
  <li><strong>IaaS:</strong> choose it when you need detailed OS, network or runtime control.</li>
  <li><strong>PaaS:</strong> choose it when you mainly want to deploy the app and let the provider handle more of the platform.</li>
  <li><strong>DBaaS:</strong> choose it when you need database capability without running and patching DB servers yourself.</li>
</ul>

<h3>9.4 How it appears in past papers</h3>
<ul>
  <li>2022/23 main asked about shared responsibility across cloud models.</li>
  <li>2022/23 reassessment tested IaaS, PaaS, SaaS and DBaaS with use-cases.</li>
  <li>2024/25 resit asked for IaaS vs PaaS and cloud business benefits.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Cloud Models</div>
<ol>
  <li>What is the main difference between IaaS and PaaS?</li>
  <li>Why can the cloud reduce capital expenditure?</li>
  <li>What does shared responsibility mean?</li>
  <li>Give one good use-case for DBaaS.</li>
  <li>Why might a business choose PaaS over IaaS?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>With IaaS the customer manages more of the system, while with PaaS the provider manages more of the platform.</li>
  <li>Because the business rents infrastructure or services instead of buying and maintaining lots of hardware up front.</li>
  <li>It means the provider and customer split duties for security, maintenance and management depending on the service model.</li>
  <li>A web app that needs a database but the team does not want to run and patch database servers itself.</li>
  <li>Because it reduces operational work and lets the team focus more on building the application.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam-safe conclusion</div>
<p>The more managed the service, the less you manage yourself. High-mark answers always connect that trade-off to a realistic use-case.</p>
</div>
</section>
"""
insert(GUIDE, S)
