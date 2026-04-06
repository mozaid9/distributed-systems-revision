import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="iam">
<h2 class="section-title">3. IAM: OAuth, OIDC, JWT &amp; SSO <span class="priority p-critical">CRITICAL — flow question risk</span></h2>
<p>Identity questions often look harder than they really are because the words sound similar. The exam becomes much easier once you separate <strong>who the user is</strong>, <strong>what they can access</strong>, and <strong>which token carries the result</strong>.</p>

<h3>3.1 Quick term map</h3>
<table>
  <tr><th>Term</th><th>Plain-English meaning</th><th>Exam note</th></tr>
  <tr><td>Authentication</td><td>Proving who the user is</td><td>Think login</td></tr>
  <tr><td>Authorisation</td><td>Deciding what the user may do</td><td>Think access rights</td></tr>
  <tr><td>SSO</td><td>One login used across several systems</td><td>User convenience + central control</td></tr>
  <tr><td>OAuth2</td><td>Delegated authorisation</td><td>Mainly about access delegation</td></tr>
  <tr><td>OIDC</td><td>Identity layer on top of OAuth2</td><td>OAuth + login identity</td></tr>
  <tr><td>JWT</td><td>A compact token format</td><td>Usually header.payload.signature</td></tr>
</table>

<div class="box warn"><div class="box-title">Most common mark-losing mistake</div>Do <strong>not</strong> say "OAuth is the login standard". OAuth2 is mainly about delegated authorisation. <strong>OpenID Connect</strong> is the layer that adds identity information for authentication-style flows.</div>

<h3>3.2 JWT in one minute</h3>
<p>A JWT (JSON Web Token) usually has <strong>three parts</strong>: <code>header.payload.signature</code>. The payload carries claims such as user ID, audience or expiry. The signature lets the receiver check the token has not been tampered with.</p>
<div class="box tip"><div class="box-title">Keep this distinction clean</div>
<strong>Signed</strong> does not automatically mean <strong>encrypted</strong>. A normal JWT can be readable if you decode it. The important point is that the signature proves integrity.
</div>

<h3>3.3 OIDC Authorisation Code Flow</h3>
<p>This is the flow you are most likely to need in a sequence-diagram style answer.</p>
<ol class="steps">
  <li><strong>User requests a protected page</strong> in the application.</li>
  <li><strong>The application redirects the browser to the Identity Provider (IdP)</strong> with details such as client ID, redirect URI and scope.</li>
  <li><strong>The user logs in at the IdP</strong>. This is where authentication happens.</li>
  <li><strong>The IdP redirects back with an authorisation code</strong>.</li>
  <li><strong>The application backend exchanges the code for tokens</strong> server-to-server.</li>
  <li><strong>The app validates the tokens and creates its own session</strong>.</li>
  <li><strong>The user can now access protected resources</strong>.</li>
</ol>

<div class="box key"><div class="box-title">Token roles</div>
<ul>
  <li><strong>ID token:</strong> identity information about the authenticated user.</li>
  <li><strong>Access token:</strong> used to call protected APIs or resources.</li>
  <li><strong>Refresh token:</strong> used to obtain new tokens without making the user log in again.</li>
</ul>
</div>

<h3>3.4 How it appears in past papers</h3>
<ul>
  <li>2022/23 reassessment asked directly about OAuth, OpenID Connect, JWT and SSO terminology.</li>
  <li>2023/24 asked for JWT structure and an OIDC sequence flow.</li>
  <li>These questions reward <strong>clear role separation</strong>: browser, app server, identity provider, tokens.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — IAM</div>
<ol>
  <li>What is the difference between authentication and authorisation?</li>
  <li>What does SSO give the user?</li>
  <li>Why is OIDC described as a layer on top of OAuth2?</li>
  <li>What are the three parts of a JWT?</li>
  <li>What is the job of the Identity Provider in the flow?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>Authentication proves who the user is. Authorisation decides what they are allowed to access or do.</li>
  <li>It lets the user sign in once and access multiple related systems without repeated logins.</li>
  <li>Because it builds on OAuth2 and adds identity information so login/authentication can be supported.</li>
  <li>Header, payload and signature.</li>
  <li>It authenticates the user and issues the code and tokens the application relies on.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">Exam answer skeleton</div>
<p>If the question says <em>"Explain the OIDC authorisation code flow"</em>, write it as a sequence: <strong>user requests page -> redirect to IdP -> login -> code returned -> backend token exchange -> session created -> protected resource returned</strong>.</p>
</div>
</section>
"""
insert(GUIDE, S)
