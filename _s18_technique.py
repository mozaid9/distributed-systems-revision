import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="technique">
<h2 class="section-title">18. Exam Technique <span class="priority p-critical">CRITICAL — converts knowledge into marks</span></h2>
<p>This exam is not just about knowing terms. It is about recognising the <strong>command word</strong>, giving the <strong>right depth for the marks</strong>, and using <strong>structure</strong> so the examiner can award marks quickly.</p>

<h3>18.1 Command words</h3>
<table>
  <tr><th>Command word</th><th>What the examiner wants</th><th>Best structure</th></tr>
  <tr><td>Explain</td><td>Definition + process + why it matters</td><td>Define, then walk through steps in order</td></tr>
  <tr><td>Compare</td><td>Both sides against the same criteria</td><td>Same headings for both, then conclude</td></tr>
  <tr><td>Discuss</td><td>Balanced strengths and weaknesses</td><td>Pros, cons, context, judgement</td></tr>
  <tr><td>Evaluate</td><td>Judge against criteria</td><td>State criteria, weigh evidence, conclude</td></tr>
  <tr><td>Justify</td><td>Choose and defend</td><td>Choice first, then reasons linked to scenario</td></tr>
  <tr><td>Design</td><td>Propose something sensible and explain it</td><td>Show design, label it, justify each part</td></tr>
</table>

<h3>18.2 Mark-depth guide</h3>
<table>
  <tr><th>Marks</th><th>Usually enough</th></tr>
  <tr><td>5</td><td>Definition + 2 or 3 explained points + one small example</td></tr>
  <tr><td>10</td><td>Short but developed explanation, often with a process or one balanced comparison</td></tr>
  <tr><td>15</td><td>Structured answer with several developed points and often a diagram</td></tr>
  <tr><td>25</td><td>Full answer with process, examples, trade-offs and a conclusion</td></tr>
</table>

<h3>18.3 Diagram questions</h3>
<div class="box key"><div class="box-title">Reliable method</div>
<ol>
  <li>Draw the simple labelled diagram early.</li>
  <li>Number the stages if the process has order.</li>
  <li>Use the diagram in your explanation: "At step 3..."</li>
  <li>Do not rely on the diagram alone — explain what it shows.</li>
</ol>
</div>

<h3>18.4 Common ways marks are lost</h3>
<ul>
  <li>Giving a definition only when the question wanted a process.</li>
  <li>Ignoring the use-case in the question.</li>
  <li>Listing only advantages and no trade-offs.</li>
  <li>Mixing up close terms such as authentication/authorisation or queue/pub-sub.</li>
  <li>Writing too much on a low-mark sub-part and running out of time later.</li>
</ul>

<h3>18.5 Before moving on checklist</h3>
<div class="box tip"><div class="box-title">Final 15-second check</div>
<ul>
  <li>Did I answer the exact command word?</li>
  <li>Did I define the key term?</li>
  <li>Did I explain the mechanism or comparison clearly?</li>
  <li>Did I use the scenario in the question?</li>
  <li>Did I include a limitation, trade-off or judgement where needed?</li>
  <li>Would a simple diagram help?</li>
</ul>
</div>

<div class="box quiz"><div class="box-title">Quick Quiz — Exam Technique</div>
<ol>
  <li>What should usually come right after the definition in an "explain" answer?</li>
  <li>What is the biggest weakness of writing two disconnected mini-essays in a compare question?</li>
  <li>What must a good evaluate answer include near the end?</li>
  <li>Why should you draw a diagram early if the question invites one?</li>
  <li>What is one common reason students drop marks even when they know the topic?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>An ordered explanation of the process or mechanism.</li>
  <li>It does not make the comparison explicit under the same criteria.</li>
  <li>A judgement based on stated criteria.</li>
  <li>Because it can earn direct marks and gives your written answer a clear structure.</li>
  <li>They answer a different question from the one actually asked or ignore the scenario.</li>
</ol>
</details>
</div>
</section>
"""
insert(GUIDE, S)
