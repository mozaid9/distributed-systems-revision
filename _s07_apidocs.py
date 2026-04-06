import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="apidocs">
<h2 class="section-title">7. API Documentation &amp; OpenAPI <span class="priority p-med">MEDIUM — easy marks if prepared</span></h2>
<p>Documentation questions are less flashy than security or messaging, but they are reliable marks because the logic is straightforward: <strong>a good API contract is only useful if people can understand and use it correctly</strong>.</p>

<h3>7.1 Why documentation matters</h3>
<ul>
  <li>It stops teams guessing paths, methods and request bodies.</li>
  <li>It reduces integration mistakes and rework.</li>
  <li>It helps frontend, backend and test teams work in parallel.</li>
  <li>It makes onboarding and long-term maintenance easier.</li>
</ul>

<h3>7.2 OpenAPI core structure</h3>
<table>
  <tr><th>Element</th><th>What it describes</th></tr>
  <tr><td>Info</td><td>Basic API details such as title and version</td></tr>
  <tr><td>Servers</td><td>Where the API lives</td></tr>
  <tr><td>Paths</td><td>The endpoints and methods</td></tr>
  <tr><td>Components</td><td>Reusable schemas, parameters and security definitions</td></tr>
  <tr><td>Tags</td><td>Logical grouping of endpoints</td></tr>
</table>

<h3>7.3 Three documentation approaches</h3>
<div class="two-col">
  <div class="box key"><div class="box-title">Design-first</div>Start by modelling the API before implementation. Good when many people need to agree the shape early.</div>
  <div class="box key"><div class="box-title">API-first</div>Start with a formal API contract, often OpenAPI. Good for parallel frontend/backend/test work.</div>
</div>
<div class="box key"><div class="box-title">Code-first</div>Generate or build docs from working code. Often practical for smaller teams where the implementation is moving quickly.</div>

<h3>7.4 Small extra: HATEOAS</h3>
<p>HATEOAS is the idea that the response can include links or hints about what actions are valid next. It is not the most common topic, but it has appeared before.</p>

<h3>7.5 How it appears in past papers</h3>
<ul>
  <li>2022/23 reassessment asked about three documentation approaches using OpenAPI.</li>
  <li>2023/24 refer/defer compared design-first, API-first and code-first.</li>
  <li>2024/25 resit asked why documenting API endpoints matters and what OpenAPI usually contains.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — API Documentation</div>
<ol>
  <li>Why can poor API documentation slow a team down even if the API works?</li>
  <li>What problem does OpenAPI solve?</li>
  <li>When is design-first especially useful?</li>
  <li>What is one advantage of code-first for a small team?</li>
  <li>What is the basic idea of HATEOAS?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>Because people may guess methods, paths or payload shapes and then waste time fixing integration mistakes.</li>
  <li>It gives a standard, clear and machine-readable way to describe the API contract.</li>
  <li>When multiple people or teams need to agree the interface before coding begins.</li>
  <li>The documentation can stay close to the implementation, which can be easier to maintain in a smaller project.</li>
  <li>The API response can help tell the client what valid next actions are available.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">What a strong answer sounds like</div>
<p>Do not just define the three approaches. Say <strong>when</strong> you would use each one and <strong>why</strong> it fits that team or project.</p>
</div>
</section>
"""
insert(GUIDE, S)
