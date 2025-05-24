# Manus_Finance

Use MCP Servers:

AI Agents to be truly useful, they must access the right content 
at the right time and even take actions like updating a document of sending an email
based on that context. Historically, connecting an AI model to all these external sources has been a messy
, ad-hoc affair. Developers had to write custom code or specialized plugins for each data source or API.


Anthropic came up with Model Context Protocol (MCP)
. It designed to bridge AI assistants with the world of data and tools, to plug in many different sources of context.

Why MCP is a hot topic right now and how MCP enables the shift towards more integrated, context-aware AI, its place in agentic workflows.


Reason why MCP is trending now:

1) Integration Problem Solver: Integrating AI agents with real-world business systems and data. MCP
defines how to connect existing data sources (file systems, DBs, APIs, etc) into AI Workflows.
   
2) Community and adoption: MCP has struck a chord as the industry moves towards more integrated and context--aware AI.

3) MCP is open and model-agnostic, and it is backed by a major AI player. MCP
appears to be the winner in the race to standardize how AI systems connect to external data.


## What is MCP and How Does it Work:

MCP lays out clear rule of how AI can find, connect to, and use extrnal tools - 
whether it's querying a DB or running a command. This lt's the model go beyond their training 
data, making them more flexible and aware of the world around them.

### Technical Overview of MCP:

The protocol uses JSON-RPC 2.0 messages to establish communication between:

* Hosts: LLM apps that initiate connections
* Clients: Connectors within the host application
* Servers: Services that provide context and capabilities

One striking feature is MCP's dynamic discovery  AI agents automatically detect
available MCP Servers and their capabilities, without hard-coded integrations. For example
, if you spin up a new MCP server (like CRM), agents can immediately recofnize it and use it
via a standardized API, offering flexibility.


## Langgraph


