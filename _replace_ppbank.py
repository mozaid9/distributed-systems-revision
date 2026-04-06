NEW_SECTION = r"""<section id="past-paper-bank">
<h2 class="section-title">Past Paper Question Bank</h2>
<p>Every question the lecturer recommended for revision is listed below with a <strong>full model answer</strong>. Use the workflow: read the question, set a timer (1 mark = 1 minute), write your answer from memory, then open the dropdown to compare.</p>
<div class="box warn"><div class="box-title">How to use these answers</div>Do NOT read the model answer first. Write your own attempt under timed conditions, then compare. Note every point you missed. The gap list IS your revision target.</div>

<!-- ─── 2022/23 MAIN ─────────────────────────────── -->
<h3>2022/23 Main Paper</h3>

<div class="box key"><div class="box-title">Q2b — Queue vs Pub-Sub (15 marks, ~18 mins)</div>
<p>Compare and contrast the shared message queue pattern with the publisher-subscriber pattern. With a diagram, give a microservice use-case for each and explain why you recommend that pattern.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2b (15 marks)</div>
<p><strong>Shared Message Queue:</strong> In this pattern a producer places a message on a queue and exactly one consumer retrieves and processes it. The message is removed once consumed. This pattern is point-to-point — one producer, one consumer per message.</p>
<p><em>Use-case:</em> An e-commerce order service places a "process payment" message on a queue. A payment microservice picks it up and charges the card. Only one payment service instance should process each payment to avoid double-charging, so the shared queue guarantees single consumption.</p>
<p><em>Why this pattern suits this use-case:</em> The queue buffers orders if the payment service is slow or temporarily down, providing resilience. If the payment service crashes mid-process, the message can be requeued. The order service does not need to wait for payment confirmation — it continues processing other orders asynchronously.</p>
<p><strong>Publisher-Subscriber:</strong> In this pattern a publisher emits a message or event to a topic or exchange. Multiple independent subscribers each receive their own copy and react independently. Adding a new subscriber does not require any change to the publisher.</p>
<p><em>Use-case:</em> When a new user registers, a user service publishes a "UserRegistered" event. Three independent subscribers receive it: an email service sends a welcome email, an analytics service records the registration, and a recommendation service initialises preferences. All three react to the same event.</p>
<p><em>Why this pattern suits this use-case:</em> Different services need to react to the same event without the user service knowing they exist. Pub-sub enables this loose coupling — new subscribers can be added without modifying the publisher. No single consumer owns the event.</p>
<p><strong>Key contrast:</strong> A shared queue routes each message to one consumer for work processing. Pub-sub broadcasts each event to all interested subscribers for independent reaction. Use a queue when only one service should act on each message. Use pub-sub when multiple services need to know that something happened.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q6b — VM vs Container (10 marks, ~12 mins)</div>
<p>With a diagram, explain the structure, benefits and key differences between a VM and a container, with an example of when to use each.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q6b (10 marks)</div>
<pre><code>Virtual Machine             Container
┌──────────────────┐        ┌──────────────────┐
│   Application    │        │   Application    │
│   Guest OS       │        │   Container      │
│   Hypervisor     │        │   Runtime        │
│   Host OS        │        │   Host OS        │
│   Hardware       │        │   Hardware       │
└──────────────────┘        └──────────────────┘</code></pre>
<p><strong>Virtual machine:</strong> A VM runs a complete guest operating system on top of a hypervisor. The hypervisor emulates hardware so multiple guest OSes can share one physical machine. Each VM is fully isolated with its own kernel, memory allocation and virtual hardware.</p>
<p><strong>Container:</strong> A container packages an application and its dependencies but shares the host operating system kernel. The container runtime (e.g. Docker) provides isolation at the process level without a full guest OS. Containers are lighter, start faster and use less memory than VMs.</p>
<p><strong>Key differences:</strong> A VM takes minutes to boot and consumes gigabytes of disk for the OS. A container starts in seconds and is typically megabytes. VM isolation is stronger because the kernel is separate. Container isolation is weaker because all containers share the host kernel — a kernel exploit could affect all containers.</p>
<p><strong>When to use a VM:</strong> Running workloads that require different operating systems (e.g. a Windows application on a Linux host), or when strong security isolation between tenants is required, such as a multi-tenant cloud hosting environment.</p>
<p><strong>When to use a container:</strong> Deploying a microservice that needs to start quickly, scale horizontally and run consistently across dev, test and production environments. Containers excel at packaging applications with their exact dependencies to eliminate "works on my machine" problems.</p>
</div>
</details>

<!-- ─── 2022/23 REASSESSMENT ──────────────────────── -->
<h3 style="margin-top:2rem">2022/23 Reassessment Paper</h3>

<div class="box key"><div class="box-title">Q1a — Monolith vs Microservices (15 marks, ~18 mins)</div>
<p>Compare and contrast a monolithic system with a distributed microservice-based system from technical and business standpoints. Five key points, up to 3 marks each.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1a (15 marks)</div>
<p><strong>1. Deployment (Technical):</strong> A monolith is deployed as a single unit — one build, one deployment. This is simple but means any change, however small, requires redeploying the entire application. Microservices are independently deployable — each service has its own pipeline, so the payments team can release without waiting for the inventory team.</p>
<p><strong>2. Scaling (Technical + Business):</strong> A monolith must be scaled as a whole even if only one function is under load. This is wasteful and expensive. With microservices, only the busy service — say, the product catalogue during a sale — needs extra instances. This reduces cloud spend and is more efficient.</p>
<p><strong>3. Resilience (Technical):</strong> In a monolith, a bug or crash in one module can bring down the entire application. In a microservice architecture, a failing shipping service does not necessarily prevent users from browsing or checking out, depending on how gracefully failures are handled. Services can fail independently.</p>
<p><strong>4. Development team agility (Business):</strong> A monolith can become a coordination bottleneck as it grows — large teams working on one codebase cause merge conflicts and slow releases. Microservices allow small, autonomous teams (two-pizza teams) to own, build and deploy their service without depending on other teams.</p>
<p><strong>5. Operational complexity (Technical + Business):</strong> A monolith is simpler to run — one application, one log file, one deployment. Microservices introduce significant operational overhead: service discovery, distributed tracing, network latency between services, and data consistency across databases. This cost is justified at scale but may not be for a small startup.</p>
<p><strong>Conclusion:</strong> For a small, stable system a monolith is often the right choice due to its simplicity. As the business scales and multiple teams need to work independently, a microservice architecture becomes increasingly attractive despite its complexity.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2a — HATEOAS + Richardson's Maturity Model (13 marks, ~16 mins)</div>
<p>Do all RESTful APIs conform to HATEOAS? Explain HATEOAS, give an example, an advantage, a disadvantage, and relate to Richardson's Maturity Model.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2a (13 marks)</div>
<p><strong>Do all REST APIs conform to HATEOAS? No.</strong> The vast majority of real-world REST APIs do not implement HATEOAS. Most APIs are at Richardson Level 2. HATEOAS (Level 3) is the ideal described in Roy Fielding's original REST dissertation but is rarely implemented because clients rarely use the links and the implementation overhead is significant.</p>
<p><strong>What HATEOAS is:</strong> HATEOAS (Hypermedia As The Engine Of Application State) is a REST constraint where each API response includes links describing what actions are available to the client next. Instead of the client needing to know all possible URLs in advance, the server guides the client through the application state via hyperlinks embedded in responses.</p>
<p><strong>Example:</strong></p>
<pre><code>GET /orders/123 →
{
  "orderId": 123,
  "status": "pending",
  "_links": {
    "self":   { "href": "/orders/123" },
    "cancel": { "href": "/orders/123/cancel", "method": "DELETE" },
    "pay":    { "href": "/orders/123/payment", "method": "POST" }
  }
}</code></pre>
<p>The client now knows exactly what actions are valid for this order without hard-coding those URLs.</p>
<p><strong>Advantage:</strong> Clients are loosely coupled to the server — the server can change URLs or restructure resources and the client follows the links dynamically rather than breaking. This promotes true REST-style evolvability.</p>
<p><strong>Disadvantage:</strong> Significantly more complex to implement and document. Most API clients ignore the links and rely on hard-coded knowledge of the API anyway, making the extra effort rarely worthwhile in practice. Response payloads are also larger.</p>
<p><strong>Richardson's Maturity Model:</strong> Level 0 — one URL, one method (like SOAP). Level 1 — multiple resource URLs. Level 2 — correct HTTP methods used with resource URLs (most real APIs reach this). Level 3 — HATEOAS: responses include hypermedia links for next actions. HATEOAS is therefore the highest maturity level, representing the full vision of REST, but it is widely acknowledged that most APIs stop at Level 2.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2b — Three OpenAPI Documentation Approaches (12 marks, ~14 mins)</div>
<p>Using the OpenAPI standard, describe design-first, API-first and code-first approaches. Justify where each is useful.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2b (12 marks)</div>
<p><strong>1. Design-first:</strong> The API contract is modelled and discussed before any implementation begins. Teams collaborate on the expected structure of requests and responses using tools like Swagger Editor. Once agreed, the contract drives both frontend and backend development in parallel. Recommended when a large team or multiple teams need to agree the API shape before anyone writes code — for example, a new product launch where UI, mobile and backend teams must work simultaneously without blocking each other.</p>
<p><strong>2. API-first:</strong> A formal OpenAPI specification is written and treated as the primary deliverable before implementation. The spec is used to auto-generate server stubs, client SDKs and mock servers so consumers can test against the API before it exists. Recommended when building a public or partner-facing API where external developers need to integrate early, or in a microservices platform where many services consume each other's APIs and stability of the contract is critical.</p>
<p><strong>3. Code-first:</strong> The API is implemented first and documentation is generated automatically from the working code using annotations (e.g. JSDoc + swagger-jsdoc in Node.js, or SpringFox in Java). Recommended for smaller teams that move quickly, prototype projects where the API shape is still evolving, or internal APIs where the development team and consumers are the same people. The risk is that documentation can lag behind actual implementation if not maintained.</p>
<p><strong>Key OpenAPI elements all three produce:</strong> <code>info</code> (title, version), <code>servers</code> (base URLs), <code>paths</code> (endpoints and methods), <code>components</code> (reusable schemas and security definitions), <code>tags</code> (logical grouping).</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q4 — Full HTTPS/TLS with Six Cryptographic Techniques (25 marks, ~30 mins)</div>
<p>With a diagram, explain how HTTPS works from web request to secure session. Show where Symmetric Encryption, Asymmetric Encryption, HMAC, Digital Signature, Digital Certificate and Key Exchange are used.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q4 (25 marks)</div>
<pre><code>Browser                        Server
  │                              │
  │──── TCP SYN ────────────────▶│
  │◀─── TCP SYN-ACK ─────────────│
  │──── TCP ACK ────────────────▶│  [TCP established]
  │                              │
  │──── ClientHello ────────────▶│  TLS version + cipher suites + client random
  │◀─── ServerHello ─────────────│  Chosen cipher + server random
  │◀─── Certificate ─────────────│  [DIGITAL CERTIFICATE + DIGITAL SIGNATURE]
  │     [browser validates]      │
  │──── Key Exchange ───────────▶│  [ASYMMETRIC ENCRYPTION / KEY EXCHANGE]
  │     [both derive session keys]│  [SYMMETRIC ENCRYPTION keys derived]
  │──── ChangeCipherSpec ───────▶│
  │──── Finished (encrypted) ───▶│  [HMAC of handshake]
  │◀─── ChangeCipherSpec ─────────│
  │◀─── Finished (encrypted) ─────│
  │                              │
  │═══ Encrypted HTTPS data ════▶│  [SYMMETRIC ENCRYPTION + HMAC per record]</code></pre>

<p><strong>Step 1 — TCP Handshake:</strong> Before TLS starts, a standard TCP three-way handshake (SYN / SYN-ACK / ACK) establishes the transport connection.</p>
<p><strong>Step 2 — ClientHello:</strong> The browser sends the TLS versions it supports, a list of cipher suites (algorithm combinations) it can use, and a client random — 32 bytes of random data that will contribute to key derivation.</p>
<p><strong>Step 3 — ServerHello + Certificate [DIGITAL CERTIFICATE + DIGITAL SIGNATURE]:</strong> The server selects a cipher suite and TLS version and sends a server random. It then sends its digital certificate, which binds the server's public key to its domain name and is signed by a Certificate Authority using a digital signature. The browser validates the certificate by: checking it has not expired, checking the domain matches, decrypting the CA's digital signature using the CA's public key and comparing the hash to confirm integrity, and walking up the chain of trust to a trusted root CA.</p>
<p><strong>Step 4 — Key Exchange [ASYMMETRIC ENCRYPTION / KEY EXCHANGE]:</strong> Using the cipher suite chosen (typically ECDHE), the browser and server exchange Diffie-Hellman public values. Both independently compute the same pre-master secret without ever sending it across the network. This is the key exchange step. Asymmetric encryption (RSA or ECDH) is used here to protect the key material. In older TLS versions, the browser would encrypt a pre-master secret with the server's public key (asymmetric encryption) and only the server's private key could decrypt it.</p>
<p><strong>Step 5 — Session Key Derivation [SYMMETRIC ENCRYPTION key setup]:</strong> Both sides independently derive a master secret from: pre-master secret + client random + server random. From the master secret, both sides derive four session keys: client_write_encryption_key, server_write_encryption_key, client_write_MAC_key, server_write_MAC_key. The encryption keys are used for symmetric encryption (AES) of all subsequent data in each direction.</p>
<p><strong>Step 6 — ChangeCipherSpec + Finished [HMAC]:</strong> Each side sends a ChangeCipherSpec message signalling the switch to encrypted communication, followed by a Finished message. The Finished message contains an HMAC of the entire handshake transcript, proving that no tampering occurred. The HMAC (Hashed Message Authentication Code) combines hashing with the MAC key to provide both integrity and authentication for every record in the session.</p>
<p><strong>Step 7 — Encrypted HTTPS data [SYMMETRIC ENCRYPTION + HMAC on every record]:</strong> All HTTP data is now encrypted using AES symmetric encryption with the session keys, which is fast. Each record also includes an HMAC using the MAC keys to detect any tampering in transit. Symmetric encryption is used for the bulk of data transfer because it is far faster than asymmetric encryption.</p>
<p><strong>Why symmetric for data and asymmetric for key exchange?</strong> Asymmetric encryption is computationally expensive — it cannot encrypt large volumes of data at speed. It is used only to securely establish the shared secret. Once the secret is agreed, symmetric AES encryption handles all actual data at high throughput.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q6 — 12 IAM Terms (25 marks, ~30 mins)</div>
<p>Define each IAM term and provide the context in which it is used.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q6 (25 marks, 2 marks each)</div>
<p><strong>Authentication (2 marks):</strong> The process of verifying that a user or system is who they claim to be. Used at login — the system checks credentials such as a username and password, biometric, or certificate. Context: a user enters their email and password; the system checks against stored hashed credentials and grants a session if they match.</p>
<p><strong>Multi-Factor Authentication (2 marks):</strong> Requiring two or more independent authentication factors from different categories: something you know (password), something you have (phone/token), something you are (biometric). Context: after entering a password, the user must also enter a one-time code sent to their phone. This reduces risk if one factor is compromised.</p>
<p><strong>Authorisation (2 marks):</strong> Determining what an authenticated user is permitted to do. Authentication says who you are; authorisation says what you can access. Context: a logged-in user with the "viewer" role can read reports but cannot delete records — that is controlled by authorisation rules.</p>
<p><strong>Security Principal (2 marks):</strong> Any entity that can be authenticated and assigned permissions — a user, a service account, a device or an application. Context: in Azure RBAC, a security principal is assigned a role (e.g. "Contributor") which governs what resources it can access.</p>
<p><strong>Single Sign-On (SSO) (2 marks):</strong> An authentication mechanism allowing a user to log in once and gain access to multiple related systems without re-authenticating for each. Context: an employee logs into their corporate portal once and can then access email, HR systems and the project management tool without entering credentials again.</p>
<p><strong>Active Directory (AD) (2 marks):</strong> Microsoft's directory service for managing users, computers and permissions within an organisation. It stores credentials and group memberships centrally. Context: when an employee joins a company, IT creates an AD account. All Windows machines and internal services authenticate against AD.</p>
<p><strong>Active Directory Federated Services (ADFS) (2 marks):</strong> An extension to Active Directory that enables SSO across organisational boundaries by sharing identity claims with external systems using federation protocols. Context: a company uses ADFS to allow employees to log into a partner company's web application using their existing corporate AD credentials without creating a separate account.</p>
<p><strong>SAML (2 marks):</strong> Security Assertion Markup Language — an XML-based standard for exchanging authentication and authorisation data between an Identity Provider and a Service Provider. Used heavily in enterprise SSO. Context: when a user accesses a SaaS application (SP), they are redirected to their corporate IdP; the IdP authenticates them and sends a SAML assertion back to the SP granting access.</p>
<p><strong>OAuth 2.0 and OpenID Connect (3 marks):</strong> OAuth 2.0 is a delegated authorisation framework — it allows a user to grant an application limited access to their resources on another service without sharing credentials (e.g. "allow this app to read my Google Calendar"). OpenID Connect is an identity layer built on top of OAuth 2.0 that adds authentication — it issues an ID token containing the user's identity claims so the application knows who the user is. Context: "Log in with Google" uses OIDC; the application gets an ID token with the user's name and email, plus an access token to call Google APIs.</p>
<p><strong>JWT (2 marks):</strong> JSON Web Token — a compact, URL-safe token structured as three Base64URL-encoded parts: header (algorithm), payload (claims such as user ID, expiry, issuer) and signature (proves integrity and authenticity). Context: after OIDC login, the ID token is a JWT. The application validates the signature using the IdP's public key and reads the payload to get the user's name and email without making another API call.</p>
<p><strong>Identity Provider (IdP) (2 marks):</strong> The system that authenticates users and issues tokens or assertions about their identity. Examples: Google, Microsoft Azure AD, Okta. Context: in OIDC, the IdP handles the login page, verifies credentials and issues the ID token and access token to the application.</p>
<p><strong>Service Provider (SP) (2 marks):</strong> The application or service that relies on the IdP to authenticate users. The SP does not manage credentials itself — it trusts the IdP. Context: in SAML federation, the SaaS application is the SP; it redirects unauthenticated users to the corporate IdP and grants access based on the SAML assertion it receives back.</p>
</div>
</details>

<!-- ─── 2023/24 MAIN ─────────────────────────────── -->
<h3 style="margin-top:2rem">2023/24 Main Paper</h3>

<div class="box key"><div class="box-title">Q1a — Express Middleware (7 marks, ~8 mins)</div>
<p>With the aid of an example, explain the concept and operation of NodeJS Express middleware.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1a (7 marks)</div>
<p>Middleware in Express is a function that has access to the request object, response object and a <code>next</code> function. It sits in the processing pipeline between the server receiving the HTTP request and the final route handler sending the response. Middleware functions are executed in the order they are registered using <code>app.use()</code>.</p>
<p>Each middleware function can: modify the request or response objects, end the request-response cycle by sending a response, or call <code>next()</code> to pass control to the next middleware or route handler. If a middleware does not call <code>next()</code> and does not send a response, the request will hang.</p>
<pre><code>app.use((req, res, next) => {
  console.log(`${req.method} ${req.path} - ${new Date().toISOString()}`);
  next(); // pass to next middleware or route
});

app.use((req, res, next) => {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ error: 'Unauthorised' });
  next(); // token present, continue
});

app.get('/data', (req, res) => {
  res.json({ result: 'ok' });
});</code></pre>
<p>In this example, the first middleware logs every request. The second checks for an authorisation header and returns 401 if missing, preventing the request from reaching the route. The <code>GET /data</code> route only executes if both middleware functions call <code>next()</code>. This demonstrates how middleware creates a reusable, ordered checkpoint system — concerns like logging, authentication and input validation are separated from the route logic itself.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2b — Alice Sends a Secure Signed Message to Bob (7 marks, ~8 mins)</div>
<p>Explain the asymmetric encryption process of Alice securely sending a message to Bob such that only Bob can read it and Bob knows it came from Alice.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2b (7 marks)</div>
<p><strong>Goal:</strong> Confidentiality (only Bob can read it) + Authenticity/Integrity (Bob knows it came from Alice and was not altered).</p>
<p><strong>Step 1 — Alice encrypts the message for confidentiality:</strong> Alice obtains Bob's public key. She encrypts the message using Bob's public key. Only Bob's private key can decrypt this — no one else, including an eavesdropper who intercepts the message, can read the content.</p>
<p><strong>Step 2 — Alice signs the message for authenticity:</strong> Alice hashes the original message (e.g. using SHA-256) to produce a message digest. She encrypts the digest using her own private key — this encrypted digest is her digital signature. She attaches the signature to the encrypted message and sends both.</p>
<p><strong>Step 3 — Bob verifies and decrypts:</strong> Bob decrypts the message using his own private key, recovering the original plaintext. Bob then verifies Alice's signature by decrypting it using Alice's public key, which recovers the original digest. Bob independently hashes the decrypted message. If the two digests match, the signature is valid — the message came from Alice (only she has her private key) and was not modified in transit.</p>
<p><strong>Properties achieved:</strong> Confidentiality — only Bob could decrypt. Authenticity — only Alice could have created the signature. Integrity — any modification to the message would change the hash and fail the comparison. Non-repudiation — Alice cannot later deny sending it, because only her private key could have produced that signature.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3a — Microservice Rationale and Properties (6 marks, ~7 mins)</div>
<p>Explain the rationale and key properties of a microservice.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3a (6 marks)</div>
<p><strong>Rationale:</strong> Microservices address the limitations of monolithic architecture as systems grow. In a monolith, all business functions are packaged together — scaling one function means scaling everything, and a bug anywhere can crash the whole system. Microservices decompose a system by business domain so that each service can be developed, deployed and scaled independently.</p>
<p><strong>Key properties:</strong></p>
<p><em>Single responsibility:</em> Each microservice is focused on one business capability (e.g. payments, orders, notifications). It does one thing well and has a well-defined boundary.</p>
<p><em>Independent deployability:</em> A microservice can be built, tested and deployed without requiring changes to other services, enabling faster release cycles and team autonomy.</p>
<p><em>Owns its own data:</em> Ideally each microservice has its own database. This prevents tight coupling through shared data and allows each service to choose the most appropriate storage technology.</p>
<p><em>Communicates via APIs:</em> Microservices interact with each other through well-defined interfaces — typically HTTP/REST or asynchronous messaging — rather than shared memory or direct database access.</p>
<p><em>Independently scalable:</em> If the product catalogue receives high traffic, only that service needs additional instances — the payment or shipping services are unaffected.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q4 — All 8 Kubernetes Components (25 marks, ~30 mins)</div>
<p>Explain the role of each K8s component: Control Plane, Kubelet, Node, Pod, ReplicaSet, Deployment, ConfigMap, Service (with ClusterIP/NodePort/LoadBalancer).</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q4 (25 marks, ~3 marks each)</div>
<p><strong>Control Plane (3 marks):</strong> The control plane is the management layer of a Kubernetes cluster. It contains the API server (single entry point for all cluster operations), the scheduler (assigns pods to nodes based on resource availability), the controller manager (runs background loops that ensure desired state matches actual state) and etcd (a distributed key-value store that holds all cluster state). The control plane makes global decisions about the cluster but does not run application workloads itself.</p>
<p><strong>Kubelet (3 marks):</strong> The Kubelet is an agent that runs on every worker node. It watches for pod specifications assigned to its node by the scheduler and is responsible for ensuring those containers are running and healthy. It communicates with the container runtime to start, stop and restart containers, and reports node and pod status back to the control plane's API server.</p>
<p><strong>Node (3 marks):</strong> A node is a physical or virtual machine in the cluster where pod workloads actually run. Each node runs a Kubelet, a container runtime (e.g. containerd) and a network proxy (kube-proxy). A cluster has multiple nodes to provide capacity and fault tolerance — if one node fails, the scheduler can reschedule its pods onto healthy nodes.</p>
<p><strong>Pod (3 marks):</strong> A pod is the smallest deployable unit in Kubernetes. It encapsulates one or more containers that share a network namespace (same IP address) and can share storage volumes. Pods are ephemeral — if a pod dies, Kubernetes creates a new one rather than restarting the original. Containers within a pod communicate via localhost.</p>
<p><strong>ReplicaSet (3 marks):</strong> A ReplicaSet ensures a specified number of identical pod replicas are running at all times. If a pod crashes or a node fails, the ReplicaSet controller creates replacement pods to maintain the desired count. You rarely create ReplicaSets directly — they are managed by Deployments. Their purpose is to guarantee availability by maintaining pod count.</p>
<p><strong>Deployment (3 marks):</strong> A Deployment manages ReplicaSets over time and adds the ability to update applications safely. When a new image version is specified, the Deployment creates a new ReplicaSet for the new version, scales it up gradually, and scales down the old ReplicaSet — a rolling update. If the update fails, it can be rolled back to a previous ReplicaSet. Kubernetes retains up to 10 previous ReplicaSet revisions for this purpose.</p>
<p><strong>ConfigMap (3 marks):</strong> A ConfigMap stores non-sensitive configuration data as key-value pairs — environment variables, config files or command-line arguments. It separates configuration from container images so the same image can run in development, staging and production with different settings injected at runtime. This avoids building separate images for each environment and keeps secrets and config out of source code.</p>
<p><strong>Service (4 marks):</strong> A Service provides a stable, permanent network endpoint to access pods, whose IP addresses change when they are recreated. The Service selects pods via labels and load-balances traffic across them. Three key types: <em>ClusterIP</em> — exposes the service on an internal cluster IP, accessible only within the cluster; use this for microservice-to-microservice communication (e.g. the API calling the database service). <em>NodePort</em> — exposes the service on a static port on every node's IP; useful for development and testing but not recommended for production. <em>LoadBalancer</em> — provisions a cloud load balancer with a public IP, routing external internet traffic to the service; use this for any production service that must be publicly accessible.</p>
</div>
</details>

<!-- ─── 2023/24 REFER/DEFER ───────────────────────── -->
<h3 style="margin-top:2rem">2023/24 Refer/Defer Paper</h3>

<div class="box key"><div class="box-title">Q2a — Three Availability Zone Resilience Benefits (6 marks, ~7 mins)</div>
<p>Provide three clear benefits an availability zone offers regarding system resilience. Use the format: "An AZ offers [benefit] which offers protection of [X] by [mechanism]."</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2a (6 marks, 2 marks each)</div>
<p><strong>Benefit 1:</strong> An availability zone offers physical separation with independent power, cooling and networking, which offers protection against a single site failure (such as a power outage or hardware failure) by ensuring that a failure in one AZ does not cascade to application instances running in a separate AZ within the same region.</p>
<p><strong>Benefit 2:</strong> An availability zone offers independent network infrastructure from other zones, which offers protection against unplanned service downtime by allowing a load balancer to automatically route all traffic to healthy instances in surviving AZs without any manual intervention, maintaining service continuity for users.</p>
<p><strong>Benefit 3:</strong> An availability zone offers proximity to other AZs within the same region with low-latency inter-AZ connections, which offers protection against data loss by enabling synchronous or near-synchronous replication of database data across zones so that if one AZ's database becomes unavailable, a replica in another AZ can be promoted with minimal or no data loss.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3a — Four Monolith/Microservice Advantages and Disadvantages (8 marks, ~10 mins)</div>
<p>Provide four advantages and/or disadvantages of monolithic and microservice architectures. 2 marks per example.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3a (8 marks)</div>
<p><strong>1. Monolith advantage — Simplicity of deployment:</strong> A monolith is deployed as a single artefact — one build pipeline, one server, one log file. This is simpler to manage for small teams and reduces operational overhead. There is no service discovery, network latency between components, or distributed tracing complexity.</p>
<p><strong>2. Monolith disadvantage — Scaling inefficiency:</strong> A monolith must be scaled as a whole. If only the product search feature is under load during a sale, the entire application must be replicated, including payment processing and user management, which wastes resources and increases cloud cost.</p>
<p><strong>3. Microservice advantage — Independent deployability:</strong> Each microservice has its own deployment pipeline. The payments team can release an update without coordinating with or impacting the inventory or shipping teams. This increases release frequency and reduces the risk of any single deployment.</p>
<p><strong>4. Microservice disadvantage — Operational complexity:</strong> Microservices introduce distributed systems challenges including network latency between services, data consistency across multiple databases, distributed tracing when debugging failures, and the need for service discovery infrastructure. This overhead is significant and can be costly for small teams or simple systems.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3b — Thick vs Thin Events (6 marks, ~7 mins)</div>
<p>Explain thick and thin events in event-driven architecture and when you would choose one over the other.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3b (6 marks)</div>
<p><strong>Thin event:</strong> A thin event carries minimal data — typically just an identifier and a timestamp indicating that something happened. For example: <code>{"type": "OrderPlaced", "orderId": "123", "timestamp": "2025-01-01T10:00:00Z"}</code>. Consumers must make a follow-up API call to the source service to fetch the full order details if they need them.</p>
<p><strong>Thick event:</strong> A thick event carries the full or partial state of the changed entity within the event payload itself. For example: the full order object including items, customer details and total price. Consumers can update their local state directly from the event without a follow-up call.</p>
<p><strong>When to choose thin:</strong> When events are published at very high frequency and bandwidth is a concern, or when most subscribers do not need the full data. Also when the source data changes rapidly and by the time a consumer processes the event, they would want the latest state anyway — making the embedded data stale.</p>
<p><strong>When to choose thick:</strong> When subscribers frequently need the state data and you want to reduce network traffic from follow-up API calls. Also useful for Event Carried State Transfer (ECST) where subscribers maintain their own local replicas of data — they need the full state in the event to update their copy. The trade-off is larger event payloads and potential for stale embedded data if not processed promptly.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3d — TLS Session Keys (4 marks, ~5 mins)</div>
<p>Explain session keys in TLS, state how many there are and what each is used for.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3d (4 marks)</div>
<p>Session keys are symmetric keys derived during the TLS handshake and used to encrypt and authenticate all data transferred during a TLS session. They are derived by both the client and server independently from the master secret, so they are never transmitted across the network.</p>
<p>There are <strong>four session keys</strong>:</p>
<ul>
  <li><strong>client_write_encryption_key:</strong> Used by the client to encrypt data it sends to the server (AES symmetric encryption).</li>
  <li><strong>server_write_encryption_key:</strong> Used by the server to encrypt data it sends to the client.</li>
  <li><strong>client_write_MAC_key:</strong> Used by the client to generate an HMAC for each record it sends, so the server can verify the record was not tampered with in transit.</li>
  <li><strong>server_write_MAC_key:</strong> Used by the server to generate an HMAC for each record it sends, so the client can verify integrity.</li>
</ul>
<p>Using four separate keys — one for each direction and one for each purpose — means that even if one key were somehow compromised, it would not expose all traffic in both directions.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q4b — TLS Handshake Step by Step (15 marks, ~18 mins)</div>
<p>Explain each step from TCP connection to bi-directional encrypted data in transit. No need to explain key generation algorithms — just refer to their use.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q4b (15 marks)</div>
<p><strong>Step 1 — TCP Handshake:</strong> A standard TCP three-way handshake (SYN / SYN-ACK / ACK) establishes the underlying transport connection before TLS begins.</p>
<p><strong>Step 2 — ClientHello:</strong> The client sends the TLS protocol versions it supports, a list of cipher suites (algorithm combinations) it can handle, and a client random — 32 bytes of random data that will be used in key derivation.</p>
<p><strong>Step 3 — ServerHello:</strong> The server selects the TLS version and cipher suite from the client's list and replies with its own server random.</p>
<p><strong>Step 4 — Server Certificate:</strong> The server sends its digital certificate (containing the server's public key, domain name and the CA's digital signature) and any intermediate certificates in the chain.</p>
<p><strong>Step 5 — Certificate Validation:</strong> The browser validates the certificate: checks the validity period has not expired, verifies the domain name matches the URL, decrypts the CA's signature using the CA's public key and compares the hash to confirm the certificate has not been tampered with, and walks up the chain of trust until it reaches a trusted root CA pre-installed in the browser or OS.</p>
<p><strong>Step 6 — Key Exchange:</strong> Using the agreed cipher suite (typically ECDHE), the client and server exchange Diffie-Hellman public values. Both independently compute the same pre-master secret without sending it over the network.</p>
<p><strong>Step 7 — Master Secret and Session Key Derivation:</strong> Both sides independently compute the master secret using the pre-master secret, client random and server random. From the master secret, both derive four session keys: client and server write encryption keys (for AES symmetric encryption) and client and server write MAC keys (for HMAC authentication of records).</p>
<p><strong>Step 8 — ChangeCipherSpec:</strong> The client sends a ChangeCipherSpec message signalling it is switching to encrypted communication using the newly derived session keys.</p>
<p><strong>Step 9 — Client Finished:</strong> The client sends an encrypted Finished message containing an HMAC of the complete handshake transcript. This proves the handshake was not tampered with.</p>
<p><strong>Step 10 — Server ChangeCipherSpec + Finished:</strong> The server mirrors steps 8 and 9. Once both Finished messages are verified successfully, the TLS handshake is complete.</p>
<p><strong>Step 11 — Encrypted HTTPS data:</strong> All subsequent HTTP application data is encrypted using AES with the session keys and authenticated with HMAC on every record. Both directions (client-to-server and server-to-client) use separate keys, providing full bi-directional encrypted and authenticated communication.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q5a — Kubernetes Rolling Upgrades (7 marks, ~8 mins)</div>
<p>Explain what rolling upgrades mean in Kubernetes and how they work.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q5a (7 marks)</div>
<p><strong>What it means:</strong> A rolling upgrade is a deployment strategy where a new version of an application is gradually introduced while the old version is gradually removed, such that at no point are all instances simultaneously unavailable. Users experience no downtime during the upgrade.</p>
<p><strong>How it works in Kubernetes:</strong> A Deployment manages the process. When the container image version in the Deployment is updated, Kubernetes creates a new ReplicaSet configured with the new image. The new ReplicaSet starts creating new pods one at a time (or in small batches, controlled by the <code>maxSurge</code> setting). Each new pod must pass its readiness probe — proving it is healthy and able to serve traffic — before Kubernetes removes an old pod (controlled by <code>maxUnavailable</code>). This continues until the new ReplicaSet is at its full desired count and the old ReplicaSet is scaled down to zero. The old ReplicaSet is not deleted — it is retained with zero replicas so that a rollback can instantly scale it back up if the new version has a problem. Kubernetes keeps a history of up to 10 previous ReplicaSets by default.</p>
<p><strong>Why no downtime:</strong> Because healthy new pods are verified and serving traffic before old pods are terminated. There is always a sufficient number of healthy pods handling requests throughout the update.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q5b — Docker Compose YAML Line-by-Line (12 marks, ~14 mins)</div>
<p>Explain what the declarations at specific lines of a docker compose.yaml file achieve.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q5b (12 marks, 2 marks per line)</div>
<p><em>Note: The exam provides a specific YAML file. These answers cover the six most-tested declaration types — apply the same reasoning to whatever the exam shows you.</em></p>
<p><strong><code>services:</code></strong> The <code>services</code> declaration defines all the containers that make up the application. Each named entry beneath it (e.g. <code>api</code>, <code>db</code>) describes one container — its image, configuration, networking and storage. This is the root block that tells Compose what to run as part of this application stack.</p>
<p><strong><code>ports:</code></strong> The <code>ports</code> declaration maps a port on the host machine to a port inside the container, in the format <code>host:container</code>. This makes the container's service reachable from outside the Docker network — for example a browser on the host can reach a web server on port 3000. Without this, the container is only reachable by other containers on the same Docker network.</p>
<p><strong><code>environment:</code></strong> The <code>environment</code> declaration injects key-value pairs into the container as environment variables at runtime. This keeps sensitive values such as database passwords and hostnames out of the container image and source code, and allows the same image to run with different configuration in development, staging and production environments.</p>
<p><strong><code>healthcheck:</code></strong> The <code>healthcheck</code> declaration defines a command that Compose runs periodically inside the container to determine whether it is ready and healthy. If the check fails repeatedly (based on the <code>retries</code> setting), the container is marked unhealthy. This status is used by other services that have <code>depends_on: condition: service_healthy</code> to delay their own startup until this service is ready.</p>
<p><strong><code>depends_on:</code></strong> The <code>depends_on</code> declaration specifies startup ordering between services. With <code>condition: service_healthy</code>, the dependent service will not start until the named service has passed its healthcheck. This prevents a situation where an API container starts and immediately crashes because the database container is still initialising.</p>
<p><strong><code>volumes:</code></strong> The <code>volumes</code> declaration mounts a named Docker volume into the container at a specified path. This persists data outside the container's ephemeral writable layer. For a database container, this means data files survive if the container is stopped, recreated or updated. Without a named volume, all database data would be lost every time the container is removed.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q6c — Sharing Data Across Microservices: Sync vs Async (7 marks, ~8 mins)</div>
<p>Discuss synchronous and the two asynchronous approaches to data sharing across microservices, with advantages and disadvantages.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q6c (7 marks)</div>
<p><strong>Synchronous — HTTP/REST API calls (4 marks):</strong> One microservice calls another's API and waits for a response before continuing. For example, the order service calls the customer service's <code>GET /customers/42</code> to retrieve customer details needed to complete an order.<br>
<em>Advantage:</em> Simple to implement and reason about — the response is available immediately in the same request flow.<br>
<em>Disadvantage:</em> Creates tight temporal coupling — if the customer service is slow or unavailable, the order service is blocked. This can cascade into system-wide slowness.</p>
<p><strong>Asynchronous 1 — Message Queue (point-to-point) (3 marks):</strong> One service places a message on a queue; another service consumes it when ready. For example, after an order is placed, an "order created" message is put on a queue and the fulfilment service processes it independently.<br>
<em>Advantage:</em> Loose coupling and resilience — the producer continues regardless of consumer availability; the queue buffers messages if the consumer is slow.<br>
<em>Disadvantage:</em> Data is not immediately available — there is a delay between the message being published and the consumer acting on it, introducing eventual consistency.</p>
<p><strong>Asynchronous 2 — Event / Pub-Sub (4 marks):</strong> A service publishes an event when its data changes; multiple subscriber services receive it and update their own local data copies (Event Carried State Transfer). For example, when the customer service updates an address, it publishes a "CustomerUpdated" event; the order service and invoice service each consume this and update their own local copies of customer data.<br>
<em>Advantage:</em> Multiple services can react to the same event; no direct dependency on the source service for ongoing data access.<br>
<em>Disadvantage:</em> Data replicated across services may be temporarily inconsistent (eventual consistency), and managing schema changes to events across many consumers can be complex.</p>
</div>
</details>

<!-- ─── 2024/25 MAIN ─────────────────────────────── -->
<h3 style="margin-top:2rem">2024/25 Main Paper</h3>

<div class="box key"><div class="box-title">Q1a — API Endpoint Design: Bookstore (6 marks, ~7 mins)</div>
<p>Design an API endpoint to retrieve a book by media type and genre with optional filters for author, title and max price. Explain the design and give an example call.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1a (6 marks)</div>
<p><strong>Method:</strong> <code>GET</code> — because the client is retrieving data, not creating or modifying anything.</p>
<p><strong>Endpoint design:</strong></p>
<pre><code>GET /books/{media}/{genre}?author={author}&title={title}&maxPrice={price}</code></pre>
<p><strong>Justification:</strong> The media type and genre are required path parameters because they identify the core resource context — the type of book being requested. They belong in the path because they define the main resource, not optional filters. The author, title and maxPrice are optional query parameters because they are filters that narrow the results — they may or may not be present. This follows the REST convention: path identifies the resource, query qualifies or filters it.</p>
<p><strong>Example call returning the 1984 book:</strong></p>
<pre><code>GET https://bookshop.example.com:443/books/hardback/dystopian?author=George%20Orwell&title=1984&maxPrice=10.99</code></pre>
<p>The server returns a JSON response including all matching books. The response would use HTTP 200 OK on success, 400 Bad Request if parameters are malformed, and 404 Not Found if no matching books exist.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3b — Kubernetes vs Docker Compose (6 marks, ~7 mins)</div>
<p>Justify two advantages Kubernetes offers over Docker Compose in a distributed enterprise system.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3b (6 marks)</div>
<p><strong>Advantage 1 — Self-healing and automatic recovery:</strong> Kubernetes continuously monitors the health of pods. If a container crashes, the ReplicaSet controller automatically creates a replacement pod to restore the desired replica count. If a node fails entirely, Kubernetes reschedules its pods onto healthy nodes. Docker Compose has no equivalent — if a container dies on a single host, it requires manual intervention or basic restart policies, and it has no concept of multi-node recovery. In an enterprise distributed system with many services running across many machines, automatic self-healing is essential for availability.</p>
<p><strong>Advantage 2 — Zero-downtime rolling updates and rollbacks:</strong> Kubernetes Deployments manage application updates by gradually replacing old pods with new ones, verifying health before removing any old pods, and retaining previous ReplicaSets for instant rollback. Docker Compose has no built-in rolling update strategy — updating an image typically requires stopping and recreating containers, causing downtime. In an enterprise production environment where continuous delivery is required and downtime is unacceptable, Kubernetes' update management is a significant operational advantage.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3c — Rolling Updates with Diagram (13 marks, ~16 mins)</div>
<p>With a diagram, explain how Kubernetes enables rolling updates with no downtime using Deployment and ReplicaSet.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3c (13 marks)</div>
<p><strong>What a ReplicaSet does:</strong> A ReplicaSet ensures a specified number of identical pod replicas are always running. If a pod dies, the ReplicaSet creates a replacement. It does not manage version changes — it only knows how to maintain a count of pods matching a specific template.</p>
<pre><code>BEFORE UPDATE                   DURING UPDATE                AFTER UPDATE
Deployment                      Deployment
    │                               │
ReplicaSet-v1 (3 pods)         ReplicaSet-v1 (1 pod)       ReplicaSet-v1 (0 pods, kept)
 [pod] [pod] [pod]              [pod]                        []
                                ReplicaSet-v2 (2 pods)      ReplicaSet-v2 (3 pods)
                                [pod*] [pod*]                [pod*] [pod*] [pod*]
                                  * = new version</code></pre>
<p><strong>How the Deployment performs the rolling update:</strong></p>
<p>Step 1: The Deployment's image version is updated (e.g. <code>myapp:v1</code> → <code>myapp:v2</code>). The Deployment controller detects the change.</p>
<p>Step 2: The Deployment creates a new ReplicaSet configured with the new image version (v2). The old ReplicaSet (v1) still exists and is still running its pods.</p>
<p>Step 3: The new ReplicaSet starts creating new pods. Each new pod must pass its readiness probe — proving it is healthy and ready to serve traffic — before Kubernetes proceeds.</p>
<p>Step 4: Once a new v2 pod is healthy and serving traffic, one old v1 pod is terminated. This is governed by <code>maxSurge</code> (how many extra pods can be created above desired count) and <code>maxUnavailable</code> (how many pods can be unavailable at once). The defaults ensure traffic is never fully dropped.</p>
<p>Step 5: This cycle repeats — new pod up, old pod down — until the new ReplicaSet is at full desired count and the old ReplicaSet is scaled to zero.</p>
<p>Step 6: The old ReplicaSet is retained at zero replicas. If the new version has problems, running <code>kubectl rollout undo</code> instantly scales the old ReplicaSet back up and scales the new one down.</p>
<p><strong>Why there is no downtime:</strong> At no point are all pods simultaneously unavailable. Healthy new pods are verified before old pods are removed. The Service continuously routes traffic only to pods that pass their readiness check, so users always reach a healthy instance throughout the update.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q4b — Messaging Patterns: HTTP, Queue, Event (15 marks, ~18 mins)</div>
<p>For each of HTTP, message queue and event messaging: one advantage, one disadvantage, one use-case. Up to 5 marks per pattern.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q4b (15 marks, 5 per pattern)</div>
<p><strong>HTTP (synchronous request-response):</strong></p>
<p><em>Advantage:</em> Simple and immediate — the caller gets a response in the same request cycle, making it easy to reason about and debug. No broker infrastructure is needed.</p>
<p><em>Disadvantage:</em> Creates temporal coupling — if the target service is slow or unavailable, the calling service is blocked and may time out. This can cascade into a system-wide slowdown if a core service degrades.</p>
<p><em>Use-case:</em> Retrieving customer details for an order. The order service calls <code>GET /customers/42</code> on the customer service and needs the response immediately to complete the order validation — there is no benefit to making this asynchronous.</p>
<p><strong>Message Queue (asynchronous point-to-point):</strong></p>
<p><em>Advantage:</em> Loose temporal coupling and resilience — the producer places a message on the queue and continues without waiting. The consumer processes it when ready. If the consumer is temporarily down, messages buffer in the queue and are not lost.</p>
<p><em>Disadvantage:</em> No immediate response — the producer cannot know the result of the operation in the same flow. The system design must account for eventual results and failures, which adds complexity. Also requires queue infrastructure (e.g. RabbitMQ).</p>
<p><em>Use-case:</em> Order fulfilment. When a customer places an order, the order service puts a "process order" message on a queue. The warehouse service processes it when ready. The customer does not need an immediate fulfilment confirmation — only a payment confirmation — so asynchronous is appropriate and the queue provides resilience if the warehouse system is briefly offline.</p>
<p><strong>Event messaging (asynchronous pub-sub / event-driven):</strong></p>
<p><em>Advantage:</em> Multiple independent services can react to the same event without the publisher knowing they exist. Adding a new subscriber requires no change to the publisher, making the architecture highly extensible and loosely coupled.</p>
<p><em>Disadvantage:</em> Eventual consistency — subscribers update asynchronously, so there is a window where different services hold different versions of the same data. This is harder to manage than synchronous calls and can cause bugs if not handled carefully.</p>
<p><em>Use-case:</em> User registration. When a new user registers, the user service publishes a "UserRegistered" event. An email service subscribes and sends a welcome email. An analytics service subscribes and records the event. A recommendations service subscribes and initialises user preferences. All three react independently — the user service has no knowledge of them and does not need to be updated when new subscribers are added.</p>
</div>
</details>

<!-- ─── 2024/25 RESIT ─────────────────────────────── -->
<h3 style="margin-top:2rem">2024/25 Resit Paper</h3>

<div class="box key"><div class="box-title">Q1a — HTTPS Properties over HTTP (8 marks, ~10 mins)</div>
<p>Explain the key properties HTTPS offers over HTTP and when you might choose one over the other.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1a (8 marks)</div>
<p>HTTPS is HTTP transmitted over a TLS-encrypted connection. It provides three security properties that plain HTTP does not:</p>
<p><strong>Confidentiality:</strong> All data in transit is encrypted using AES symmetric encryption with session keys established during the TLS handshake. An attacker who intercepts network packets sees only ciphertext and cannot read the content — login credentials, payment details, personal data are protected.</p>
<p><strong>Integrity:</strong> Each TLS record includes an HMAC (Hash-based Message Authentication Code). If any byte of the data is altered in transit by an attacker performing a man-in-the-middle attack, the HMAC check fails and the recipient detects the tampering.</p>
<p><strong>Authenticity:</strong> The server presents a digital certificate signed by a trusted Certificate Authority. The browser validates this certificate, which proves the server is genuinely who it claims to be. This prevents an attacker from impersonating the server.</p>
<p><strong>When to use HTTPS:</strong> Any application that transmits credentials, personal data, payment information, session cookies or private content must use HTTPS. Modern browsers actively warn users about HTTP pages and browsers may block mixed content. HTTPS should be the default for all production services.</p>
<p><strong>When HTTP might be acceptable:</strong> Internal service-to-service communication within a fully trusted private network (e.g. behind a VPN or within a Kubernetes cluster) where the network itself provides sufficient isolation, and where the overhead of TLS is not justified. However, a defence-in-depth approach would still prefer HTTPS even internally.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q1b — Why Document APIs + OpenAPI Elements (8 marks, ~10 mins)</div>
<p>Why is documenting API endpoints important? What key elements are included using the OpenAPI standard?</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1b (8 marks)</div>
<p><strong>Why documentation matters:</strong> An API is only useful if its consumers can integrate with it correctly. Without clear documentation, developers guess at request formats, parameter names and response structures — leading to integration errors, wasted development time and support overhead. Good documentation acts as a binding contract between the API provider and consumer, enabling parallel development (frontend and backend can work simultaneously against the same agreed spec), reducing onboarding time for new developers, and making the API easier to test and maintain over time.</p>
<p><strong>Key OpenAPI elements:</strong></p>
<ul>
  <li><strong><code>openapi</code>:</strong> The OpenAPI specification version being used (e.g. 3.0.3).</li>
  <li><strong><code>info</code>:</strong> Metadata about the API — title, version, description and contact information.</li>
  <li><strong><code>servers</code>:</strong> The base URLs where the API is hosted (development, staging, production).</li>
  <li><strong><code>paths</code>:</strong> The core of the spec — defines each endpoint URL, the HTTP methods it supports, request parameters, request body schema and possible response codes and schemas.</li>
  <li><strong><code>components</code>:</strong> Reusable definitions for schemas (data models), parameters, responses and security schemes — referenced via <code>$ref</code> to avoid duplication.</li>
  <li><strong><code>tags</code>:</strong> Labels that logically group related endpoints in the documentation UI (e.g. all "Books" endpoints grouped together).</li>
</ul>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q1c — Express Middleware Purpose and Use-case (9 marks, ~11 mins)</div>
<p>Explain the purpose and benefits of Express middleware. Give a use-case with a middleware function and explain how and when it is called.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q1c (9 marks)</div>
<p><strong>Purpose:</strong> Middleware in Express is a function that executes in the request-response pipeline between the server receiving an HTTP request and the final route handler sending the response. It has access to the request (<code>req</code>), response (<code>res</code>) and a <code>next</code> function. Calling <code>next()</code> passes control to the next function in the chain; not calling it (and not sending a response) halts the request.</p>
<p><strong>Benefits:</strong> Middleware enables separation of concerns — authentication, logging, input validation and error handling can be written once and applied across all routes or specific routes without duplicating code in every handler. It creates a reusable, ordered pipeline that makes applications easier to extend and maintain.</p>
<p><strong>Use-case — JWT authentication middleware:</strong> A web application has many protected routes. Rather than checking the authorisation token inside every route handler, a single middleware function handles it:</p>
<pre><code>function requireAuth(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token provided' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // attach user to request for downstream use
    next();             // token valid — proceed to route handler
  } catch (err) {
    res.status(403).json({ error: 'Invalid token' });
  }
}

app.get('/profile', requireAuth, (req, res) => {
  res.json({ user: req.user });
});</code></pre>
<p>This middleware is called after the HTTP request is received and parsed but before the <code>/profile</code> route handler executes. It verifies the JWT, rejects invalid or missing tokens with a 401/403 response, and — if valid — attaches the decoded user object to <code>req</code> so the route handler can use it. The same <code>requireAuth</code> function can be added to any protected route without code duplication.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2a — IaaS vs PaaS, When to Choose (5 marks, ~6 mins)</div>
<p>Explain the difference between IaaS and PaaS. When would you choose one over the other?</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2a (5 marks)</div>
<p><strong>IaaS (Infrastructure as a Service):</strong> The cloud provider manages the physical hardware, virtualisation and network infrastructure. The customer manages everything above that — the operating system, runtime, middleware, applications and data. Examples: Azure Virtual Machines, AWS EC2. The customer has maximum control but maximum responsibility.</p>
<p><strong>PaaS (Platform as a Service):</strong> The cloud provider manages the infrastructure and also the operating system, runtime environment and middleware. The customer only manages their application code and data. Examples: Azure App Service, Heroku. The customer has less control but significantly less operational overhead — they do not patch OS or runtime themselves.</p>
<p><strong>When to choose IaaS:</strong> When you need detailed control over the OS configuration, need to install specific software versions, have workloads that require custom runtime environments, or are migrating existing on-premises systems with specific dependencies. Also when regulatory requirements demand visibility into the OS layer.</p>
<p><strong>When to choose PaaS:</strong> When your team wants to focus on writing application code without managing servers or OS patches. Ideal for web applications, APIs and microservices where the platform's managed scaling and deployment tooling adds value. PaaS reduces operational effort and is well-suited for teams without dedicated infrastructure specialists.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2b — Resilience + Three Examples (10 marks, ~12 mins)</div>
<p>Explain "resilience" in relation to cloud-based systems and provide three examples of how to make solutions resilient.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2b (10 marks)</div>
<p><strong>What resilience means:</strong> Resilience in cloud-based systems is the ability of a system to withstand failures, recover from them quickly, and continue to function correctly — either at full capacity or at gracefully degraded capacity — without significant disruption to users. It is about planning for failure rather than assuming everything will work. A resilient system expects individual components to fail and designs around that expectation.</p>
<p><strong>Example 1 — Multiple availability zones:</strong> Deploy application instances across at least two geographically separate availability zones within the same cloud region. Each AZ has independent power, networking and cooling. A load balancer distributes traffic across AZs. If one AZ suffers a complete outage, the load balancer routes all traffic to the remaining AZ and users experience no downtime. This protects against site-level failures.</p>
<p><strong>Example 2 — Auto-scaling with a load balancer:</strong> Configure a load balancer in front of an auto-scaling group of application instances. If one instance becomes unhealthy, the load balancer stops sending traffic to it and the auto-scaling group creates a replacement. If traffic spikes suddenly, new instances are automatically added. This ensures the system remains available and performant during both failures and high-demand events without manual intervention.</p>
<p><strong>Example 3 — Database read replicas and backups:</strong> Configure a primary database with one or more read replicas in different availability zones. Reads are distributed across replicas, reducing load on the primary. If the primary fails, a replica can be promoted to become the new primary — minimising data loss and recovery time. Regular automated backups to separate storage ensure that even a catastrophic data loss event can be recovered from within a defined recovery time objective.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q2c — Load Balancer with Diagram (10 marks, ~12 mins)</div>
<p>With a diagram, explain the purpose and operation of a load balancer in elastic-compute solutions.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q2c (10 marks)</div>
<pre><code>                    Internet
                       │
              ┌────────▼────────┐
              │  Load Balancer  │  ← single public entry point
              │  (health checks)│
              └──┬──────────┬───┘
                 │          │
        ┌────────▼──┐  ┌────▼──────┐
        │  Instance │  │ Instance  │   ← AZ-1
        │  (App v1) │  │ (App v1)  │
        └───────────┘  └───────────┘
        ┌────────────┐
        │  Instance  │   ← AZ-2 (auto-scaled in, new)
        │  (App v1)  │
        └────────────┘</code></pre>
<p><strong>Purpose:</strong> A load balancer acts as a single public entry point that distributes incoming requests across multiple backend application instances. Its purpose is to: (1) distribute load so no single instance is overwhelmed, (2) detect unhealthy instances and stop sending traffic to them, and (3) enable horizontal scaling by adding or removing instances without the client ever needing to know about it.</p>
<p><strong>Operation in an elastic-compute context:</strong> The load balancer continuously sends health-check requests (e.g. <code>GET /health</code>) to each registered instance. If an instance fails to respond within a threshold, it is marked unhealthy and removed from the pool — traffic is redistributed to healthy instances automatically. When demand increases, an auto-scaling group detects the increased load and launches additional instances. These new instances register with the load balancer and begin receiving traffic once they pass their health check. When demand drops, excess instances are terminated and deregistered from the load balancer. The client always connects to the same load balancer IP or DNS name — the underlying pool of instances is completely transparent to it.</p>
<p><strong>Resilience benefit:</strong> Because instances span multiple availability zones, a single AZ failure takes down only some instances. The load balancer continues routing to healthy instances in surviving AZs, maintaining service continuity.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3b — Message Queue for Loose Coupling (8 marks, ~10 mins)</div>
<p>Explain how a message queue loosely couples microservices and increases resilience. Provide a use-case.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3b (8 marks)</div>
<p><strong>How a message queue achieves loose coupling:</strong> In a synchronous HTTP design, Service A calls Service B directly and waits for a response. This creates temporal coupling — A is dependent on B being available and responsive at the same moment. If B is slow, A is slow. If B is down, A fails. A message queue removes this direct dependency. Service A places a message on the queue and immediately continues its own work. Service B consumes from the queue at its own pace. A and B do not need to be running simultaneously or at the same speed.</p>
<p><strong>How it increases resilience:</strong> If Service B crashes, messages accumulate in the queue rather than being lost. When B recovers, it picks up where it left off. The queue acts as a buffer that absorbs demand spikes — if B is slow during a traffic burst, the queue holds the backlog and B processes it over time rather than dropping requests. Service A is unaffected by B's slowness or downtime.</p>
<p><strong>Use-case — Order processing:</strong> An e-commerce platform has an order service (A) and an email notification service (B). When a customer places an order, the order service places an "OrderConfirmed" message on a RabbitMQ queue and immediately returns a confirmation to the customer. The email service consumes messages from the queue and sends confirmation emails. If the email service is temporarily down for maintenance, orders are not lost — messages queue up and emails are sent when the service recovers. The order service is completely unaffected by the email service's availability, and the customer experience is not degraded.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q3c — Publisher-Subscriber Pattern with Use-case (8 marks, ~10 mins)</div>
<p>Explain the publisher-subscriber messaging pattern and apply it to a relevant use-case.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q3c (8 marks)</div>
<p><strong>The pattern:</strong> In the publisher-subscriber (pub-sub) pattern, a publisher emits a message or event to a topic or exchange without knowing which services will receive it. Multiple subscribers register their interest in that topic and each receives their own independent copy of the message. The publisher and subscribers are fully decoupled — neither knows about the other.</p>
<p><strong>How it works technically (e.g. using RabbitMQ fanout exchange):</strong> The publisher sends a message to a fanout exchange. RabbitMQ delivers a copy of the message to every queue bound to that exchange. Each subscriber has its own queue and consumes from it independently at its own pace. A subscriber can join or leave without any change to the publisher or other subscribers.</p>
<p><strong>Use-case — Product price update:</strong> An e-commerce platform has a product management service that can update prices. When a price changes, the product service publishes a "PriceUpdated" event containing the product ID and new price to a fanout exchange. Three independent subscribers react: the search indexing service updates its search index so users see the new price in search results; the basket service updates any active baskets containing that product; the price history service records the change for analytics. Each subscriber reacts independently and asynchronously — the product service has no knowledge of any of them and requires no modification when a new subscriber is added.</p>
<p><strong>Key advantage over a shared queue:</strong> In a shared queue, each message is delivered to exactly one consumer. In pub-sub, every subscriber receives the same message. Use pub-sub when multiple independent services need to react to the same event.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q4c — Five Business Benefits of Microservices over Monolith (10 marks, ~12 mins)</div>
<p>Provide and justify five business benefits of a distributed microservice architecture over a monolith.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q4c (10 marks, 2 marks each)</div>
<p><strong>1. Faster time to market:</strong> Independent deployment pipelines mean each team can release its service without coordinating with other teams. A bug fix in the payments service goes live in minutes without a full application release. This accelerates the business's ability to respond to customer needs and competitive pressure.</p>
<p><strong>2. Cost-efficient scaling:</strong> Only the services under load need to be scaled. During a flash sale, the product catalogue and checkout services can scale out while the admin dashboard and reporting services remain at minimum capacity. In a monolith the entire application must scale, even the parts that are not under load — wasting cloud spend.</p>
<p><strong>3. Improved system resilience:</strong> A failure in one microservice does not necessarily bring down the entire system. If the recommendation service fails, users can still browse and purchase — they just do not see recommendations. A monolith failure affects every user and every function simultaneously. This resilience translates directly to reduced revenue loss during incidents.</p>
<p><strong>4. Team autonomy and organisational agility:</strong> Small, autonomous teams own individual services end-to-end. They can choose their own technology stack, iterate quickly and make decisions without waiting for approval from a central architecture team. This mirrors how successful technology organisations like Amazon and Netflix structure their engineering teams, enabling innovation at speed.</p>
<p><strong>5. Technology flexibility and reduced lock-in:</strong> Different services can use the technology most suited to their needs — a machine learning service in Python, a high-throughput messaging service in Go, a web API in Node.js. In a monolith, all teams are locked into one language and framework, which may not be optimal for every business function and makes it harder to adopt new technologies as they emerge.</p>
</div>
</details>

<div class="box key" style="margin-top:1rem"><div class="box-title">Q5c — JSON Structure: Bob, Age 25, Three Children (5 marks, ~5 mins)</div>
<p>Create an appropriate JSON structure for a person aged 25 named Bob Martin with children Jim, Jane and Susan.</p>
</div>
<details><summary style="cursor:pointer;color:#7e22ce;font-weight:700;margin:.6rem 0 .3rem">▶ Show full model answer</summary>
<div class="box model"><div class="box-title">Model Answer — Q5c (5 marks)</div>
<pre><code>{
  "age": 25,
  "firstName": "Bob",
  "lastName": "Martin",
  "children": [
    "Jim",
    "Jane",
    "Susan"
  ]
}</code></pre>
<p><strong>Key points:</strong> Numbers (<code>25</code>) are not quoted. Strings are in double quotes. The children are represented as a JSON array (<code>[ ]</code>) because there are multiple values of the same type. Keys are in double quotes. No trailing comma after the last element or property. The structure is valid JSON and accurately represents the data described.</p>
</div>
</details>

<div class="box tip" style="margin-top:1.5rem"><div class="box-title">Fastest high-value practice set</div>
If you are short on time, do these five first (they cover the most marks and most-tested topics):<br>
<strong>2022/23 resit Q4</strong> (TLS/HTTPS 25 marks) → <strong>2022/23 resit Q6</strong> (IAM terms 25 marks) → <strong>2023/24 main Q4</strong> (K8s components 25 marks) → <strong>2024/25 main Q4b</strong> (messaging patterns 15 marks) → <strong>2023/24 refer/defer Q4b</strong> (TLS handshake 15 marks).
</div>
</section>"""

with open('/Users/zaid/Documents/DISTRIBUTEDEXAMREVISION/CO3404_Revision_Guide.html', 'r') as f:
    content = f.read()

start_tag = '<section id="past-paper-bank">'
end_tag = '</section>'

start_idx = content.find(start_tag)
# find the closing </section> after start
end_idx = content.find(end_tag, start_idx) + len(end_tag)

content = content[:start_idx] + NEW_SECTION + content[end_idx:]

with open('/Users/zaid/Documents/DISTRIBUTEDEXAMREVISION/CO3404_Revision_Guide.html', 'w') as f:
    f.write(content)

print(f"Done. File is now {len(content)} chars.")
