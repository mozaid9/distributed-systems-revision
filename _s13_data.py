import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="data">
<h2 class="section-title">13. Data Layer, ACID &amp; SAGA <span class="priority p-high">HIGH — common scaling and transaction topic</span></h2>
<p>Database questions often look varied, but they usually fall into three buckets: <strong>keeping data correct</strong>, <strong>scaling reads and writes</strong>, and <strong>handling distributed transactions</strong>.</p>

<h3>13.1 Keeping data correct</h3>
<p><strong>Referential integrity</strong> protects relationships between related records, for example making sure an order still points to a valid customer. Common actions include <strong>cascade</strong>, <strong>restrict</strong> and <strong>set null</strong>.</p>

<h3>13.2 Connection pooling and read replicas</h3>
<ul>
  <li><strong>Connection pool:</strong> a reusable set of ready-made database connections.</li>
  <li><strong>Read replica:</strong> a read-only copy of the primary database used to spread read traffic.</li>
</ul>
<div class="box key"><div class="box-title">Important limitation</div>Read replicas help with <strong>reads</strong>. They do <strong>not</strong> remove the main write bottleneck, and they may briefly return stale data because of replication lag.</div>

<h3>13.3 Sharding and consistent hashing</h3>
<p><strong>Sharding</strong> splits data across nodes. <strong>Consistent hashing</strong> is a strategy that reduces how much data must move when nodes are added or removed.</p>

<h3>13.4 ACID and SAGA</h3>
<table>
  <tr><th>Term</th><th>Meaning</th></tr>
  <tr><td>Atomicity</td><td>All parts succeed together or none count as complete</td></tr>
  <tr><td>Consistency</td><td>Rules and integrity are preserved</td></tr>
  <tr><td>Isolation</td><td>Concurrent transactions should not interfere improperly</td></tr>
  <tr><td>Durability</td><td>Committed data survives failure</td></tr>
</table>
<p>ACID works naturally inside one transactional database. Across multiple microservices and databases, a single all-or-nothing transaction is much harder. A <strong>SAGA</strong> breaks the business process into local steps plus <strong>compensating actions</strong> if something later fails.</p>

<div class="box warn"><div class="box-title">Classic distributed-systems trap</div>Do not assume one normal database transaction can simply stretch across lots of microservices with no extra cost or complexity.</div>

<h3>13.5 How it appears in past papers</h3>
<ul>
  <li>2024/25 main asked about connection pooling and read-replica scaling.</li>
  <li>2022/23 main asked about relational scaling, sharding and consistent hashing.</li>
  <li>2023/24 asked for the SAGA orchestration pattern.</li>
  <li>Refer/defer tested ACID and distributed transaction difficulty.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Data</div>
<ol>
  <li>What does referential integrity protect?</li>
  <li>Why is connection pooling better than opening a fresh connection for every request?</li>
  <li>What does a read replica improve?</li>
  <li>What is the core idea of a SAGA?</li>
  <li>What problem does consistent hashing try to reduce?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>It protects the validity of relationships between related records.</li>
  <li>Because it reuses ready-made connections and reduces the overhead of constant connection setup.</li>
  <li>Read capacity and sometimes read availability.</li>
  <li>It breaks one large business transaction into local steps and uses compensation if a later step fails.</li>
  <li>It reduces how much data must be reassigned when nodes are added or removed.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam-safe summary line</div>
<p>Read replicas help reads, sharding helps distribution, and SAGA helps when one business process spans multiple services and databases.</p>
</div>
</section>
"""
insert(GUIDE, S)
