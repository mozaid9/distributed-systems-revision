import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="rapid">
<h2 class="section-title">19. Rapid-Fire Review <span class="priority p-critical">CRITICAL — final pass section</span></h2>
<p>Use this section in the last few days and again the day before the exam. It is for <strong>fast recall</strong>, not first-time learning.</p>

<h3>19.1 Highest-value topics</h3>
<ul>
  <li>TLS, certificates, digital signatures and HTTPS process questions.</li>
  <li>Messaging patterns: synchronous vs asynchronous, queues, pub-sub and event-driven flow.</li>
  <li>Monolith vs microservices, including trade-offs and API gateway reasoning.</li>
  <li>API design, Express middleware, CORS and OpenAPI documentation.</li>
  <li>Cloud models, resilience, load balancing and availability zones.</li>
  <li>Containers, named volumes, environment variables, Kubernetes objects and rolling updates.</li>
  <li>Identity and access: authentication, authorisation, OAuth, OIDC, JWT and SSO.</li>
</ul>

<h3>19.2 Quick-fire definitions</h3>
<table>
  <tr><th>Term</th><th>Fast definition</th></tr>
  <tr><td>Loose coupling</td><td>Minimal dependence on another component's internal details.</td></tr>
  <tr><td>Middleware</td><td>Code that runs between receiving a request and sending a response.</td></tr>
  <tr><td>CORS</td><td>Browser rule controlling whether one origin may call another.</td></tr>
  <tr><td>Named volume</td><td>Docker-managed persistent storage mounted into a container.</td></tr>
  <tr><td>Digital certificate</td><td>Signed document binding a public key to an identity.</td></tr>
  <tr><td>JWT</td><td>Compact token commonly structured as header.payload.signature.</td></tr>
  <tr><td>Read replica</td><td>Read-only copy used to spread read traffic away from the primary DB.</td></tr>
  <tr><td>SAGA</td><td>Distributed transaction pattern using local steps plus compensation.</td></tr>
</table>

<h3>19.3 Common compare pairs</h3>
<table>
  <tr><th>Pair</th><th>Core contrast</th></tr>
  <tr><td>Monolith vs microservices</td><td>Simplicity vs agility and independent scaling</td></tr>
  <tr><td>HTTP vs HTTPS</td><td>Plain transport vs transport protected by TLS</td></tr>
  <tr><td>Queue vs pub-sub</td><td>One consumer vs many subscribers</td></tr>
  <tr><td>VM vs container</td><td>Full OS isolation vs lighter shared-kernel isolation</td></tr>
  <tr><td>IaaS vs PaaS</td><td>More control/responsibility vs less platform work</td></tr>
  <tr><td>Thick vs thin event</td><td>Carry state vs carry minimal notification data</td></tr>
  <tr><td>NodePort vs ClusterIP vs LoadBalancer</td><td>Node exposure vs internal only vs cloud-integrated exposure</td></tr>
</table>

<h3>19.4 Sequences to memorise</h3>
<ul>
  <li><strong>TLS:</strong> ClientHello -> ServerHello + certificate -> certificate validation -> key agreement -> session keys -> encrypted traffic.</li>
  <li><strong>Digital signature verification:</strong> hash message -> sign with private key -> verify with public key -> compare digests.</li>
  <li><strong>OIDC flow:</strong> protected page -> redirect to IdP -> login -> code returned -> token exchange -> session created.</li>
  <li><strong>Kubernetes rolling update:</strong> new ReplicaSet up -> new pods healthy -> traffic shifts -> old ReplicaSet down.</li>
  <li><strong>Event-carried state transfer:</strong> source data change -> publish event with state -> subscribers update local copies -> eventual consistency.</li>
</ul>

<div class="box tip"><div class="box-title">How to use this section</div>Cover one column or one bullet line, try to say it from memory, then uncover and check yourself. This is much more effective than just staring at the page.</div>
</section>
"""
insert(GUIDE, S)
