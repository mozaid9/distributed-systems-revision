import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="architecture">
<h2 class="section-title">4. Monolith vs Microservices <span class="priority p-critical">CRITICAL — appears constantly</span></h2>
<p>This is one of the safest revision topics because it comes up again and again. The exam rarely wants "microservices are better". It usually wants a <strong>balanced trade-off answer</strong> with technical and business reasoning.</p>

<h3>4.1 The two shapes in simple terms</h3>
<table>
  <tr><th>Architecture</th><th>Simple meaning</th><th>Main strength</th><th>Main weakness</th></tr>
  <tr><td>Monolith</td><td>One main application deployed as one unit</td><td>Simplicity</td><td>Harder to scale and change independently</td></tr>
  <tr><td>Microservices</td><td>Many smaller services cooperating over a network</td><td>Agility and independent scaling</td><td>Extra operational and communication complexity</td></tr>
</table>

<h3>4.2 What "loose coupling" means</h3>
<p><strong>Loose coupling</strong> means one service depends as little as possible on the internal details of another. If the payments service changes its internal code, the orders service should not break as long as the agreed interface stays stable.</p>
<div class="box tip"><div class="box-title">Easy memory line</div>Loose coupling = <strong>"I know how to call you, not how you work inside."</strong></div>

<h3>4.3 Why businesses move towards microservices</h3>
<ul>
  <li>Different teams can work and deploy independently.</li>
  <li>Busy services can scale without scaling the whole system.</li>
  <li>One failing service does not always bring down everything else.</li>
  <li>Different parts of the system can evolve at different speeds.</li>
</ul>

<h3>4.4 Functional vs non-functional requirements</h3>
<p><strong>Functional requirements</strong> describe <strong>what the system must do</strong>. <strong>Non-functional requirements</strong> describe <strong>how well it must do it</strong>.</p>
<table>
  <tr><th>Requirement type</th><th>Simple meaning</th><th>Examples</th></tr>
  <tr><td>Functional</td><td>Features or behaviours the system must provide</td><td>User can log in, customer can place an order</td></tr>
  <tr><td>Non-functional</td><td>Quality conditions or constraints on the system</td><td>Fast response time, high availability, strong security</td></tr>
</table>
<div class="box tip"><div class="box-title">Fast memory line</div>Functional = <strong>what it does</strong>. Non-functional = <strong>how well it does it</strong>.</div>

<h3>4.5 Why monoliths still matter</h3>
<div class="box key"><div class="box-title">Do not throw monoliths away too quickly</div>
For a small, stable system a monolith can be the smarter choice because it is simpler to build, test, deploy and debug. A strong answer says <strong>when the monolith is sensible</strong>, not just when microservices are attractive.
</div>

<h3>4.6 3-tier architecture</h3>
<p>A basic <strong>3-tier architecture</strong> separates the system into three main layers:</p>
<ol>
  <li><strong>Presentation tier</strong> — the web UI or client.</li>
  <li><strong>Application tier</strong> — the business logic / API.</li>
  <li><strong>Data tier</strong> — the database.</li>
</ol>
<pre><code>Browser / UI
     |
App / API / server logic
     |
Database
</code></pre>
<p>This is not exactly the same thing as microservices, but it is still a very useful architecture pattern and it appears in the current slide deck. It is especially useful when explaining separation of concerns and network placement such as web/app/database subnets.</p>

<h3>4.7 API Gateway in this topic</h3>
<p>An <strong>API gateway</strong> is a single front door in front of several backend services. It can route requests, centralise authentication, apply rate limiting and sometimes combine results from multiple services into one response.</p>
<div class="box warn"><div class="box-title">Trade-off</div>The gateway itself becomes important infrastructure, so it must be scalable and resilient. Otherwise it becomes a bottleneck or single point of failure.</div>
<div class="box model"><div class="box-title">5-mark API gateway answer shape</div>
<p>State that it is a single entry point, then give 2-3 benefits such as routing, centralised security, rate limiting or response aggregation, and finish with one trade-off such as bottleneck or single point of failure risk.</p>
</div>

<h3>4.8 How it appears in past papers</h3>
<ul>
  <li>2022/23 reassessment compared monolith and microservice approaches.</li>
  <li>2023/24 asked for properties of a microservice and a composite microservice.</li>
  <li>2024/25 resit asked for business benefits of a distributed microservice architecture.</li>
  <li>2024/25 resit also asked directly about functional vs non-functional requirements.</li>
  <li>API gateway reasoning appears repeatedly as a design justification question.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Architecture</div>
<ol>
  <li>What makes a distributed system still feel like one system to the user?</li>
  <li>What is the biggest operational advantage of a monolith for a small stable system?</li>
  <li>Why can microservices scale more cheaply in some cases?</li>
  <li>What does loose coupling mean in simple terms?</li>
  <li>What is one risk of splitting a system into many services?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>Because the separate services cooperate behind the scenes and present one overall user experience.</li>
  <li>It is usually simpler to build, deploy, test and debug because everything is in one main application.</li>
  <li>Because you can often scale only the busy service instead of scaling the whole application.</li>
  <li>It means one service depends as little as possible on the internal details of another service.</li>
  <li>More complexity, including network latency, harder tracing and data consistency issues.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">High-mark structure for compare questions</div>
<p>Use the same headings for both sides: <strong>deployment, scaling, team independence, resilience, data consistency, operational complexity</strong>. End with a judgement about which is better for the scenario given.</p>
</div>
</section>
"""
insert(GUIDE, S)
