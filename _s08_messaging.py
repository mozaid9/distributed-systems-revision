import sys; sys.path.insert(0,'.')
from _section_writer import insert, GUIDE

S = r"""
<section id="messaging">
<h2 class="section-title">8. Messaging: Queues, Pub-Sub &amp; Events <span class="priority p-critical">CRITICAL — appears in every paper set</span></h2>
<p>Messaging is one of the most repeated exam themes. The safest way to remember it is to separate <strong>ask-and-wait</strong>, <strong>hand-off work</strong>, and <strong>announce something happened</strong>.</p>

<h3>8.1 Quick mental map</h3>
<table>
  <tr><th>Pattern</th><th>Simple meaning</th><th>Typical strength</th><th>Typical weakness</th></tr>
  <tr><td>HTTP</td><td>Ask now and wait for a reply</td><td>Simple and immediate</td><td>Tighter coupling</td></tr>
  <tr><td>Message queue</td><td>Hand off work and continue</td><td>Resilience and buffering</td><td>No immediate result</td></tr>
  <tr><td>Pub-sub</td><td>One message or event sent to many interested consumers</td><td>Extensibility</td><td>Harder tracing and consistency</td></tr>
  <tr><td>Event-driven</td><td>Services react to facts that something happened</td><td>Loose coupling</td><td>Eventual consistency complexity</td></tr>
</table>

<div class="box key"><div class="box-title">One-line memory aid</div>
HTTP = ask and wait.<br>
Queue = hand off and continue.<br>
Pub-sub = tell many listeners.<br>
Event = a fact that happened, not a command.
</div>

<h3>8.2 Queue vs pub-sub</h3>
<p>In a <strong>shared queue</strong>, one message is typically processed by one consumer. In <strong>publisher-subscriber</strong>, multiple subscribers can each receive the same event or message and react independently.</p>

<h3>8.3 Thick and thin events</h3>
<ul>
  <li><strong>Thin event:</strong> carries minimal data, often just an ID and timestamp. Consumers usually make another API call for the full state.</li>
  <li><strong>Thick event:</strong> carries useful state data with it, so consumers may not need a follow-up call.</li>
</ul>
<div class="box warn"><div class="box-title">Trade-off</div>Thin events reduce payload size but often increase follow-up API traffic. Thick events reduce follow-up calls but can duplicate more data and need careful schema design.</div>

<h3>8.4 Event Notification vs Event Carried State Transfer (ECST)</h3>
<table>
  <tr><th>Pattern</th><th>What the event carries</th><th>What consumers usually do next</th></tr>
  <tr><td>Event Notification</td><td>Minimal information such as ID and timestamp</td><td>Call another service or API to fetch the full data</td></tr>
  <tr><td>Event Carried State Transfer (ECST)</td><td>The changed state itself</td><td>Update local data directly from the event</td></tr>
</table>
<div class="box key"><div class="box-title">Simple way to remember it</div>
Event Notification says <strong>"something happened"</strong>.<br>
ECST says <strong>"something happened and here is the new state"</strong>.
</div>
<p>ECST is closely tied to <strong>thick events</strong>. Event Notification is closely tied to <strong>thin events</strong>.</p>

<h3>8.5 RabbitMQ vs Kafka at a simple level</h3>
<table>
  <tr><th>Technology</th><th>Best thought of as</th><th>Good for</th></tr>
  <tr><td>RabbitMQ</td><td>Message broker with queues and exchanges</td><td>Reliable message delivery patterns</td></tr>
  <tr><td>Kafka</td><td>Persistent event streaming platform</td><td>Replayable event streams and high-volume streaming</td></tr>
</table>

<h3>8.6 How it appears in past papers</h3>
<ul>
  <li>2022/23 main compared shared queue and pub-sub and also asked about event-driven data sharing.</li>
  <li>2023/24 asked for a redraw from message-based to event-driven architecture.</li>
  <li>2024/25 main asked for advantage, disadvantage and use-case for HTTP, queue and event messaging.</li>
  <li>Refer/defer asked about thick vs thin events and synchronous vs asynchronous approaches.</li>
  <li>The lecturer's revision strategy explicitly highlights Event Notification and ECST as new-year priorities.</li>
</ul>

<div class="box quiz"><div class="box-title">Quick Quiz — Messaging</div>
<ol>
  <li>Why is HTTP usually described as synchronous between services?</li>
  <li>What advantage does a message queue bring when the consumer is slow or temporarily unavailable?</li>
  <li>How is pub-sub different from a single shared queue?</li>
  <li>What is the difference between Event Notification and ECST?</li>
  <li>Why can event-driven designs lead to eventual consistency?</li>
</ol>
<details><summary style="cursor:pointer;color:#854d0e;font-weight:600;margin-top:.5rem">Show Answers</summary>
<ol style="margin-top:.5rem">
  <li>Because the caller normally waits for the response before that interaction can finish.</li>
  <li>It can buffer the work so the producer does not have to wait for the consumer to be ready immediately.</li>
  <li>In pub-sub, multiple subscribers can each receive the same message or event; in a shared queue, one message usually goes to one consumer.</li>
  <li>Event Notification carries minimal data and usually needs a follow-up read; ECST carries the changed state so consumers can update directly.</li>
  <li>Because services update asynchronously, so different copies of data may be briefly out of sync before they catch up.</li>
</ol>
</details>
</div>

<div class="box model"><div class="box-title">High-mark answer shape</div>
<p>For pattern-choice questions, always tie the answer to <strong>immediacy, coupling, resilience, number of consumers, and consistency</strong>. For Event Notification vs ECST, explicitly say whether consumers need a follow-up API call.</p>
</div>
</section>
"""
insert(GUIDE, S)
